##Take input as the number of GPS Files in system. The files should be named GPS1,GPS2..GPSn
##Output files are Leader.txt containing all the leaders and Clusters.txt containing the clusters.
from __future__ import division
def computeDistance(a,b,c,d):
    Coords1=[]
    Coords2=[]
    Coords1.append(a)
    Coords1.append(b)
    Coords2.append(c)
    Coords2.append(d)
    
    Coords1[0]=math.radians(float(Coords1[0]))
    Coords1[1]=math.radians(float(Coords1[1]))
    Coords2[0]=math.radians(float(Coords2[0]))
    Coords2[1]=math.radians(float(Coords2[1]))
    if Coords1!=Coords2:
        
        distance=math.acos(math.sin(Coords1[0])*math.sin(Coords2[0])+math.cos(Coords1[0])*math.cos(Coords2[0])*math.cos(Coords1[1]-Coords2[1]))*6371*1000
    else:
        distance=0


    return distance


import os
import math
from os import listdir
import time

curr_dir=os.getcwd();
i=0
list_of_file_data={}
filename=""
complete_list=[]
folder=raw_input("Enter the folder name/path : ")
fileList=listdir(folder)
no_of_files=len(fileList)
i=0
print "Loading..."
os.chdir(folder)
for files in fileList:
	list_of_file_data[i]=[]
	print files
	list_of_file_data[i]=open(files).readlines()
	#print len(list_of_file_data[i])
	i+=1

temp=[]
complete_lat_long=[]
original_lat_long=[]
i=0
dist=0
objlist=[]
visited=[]
class LatLon:
    def __init__(self):
        self.Lat=0.00
        self.Lon=0.00
        self.trail=0
        self.weight=0
        self.timestamp=0
        self.neighbour_list=[]
        self.visited=0
        self.index=0
        self.trail_flag=[]
        self.busstop=0
print no_of_files
c=0
i=0
while i<no_of_files:
    count=0
    
    print "i",i
    
    for e in list_of_file_data[i]:
        
        temp=e.rstrip("\n").split(",")
        
        original_lat_long.append(temp[0].rstrip(" ")+","+temp[1].lstrip(" ").rstrip(" "))

      #  print temp[0]+"\t"+temp[1]+"\t"+str(i)
        obj=LatLon()
        obj.Lat=temp[0]
        obj.Lon=temp[1]
        obj.trail=str(i)
        obj.timestamp=temp[3]
        obj.visited=0
        obj.index=temp[4]
        for j in range(0,no_of_files):
            obj.trail_flag.append(False)
        objlist.append(obj)
        c=c+1         
        count+=1
    print count
    print i
    i+=1

complete_lat_long=original_lat_long
print "c",c

r = float(raw_input("Enter r : "))
t = float(raw_input("Enter t : "))
print "for r=",r
os.chdir(curr_dir);

complete_lat_long=original_lat_long
list_of_weights={}

l=0
outlier=0
print "For t=",t

f2=open("b.txt","w")


f3=open("c.txt","w")


filter_list=[]
filter_list_weight=[]
outlier_list=[]

fname2=raw_input("Enter filename of FILTER GPS file with .txt extension : ")
f5=open(fname2,"w")

fname3=fname2+"_details"
f6=open(fname3,"w")
f6.write("Latitude")
f6.write(",")
f6.write("Longitude")
f6.write("\n")
print len(objlist)
busStop=[]
old=time.time()
for count in objlist:
    
    lat1=count.Lat
    lon1=count.Lon    
    
    for index,e1 in enumerate(objlist):
        lat2=e1.Lat
        lon2=e1.Lon
        
        if(count.trail!=e1.trail) and (count.trail_flag[int(e1.trail)]!=True):
            
            
            try:
                distance=computeDistance(lat1,lon1,lat2,lon2)
            except:
                pass

            if(distance<r):                
                count.neighbour_list.append(index)
                count.trail_flag[int(e1.trail)]=True

    count.weight=len(count.neighbour_list)

    if (count.weight>t):        
        try:
            busStop.append(count)
            '''f5.write(count.Lat)
            f5.write(",")
            f5.write(count.Lon)
            f5.write(",")
            f5.write(count.trail)
            f5.write("\n")
            '''

            

            '''f6.write(count.Lat)
            f6.write(",")
            f6.write(count.Lon)
            f6.write("\t")
            f6.write(count.trail)
            f6.write("\t")
            f6.write(count.timestamp)
            f6.write("\t")
            f6.write(str(count.weight))
            f6.write("\t")
            f6.write(len(count.neighbour_list))
            f6.write("\n")'''
            #f6.write('\n'.join(set(count.neighbour_list)))
                
        except Exception:
            pass
            print "Error in printing"


f3.close()
print "Out of inner Loop"        
now=time.time()
print now-old
f6.close()

'''bcount=1
print len(busStop)
prev=busStop[0]

trail_no=prev.trail

flag=True
moreR=[]
for i, point in enumerate(busStop):
    if i!=0:
        if trail_no==point.trail:

            if point.busstop==0 or len(moreR)>=1:
                
                print "busstop=0",i
                if computeDistance(prev.Lat,prev.Lon,point.Lat,point.Lon)<=r:
                    print "within r",i
                    flag=True
                    size=len(moreR)
                    if size>1:
                        for index, xpoint in enumerate(moreR):
                            if index<size-1:
                                xpoint.busstop=bcount
                                for n in xpoint.neighbour_list:
                                    if objlist[n].busstop==0:
                                        objlist[n].busstop=bcount
                                bcount+=1
                    moreR=[]
                    if prev.busstop==0:
                        print "prev busstop=0",i,bcount
                        #bcount+=1
                        prev.busstop=bcount
                        for n in prev.neighbour_list:
                            if objlist[n].busstop==0:
                                objlist[n].busstop=bcount
                    point.busstop=prev.busstop
                    for n in point.neighbour_list:
                        if objlist[n].busstop==0:
                            objlist[n].busstop=bcount
                else:
                    moreR.append(point)
                    
                    #raw_input(">r")
                    if flag:
                        bcount+=1
                        flag=False
        
        else:
            trail_no=point.trail
        prev=point
print "complete"
f5.write("Latitude,Longitude,timestamp,trail_no,BusStop_no\n")
                
for point in busStop:

    f5.write(point.Lat+","+point.Lon+","+point.timestamp+","+point.trail+","+str(point.busstop)+"\n")

f5.close()  

fname7=raw_input("Enter filename of FILTER GPS file with .txt extension : ")
f7=open(fname7,"w")
i=1
while i<=bcount:
    for point in busStop:
        if i==point.busstop:
            f7.write(point.Lat+","+point.Lon+","+point.timestamp+","+point.trail+","+str(point.busstop)+"\n")
    i+=1
f7.close()'''
