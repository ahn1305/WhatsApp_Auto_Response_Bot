# imports 
import pyautogui as pt
from time import sleep
import pyperclip
import os

#------------------------------------------------------------------------------------------

sleep(5) # delay the program for 5 seconds

position1 = pt.locateOnScreen("images/smile_paperclip.png",confidence=.6) 
#locate the smilie_paperclip_png, confidence looks 60 percent alike to the picture
x = position1[0]
y = position1[1]

#------------------------------------------------------------------------------------------

#gets message
def gets_message():
    global x,y

    position = pt.locateOnScreen("images/smile_paperclip.png",confidence=.6)
    x = position[0]
    y = position[1]
    pt.moveTo(x, y, duration=.9)
    pt.moveTo(x + 70, y - 70, duration=.9) #more uppercorner moves to zero, bottom - larger
    pt.tripleClick()
    pt.rightClick()
    pt.moveRel(12,15)
    pt.click()
    whatsapp_message = pyperclip.paste()
    pt.click()
    print("Message received: " + whatsapp_message)
    os.system("spd-say "+whatsapp_message)
    return whatsapp_message
    

#Posts 
def post_response(message):

    position = pt.locateOnScreen("images/smile_paperclip.png",confidence=.6)
    x = position[0]
    y = position[1]
    pt.moveTo(x + 200, y + 20, duration=.5)
    pt.click()
    pt.typewrite(message, interval=.01)

    pt.typewrite("\n", interval=.01)



## Process response
def process_response(message):
    if str(message) == "Hi" or str(message) == "Hii" or str(message) == "Hi da" or str(message) == "Hii da":
        return "Hi"
    elif str(message) == "How are you" or str(message) == "How are you?" or str(message) == "How are u" or str(message) == "How are u?" or str(message) == "How r you" or str(message) == "How r you?" or str(message) == "How r u" or str(message) == "How r u?":
        return "Iam fine !!"
    else:
        return "Error: Iam not trained to answer this -- AWBOT"
    

# Check for new messages

def check_for_new_messages():
    pt.moveTo(x+70,y-50, duration=.5)

    while True:
        #Continuously checks for green dot and new messages
        try:
            position = pt.locateOnScreen("images/green_circle_1.png", confidence=.7)
            if position is not None:
                pt.moveTo(position)
                pt.moveRel(-100,0)
                pt.click()
                sleep(0.5)

        except(Exception):
            print("No new messages")

        if pt.pixelMatchesColor(int(x+70), int(y-50), (255,255,255), tolerance=10):
            print("it is white")
            processed_message = process_response(gets_message())
            post_response(processed_message)
        else:
            print("No new messages")
        
        sleep(5)


check_for_new_messages()
#processed_message = process_response(gets_message())
#post_response(processed_message)

