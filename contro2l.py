import mediapipe as mp
from math import hypot
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import numpy as np
import cv2
import keyboard
from pynput import keyboard as key2
import asyncio
import time
import winsound

motion = False
looper = True
play = True

def on_activate_a():
    print('<ctrl>+<alt>+<win> pressed')
    winsound.Beep(350, 50)
    global motion
    motion=True

with key2.GlobalHotKeys({'<ctrl>+<alt>+<cmd>': on_activate_a}) as listener:
    
    while looper:

        motion = False
        repeater = True

        print("start")
        winsound.Beep(300, 250)
        cap = cv2.VideoCapture(0) #Checks for 
        print("cam loaded")
        winsound.Beep(500, 175)

        mpHands = mp.solutions.hands #detects hand/finger
        hands = mpHands.Hands()   #complete the initialization configuration of hands
        mpDraw = mp.solutions.drawing_utils

        #To access speaker through the library pycaw 
        #devices = AudioUtilities.GetSpeakers()
        #interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
        #volume = cast(interface, POINTER(IAudioEndpointVolume))
        #volbar=400
        #volper=0

        length=0 

        y_in=0
        y_mid=0

        x_in=0
        x_mid=0

        delta_y_in=0

        zoom = False

        #volMin,volMax = volume.GetVolumeRange()[:2]

        while not motion: 
            if repeater:
                print("waiting..")
                repeater=False

            time.sleep(1)
        
        while motion:
            success,img = cap.read() #If camera works capture an image
            imgRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB) #Convert to rgb
            
            #Collection of gesture information
            results = hands.process(imgRGB) #completes the image processing.
        
            lmList = [] #empty list
            if results.multi_hand_landmarks: #list of all hands detected.
                #By accessing the list, we can get the information of each hand's corresponding flag bit
                for handlandmark in results.multi_hand_landmarks:
                    for id,lm in enumerate(handlandmark.landmark): #adding counter and returning it
                        # Get finger joint points
                        h,w,_ = img.shape
                        cx,cy = int(lm.x*w),int(lm.y*h)
                        lmList.append([id,cx,cy]) #adding to the empty list 'lmList'
                    mpDraw.draw_landmarks(img,handlandmark,mpHands.HAND_CONNECTIONS)

            if lmList != []:
                #getting the value at a point
                                #x      #y
                x1,y1 = lmList[4][1],lmList[4][2]  #thumb
                x2,y2 = lmList[8][1],lmList[8][2]  #index finger

                x3,y3 = lmList[12][1],lmList[12][2]  #mid finger
                x4,y4 = lmList[16][1],lmList[16][2]  #four finger
                x5,y5 = lmList[18][1],lmList[18][2]  #pinky finger

                #print ("middle x " +  str(x3) + " y " + str(y3))

                #creating circle at the tips of thumb and index finger
                cv2.circle(img,(x1,y1),13,(255,0,0),cv2.FILLED) #image #fingers #radius #rgb
                cv2.circle(img,(x2,y2),13,(255,0,0),cv2.FILLED) #image #fingers #radius #rgb
                cv2.circle(img,(x3,y3),13,(255,0,0),cv2.FILLED) #image #fingers #radius #rgb
                cv2.circle(img,(x4,y4),13,(255,0,0),cv2.FILLED) #image #fingers #radius #rgb
                cv2.circle(img,(x5,y5),13,(255,0,0),cv2.FILLED) #image #fingers #radius #rgb

                cv2.line(img,(x1,y1),(x2,y2),(255,0,0),3)  #create a line b/w tips of index finger and thumb
                cv2.line(img,(x1,y1),(x3,y3),(255,0,0),3)  #create a line b/w tips of index finger and thumb     
                cv2.line(img,(x1,y1),(x4,y4),(255,0,0),3)  #create a line b/w tips of index finger and thumb    
                cv2.line(img,(x1,y1),(x5,y5),(255,0,0),3)  #create a line b/w tips of index finger and thumb    

        
                #prev_len = length    
                length = hypot(x2-x1,y2-y1) #distance b/w tips using hypotenuse

                length_mid = hypot(x3-x1,y3-y1)

                #length_four = hypot(x4-x1,y4-y1)

                length_five = hypot(x5-x1,y4-y1)

                #delta = np.abs(length-prev_len)
            
                prev_y_in = y_in
                y_in = y2

                prev_x_in = x_in
                x_in = x2

                prev_y_mid= y_mid
                y_mid = y3

                prev_x_mid= x_mid
                x_mid = x3

                #prev_delta_y_in = delta_y_in
                
                delta_y_in = y_in - prev_y_in

                delta_y_mid = y_mid - prev_y_mid

                delta_x_in = x_in - prev_x_in

                delta_x_mid = x_mid - prev_x_mid

                #double_d = np.abs(delta_y_in-prev_delta_y_in)

                if 12<np.abs(delta_y_in) and length <30 and length_mid>50 and play:
                    if delta_y_in>0 and not zoom:
                        keyboard.press_and_release('down arrow')
 #                       keyboard.press_and_release('down arrow')
                        print ("scroll down")

                if 12<np.abs(delta_y_mid) and length_mid <35 and length<30 and play:
                    if delta_y_mid<0 and not zoom:
                        keyboard.press_and_release('up arrow')
#                        keyboard.press_and_release('up arrow')
                        print ("scroll up")

                if 40<np.abs(delta_x_in) and length <30 and length_mid>50 and play: 
                    if delta_x_in<0 and not zoom:
                       # keyboard.press_and_release('Ctrl + one')
                        #zoom = True
                        print ("Zoom in")
                       # time.sleep(2)

                if 40<np.abs(delta_x_mid) and length_mid <35 and length<30 and play:
                    if delta_x_mid>0 and zoom:
                      #  keyboard.press_and_release('Ctrl + one')
                       # zoom=False
                        print ("Zoom out")
                       # time.sleep(2)
                 
                if length_five > 300:
                    play = not play 
                    
                    if play:
                        winsound.Beep(100, 150)
                        winsound.Beep(400, 150)
                        print("gesture recognition started ...")
                    else:
                        winsound.Beep(100, 250)
                        print("gesture recognition stopped ...")
                    time.sleep(3)

                if length_five > 400:
                    break
                        
            cv2.imshow('Image',img) #Show the video 
            if cv2.waitKey(1) & 0xff==ord(' '): #By using spacebar delay will stop
                break
        
        
        cap.release()     #stop cam    
        cv2.destroyAllWindows() #close window
        print("closing")

    listener.join()


  