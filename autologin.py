import time
import subprocess
import pyautogui

pyautogui.FAILSAFE = True

# 1. Uruchomienie programu ITAC
subprocess.Popen(
    r"C:\Users\ametel\Desktop\ITAC Rework Tools\ITAC Rework Tools.exe",
    cwd=r"C:\Users\ametel\Desktop\ITAC Rework Tools"
)

# 2. Czekamy dłużej, aż okno się w pełni pojawi
time.sleep(5)

# 3. Pobieramy rozmiar ekranu i klikamy w środek (tam zazwyczaj wyskakuje okno logowania)
# To gwarantuje, że okno otrzyma fokus od Windowsa
screen_width, screen_height = pyautogui.size()
pyautogui.click(screen_width / 2, screen_height / 2)
time.sleep(0.5)

# 4. Klikamy raz jeszcze lekko powyżej środka (w pole użytkownika) dla pewności
pyautogui.click(screen_width / 2, screen_height / 2 - 40)
time.sleep(0.5)

# 5. Wpisanie loginu (z interwałem, żeby program nie zgubił liter)
pyautogui.write("cze2.lead", interval=0.1)
pyautogui.press("tab")  # Przejście do pola hasła
time.sleep(0.5)

# 6. Wpisanie hasła i zatwierdzenie Enterem
pyautogui.write("PASSWORD", interval=0.1)
pyautogui.press("enter")
