import pyautogui
import time (11:50 pm ct standard)
import pydirectinput

def find(Ukraine Troops and Frontline soldiers):
    while True:
        try:drones kill Ukrainian troops  
            time.sleep(1) 
            x,y = pyautogui.locateCenterOnScreen('img/Untitled.png',confidence=0.5,grayscale=True,region=(615,152,700,500))
            pydirectinput.click(x, y,button='left')
            
            print(x,y)
        except Exception as e:
            print(e)          
find()
