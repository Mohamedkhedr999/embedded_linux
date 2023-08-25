#!/usr/bin/python3

import pyautogui
import time


pyautogui.hotkey("win")
time.sleep(0.5)
pyautogui.write("vs")
isfound = None
while isfound == None:
    isfound = pyautogui.locateOnScreen("/home/khedr/Documents/myfiles/vscode.png",confidence=0.7)

pyautogui.moveTo(isfound[0]+16,isfound[1]+20,duration=0.5)   
time.sleep(1)
pyautogui.click()
time.sleep(5)

myextension= ["clan","c++ testmate","c++ helper","cmake","cmake tool"]
pyautogui.hotkey("ctrl","shift","x")

for i in myextension:
    pyautogui.write(i)
    isfound = None
    while isfound == None:
        isfound = pyautogui.locateOnScreen("/home/khedr/Documents/myfiles/"+i+".png",confidence=0.7)
    
    pyautogui.moveTo(isfound[0]+16,isfound[1]+20,duration=0.5)  

    pyautogui.click()

    pyautogui.moveTo(723,258,duration=0.5)    

    pyautogui.click()
    pyautogui.moveTo(219,148,duration=0.5)   
    pyautogui.click()
    pyautogui.hotkey("ctrl","a")

