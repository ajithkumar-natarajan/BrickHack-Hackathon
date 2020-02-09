# -*- coding: utf-8 -*-
"""
Created on Sun Feb 09 04:25:46 2020

@author: ajithkumar-natarajan
"""

"""Module importation"""
import serial
import json
import os.path


"""Opening default serial port"""
try:
    arduino = serial.Serial("/dev/ttyACM0",timeout=1)
except:
    print('Please check the port')

"""Initialising variables""" 
rawdata=[]
count=0

"""Receiving data and storing it in a list"""
while count<4:
    rawdata.append(str(arduino.readline().rstrip()))
    count+=1
print(rawdata)

#def clean(L):   #L is a list
#    newl=[]     #initialising the new list
#    for i in range(len(L)):
#        temp=L[i][2:]
#        newl.append(temp[:-5])
#    return newl

#cleandata=Convert(rawdata)


def write(L):
    data_dict = dict()
    data_dict['Temperature'] = float(L[0])
    data_dict['AirPressure'] = float(L[1])
    if(L[2] == "Yes"):
        L[2] = 1
    else:
        L[2] = 0
    data_dict['LightReplacement'] = L[2]
    data_dict['Grocery'] = L[3]

    # if os.path.isfile('../Front-end/data.json'):
    #     count = 0

    # else:
    #     with open('../Front-end/data_cumulative.txt', 'w') as f_cum:
    #         f_cum.readline([cum])

    # if(int(cum[2]) < 31):
    #     if(LightReplacement == "Yes"):
    #         cum[0] = int(cum[0])+1
    #     if(Grocery == "Yes"):
    #         cum[1] = int(cum[1])+1
    # else:
    #     if(LightReplacement == "Yes"):
    #         cum[0] = 1
    #     if(Grocery == "Yes"):
    #         cum[1] = 1
    # if(count == 0):
    #     cum[2] = 0
    # else:
    #     cum[2] = int(cum[2]) + 1

    with open('../Front-end/data.json', 'w') as fp1:
        str_begin = "jsonstr = ["
        str_end = "];"
        fp1.write(str_begin)
        fp1.close()
    with open('../Front-end/data.json', 'a') as fp2:
        json.dump(data_dict, fp2)
    with open('../Front-end/data.json', 'a') as fp1:
        fp1.write(str_end)
write(rawdata)