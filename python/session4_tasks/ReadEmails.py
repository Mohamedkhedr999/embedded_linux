import pyautogui
import time

pyautogui.hotkey("win")
time.sleep(1)
pyautogui.write("gm")
time.sleep(1)
pyautogui.hotkey("enter")
#time.sleep(2)
islocated = None
while islocated == None :
    islocated=pyautogui.locateOnScreen("/home/khedr/Documents/myfiles/Screenshot from 2023-08-27 23-08-04.png",confidence=0.9)

pyautogui.moveTo(islocated[0],islocated[1],duration=0.5)
pyautogui.click()
islocated = None
while islocated == None :
    islocated=pyautogui.locateOnScreen("/home/khedr/Documents/myfiles/Screenshot from 2023-08-27 23-08-29.png",confidence=0.9)

pyautogui.moveTo(islocated[0]+30,islocated[1]+10,duration=0.5)
pyautogui.click()