import os
def retrieveFile(filename):
    f = open(filename,'r')
    Data = f.readlines()
    lines=[]
    m=[]
    for line in Data[1:]:
        m=line[line.find("'")+1:line.find("'",line.find("'")+1)]
        lines.append(m+",u\n")  
    f.close()
    return lines
folder=raw_input("Enter the folder name/path : ")
fileList=os.listdir(folder)
os.chdir(folder)
p1="Input 2nd clustering"
os.mkdir(p1)
for fname in fileList:
    print "Processing %s Please Wait....." %(fname)
    trail=retrieveFile(fname)
    p2=p1+"/"+fname.rstrip(".txt")+"_mod.txt"
    f2=open(p2,"w")
    for i in trail:
        f2.write(i)
    f2.close()
print "Processing Completed\n"
        