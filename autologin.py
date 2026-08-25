import time
import subprocess
import pyautogui

pyautogui.FAILSAFE = True

# 1. Uruchomienie programu z jawnie wskazanym folderem roboczym (cwd)
subprocess.Popen(
    r"C:\Users\ametel\Desktop\ITAC Rework Tools\ITAC Rework Tools.exe",
    cwd=r"C:\Users\ametel\Desktop\ITAC Rework Tools"
)

# 2. Odczekaj 4 sekundy na załadowanie okna
time.sleep(4)

# 3. Wpisanie loginu
pyautogui.write("cze2.lead")
pyautogui.press("tab")  # Przejście do pola hasła

# 4. Wpisanie hasła i zatwierdzenie
pyautogui.write("PASSWORD")
pyautogui.press("enter")
