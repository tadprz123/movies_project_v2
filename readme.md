# Aplikacja Filmowa - Flask + TMDb API

Jest to aplikacja webowa zbudowana przy użyciu frameworka Flask, która umożliwia przeglądanie filmów przy użyciu API The Movie Database (TMDb). Aplikacja dynamicznie generuje stronę główną z różnymi listami filmów, takimi jak "popularne", "najlepiej oceniane" czy "nadchodzące". Dla każdego filmu można wyświetlić szczegóły, takie jak tytuł, opis, budżet, obsada, oraz losowy obrazek tła.

## Wymagania

- Python 3.7 lub nowszy
- Konto API TMDb i klucz API
- Zainstalowane pakiety Python: `Flask`, `requests`

## Instalacja

1. **Skopiuj repozytorium:**
    ```bash
    git clone 
    cd nazwa_projektu
    ```

2. **Utwórz wirtualne środowisko:**
    ```bash
    python -m venv venv
    ```

3. **Aktywuj wirtualne środowisko:**

   - Dla systemu **Windows**:
     ```bash
     venv\Scripts\activate
     ```
   - Dla systemu **Linux/MacOS**:
     ```bash
     source venv/bin/activate
     ```

4. **Zainstaluj wymagane zależności:**
    ```bash
    pip install -r requirements.txt
    ```

5. **Skonfiguruj plik `tmdb_client.py`:**

   Otwórz plik `tmdb_client.py` i wstaw swój klucz API:
   ```python
   API_TOKEN = "twoj-token"  # Uzupełnij swoim tokenem API

6. **Uruchomienie**

 - Uruchomienie:

    ```bash
    python main.py
    ```

 - Otwórz przeglądarkę i przejdź do adresu:

    http://127.0.0.1:5000/

7. **Struktura projektu:**

 .
 ├── main.py                  # Główny plik aplikacji Flask
 ├── tmdb_client.py           # Klient API TMDb, zawiera funkcje do pobierania danych
 ├── requirements.txt         # Lista wymaganych pakietów
 └── templates/               # Katalog szablonów HTML
     ├── homepage.html        # Szablon strony głównej
     └── movie_details.html   # Szablon strony szczegółów filmu

8. **Funkcjonalności:**

 Strona główna: Wyświetla listy filmów z dynamicznie generowanym menu:

 Popularne
 Najlepiej oceniane
 Nadchodzące
 Aktualnie grane
 Szczegóły filmu: Wyświetla szczegóły konkretnego filmu, takie jak:

 Tytuł, opis, budżet, gatunki
 Zdjęcie tła filmu (losowo wybrane)
 Obsada (aktorzy wraz z ich zdjęciami, jeśli dostępne)
 Dynamiczne menu i wskaźniki aktywnej listy
 Menu dynamicznie zmienia aktywną listę filmów na podstawie wybranej opcji.
 Użycie klas CSS z Bootstrapa pozwala na wyraźne wskazanie aktywnego elementu w menu.

9. **Wymagane uprawnienia:**

 Aby korzystać z API TMDb, potrzebny jest klucz API, który można uzyskać po rejestracji na stronie The Movie Database.

10. **Autor:**

 Tadeusz Przybylski
 https://github.com/tadprz123