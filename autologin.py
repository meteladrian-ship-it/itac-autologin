import time
import subprocess
import pyautogui

pyautogui.FAILSAFE = True

# 1. Uruchomienie programu ITAC
subprocess.Popen(
    r"C:\Users\ametel\Desktop\ITAC Rework Tools\ITAC Rework Tools.exe"
)

# 2. Odczekaj 4 sekundy na załadowanie okna
time.sleep(4)

# 3. Klikamy w pole użytkownika (zakładamy, że okno otwiera się na środku ekranu lub po prostu używamy bezpiecznych tabulatorów)
# Wyczyśćmy pole i wpiszemy login
pyautogui.press('tab') # upewnienie się co do fokusu
pyautogui.write("cze2.lead")

# 4. Przejście do pola hasła
pyautogui.press("tab")

# 5. Wpisanie hasła i zatwierdzenie
pyautogui.write("PASSWORD")
pyautogui.press("enter")
