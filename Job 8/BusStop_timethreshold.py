import os
def retrieveFile(filename):
    f = open(filename,'r')
    Data = f.readlines()
    lines=[]
    field=[]
    for line in Data:
        line=line.rstrip(",\n")
        field=line.split(",")
        lines.append(field)  
    f.close()
    return lines

folder=raw_input("Enter the folder name/path : ")
time_threshold=input("Enter the threshold for time spent at Bus stop : ")
fileList=os.listdir(folder)
os.chdir(folder)
path="Output_details"
os.mkdir(path)
bus_summary=[]
trail_tot_time=0
trail_tot_point=0
trail_tot_Stopnum=0
for fname in fileList:
    print "Processing %s Please Wait....." %(fname)
    trail=[]
    name=[]
    trail=retrieveFile(fname)
    tot_point=len(trail)
    lat=trail[1][0]
    lon=trail[1][1]
    start_time=trail[1][-1]
    tot_time=1
    Stopnum=0
    trail_time=0
    name=fname.rstrip(".txt").split("_")
    f=path+"/"+(name[0]+"_"+name[1]+"_"+name[-1]+"_t"+str(time_threshold)+".txt")
    out=open(f,"w")
    out.write("Waiting time,BusStop Number,Latitude,Longitude\n")
    for i in xrange(2,len(trail)):
        if lat==trail[i][0] and lon==trail[i][1]:
            tot_time+=1
        else:
            if tot_time>=time_threshold:
                Stopnum+=1
                v=str(tot_time)+","+start_time+","+str(Stopnum)+","+str(lat)+","+str(lon)+"\n"
                trail_time+=tot_time
                out.write(v)
            tot_time=0
            lat=trail[i][0]
            lon=trail[i][1]
            start_time=trail[i][-1]
    out.close()
    fraction=round((Stopnum*100.0)/tot_point,1)
    trail_tot_time+=trail_time
    trail_tot_point+=tot_point
    trail_tot_Stopnum+=Stopnum
    bus_summary.append(fname+"\t"+str(trail_time)+"\t\t"+str(tot_point)+"\t\t"+str(Stopnum)+"("+str(fraction)+"%)")
print bus_summary[0]
print "Proceesing Complete"