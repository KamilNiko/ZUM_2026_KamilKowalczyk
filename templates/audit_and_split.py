"""Audyt danych i zapis podziału PolEmo 2.0 (wariant all_text) — Zadanie 1.

Uruchomienie (z dowolnego katalogu):
    .venv/bin/python templates/audit_and_split.py

Skrypt nie trenuje i nie uruchamia żadnego modelu. Zbiór test jest tylko
opisywany statystycznie (rozkład klas, długości, duplikaty), co jest
dozwolone przed zamrożeniem final test.
"""

import re
from pathlib import Path

import pandas as pd
from datasets import load_dataset

# Oficjalne repozytorium używa skryptu ładującego (polemo2-official.py), którego
# biblioteka `datasets` >= 4 już nie obsługuje. Korzystamy więc z automatycznej
# konwersji do Parquet przygotowanej przez Hugging Face, przypiętej do commita,
# żeby numery wierszy (nasze identyfikatory) były stabilne.
DATASET_NAME = "clarin-pl/polemo2-official"
DATASET_CONFIG = "all_text"
PARQUET_REVISION = "b2ced85046c77edf649d6ac991cc0ef5b8bca13c"  # refs/convert/parquet

SEED = 2026  # oficjalny podział nie wymaga losowania; seed używany w kolejnych zadaniach

REPO_ROOT = Path(__file__).resolve().parents[1]
SPLITS_DIR = REPO_ROOT / "splits"

# Nazwy zbiorów w HF -> nazwy plików zgodne z splits/README.md
SPLIT_FILES = {
    "train": "train_ids.csv",
    "validation": "validation_ids.csv",
    "test": "test_ids.csv",
}


def load_polemo() -> pd.DataFrame:
    """Zwraca jedną ramkę z kolumnami: id, split, text, label."""
    ds = load_dataset(DATASET_NAME, revision=PARQUET_REVISION, data_dir=DATASET_CONFIG)
    label_names = ds["train"].features["target"].names  # ['zero', 'minus', 'plus', 'amb']

    frames = []
    for split in SPLIT_FILES:
        df = ds[split].to_pandas()
        df.insert(0, "id", range(len(df)))  # numer wiersza w oficjalnym zbiorze
        df.insert(1, "split", split)
        df["label"] = df["target"].map(lambda t: label_names[t])
        frames.append(df.drop(columns="target"))
    return pd.concat(frames, ignore_index=True)


def save_splits(full_df: pd.DataFrame) -> None:
    SPLITS_DIR.mkdir(exist_ok=True)
    for split, filename in SPLIT_FILES.items():
        ids = full_df.loc[full_df["split"] == split, ["id"]]
        ids.to_csv(SPLITS_DIR / filename, index=False)
        print(f"  {filename}: {len(ids)} identyfikatorów")


def normalize(text: str) -> str:
    """Normalizacja do wykrywania prawie-duplikatów: małe litery, bez interpunkcji i nadmiarowych spacji."""
    text = re.sub(r"[^\w\s]", " ", text.lower())
    return re.sub(r"\s+", " ", text).strip()


def audit_duplicates(full_df: pd.DataFrame, key: str, title: str) -> None:
    print(f"\n=== {title} ===")
    dup_mask = full_df.duplicated(subset=[key], keep=False)
    dups = full_df[dup_mask]
    n_groups = dups[key].nunique()
    print(f"Wiersze należące do grup duplikatów: {len(dups)} (grup: {n_groups})")
    if dups.empty:
        return

    groups = dups.groupby(key).agg(
        splits=("split", lambda s: tuple(sorted(set(s)))),
        n_labels=("label", "nunique"),
        size=("id", "size"),
    )
    print("Grupy wg zbiorów, w których występują:")
    print(groups["splits"].value_counts().to_string())

    cross = groups[groups["splits"].map(len) > 1]
    print(f"Grupy przekraczające granicę podziału (potencjalny wyciek): {len(cross)}")
    print(f"Grupy z niespójną etykietą: {(groups['n_labels'] > 1).sum()}")


def run_audit_and_splits() -> None:
    print("=== POBIERANIE ZBIORU POLEMO 2.0 (all_text) ===")
    full_df = load_polemo()

    print("\n=== LICZBA PRZYKŁADÓW ===")
    print(full_df["split"].value_counts().reindex(SPLIT_FILES).to_string())
    print(f"Razem: {len(full_df)}")

    print("\n=== ZAPIS PODZIAŁU (splits/) ===")
    save_splits(full_df)

    print("\n=== ROZKŁAD KLAS (liczba i udział %) ===")
    counts = pd.crosstab(full_df["label"], full_df["split"])[list(SPLIT_FILES)]
    shares = (counts / counts.sum() * 100).round(1).add_suffix(" %")
    print(pd.concat([counts, shares], axis=1).to_string())

    print("\n=== BRAKI DANYCH ===")
    empty_text = full_df["text"].fillna("").str.strip().eq("")
    print(f"Brakujące wartości:\n{full_df[['text', 'label']].isna().sum().to_string()}")
    print(f"Puste teksty (po usunięciu spacji): {empty_text.sum()}")

    audit_duplicates(full_df, "text", "DUPLIKATY DOKŁADNE")
    full_df["text_norm"] = full_df["text"].map(normalize)
    audit_duplicates(full_df, "text_norm", "PRAWIE-DUPLIKATY (po normalizacji)")

    print("\n=== STATYSTYKI DŁUGOŚCI TEKSTU (słowa) ===")
    full_df["word_count"] = full_df["text"].str.split().str.len()
    print(full_df.groupby("split")["word_count"].describe().reindex(SPLIT_FILES).round(1).to_string())
    print("\nŚrednia długość wg klasy (train):")
    print(full_df[full_df["split"] == "train"].groupby("label")["word_count"].mean().round(1).to_string())

    print("\n=== PRZYKŁADY (train, po jednym na klasę, skrócone) ===")
    train = full_df[full_df["split"] == "train"]
    for label, group in train.groupby("label"):
        row = group.sample(1, random_state=SEED).iloc[0]
        print(f"[{label}] id={row['id']}: {row['text'][:200]}...")


if __name__ == "__main__":
    run_audit_and_splits()
