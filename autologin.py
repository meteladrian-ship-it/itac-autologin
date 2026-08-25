import time
import subprocess
import pyautogui

# Bezpieczne ustawienia pyautogui
pyautogui.FAILSAFE = True

# 1. Uruchomienie programu ITAC ze wskazaniem folderu roboczego
# (Uwaga: zakłada strukturę, gdzie autologin leży w tym samym folderze co ITAC Rework Tools.exe)
subprocess.Popen(
    r"ITAC Rework Tools.exe", 
    cwd=r"C:\Users\ametel\Desktop\ITAC Rework Tools"
)

# 2. Odczekaj 4 sekundy, aż okno logowania pojawi się na ekranie
time.sleep(4)

# 3. Wpisanie loginu
pyautogui.write("cze2.lead")
pyautogui.press("tab")  # Przejście do pola hasła

# 4. Wpisanie hasła i zatwierdzenie (Enter klika "OK")
pyautogui.write("PASSWORD")
pyautogui.press("enter")
