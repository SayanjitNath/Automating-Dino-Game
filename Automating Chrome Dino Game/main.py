import pyautogui # pip install pyautogui
from PIL import Image, ImageGrab # pip install pillow
import time

def hit(key):
    pyautogui.keyDown(key)
    return

def isCollide(data):
    for i in range(250, 300):
        for j in range(410, 563):
            if data[i, j] < 171:
                hit("down")
                return

    for i in range(350, 500):
        for j in range(700, 710):
            if data[i, j] < 100:
                hit("up")
                return
    return

if __name__ == "__main__":
    print("Hey.. Dino game about to start in 3 seconds")
    time.sleep(2)
    # hit('up') 

    while True:
        image = ImageGrab.grab().convert('L')  
        data = image.load()
        isCollide(data)



        # Draw the rectangle for cactus
        # for i in range(350, 550):
        #     for j in range(700, 710):
        #         data[i, j] = 0
        
        # # Draw the rectangle for birds
        # for i in range(250, 300):
        #     for j in range(410, 563):
        #         data[i, j] = 171

        # image.show()
        # break
      

