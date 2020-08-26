from pyautogui import *
import pyautogui as pq
import time
import keyboard
def click(x,y):
    pq.moveTo(x,y)
    pq.mouseDown()
    time.sleep(0.01) 
    pq.mouseUp()
while keyboard.is_pressed('q') == False:
    
    if pq.pixel(480, 552)[0] == 0:
        click(480, 552)
    if pq.pixel(590, 561)[0] == 0:
        click(590, 561)
    if pq.pixel(700, 571)[0] == 0:
        click(700, 571)
    if pq.pixel(800, 569)[0] == 0:
        click(800, 569)
