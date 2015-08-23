import sys
import re
class landmark:
	def __init__(self,x,y,z,alt,time,anchor):
		self.x=x
		self.y=y
		self.z=z
		self.time=time
		self.alt=alt
		self.anchor=anchor
		
		
def retrieveFile(filename):
	f = open(filename,'r')
	Data = f.readlines()
	#print Data
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
	minus=[]
	plus=[]
	marker={}
	markerType=""
	temp=[]
	for line in lines:
	
		fields=line.split(",")
		flength=len(fields)
		if flength==5 and mflag:
			if m>5:
			
				temp.pop(0)
				temp.append(line)
				#print temp
			else:
				
				temp.append(line)
				m=m+1
		elif flength==5 and pflag:
			print "plusss"
			if p<=5:
				
				temp.append(line)
				#print "plus",temp
				p=p+1
			else:
				p=0
				mflag=True
				m=0
				pflag=False
				marker[markerType]=temp
				#print temp
				temp=[]
				markerType=""	
					
		elif flength==6:
			mflag=False
			pflag=True
			l=landmark(fields[0],fields[1],fields[2],fields[3],fields[4],fields[5].rstrip("+"))
			#anomaly.append(l)
			#r=re.match("^[a-z]{1,20}_[0-9]{1,5}$",l.anchor)
			#if r:
			anomaly.append(l)
			markerType=fields[5]
			temp.append(line)
			#print "landmark",temp	
	print marker.keys()
	for values in marker:
		value=values.strip("+")
		fos=open("gpslog/"+value+".txt","w")
		
		data=marker[values]
		for i in data:
			fos.write(i+"\n")
		fos.close()
		
lines = retrieveFile(sys.argv[1])

parse(lines)
