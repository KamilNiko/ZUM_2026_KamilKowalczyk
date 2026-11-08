# Projekt końcowy ZUM 2026/2027

To repozytorium rozwijasz przez cały semestr. Górna część tego pliku mówi, jak pracować. Dolna część to dokumentacja Twojego projektu, którą uzupełniasz w kolejnych zadaniach.

## Jak pracować z tym repozytorium

### Co robisz

Przeprowadzasz jeden wiarygodny eksperyment nadzorowanej klasyfikacji jednolabelowej. Każdy przykład ma dokładnie jedną klasę docelową. Pracujesz na tekście, obrazie, audio albo danych multimodalnych. Projekt jest indywidualny.

Projekt ma trzy poziomy:
1. **Poziom A. Punkt odniesienia.** Prosty, sensowny baseline.
2. **Poziom B. Podejście pretrained.** Co najmniej jedno podejście pretrained. Dobrym pierwszym krokiem jest zamrożony encoder i prosty klasyfikator. Fine tuning nie jest obowiązkowy.
3. **Poziom C. Jedno uzasadnione rozszerzenie.** Odpowiada na to samo pytanie projektu i nie zmienia zmiennej docelowej ani problemu klasyfikacyjnego.

Pełne zasady są w pliku [PROJECT_RULES.md](PROJECT_RULES.md). Przeczytaj je przed zgłoszeniem tematu.

### Od czego zacząć

1. Utwórz własne repozytorium z tego szablonu: wybierz „Use this template”, a następnie „Create a new repository”.
2. Nazwij repozytorium `ZUM_2026_ImięNazwisko`.
3. Repozytorium może być publiczne albo prywatne. Jeśli jest prywatne, dodaj konto prowadzącej wskazane na platformie kursu. Jeśli Twoje dane zawierają informacje osobowe albo wrażliwe, przeczytaj najpierw zasadę o prywatności w [zasadach projektu](PROJECT_RULES.md).
4. Przeczytaj [instrukcję zgłoszenia tematu](assignments/00_topic_submission.md) i zgłoś temat.

### Kolejność i terminy

Wszystkie terminy przypadają w niedzielę o godzinie 23:59. Wszystko oddajesz na platformie kursu.

| Etap | Instrukcja | Termin | Punkty | Co oddajesz |
|---|---|---|---|---|
| Zgłoszenie tematu | [00_topic_submission.md](assignments/00_topic_submission.md) | 18 października 2026 | 0, obowiązkowe | wypełniony szablon zgłoszenia |
| Zadanie 1 | [01_data_and_protocol.md](assignments/01_data_and_protocol.md) | 8 listopada 2026 | 15 | link do repozytorium i tag `task-1` |
| Akceptacja artykułu spoza listy | [scientific_paper_review.md](assignments/scientific_paper_review.md) | 22 listopada 2026 | 0, obowiązkowe dla źródeł spoza listy | pełny opis bibliograficzny oraz DOI albo oficjalny link |
| Zadanie 2 | [02_baseline.md](assignments/02_baseline.md) | 29 listopada 2026 | 15 | link i tag `task-2` |
| Artykuł naukowy | [scientific_paper_review.md](assignments/scientific_paper_review.md) | 6 grudnia 2026 | 10, poza projektem | plik PDF albo Markdown |
| Zadanie 3 | [03_pretrained.md](assignments/03_pretrained.md) | 20 grudnia 2026 | 20 | link i tag `task-3` |
| Zadanie 4 | [04_extension.md](assignments/04_extension.md) | 17 stycznia 2027 | 20 | link i tag `task-4` |
| Zadanie 5 | [05_final_evaluation.md](assignments/05_final_evaluation.md) | 31 stycznia 2027 | 30 | link oraz tagi `final-freeze` i `task-5` |

Projekt jest wart 100 punktów. Artykuł jest osobnym zadaniem za 10 punktów.

### Final test w skrócie

1. Final test wydzielasz w Zadaniu 1 i od razu go zamrażasz.
2. Do końca Zadania 4 nie uruchamiasz na nim żadnego modelu. Wszystkie porównania i wybór systemu robisz na validation.
3. W Zadaniu 5 wybierasz dokładnie jeden finalny system, zapisujesz go w `final_system.md` i tworzysz tag `final-freeze`.
4. Nie trenujesz systemu ponownie na `train + validation` ani na żadnym większym zbiorze.
5. Dopiero potem uruchamiasz final test, jeden raz, tylko dla tego systemu. Wynik testu nie może zmienić systemu.

Szczegóły są w [zasadach projektu](PROJECT_RULES.md), w części „Zasady final test”.

### Tagi Git

Każde oddanie wskazuje commit oznaczony tagiem. Oceniamy stan repozytorium z tego commita.

```bash
git add .
git commit -m "Zadanie 1: protokół i podział danych"
git tag -a task-1 -m "Zadanie 1"
git push origin main
git push origin task-1
```

Polecenie `git ls-remote --tags origin` pokazuje, czy tag jest już na GitHub. Tag możesz też utworzyć na stronie GitHub w zakładce Releases. Nie przesuwaj i nie usuwaj tagów po oddaniu.

### Gdzie co zapisujesz

| Miejsce | Co tam trafia |
|---|---|
| `README.md`, część dolna | dokumentacja projektu |
| `notebooks/` | notebooki kolejnych etapów |
| `src/` | kod wspólny dla notebooków (opcjonalnie) |
| `splits/` | identyfikatory przykładów train, validation i final test ([opis formatu](splits/README.md)) |
| `results/` | metryki i predykcje na validation, dziennik eksperymentów, wynik final test (dopiero po `final-freeze`); [opis układu](results/README.md) |
| `final_system.md` | zapis finalnego systemu (Zadanie 5); [szablon](templates/final_system_template.md) |
| `data/sample/` | mała próbka danych, jeśli licencja i zasady prywatności na to pozwalają |
| `templates/` | szablony do skopiowania |

### Czego nie wrzucasz

* pełnych zbiorów danych;
* dużych wag modeli i checkpointów (przechowujesz je poza repozytorium i opisujesz, gdzie są);
* danych, próbek ani identyfikatorów umożliwiających identyfikację osób;
* haseł, tokenów i kluczy API;
* plików tymczasowych środowiska.

Plik `.gitignore` blokuje typowe przypadki, ale to Ty odpowiadasz za zawartość repozytorium.

### Jak oceniamy

Liczy się poprawność metodologiczna, uzasadnienie decyzji i jakość analizy. Wysokość wyniku nie jest sama w sobie kryterium. Projekt z niższym F1, wykonany poprawnie i dobrze przeanalizowany, może dostać więcej punktów niż projekt z bardzo wysokim wynikiem uzyskanym przy wycieku danych. Kryteria każdego zadania są w jego instrukcji, a rubryka ogólna w [zasadach projektu](PROJECT_RULES.md).

---

# Dokumentacja projektu

Uzupełniaj sekcje w zadaniach podanych w nawiasach. Zastępuj teksty w nawiasach kwadratowych.

## Informacje ogólne

* Tytuł: Klasyfikacja wydźwięku polskich recenzji (PolEmo 2.0): TF-IDF a zamrożony enkoder HerBERT
* Autor: Kamil Kowalczyk
* Modalność: tekst (język polski)
* Problem klasyfikacji: wydźwięk całej recenzji, 4 klasy: `minus`, `plus`, `amb`, `zero`

## Problem i pytanie eksperymentalne (Zadanie 1)

* **Problem klasyfikacji:** nadzorowana klasyfikacja jednolabelowa tekstu w języku polskim. Każdą recenzję przypisujemy do dokładnie jednej z 4 klas wydźwięku: `minus` (negatywna), `plus` (pozytywna), `amb` (ambiwalentna) albo `zero` (neutralna).
* **Pytanie eksperymentalne:** czy polski model pretrenowany HerBERT (`allegro/herbert-base-cased`) z zamrożonym enkoderem uzyska wyższe Macro-F1 na zbiorze validation niż klasyczny baseline TF-IDF z regresją logistyczną? Czy największa przewaga HerBERTa ujawni się w najtrudniejszej klasie `amb` (recenzje ambiwalentne)?

### Jednostka generalizacji

* **Jednostka generalizacji:** pojedyncza recenzja.
* **Uzasadnienie i przyszłe dane:** model ma działać na nowych, niezależnych recenzjach konsumenckich w języku polskim z tych samych domen (medycyna, hotele, produkty, uczelnie).
* **Ograniczenie jednostki:** PolEmo 2.0 nie zawiera identyfikatorów autorów recenzji ani ocenianych obiektów (np. konkretnego hotelu lub lekarza). Z tego powodu podział grupowy według autorów nie jest możliwy. Klasyfikacja odbywa się na poziomie pojedynczego dokumentu, a brak identyfikatorów autorów opisuję jako ograniczenie projektu.

## Dane i licencja (Zadanie 1)

* **Źródło danych:** zbiór **PolEmo 2.0** (`clarin-pl/polemo2-official`, wariant `all_text`) udostępniony przez CLARIN-PL na platformie [Hugging Face](https://huggingface.co/datasets/clarin-pl/polemo2-official). Oryginał: [repozytorium CLARIN-PL](https://clarin-pl.eu/dspace/handle/11321/710).
* **Publikacja:** Kocoń J., Miłkowski P., Zaśko-Zielińska M. (2019). *Multi-Level Sentiment Analysis of PolEmo 2.0: Extended Corpus of Multi-Domain Consumer Reviews.* CoNLL 2019, s. 980–991. DOI: [10.18653/v1/K19-1092](https://doi.org/10.18653/v1/K19-1092).
* **Sposób pobrania:** dane pobiera automatycznie skrypt [`src/audit_and_split.py`](src/audit_and_split.py). Oficjalny skrypt ładujący zbioru nie działa z biblioteką `datasets` w wersji 4 i nowszej, dlatego używam automatycznej konwersji do Parquet (`refs/convert/parquet`) przypiętej do commita `b2ced85046c77edf649d6ac991cc0ef5b8bca13c`.
* **Sposób oznaczenia etykiet:** ręczna anotacja ekspercka na poziomie całych dokumentów (oraz zdań) w schemacie 2+1: dwóch anotatorów i superanotator rozstrzygający niezgodności. Autorzy raportują zgodność (Positive Specific Agreement) 0,91 dla tekstów.
* **Licencja:** CC BY-NC-SA 4.0 (użycie niekomercyjne, z uznaniem autorstwa, na tych samych warunkach). Karta zbioru jest niespójna: treść podaje CC BY-NC-SA 4.0, metadane `cc-by-sa-4.0`, a skrypt ładujący `CC-BY-4.0`. Przyjmuję najbardziej restrykcyjną z nich. Projekt ma charakter edukacyjny i niekomercyjny.
* **Ochrona prywatności:** teksty recenzji zawierają wzmianki o osobach trzecich (np. nazwiska lekarzy, profesorów). Dlatego surowe teksty recenzji nie są commitowane do publicznego repozytorium GitHub. Katalog `splits/` zawiera wyłącznie pliki z indeksami: `train_ids.csv`, `validation_ids.csv`, `test_ids.csv`.
* **Znane ograniczenia:** brak metadanych o autorze, ocenianym obiekcie i dacie. Około 85% recenzji pochodzi z domen medycyny i hoteli. Tekst jest wstępnie stokenizowany (spacje przed interpunkcją).

## Protokół (Zadanie 1)

### Audyt danych

Łączny rozmiar zbioru wynosi **8 216 przykładów**. Audyt wykonuje skrypt `src/audit_and_split.py`.

| Zbiór | Liczba przykładów | Liczba niezależnych jednostek | Udział % | `minus` % | `plus` % | `amb` % | `zero` % |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **train** | 6 573 | 6 573 | 80,0% | 37,6% | 27,7% | 19,9% | 14,8% |
| **validation** | 823 | 823 | 10,0% | 36,9% | 28,7% | 18,8% | 15,6% |
| **final test** | 820 | 820 | 10,0% | 41,3% | 27,7% | 16,6% | 14,4% |

* **Braki danych:** brakujące wartości (`text` / `label`): 0. Puste teksty po usunięciu spacji: 0.
* **Statystyki długości tekstu:** średnia długość recenzji wynosi 133,5 słowa w `train`, 130,7 w `validation` i 128,8 w `test`. Mediana dla całego zbioru wynosi 119 słów, minimum 1 słowo, maksimum 987 słów.
* **Limit długości HerBERTa:** model HerBERT ma limit 512 tokenów. Teksty przekraczające ten limit będą przycinane (*truncation*). Udział przyciętych tekstów zmierzę w Zadaniu 3.
* **Audyt duplikatów:**
    * **Dokładne duplikaty** (*exact duplicates*): 0 wierszy w całym zbiorze.
    * **Prawie-duplikaty** (*near-duplicates*, po normalizacji: małe litery, bez interpunkcji i nadmiarowych spacji): 1 grupa (2 przykłady) przekraczająca granicę podziału między `train` (id 3179) a `test` (id 160). Oba przykłady mają tę samą etykietę `zero`.

**Liczba niezależnych jednostek i stabilność estymaty.** Jednostką jest recenzja, więc liczba jednostek równa się liczbie przykładów. Recenzje tego samego autora lub obiektu nie są jednak w pełni niezależne, a zbiór nie pozwala tego sprawdzić. Faktyczna liczba niezależnych jednostek może więc być mniejsza. Validation i test mają po około 820 recenzji, ale klasy `amb` i `zero` liczą w nich tylko 118–155 przykładów. F1 tych klas, a przez to Macro-F1, może się więc wahać o kilka punktów procentowych. Wyniki na validation będę raportować z przedziałami ufności z bootstrapu, a małych różnic między modelami nie będę interpretować jako przewagi.

### Analiza wycieku danych (Data Leakage)

1. **Prawie-duplikaty:** pojedyncza para prawie-duplikatów przekraczająca granicę `train`–`test` została odnotowana w audycie. Oficjalny podział PolEmo 2.0 jest zamrożony, więc nie modyfikuję ręcznie zbiorów i traktuję tę parę jako zmierzone ograniczenie zbioru źródłowego. Dotyczy 1 z 820 przykładów testowych (0,12%).
2. **Ten sam autor lub obiekt po obu stronach podziału:** recenzje tego samego hotelu, lekarza albo produktu mogą trafić do różnych zbiorów, a model może zapamiętać nazwy własne skorelowane z wydźwiękiem. Bez metadanych nie da się temu zapobiec. Opisuję to jako ograniczenie, a w analizie błędów sprawdzę, czy model opiera się na nazwach własnych.
3. **Brak przecieku TF-IDF:** transformacja TF-IDF oraz dopasowanie słownika i wag IDF (`fit`) będą wykonywane wyłącznie na zbiorze treningowym, w ramach `Pipeline` scikit-learn.
4. **Brak przecieku preprocessingu:** standaryzacja cech (np. `StandardScaler` na embeddingach HerBERTa) i czyszczenie danych będą dopasowywane wyłącznie na statystykach ze zbioru treningowego.
5. **Zamrożenie zbioru testowego:** zbiór final test (`test_ids.csv`) zostaje zamrożony na etapie Zadania 1 i nie będzie używany do trenowania, selekcji modeli ani strojenia hiperparametrów. Do tego służy wyłącznie validation.
6. **Wiedza z pretreningu:** HerBERT był trenowany na dużych polskich korpusach internetowych, które mogły zawierać te same recenzje. Tego nie da się wykluczyć, więc opisuję to jako ograniczenie porównania.

### Podział, metryki i losowość

* **Podział:** oficjalny podział autorów zbioru (train / validation / test, ok. 80/10/10%), bez zmian. Dzięki temu wyniki są porównywalne z literaturą. Rozkład klas w zbiorach jest zbliżony, a podział grupowy nie jest możliwy z powodu braku identyfikatorów autorów.
* **Metryka główna:** **Macro-F1**. Uwzględnia nierównowagę klas i daje równą wagę każdej klasie, w tym najtrudniejszej klasie `amb`. Jest też metryką zalecaną w karcie zbioru.
* **Metryki pomocnicze:** accuracy, F1 dla poszczególnych klas oraz macierz pomyłek (*confusion matrix*).
* **Ziarno losowości (seed):** `RANDOM_STATE = 2026`. Sam podział jest oficjalny i nie zawiera losowości. Seed stosuję we wszystkich modelach i wszędzie, gdzie występuje losowość (losowanie przykładów, bootstrap, `numpy`, `torch`).
* **Final test:** zamrożony w commicie z tagiem `task-1`, identyfikatory w `splits/` (kolumna `id` = numer wiersza w oficjalnym zbiorze). Jeśli podział był później poprawiany, podaj commit poprawionej wersji i opisz zmianę w dzienniku zmian.

## Wyniki (Zadania 2 do 5)

Wyniki na validation:

| Podejście | Zadanie | Metryka główna | Metryki pomocnicze | Czas i sprzęt | Uwagi |
|---|---|---|---|---|---|
| Trivial baseline | 2 | | | | |
| Baseline | 2 | | | | |
| Podejście pretrained | 3 | | | | |
| Rozszerzenie | 4 | | | | |

Wynik na final test, wyłącznie dla finalnego systemu i dopiero po utworzeniu tagu `final-freeze`:

| System | Metryka główna | Metryki pomocnicze |
|---|---|---|
| [nazwa z `final_system.md`] | | |

## Finalny system (Zadanie 5)

Pełny zapis jest w `final_system.md`. [Krótkie uzasadnienie wyboru na podstawie validation.]

## Reprodukcja

[Wersja Pythona, instalacja środowiska, pobranie danych, kolejność uruchamiania notebooków albo skryptów, sprzęt, przybliżony czas.]

## Ograniczenia

[Ograniczenia danych, protokołu i wyników. Czego wynik nie dowodzi.]

## Dziennik zmian

| Data | Zadanie | Co zmieniono i dlaczego |
|---|---|---|
| 2026-11-08 | 1 | Audyt danych, zapis oficjalnego podziału w `splits/`, uzupełnienie sekcji problemu, danych i protokołu. |
| 2026-11-08 | 1 | Przeniesienie skryptu audytu z `templates/` do `src/` (zgodnie z przeznaczeniem katalogów). Podział danych bez zmian. Tag `task-1` wskazuje commit `ae05713` sprzed przeniesienia. |

## Licencja projektu

[Na przykład MIT. Dane używane zgodnie z licencją opisaną w sekcji „Dane i licencja”.]