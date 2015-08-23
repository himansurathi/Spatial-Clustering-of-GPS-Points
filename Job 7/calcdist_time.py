#!/usr/bin/env python
from math import *
import os
from os import listdir
from datetime import datetime
import re

class disttime:
    def __init__(self,trail_no,dist,time,start_time,end_time):
        self.trail_no=trail_no
        self.dist=dist
        self.time=time
        self.start_time=start_time
        self.end_time=end_time

class info:
    def __init__(self,lat1,long1,alt,timestamp):
        self.lat1=lat1
        self.long1=long1
        self.alt=alt
        self.timestamp=timestamp

def distance(lat1,lat2,long1,long2):
    q=radians(lat2-lat1)
    r=radians(long2-long1)
    lat2=radians(lat2)
    lat1=radians(lat1)
    a=sin(q/2)*sin(q/2)+cos(lat1)*cos(lat2)*sin(r/2)*sin(r/2)
    c=2*atan2(sqrt(a),sqrt(1-a))
    R=6371*1000
    d=R*c
    return d

def caltime(t1,t2):
    FMT="%H:%M:%S"
    tdelta=datetime.strptime(t2,FMT)-datetime.strptime(t1,FMT)
    second = tdelta.total_seconds()
    return second

def Gps_log(input_file,trail_no):
    f = open(input_file,"r")
    data = f.readlines()
    s=0
    trail=[]
    for i in range(1,len(data)):               #checking for all the lines in a file   
	point=data[i].rstrip("\n").split(",")
	latitude=float(point[0])
	longitude=float(point[1])
	altitude=float(point[2])
	timestamp=str(point[3])
        pointObj=info(latitude,longitude,altitude,timestamp)
        trail.append(pointObj) 
    for j,point in enumerate(trail):
        if j!=0:
            lat2=point.lat1
            long2=point.long1
            lat1=trail[j-1].lat1
            long1=trail[j-1].long1
            d=distance(lat1,lat2,long1,long2)
            s=s+d
    time1=caltime(trail[0].timestamp,trail[len(trail)-1].timestamp)
    obj=disttime(trail_no,s,time1,trail[0].timestamp,trail[len(trail)-1].timestamp)
    trail1.append(obj)
    f.close()
    
trail1=[]
curr_dir=os.getcwd()
folder=raw_input("Enter the folder name/path:")
fileList=listdir(folder)
no_of_files=len(fileList)
os.chdir(folder)
for fileno,File in enumerate(fileList):
        print File
        #num=re.findall(r'\d+',File)
        Gps_log(File,0)
        name=raw_input("Enter filename of FILTER GPS file with .txt extension : ")
out=open(name,"w")
out.write("#trail_no,total_distance,total_time,start_time,end_time\n")
i=1
while i<=len(trail1):
    for obj in trail1:
        if i==int(obj.trail_no):
            out.write(str(obj.trail_no)+","+str(obj.dist)+","+str(obj.time)+","+str(obj.start_time)+","+str(obj.end_time)+"\n")
            break
    i+=1
out.close()
