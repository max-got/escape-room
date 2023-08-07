#Import the necessary Packages and scritps for this software to run 
import cv2
import mediapipe as freedomtech
from gtts import gTTS
import os
from collections import Counter
#from module import findnameoflandmark, findpostion, speak
import math
import RPi.GPIO as GPIO
import time
from sense_hat import SenseHat

sense = SenseHat()

drawingModule = freedomtech.solutions.drawing_utils
handsModule = freedomtech.solutions.hands

mod=handsModule.Hands()


h=480
w=640

def main():

    sense.clear()

    #Use CV2 Functionality to create a Video stream and add some values + variables
    cap = cv2.VideoCapture(0)
    tip=[8,12,16,20]
    tipname=[8,12,16,20]


    text=""

    sequence=[]

    #Farben
    r = (255,0,0)
    b = (0,0,255)
    y = (255,255,0)
    o = (0,0,0)
    w = (255,255,255)

    #Bilder als Listen
    logo = [
            r, w, r, w, r, w, r, w,
            w, w, w, w, w, w, w, w,
            r, r, r, r, r, r, r, w,
            w, w, w, w, w, w, w, w,
            r, r, r, r, r, r, r, w,
            w, w, w, w, w, w, w, w,
            r, w, r, w, r, w, r, w,
            w, r, w, r, w, r, w, w,
            ]

    love = [
            w, r, r, w, w, r, r, w,
            r, r, r, r, r, r, r, r,
            r, r, r, r, r, r, r, r,
            r, r, r, r, r, r, r, r,
            w, r, r, r, r, r, r, w,
            w, w, r, r, r, r, w, w,
            w, w, r, r, r, r, w, w,
            w, w, w, r, r, w, w, w,
            ]

    sad = [
            w, w, y, y, y, y, w, w,
            w, y, y, y, y, y, y, w,
            y, w, w, y, y, w, w, y,
            y, w, o, y, y, o, w, y,
            y, y, b, y, y, b, y, y,
            y, y, b, y, y, b, y, y,
            w, y, o, o, o, o, y, w,
            w, w, y, y, y, y, w, w,
            ]
            
#Create an infinite loop which will produce the live feed to our desktop and that will search for hands
    while True:
        ret, frame = cap.read() 

        
        #Determines the frame size, 640 x 480 offers a nice balance between speed and accurate identification
        frame1 = cv2.resize(frame, (640, 480))
        
        #Below is used to determine location of the joints of the fingers 
        a=findpostion(frame1)
        b=findnameoflandmark(frame1)
        
        if len(b and a)!=0:
                
            if indexUp(a) and middleDown(a) and ringDown(a) and pinkyUp(a) and thumbUp(a):
                sense.set_pixels(love)
                #text="I <3 U"
                #print(text)
                
            if indexDown(a) and middleUp(a) and ringDown(a) and pinkyDown(a) and thumbDown(a):
                sense.set_pixels(sad)
                #text=":("
                #print(text)
            
            #Alle Buchstaben des Alphabets in ALS uebersetzt
            #Aufrufen der Funktion detected() wenn Buchstabe erkannt wird
            if indexDown(a) and middleDown(a) and ringDown(a) and pinkyDown(a) and a[4][2:] < a[3][2:] and a[4][1:] > a[0][1:] and a[4][1:] > a[6][1:] and a[4][2:] < a[7][2:]    :
                detected("A", sequence)
                
            if indexUp(a) and middleUp(a) and ringUp(a) and pinkyUp(a) and thumbDown(a):
                detected("B", sequence)
            
            if  a[8][1:] > a[7][1:] > a[6][1:] and a[12][1:] > a[11][1:] > a[10][1:] and a[16][1:] > a[15][1:] > a[14][1:] and a[20][1:] > a[19][1:] > a[18][1:] and a[4][1:] > a[3][1:] > a[2][1:] and a[4][2:] > a[5][2:]:
                detected("C", sequence)
            
            if a[8][2:] < a[6][2:] and a[12][2:] > a[11][2:] > a[10][2:] and a[16][2:] > a[15][2:] > a[14][2:] and a[20][2:] > a[19][2:] > a[18][2:] and a[4][1:] < a[5][1:]:
                detected("D", sequence)
                
            if a[8][2:] > a[7][2:] > a[6][2:] and a[12][2:] > a[11][2:] > a[10][2:] and a[16][2:] > a[15][2:] > a[14][2:] and a[20][2:] > a[19][2:] > a[18][2:] and a[4][1:] < a[5][1:] and a[4][2:] > a[12][2:] and a[4][2:] > a[16][2:]:
                detected("E", sequence)
                
            if indexDown(a) and middleUp(a) and ringUp(a) and pinkyUp(a) and thumbUp(a):
                detected("F", sequence)
            
            if a[8][1:] < a[7][1:] < a[6][1:] < a[5][1:] and a[12][1:] > a[11][1:] > a[10][1:]  and a[16][1:] > a[15][1:] > a[14][1:] and a[20][1:] > a[19][1:] > a[18][1:] and a[4][1:] < a[3][1:] < a[2][1:] < a[1][1:]:  
                detected("G", sequence)
                
            if a[8][1:] < a[7][1:] < a[6][1:] < a[5][1:] and a[12][1:] < a[11][1:] < a[10][1:] < a[9][1:] and a[16][1:] > a[15][1:] > a[14][1:] and a[20][1:] > a[19][1:] > a[18][1:] and a[4][1:] < a[3][1:] < a[2][1:] < a[1][1:]:  
                detected("H", sequence)
                
            if indexDown(a) and middleDown(a) and ringDown(a) and pinkyUp(a) and thumbUp(a) and a[13][1:] > a[0][1:]:
                detected("I", sequence)
            
            if indexDown(a) and middleDown(a) and ringDown(a) and a[20][2:] < a[19][2:] < a[18][2:] < a[17][2:] and a[4][1:] < a[3][1:] and a[3][2:] < a[2][2:] and a[13][1:] < a[0][1:]:
                detected("J", sequence)
                
            if indexUp(a) and middleUp(a) and ringDown(a) and pinkyDown(a) and thumbUp(a) and a[9][1:] < a[4][1:] < a[5][1:] and a[4][2:] < a[5][2:]:
                detected("K", sequence)
                
            if indexUp(a) and middleDown(a) and ringDown(a) and pinkyDown(a) and a[4][1:] > a[3][1:] > a[2][1:]:
                detected("L", sequence)
            
            if indexDown(a) and middleDown(a) and ringDown(a) and pinkyDown(a) and a[14][1:] > a[4][1:] > a[17][1:]:
                detected("M", sequence)
                
            if indexDown(a) and middleDown(a) and ringDown(a) and pinkyDown(a) and a[11][1:] > a[4][1:] > a[15][1:] and a[4][2:] > a[13][2:]:
                detected("N", sequence)
                
            if  a[8][1:] > a[7][1:] > a[6][1:] and a[12][1:] > a[11][1:] > a[10][1:] and a[16][1:] > a[15][1:] > a[14][1:] and a[20][1:] > a[19][1:] > a[18][1:] and a[4][1:] > a[3][1:] > a[2][1:] and a[4][2:] < a[8][2:]:
                detected("O", sequence)
                
    #P und Q Handhaltung wird nicht erkannt :(          
    #        if a[8][1:] < a[7][1:] < a[6][1:] and middleDown() and a[12][2:] > a[4][2:] > a[11][2:] and a[4][1:] < a[3][1:]:
    #            detected("P", sequence)
    #          
    #        if a[8][2:] > a[7][2:] > a[6][2:] and a[4][2:] > a[3][2:] > a[2][2:] and :
    #            detected("Q", sequence)
                
            if indexUp(a) and middleUp(a) and ringDown(a) and pinkyDown(a) and a[4][2:] < a[3][2:] and a[8][1:] < a[12][1:]:
                detected("R", sequence)
            
            if indexDown(a) and middleDown(a) and ringDown(a) and pinkyDown(a) and a[4][1:] < a[6][1:] and a[4][2:] < a[11][2:] and a[10][2:] < a[4][2:] < a[11][2:]:
                detected("S", sequence)
                
            if indexDown(a) and middleDown(a) and ringDown(a) and pinkyDown(a) and a[10][1:] < a[4][1:] < a[6][1:] and a[4][2:] < a[10][2:]:
                detected("T", sequence)
                
            if indexUp(a) and middleUp(a) and ringDown(a) and pinkyDown(a) and thumbDown(a):
                detected("U", sequence)
                
            if indexUp(a) and middleUp(a) and ringDown(a) and pinkyDown(a) and thumbDown(a) and a[12][1:] < a[9][1:]:
                detected("V", sequence)
                
            if indexUp(a) and middleUp(a) and ringUp(a) and pinkyDown(a) and thumbDown(a):
                detected("W", sequence)
                
            if middleDown(a) and ringDown(a) and pinkyDown(a) and thumbDown(a) and a[8][1:] < a[6][1:] and a[8][2:] > a[7][2:] and a[6][2:] < a[5][2:]:
                detected("X", sequence)
                
            if indexDown(a) and middleDown(a) and ringDown(a) and pinkyUp(a) and thumbUp(a): 
                detected("Y", sequence)
                
            if indexUp(a) and middleDown(a) and ringDown(a) and pinkyDown(a) and a[4][1:] < a[12][1:]:
                detected("Z", sequence)
            
            #sense.show_message(text)
            #print(sequence)
                
            
            #Aufruf der Funktion checkSolution() bei einer Eingabelaenge von 3
            if len(sequence) == 3:

                if checkSolution(sequence, logo) == True:
                    return True
                
        
        
        #Below shows the current frame to the desktop 
        cv2.imshow("Frame", frame1);
        key = cv2.waitKey(1) & 0xFF


#Einfache Finger Positionen checken
#Koordinaten der Fingerposition mit einander vergleichen um Ausrichtung der Finger zu bestimmen

def indexUp(a):
    if a[8][2:] < a[6][2:]:
        return True

def indexDown(a):
    if a[8][2:] > a[6][2:]:
        return True
    
def middleUp(a):
     if a[12][2:] < a[10][2:]:
         return True
        
def middleDown(a):
     if a[12][2:] > a[10][2:]:
         return True

def ringUp(a):
     if a[16][2:] < a[14][2:]:
         return True
        
def ringDown(a):
     if a[16][2:] > a[14][2:]:
         return True
        
def pinkyUp(a):
     if a[20][2:] < a[18][2:]:
         return True
        
def pinkyDown(a):
     if a[20][2:] > a[18][2:]:
         return True
        
def thumbUp(a):
    if a[1][1:] < a[4][1:]:
        return True

def thumbDown(a):
    if a[1][1:] > a[4][1:]:
        return True
    
def setSequence(value, sequence):
    sense.clear()
    if len(sequence) == 0:
        sequence.append(value)
        
    if value != sequence[-1]:
        sequence.append(value)
    
    if len(sequence) > 3:
        sequence.pop(0)


def checkSolution(solution, logo):
    #f = open("solution.txt")
    solution = ''.join(solution)
    print(solution)
    print(bytes.fromhex("544842").decode('utf-8'))
    if solution == bytes.fromhex("544842").decode('utf-8'):
        print("Glueckwunsch!")
        sense.set_pixels(logo)
        return True
    else:
        return False
        
def letter(letter):
    sense.show_letter(letter)
    
def detected(text, sequence):
    setSequence(text,sequence)
    letter(text)
    #print(text)
    
def findpostion(frame1):
    list=[]
    results = mod.process(cv2.cvtColor(frame1, cv2.COLOR_BGR2RGB))
    if results.multi_hand_landmarks != None:
       for handLandmarks in results.multi_hand_landmarks:
           drawingModule.draw_landmarks(frame1, handLandmarks, handsModule.HAND_CONNECTIONS)
           list=[]
           for id, pt in enumerate (handLandmarks.landmark):
                x = int(pt.x * w)
                y = int(pt.y * h)
                list.append([id,x,y])
    #print(list)
    return list          

def findnameoflandmark(frame1):
     list=[]
     results = mod.process(cv2.cvtColor(frame1, cv2.COLOR_BGR2RGB))
     if results.multi_hand_landmarks != None:
        for handLandmarks in results.multi_hand_landmarks:


            for point in handsModule.HandLandmark:
                 list.append(str(point).replace ("< ","").replace("HandLandmark.", "").replace("_"," ").replace("[]",""))
     return list



#main()
