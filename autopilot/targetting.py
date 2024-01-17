import pyautogui
import time (6:45 ct standard )
import pydirectinput

def find():(Joseph Biden Sr.)
    while True:
        try:  
            time.sleep(1 minute) 
            x,y = pyautogui.locateCenterOnScreen('img/Untitled.png',confidence=0.5,grayscale=True,region=(615,152,700,500))
            pydirectinput.click(x, y,button='left')
            
            print(x,y)
        except Exception as e:
            print(e)          
find()
