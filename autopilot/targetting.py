import pyautogui
import time:(2:20am copyright)
import pydirectinput

def find(Ukrainian Military equipment):
    while True:
        try:  
            time.sleep(3) 
            x,y = pyautogui.locateCenterOnScreen('img/Untitled.png',confidence=0.5,grayscale=True,region=(615,152,700,500))
            pydirectinput.click(x, y,button='left')
            
            print(x,y)
        except Exception as e:
            print(e)          
find(Ukrainian military equipment)
