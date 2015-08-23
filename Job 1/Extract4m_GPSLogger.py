import sys
import re
import math

#from datetime import time, timedelta
import datetime
data_set = []

def retrieveFile(filename):
    f = open(filename,'r')
    Data = f.readlines()
    lines=Data[0].split("\r");
    f.close()
    return lines
    

def computeDistance(a,b,c,d):
    Coords1=[]
    Coords2=[]
##    Coords1[0]=a
##    Coords1[1]=b
##    Coords2[0]=c
##    Coords2[1]=d
##
    Coords1.append(a)
    Coords1.append(b)
    Coords2.append(c)
    Coords2.append(d)
    
    #Coords1=a.split(",")
    #Coords2=b.split(",")
    ##print Coords1,Coords2
##    if(Coords1[0]==Coords2[0] and Coords1[1]==Coords2[1]):
##        return 2
    Coords1[0]=math.radians(float(Coords1[0]))
    Coords1[1]=math.radians(float(Coords1[1]))
    Coords2[0]=math.radians(float(Coords2[0]))
    Coords2[1]=math.radians(float(Coords2[1]))
    distance=math.acos(math.sin(Coords1[0])*math.sin(Coords2[0])+math.cos(Coords1[0])*math.cos(Coords2[0])*math.cos(Coords1[1]-Coords2[1]))*6371*1000

##    except:
##        distance=2


    return distance

prantika=[23.5642683333,87.2829133333]
durgapur=[23.494395,87.317125]
time=[]
lat=[]
lng=[]
speed=[]
def fileWrite(start,end,fCount,fileLength):
        f="gps_bus_trails5_"+str(fCount)+".txt"
        create=open(f,'w')
        create.write("latitude,longitude,speed,time\n");
        #print start,end
        for f in range(start,end):                           
                create.write(str(lat[f])+","+str(lng[f])+","+str(speed[f])+","+time[f]+"\n")
                #elif f<(fileLength-1):
        #   create.write(str(lat[f])+","+str(lng[f])+","+alt[f+1]+","+time[f]+"\n")
        #else:
        #   create.write(str(lat[f])+","+str(lng[f])+","+alt[f-1]+","+time[f]+"\n")
            
                                
def sourceExtract(count,fileLength,source):
    while count<fileLength:
            #file write
            if computeDistance(source[0],source[1],lat[count],lng[count])>20:
                raw_input("source")
                flag=True
                print count
                count=count+1
                break
            count=count+1
    return count

def destinationExtract(count,fileLength,destination):
    while count<fileLength:
            #file write
            if computeDistance(destination[0],destination[1],lat[count],lng[count])<20:
                raw_input("destination")
                flag=True
                print count
                count=count+1
                break
            count=count+50
    return count

def extractSrcDest(count,fileLength,source,destination):
    
    count=destinationExtract(count,fileLength,destination)
    count=sourceExtract(count,fileLength,destination)
    

def main():
    lines = retrieveFile("GPSLOG05.txt");
    m=0
    #print len(lines)
    for line in lines:
        finalLat=0.0
        finalLong=0.0
        finalTime=0.0
        matchData=re.search(r'(\$[A-Z]{5}),(\d{6}.\d{1,5}),(A,(\d{4,6}.\d{4,6})|(\d{4,6}.\d{4,6})),[A-Z]{1},(\d{4,6}.\d{4,6}),[A-Z]{1},([0-9]{1,4}.\d{1,4}),',line)
        try:
                        #print matchData.group(1), matchData.group(2),matchData.group(4),matchData.group(5),matchData.group(6),matchData.group(7)
                        if matchData.group(1)=='$GPRMC':
                                gmt=matchData.group(2);
                                #print gmt
                                matchgmt=re.search(r'(\d{2})(\d{2})(\d{2})\.(\d{3,6})',gmt)
                                hh=int(matchgmt.group(1));
                                mm=int(matchgmt.group(2));
                                ss=int(matchgmt.group(3));
                                sss=int(matchgmt.group(4));
                                ist=datetime.datetime(2014,1,1,hh,mm,ss,sss)+datetime.timedelta(hours=5,minutes=30)
                                t=ist.strftime("%H:%M:%S")
                                time.append(t)#Append Time
                                longi=matchData.group(6)        #Extract Longitude
                                matchlong=re.search(r'(\d{3})(\d{2}\.\d{4,6})',longi)
                                deg=int(matchlong.group(1))
                                minute=float(matchlong.group(2))
                                minute=minute/60        #coversion to degree
                                finalLong=deg+minute
                                lng.append(finalLong)       #Append Longitude
                                #alt.append(matchData.group(8))
                                '''if matchData.group(1) == "$GPGGA":
                                        
                                        lati=matchData.group(5);    #Extract Latitude
                                        matchlat=re.search(r'(\d{2})(\d{2}\.\d{4,6})',lati)
                                        deg=int(matchlat.group(1))
                                        minute=float(matchlat.group(2))
                                        minute=minute/60        #Coversion to Degree
                                        finalLat=deg+minute 
                                        lat.append(finalLat)        #Append Latitude
                                '''
                                lati=matchData.group(4)
                                matchlat=re.search(r'(\d{2})(\d{2}\.\d{4,6})',lati)
                                deg=int(matchlat.group(1))
                                minute=float(matchlat.group(2))
                                minute=minute/60
                                finalLat=deg+minute
                                lat.append(finalLat)
                                speed.append(str(float(matchData.group(7))*30.8666666667))
                                #lng.append(finalLong)
                                                

        except Exception,e:
            print e.args
            

    #print lat
    #print lng
    
    
    fCount=1
    cordLength=len(lat)
    fileLength=len(lat)
    
    i=0
    start=0
    select=-1
    while i<fileLength:
        flag=False
        if select==-1:
            source=prantika
            destination=durgapur
        else:
            source=durgapur
            destination=prantika
            
        i=sourceExtract(i,fileLength,source)
        i=destinationExtract(i,fileLength,destination)
        #while i<fileLength:
        #   #file write
        #   if computeDistance(prantika[0],prantika[1],lat[i],lng[i])>20:
        #       raw_input("source")
        #       flag=True
        #       print i
        #       i=i+1
        #       break
        #   i=i+1
        #while i<fileLength:
        #   #file write
        #   if computeDistance(durgapur[0],durgapur[1],lat[i],lng[i])<20:
        #       raw_input("destination")
        #       flag=False
        #       break
        #   else:
        #       i=i+50
        fileWrite(start,i,fCount,fileLength)
        #create=open('GPSLogger_latlng'+str(fCount)+".txt",'w')
        #print start,i
        #for f in range(start,i):
        #   if alt[f]!=None:
        #           
        #       create.write(str(lat[f])+","+str(lng[f])+","+alt[f]+","+time[f]+"\n")
        #   elif f<(i-1):
        #       create.write(str(lat[f])+","+str(lng[f])+","+alt[f+1]+","+time[f]+"\n")
        #   else:
        #       create.write(str(lat[f])+","+str(lng[f])+","+alt[f-1]+","+time[f]+"\n")
        #       
        fCount=fCount+1
        start=i+1
        select=select * -1
        
            
    
    
    
    '''
    while True:
        limit=0
        if cordLength<=7000:
        
            create=open('GPSLogger_latlng'+str(fCount)+".txt",'w')
            
            for l in range(len(lat)):
                if alt[l]!=None:
                    
                    create.write(str(lat[l])+","+str(lng[l])+","+alt[l]+","+time[l]+"\n")
                elif l<(fileLength-1):
                    create.write(str(lat[l])+","+str(lng[l])+","+alt[l+1]+","+time[l]+"\n")
                else:
                    create.write(str(lat[l])+","+str(lng[l])+","+alt[l-1]+","+time[l]+"\n")
                limit=l


            create.close()  
            del lat[0:limit+1]
            del lng[0:limit+1]
            break
        else:
        
            create=open('GPSLogger_latlng'+str(fCount)+".txt",'w')
            for l in range(len(lat)):
                if l>1000:
                    break
                if alt[l]!=None:
                    create.write(str(lat[l])+","+str(lng[l])+","+alt[l]+"   ,"+time[l]+"\n")
                elif l<(fileLength-1):
                    create.write(str(lat[l])+","+str(lng[l])+","+alt[l+1]+","+time[l]+"\n")
                else:
                    create.write(str(lat[l])+","+str(lng[l])+","+alt[l-1]+","+time[l]+"\n")
                
                
                limit=l
                
            create.close()
            del lat[0:limit+1]
            del lng[0:limit+1]
            fCount=fCount+1
            
        cordLength=len(lat)
    '''

if __name__ == '__main__':
    main()
