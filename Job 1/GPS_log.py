from math import *
def distance(lat1,lat2,long1,long2):#function to find Distance
    lat2=radians(lat2)
    lat1=radians(lat1)
    q=radians(lat2-lat1)
    r=radians(long2-long1)
    a=sin(q/2)*sin(q/2)+cos(lat1)*cos(lat2)*sin(r/2)*sin(r/2)
    c=2*atan2(sqrt(a),sqrt(1-a))
    d=r*c
    return d;

def bearing(lat1,lat2,long1,long2):# function to find bearing
    lat1=radians(lat1)
    lat2=radians(lat2)
    q=radians(lat2-lat1)
    r=radians(long2-long1)
    b=atan2(sin(r)*cos(lat2),cos(lat1)*sin(lat2)-sin(lat1)*cos(lat2)*cos(r))
    return b

def Gps_log(input_file,output_file):
    p=1
    f = open(input_file,"r")
    Data = f.readlines()
    lines=Data[0].split(",") #stores indivisual numbers in a list
    lat1=float(lines[0])# stores latitude as an int 
    long1=float(lines[1])# stores longitude as an int
    ts1=lines[3]#stores time in hr:min:sec format
    time1=ts1.split(":")#splits time in hours minutes and seconds
    t1=float(time1[0])*3600+float(time1[1])*60+float(time1[2])#stores time in seconds
    r=6371#radius of Earth
    out=open(output_file,"w")
    out.write("Speed(km/s),Bearing,Time(s)\n")
    for i in xrange(1,len(Data)):#Process repeats till end of file
        lines=Data[i].split(",")#Repeat same for next line
        lat2=float(lines[0])
        long2=float(lines[1])
        ts2=lines[3]
        time2=ts2.split(":")
        t2=float(time2[0])*3600+float(time2[1])*60+float(time2[2])
        if ((t2-t1)>=1):#so that at leat one sec gap is there
            d=distance(lat1,lat2,long1,long2)
            b=bearing(lat1,lat2,long1,long2)
            p+=1
            var=str(d/(t2-t1))+','+str(b)+','+str(p)+'\n'
            out.write(var)#var is a string and writing to output file
            lat1=lat2
            long1=long2
            ts2=ts1
            t2=t1#present values become previous values
    f.close()
    out.close()#all files are closed

def main():
    inp="GPSLogger_latlng"
    out="GPSLogger_latlng_output"
    for i in xrange(1,9):
        f1=str(inp+str(i)+".txt")
        f2=str(out+str(i)+".txt")
        Gps_log(f1,f2)
        print "Check ",f2
main()
