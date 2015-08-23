import math
f=open("test case.txt","r")
Data = f.readlines()
lines=[]
i=1;
p=[]
x=0
y=0
z=0
#print total
for line in Data:
    lines.append(line.rstrip(",\n").split(","))  
print lines
w=open("output_down.txt","w")
for i in xrange(1,len(lines)-1,2):
    q=(lines[i]+lines[i+1])
    for j in q:
        if j!="" :
            w.write(j+",")
    w.write("\n")
    p.append(q)
f.close()
w.close()
lines=[]
w=open("output_down.txt","r")
Data = w.readlines()
m=[]
d=open("Central.txt","w")
d.write("Latitude,Longitude,Busstop\n")
for line in Data:
    lines.append(line.rstrip(",\n").split(","))  
for t in lines:
    q=t[-1]
    if not q in m:
        m.append(q)
        lat=[]
        long=[]
        for l in lines:
            if l[-1]==t[-1]:
                lat.append(l[0])
                long.append(l[1]) 
        x=0
        y=0
        z=0
        lat_rad=0
        lon_rad=0
        total=len(lat)
        for i in xrange(0,total):
            lon_rad=float(long[i])*math.pi/180
            lat_rad= float(lat[i])*math.pi/180
            a=math.cos(lat_rad)*math.cos(lon_rad)
            b=math.cos(lat_rad)*math.sin(lon_rad)
            c=math.sin(lat_rad)
            x+=a
            y+=b
            z+=c
        x/=total
        y/=total
        z/=total
        lon=math.atan2(b,a)
        Hyp=math.sqrt(a*a+b*b)
        lat=math.atan2(c,Hyp)
        d.write(str(lat*180/math.pi)+","+str(lon*180/math.pi)+","+m[-1]+"\n")