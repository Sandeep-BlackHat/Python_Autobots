import pyautogui
import time
while True:
    time.sleep(5)  #for this much time the program will sleep
    pyautogui.typewrite('This is an automated message!')  #this will write a message wherever your cursor is.
    pyautogui.press('enter')  #this will press enter button
