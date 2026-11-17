# Podstawy-przetwarzania-Obrazu
Przetwarzanie obrazów z użyciem Pythona
Projekt przedstawia podstawowe operacje przetwarzania obrazu rastrowego z wykorzystaniem języka Python oraz popularnych bibliotek.

# Wykorzystane biblioteki
* **OpenCV (cv2)**  – wczytywanie, zmiana rozmiaru, konwersja i obracanie obrazu.
* **NumPy (numpy)** – przekształcanie danych obrazu w tablice liczb oraz operacje na macierzach.
* **Matplotlib (matplotlib.pyplot)** – wyświetlanie oryginalnego i przetworzonego obrazu.
* **Urllib (urllib.request)** – pobieranie obrazu z internetu.

# Wykonane operacje w projekcie
* Pobranie obrazu z internetu – wykorzystanie adresu URL oraz modułu urllib.request.
* Wczytanie obrazu – odczyt pobranych danych za pomocą funkcji cv2.imdecode().
* Wyświetlenie oryginalnego obrazu – prezentacja obrazu w kolorach RGB przy użyciu biblioteki Matplotlib.
* Zmniejszenie rozdzielczości – pomniejszenie szerokości i wysokości obrazu o 50% za pomocą cv2.resize().
* Konwersja do skali szarości (grayscale) – zmiana obrazu kolorowego na odcienie szarości przy użyciu cv2.cvtColor().
* Obrót obrazu – obrócenie obrazu o 90 stopni zgodnie ze wskazówkami zegara za pomocą cv2.rotate().
* Wyświetlenie obrazu wynikowego – prezentacja obrazu po wykonanych operacjach.
* Wyświetlenie macierzy obrazu – wypisanie wymiarów tablicy oraz fragmentu macierzy zawierającego wartości pikseli (5x5).
