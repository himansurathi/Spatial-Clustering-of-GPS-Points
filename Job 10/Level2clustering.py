import math
import os
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
#trailway=input("Enter 1 for up trail and 0 for down trail:")
def func_plot(neighbour,m,n,num):
    for i in xrange (0,len(neighbour)):
        fiel=neighbour[i].split(",")
        lat_neigh=fiel[1]
        lon_neigh=fiel[2]
        wait_time_neigh=fiel[0]
        trail_neigh=fiel[3]
        if i!=0:
            m.write(lat_neigh+","+lon_neigh+","+str(wait_time_neigh)+","+str(trail_neigh)+"\n")
        else:
            n.write(lat_neigh+","+lon_neigh+","+str(wait_time_neigh)+","+str(trail_neigh)+"\n")
    
'''if trailway==1:
    info=open("Group_up_t"+str(BusStop_timethreshold.time_threshold)+"r"+str(distance_threshold)+"_summary.txt","w")
else:
    info=open("Group_down_t"+str(BusStop_timethreshold.time_threshold)+"r"+str(distance_threshold)+"_summary.txt","w")
'''
level1=raw_input("Enter the folder name/path : ")
os.chdir(level1)
fileList=os.listdir(level1)
#print os.getcwd()
#os.mkdir("level2 Cluster")
given_trail=input("Enter the number of trails : ")
group_threshold=input("Enter the threshold for the cluster : ")
global_head={}
m=0
file_no=0
count=0
for t in fileList:
    print "Processing %s Please Wait....." %(t)
    f1 = open(t,'r')
    Data1=f1.readlines()
    #print Data1
    gtrail_no=t.split("_")
    field1=[]
    for line1 in Data1:
        line1=line1.rstrip(",\n")
        global_group=[]
        if line1[-1]=="u":
            gwait=(line1.split(","))[0]
            glat=(line1.split(","))[1]
            glon=(line1.split(","))[2]
            global_group.append(line1[:-1]+str(gtrail_no[1]+gtrail_no[2]))
            m=file_no+1
            for it in xrange(m,len(fileList)):
                f2=open(fileList[it],'r')
                trail_no=fileList[it].split("_")
                Data2=f2.readlines()
                field2=[]
                flag=1
                for line2 in Data2:
                    line2=line2.rstrip(",\n")
                    glist=[]
                    if flag and line2[-1]=="u":
                        glist=line2.split(",")
                        wait_time=int(glist[0])
                        lat=float(glist[1])
                        lon=float(glist[2])
                        #print global_group
                        #print global_group
                        for iterator in xrange(0,len(global_group)):
                            glat=(global_group[iterator].split(","))[1]
                            glon=(global_group[iterator].split(","))[2]
                            dist=computeDistance(glat,glon,lat,lon)
                            # print glat,glon,dist
                            if dist<=group_threshold:
                                global_group.append(line2[:-1]+str(trail_no[1]+trail_no[2]))
                                line2=line2[:-1]+"m"
                                flag=0
                                break
                    line2+="\n"
                    field2.append(line2)
                f2.close()
                f2=open(fileList[it],"w")
                for i in field2:
                    f2.write(i)
                f2.close()
            line1=line1[:-1]+"m"
            global_head[count]=global_group
            count+=1
        line1+="\n"
        field1.append(line1)
    f1.close()
    f1=open(t,"w")
    for i in field1:
        f1.write(i)
    f1.close()
    file_no+=1
file_clust=open("All Cluster.txt","w")
file_clust.write("Latitude,Longitude,Wait time,Trail_no\n")
e=0
for keys in global_head:
    if len(global_head[keys])>=15*given_trail/100.0:
        #file_cat=open(str(keys)+"Cluster.txt","w")
        file_cat=open(str(e)+"Cluster.txt","w")
        file_cat.write("Latitude,Longitude,Wait time,Trail_no\n")
        for m in global_head[keys]:
            p=m.split(",")
            q=p[1]+","+p[2]+","+p[0]+","+p[3]+"\n"
            file_cat.write(q)
            file_clust.write(q)
        file_cat.close()
        e+=1
file_clust.close()
output=open("Level2_clustering.txt","w")
output.write("Group ID,Consecutive Group Distance(mts),Wait time,Farthest distance(mts),Group length,Group(Wait time,Latitude,Longitude,Trail_no)\n")
file_head=open("Head Cluster.txt","w")
file_head.write("Latitude,Longitude,WaitTime,Trailno\n")
out1=open("out25.txt","w")
out2=open("out50.txt","w")
out3=open("out75.txt","w")
out4=open("out100.txt","w")
out1.write("Group ID,Consecutive Group Distance(mts),Wait time,Farthest distance(mts),Group length,Group(Wait time,Latitude,Longitude,Trail_no)\n")
out2.write("Group ID,Consecutive Group Distance(mts),Wait time,Farthest distance(mts),Group length,Group(Wait time,Latitude,Longitude,Trail_no)\n")
out3.write("Group ID,Consecutive Group Distance(mts),Wait time,Farthest distance(mts),Group length,Group(Wait time,Latitude,Longitude,Trail_no)\n")
out4.write("Group ID,Consecutive Group Distance(mts),Wait time,Farthest distance(mts),Group length,Group(Wait time,Latitude,Longitude,Trail_no)\n")
plotout1=open("outplot25.txt","w")
plotout2=open("outplot50.txt","w")
plotout3=open("outplot75.txt","w")
plotout4=open("outplot100.txt","w")
plotout1.write("Latitude,Longitude,WaitTime,Trailno\n")
plotout2.write("Latitude,Longitude,WaitTime,Trailno\n")
plotout3.write("Latitude,Longitude,WaitTime,Trailno\n")
plotout4.write("Latitude,Longitude,WaitTime,Trailno\n")
head1=open("outhead25.txt","w")
head2=open("outhead50.txt","w")
head3=open("outhead75.txt","w")
head4=open("outhead100.txt","w")
head1.write("Latitude,Longitude,WaitTime,Trailno\n")
head2.write("Latitude,Longitude,WaitTime,Trailno\n")
head3.write("Latitude,Longitude,WaitTime,Trailno\n")
head4.write("Latitude,Longitude,WaitTime,Trailno\n")
maxgl2=0
last_lat=0
last_lon=0
e=0
for keys,values in global_head.items():
    string=[]
    points=[]
    w=0
    for i in global_head[keys]:
        string=i.split(",")
        points.append(string)
    gl=len(global_head[keys])
    if gl>maxgl2:
        maxgl2=gl
    mat=[[0]*gl]*gl
    group_time=0
    maxlength=0
    maximum=0
    row=0
    for i in xrange(0,gl):
        lat1=points[i][1]
        lon1=points[i][2]
        group_time+=int(points[i][0])
        col=0
        m=0
        for j in xrange(0,gl):
            lat2=points[j][1]
            lon2=points[j][2]
            d=computeDistance(lat1,lon1,lat2,lon2)
            if d>maxlength:
                maxlength=d
            mat[row][col]=float(points[i][0])/(d+1)
                #fout.write(str(dist[k][j])+" ") #display distance matrix
            m=m+mat[row][col]
            col+=1
        if m>maximum:
            maximum=m
            neighbour=[]
            lat_ghead=lat1
            long_ghead=lon1
            time_ghead=points[i][0]
            neighbour.append(str(time_ghead)+","+str(lat_ghead)+","+str(long_ghead)+","+str(points[i][-1]))
            for c in xrange(0,len(points)):
                if lat_ghead!=points[c][1] or long_ghead!=points[c][2] or time_ghead!=points[c][0]:
                    neighbour.append(points[c][0]+","+points[c][1]+","+points[c][2]+","+points[c][-1]) 
        row+=1
        # fout.write("\n") #print matrix in new line
    if len(global_head[keys])>=15.0*given_trail/100:
        if keys!=0:
            dist_grouphead=computeDistance(lat_ghead,long_ghead,last_lat,last_lon)
        else:
            dist_grouphead=-1
        neigh=neighbour[-1].split(",")
        last_lat=neigh[1]
        last_lon=neigh[2]
        output.write(str(e)+",\t"+str(round(dist_grouphead,2))+",\t"+str(round(group_time/len(global_head[keys]),2))+",\t"+str(round(maxlength,2))+",\t"+str(len(global_head[keys]))+",\t"+str(neighbour)+"\n")
        file_head.write(lat_ghead+","+long_ghead+","+time_ghead+","+str(points[i][-1])+"\n")
        if  len(global_head[keys])<=given_trail*25.0/100:
            func_plot(neighbour,plotout1,head1,1)
            out1.write(str(e)+",\t"+str(round(dist_grouphead,2))+",\t"+str(round(group_time/len(global_head[keys]),2))+",\t"+str(round(maxlength,2))+",\t"+str(len(global_head[keys]))+",\t"+str(neighbour)+"\n")
        #out1.write(str(keys)+",\t"+str(round(dist_grouphead,2))+",\t"+str(round(group_time/len(global_head[keys]),2))+",\t"+str(round(maxlength,2))+",\t"+str(len(global_head[keys]))+",\t"+str(neighbour)+"\n")
        elif len(global_head[keys])>=given_trail*25.0/100 and len(global_head[keys])<=given_trail*50.0/100:
            func_plot(neighbour,plotout2,head2,2)
            out2.write(str(e)+",\t"+str(round(dist_grouphead,2))+",\t"+str(round(group_time/len(global_head[keys]),2))+",\t"+str(round(maxlength,2))+",\t"+str(len(global_head[keys]))+",\t"+str(neighbour)+"\n")
        #out2.write(str(keys)+",\t"+str(round(dist_grouphead,2))+",\t"+str(round(group_time/len(global_head[keys]),2))+",\t"+str(round(maxlength,2))+",\t"+str(len(global_head[keys]))+",\t"+str(neighbour)+"\n")
        elif len(global_head[keys])>=given_trail*50.0/100 and len(global_head[keys])<=given_trail*75.0/100:
            func_plot(neighbour,plotout3,head3,3)
            out3.write(str(e)+",\t"+str(round(dist_grouphead,2))+",\t"+str(round(group_time/len(global_head[keys]),2))+",\t"+str(round(maxlength,2))+",\t"+str(len(global_head[keys]))+",\t"+str(neighbour)+"\n")
        #out3.write(str(keys)+",\t"+str(round(dist_grouphead,2))+",\t"+str(round(group_time/len(global_head[keys]),2))+",\t"+str(round(maxlength,2))+",\t"+str(len(global_head[keys]))+",\t"+str(neighbour)+"\n")
        elif len(global_head[keys])>=given_trail*75.0/100 and len(global_head[keys])<=given_trail*100.0/100:
            func_plot(neighbour,plotout4,head4,4)
            out4.write(str(e)+",\t"+str(round(dist_grouphead,2))+",\t"+str(round(group_time/len(global_head[keys]),2))+",\t"+str(round(maxlength,2))+",\t"+str(len(global_head[keys]))+",\t"+str(neighbour)+"\n")
        e+=1
    #print last_lat,last_lon
    
    
#        out4.write(str(keys)+",\t"+str(round(dist_grouphead,2))+",\t"+str(round(group_time/len(global_head[keys]),2))+",\t"+str(round(maxlength,2))+",\t"+str(len(global_head[keys]))+",\t"+str(neighbour)+"\n")
    #if len(global_head[keys])>=15.0*given_trail/100:
    #output.write(str(keys)+",\t"+str(round(dist_grouphead,2))+",\t"+str(round(group_time/len(global_head[keys]),2))+",\t"+str(round(maxlength,2))+",\t"+str(len(global_head[keys]))+",\t"+str(neighbour)+"\n")
    #file_head.write(lat_ghead+","+long_ghead+","+time_ghead+","+str(points[i][-1])+"\n")
output.close()
out1.close()
plotout1.close()
head1.close()
out2.close()
plotout2.close()
head2.close()
out3.close()
plotout3.close()
head3.close()
out4.close()
plotout4.close()
head4.close()
file_head.close()
print "Process Completed"