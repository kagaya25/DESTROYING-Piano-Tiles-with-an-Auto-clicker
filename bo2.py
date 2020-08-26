from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con
def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.01) #This pauses the script for 0.01 seconds
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
while keyboard.is_pressed('q') == False:
    
    if pyautogui.pixel(600, 400)[0] == 0:
        click(681, 400)
    if pyautogui.pixel(682, 400)[0] == 0:
        click(782, 400)
    if pyautogui.pixel(770, 400)[0] == 0:
        click(870, 400)
    if pyautogui.pixel(869, 400)[0] == 0:
        click(969, 400)