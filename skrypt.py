from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pyautogui
import os

# Ustawienia
pdf_url = "https://upkrakow-my.sharepoint.com/personal/mateusz_lasek_student_up_krakow_pl/_layouts/15/onedrive.aspx?id=%2Fpersonal%2Fmateusz%5Flasek%5Fstudent%5Fup%5Fkrakow%5Fpl%2FDocuments%2Ftestowy%2FDokument%20bez%20tytu%C5%82u%2Epdf&parent=%2Fpersonal%2Fmateusz%5Flasek%5Fstudent%5Fup%5Fkrakow%5Fpl%2FDocuments%2Ftestowy"
output_folder = r"D:\Egzamin_inzynierski\skrypt_screeny\screeny"  # Folder do zapisywania screenshotów

# Upewnij się, że folder istnieje
os.makedirs(output_folder, exist_ok=True)

# Ścieżka do WebDrivera
driver_path = r"D:\Egzamin_inzynierski\skrypt_screeny\chromedriver.exe"
service = Service(driver_path)

# Konfiguracja Selenium
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# Otwórz PDF w przeglądarce
driver.get(pdf_url)
print("Otworzono przeglądarkę. Zaloguj się na konto i otwórz PDF.")
input("Po zakończeniu logowania i załadowaniu PDF, naciśnij ENTER...")

# Zmiana na pełny ekran
time.sleep(4)
pyautogui.press('f11') # Symulacja naciśnięcia klawisza F11

# Zrób zrzuty ekranu każdej strony PDF
page_number = 1
while True:
    try:
        # Zrób zrzut ekranu
        screenshot = pyautogui.screenshot()
        screenshot.save(f"{output_folder}\\page_{page_number}.png")
        print(f"Zapisano stronę {page_number}")

        # Przewiń do następnej strony
        driver.find_element(By.TAG_NAME, "body").send_keys(Keys.PAGE_DOWN)
        time.sleep(2)  # Poczekaj na załadowanie następnej strony

        page_number += 1

    except Exception as e:
        print(f"Zakończono na stronie {page_number - 1}: {e}")
        break

# Zamknij przeglądarkę
driver.quit()
