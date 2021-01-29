import os
import time

import pyautogui
screenWidth, screenHeight = pyautogui.size()

currentMouseX, currentMouseY = pyautogui.position()
pyautogui.moveTo(45, 1015)
time.sleep(1)
pyautogui.click() 
pyautogui.write('Notepad', interval=0.05)
time.sleep(1)
pyautogui.press('enter')
time.sleep(1)
pyautogui.write('bruh', interval=0.05)
