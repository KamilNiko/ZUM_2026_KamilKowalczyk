# Zgłoszenie tematu

Odpowiedź mieści się na jednej stronie. Projekt dotyczy nadzorowanej klasyfikacji jednolabelowej: każdy przykład ma dokładnie jedną klasę.

1. Roboczy tytuł:
Klasyfikacja wydźwięku polskich recenzji (PolEmo 2.0): Porównanie modelu TF-IDF z polskim enkoderem HerBERT.

2. Modalność (tekst, obraz, audio albo dane multimodalne):
Tekst (język polski)

3. Problem klasyfikacji (co jest klasą i ile jest klas):
Nadzorowana klasyfikacja jednolabelowa. Każda recenzja jest przypisana do dokładnie jednej z 4 klas wydźwięku: negatywny, pozytywny, neutralny oraz ambiwalentny

4. Pytanie eksperymentalne (co chcesz sprawdzić):
Czy polski model pretrendowany HerBERT (z zamrożonym enkoderem) uzyska wyższy wynik Macro-F1 na zbiorze walidacyjnym niż klasyczny baseline TF-IDF z regresją logistyczną, i czy największa przewaga HerBERTa wystąpi przy najtrudniejszej klasie ambiwalentnej (recenzje zawierające jednocześnie pochwały i zastrzeżenia)

5. Źródło danych (link):
Oficjalny zbiór PolEmo 2.0 (wariant `all_text`) udostępniony przez CLARIN-PL na platformie Hugging Face: `https://huggingface.co/datasets/clarin-pl/polemo2-official`

6. Przybliżona wielkość zbioru:
Łącznie 8 216 recenzji, z gotowym podziałem na zbiór treningowy (6 573), walidacyjny (823) i testowy (820). Średnia długość recenzji wynosi około 133 słowa.

7. Lista klas i sposób oznaczenia etykiet:
`minus` (negatywny, ~38%), `plus` (pozytywny, ~28%), `amb` (ambiwalentny, ~20%) oraz `zero` (neutralny, ~15%). Etykiety zostały ręcznie przygotowane przez autorów zbioru w schemacie niezależnych anotacji.

8. Licencja danych:
Licencja akademicka / niekomercyjna (CC BY-NC-SA 4.0 / CC BY-SA 4.0) — dozwolony użytek edukacyjny i badawczy z cytowaniem autorów publikacji.

9. Proponowana jednostka generalizacji:
Pojedyncza recenzja. Wykorzystuję oficjalny podział `train` / `validation` / `test`. Ze względu na brak identyfikatorów autorów lub ocenianych obiektów w zbiorze, brak możliwości wykluczenia ich powtórzeń traktuję i opisuję jako ograniczenie projektu.

10. Planowany baseline:
* Trivial baseline: Przewidywanie najczęstszej klasy (`minus`).
* Właściwy baseline: TF-IDF (unigramy i bigramy) z Regresją Logistyczną (`class_weight="balanced"`)

11. Wstępny pomysł na model pretrained:
Wstępny pomysł na model pretrained: Model `allegro/herbert-base-cased` wykorzystany jako zamrożony enkoder. Wektory reprezentacji tekstu (uśrednione `mean pooling`) zostaną przekazane do takiego samego klasyfikatora Regresji Logistycznej, aby porównanie z baseline było sprawiedliwe.

12. Potencjalne ograniczenia obliczeniowe:
Brak istotnych ograniczeń. Baseline na CPU trenuje się w kilka sekund, a wygenerowanie embeddingów HerBERTa na darmowym GPU w Colab zajmie zaledwie kilka minut (wyliczone wektory zostaną zapisane do ponownego użycia).

13. Dane osobowe, wrażliwe albo z ograniczeniami dostępu lub redystrybucji (tak albo nie; jeśli tak, jak je przechowasz):
Tak (częściowo). Recenzje ze zbioru zawierają imiona i nazwiska ocenianych osób (np. wykładowców czy lekarzy). Aby zachować prywatność oraz zasady licencji, surowe teksty nie będą umieszczane w publicznym repozytorium GitHub. Pliki w katalogu `splits/` będą zawierać wyłącznie numery wierszy, a dane będą pobierane bezpośrednio skryptem. 
