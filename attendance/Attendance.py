import cv2
from cv2 import FONT_HERSHEY_COMPLEX
import numpy as np
import os
import face_recognition
from datetime import datetime
from database import*

def faceEncodings(images):
    encodeList=[]
    for img in images:
        img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        encode=face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList

def f(x):
    if (x > 4) and (x <= 8):
        return 'Morning'
    elif (x > 8) and (x <= 12 ):
        return 'Morning'
    elif (x > 12) and (x <= 16):
        return'Eve'
    elif (x > 16) and (x <= 20) :
        return 'Eve'
    elif (x > 20) and (x <= 24):
        return'Eve'

def attendance(id,newtime,newdate,hour):
    
    type=f(hour)

    chkAtt=checkAttendance(id,newdate,type)

    if(chkAtt == True):

        sql = """INSERT INTO attendance (user_id,time_type, today_date, check_in_time) VALUES (%s,%s,%s,%s)"""
        val = (id,type,newdate,newtime)
        mycursor.execute(sql,val)
        con.commit()
    
    else:
        sql = '''UPDATE attendance SET check_out_time = %s WHERE user_id = %s AND today_date = %s AND time_type = %s '''
        val = (newtime, id, newdate, type)
        mycursor.execute(sql,val)
        con.commit()


def checkAttendance(id,newdate,type):
    
    sql = '''SELECT * from attendance WHERE user_id=%s AND today_date=%s AND time_type=%s'''
    val = (id,newdate,type)
    mycursor.execute(sql,val)
    result = mycursor.fetchone()
    row_count = mycursor.rowcount

    if row_count == 0:
        return True
    else:
        return False




