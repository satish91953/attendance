import cv2
import numpy as np
import os
from Attendance import*
from datetime import datetime
from database import*
import face_recognition


print('tranning process start...')
        
path='img\images'
images=[]
personid=[]
personName=[]
myList=os.listdir(path)
# print(myList)
for cu_img in myList:
    current_Img=cv2.imread(f'{path}/{cu_img}')
    images.append(current_Img)
    fnamef=cu_img.split("_")
    geti = fnamef[1]
    getid = geti.split(".")
    personid.append(getid[0])
    personName.append(fnamef[0])
# print(personName)
# print(personid)
# print(images)
encodeListKnown=faceEncodings(images)
print('Tranning process completed')
cap=cv2.VideoCapture("rtsp://admin:cctv@321@192.168.1.250:554/cam/realmonitor?channel=1&subtype=0")
# cap=cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)
        
# img_counter = 0
if cap.isOpened():
            
   while True:
                                        
       success,frame=cap.read()
               
       # facess = cv2.resize(frame, (400, 300)) 
       # resized = cv2.resize(frame,(0,0), fx=0.5, fy=0.5)
       faces=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
       facesCurrentFrame=face_recognition.face_locations(faces)
       encodesCurrentFrame=face_recognition.face_encodings(faces,facesCurrentFrame)    
       for encodeFace,faceloc in zip(encodesCurrentFrame,facesCurrentFrame):
           matches=face_recognition.compare_faces(encodeListKnown,encodeFace)
           faceDis=face_recognition.face_distance(encodeListKnown,encodeFace)
                    
           matchIndex=np.argmin(faceDis)
                                    
           if matches[matchIndex]:
              id=personid[matchIndex]
              name=personName[matchIndex]
              time_now=datetime.now()
              hour=time_now.hour
              newdate=time_now.strftime('%Y-%m-%d') 
              newtime=time_now.strftime('%H:%M:%S')
              # time=time_now.strftime('%I:%M:%S')
              # print(time,newdate)
              attendance(id,newtime,newdate,hour)
                    
              cv2.waitKey(10)
else:
   print("Camera Not Working...")
        
cap.release()
cv2.destroyAllWindows()



