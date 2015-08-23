import sys
class landmark:
    def __init__(self,x,y,z,time,anchor,a="0"):
        self.x=x
        self.y=y
        self.z=z
        self.time=time
        self.anchor=anchor
        
        
def retrieveFile(filename):
    f = open(filename,'r')
    Data = f.readlines()
    lines=[]
    for line in Data:
        line=line.rstrip(",\n")
        lines.append(line)
    f.close()
    return lines
    
    
def parse(lines):
    anomaly=[]
    mflag=True
    pflag=False
    m=0
    p=0
    x=[]
    y=[]
    markerType=""
    temp=[]
    for line in lines:
        fields=line.split(",")
        flength=len(fields)
        if flength==4 and mflag:
            if m>=225 :
                temp.pop()
                temp.append(line)
            else:
                temp.append(line)
                m=m+1
        elif flength==4 and pflag:
            if p<225 :
                
                temp.append(line)
                p=p+1
            else:
                p=0
                mflag=True
                m=1
                pflag=False
                x.append(markerType)
                y.append(temp)
                temp=[]
                markerType="" 
                temp.append(line)  
                    
        elif flength==5:
            mflag=False
            pflag=True
            if m<225 and m>0 and p==0:
                t=y[-1]
                for i in xrange(-1,m-226,-1):
                    temp.insert(0,t[i])
                m=0
            if p!=0:
                x.append(markerType)
                y.append(temp)
                r=[]
                for i in xrange(len(temp)-p,len(temp)):
                    r.append(temp[i])
                temp=[]
                temp=r  
                markerType=""
                r=[]
                
            l=landmark(fields[0],fields[1],fields[2],fields[3],fields[4].rstrip("+"))
            
            anomaly.append(l)
            c=fields[4].find("+")
            if c!=len(fields[4])-1:
                p=0
                mflag=True
                m=0
                pflag=False
                if markerType!="":
                    x.append(markerType)
                    y.append(temp)
                temp=[]
                markerType=""   
                continue
            markerType=fields[4]
            temp.append(line)
            if p!=0:
                p=0
                m=0
    if p!=0:
        if x[-1]!=markerType:
            x.append(markerType)
        y.append(temp)
        temp=[]
    print x
    p=0
    for values in x:
        t=values.strip("+").split("_")
        fos=open("log/log_2/"+t[0]+".txt","a+")
        data=y[p]
        for i in data:
            fos.write(i+"\n")
        fos.close()
        p=p+1   
lines = retrieveFile(sys.argv[1])

parse(lines)
