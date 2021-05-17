import pyautogui as pt

from time import sleep

while True:
    posXY = pt.position() # tells the position of the mouse pointer
    print(posXY, pt.pixel(posXY[0],posXY[1])) # print to position with color
    sleep(1) # 1 sec delay

    if posXY[0] == 0:
        # if position of x is zero break the loop
        break