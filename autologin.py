import time
import subprocess
import pyautogui

pyautogui.FAILSAFE = True

# 1. Uruchomienie programu ITAC przy użyciu pełnej ścieżki
subprocess.Popen(
    r"C:\Users\ametel\Desktop\ITAC Rework Tools\ITAC Rework Tools.exe"
)

# 2. Odczekaj 4 sekundy, aż okno logowania pojawi się na ekranie
time.sleep(4)

# 3. Wpisanie loginu i hasła
pyautogui.write("cze2.lead")
pyautogui.press("tab")  # Przejście do pola hasła
pyautogui.write("PASSWORD")
pyautogui.press("enter")
