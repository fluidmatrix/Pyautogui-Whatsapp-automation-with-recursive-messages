import pyautogui
import webbrowser as wb
import time

wb.open("https://web.whatsapp.com")
time.sleep(15)
for i in range(101):
    pyautogui.typewrite(f"kaam karlo, yeh {i} dhamki hai\n")
    pyautogui.press("enter")
