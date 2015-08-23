# Spatial-Clustering-of-GPS-Points

**Identification of Public Bus Stops and characterising their waiting time** is of significance 
in the domain of Intelligent Transportation System and public interest. 

![Alt text](https://cloud.githubusercontent.com/assets/7629815/9429771/11578500-49fa-11e5-9cd6-43b9b4f461a8.jpg)

## Motivation
>Surveys suggest that the existing systems and algorithms cannot be merely replicated 
in the context of developing regions, because of the kind of heterogeneity and chaotic situation prevalent in their transport system, in contrast to the orderly and much regulated system of the developed world. 
>Moreover a significant fraction of population residing here is not so tech-savvy, 
hence crowd-sourced based strategies renders useless. 
>Either novel algorithms/techniques are required or the existing ones have to undergo suitable adaptation 
and innovation to suit the contrasting characteristics of developing regions. 

So Using customized hardware we present the analysis of public bus GPS traces of more than **1000 km for a 23 km route of Durgapur**, 
a suburban city (West Bengal, India). We have revealed **53 Bus Stops with 2% false positive** along with their waiting time 
distribution using a density based spatio-temporal clustering algorithm.

The Live project is being updated in this [link](http://www.nitdgp.ac.in/MCN-RG/landmark/home.html)
A corresponding paper has been published in **ACM SIGSPATIAL MOBIGIS 2014** which can be found in this [link](http://dl.acm.org/citation.cfm?doid=2675316.2675323) 

![Alt text](https://cloud.githubusercontent.com/assets/7629815/9429750/7d21e984-49f9-11e5-811c-260b1fe9753c.png)

![Alt text](https://cloud.githubusercontent.com/assets/7629815/9429795/7b321594-49fa-11e5-98b1-fa3a18104771.jpg)

I was luckily a part of this project. And As a summer intern I had been assigned various Jobs which I had fulfilled in my intern ship

###My Contribution

##### JOB1
* **Input** -Latitude, Longitude, Altitude, TimeStamp
* **Output** -Speed (km/sec), Bearing, Time(s)
* **Work** -First of all GPS(Latitude,Longitude,Altitude,Timestamp) are extracted from The given recoded trail. 
Read, Processed and Parsed the input file to create output file using a pre-existing Formula for finding Speed and Time. 
The Speed-Time and Bearing Time Plots were created using GNU Plot. The same Code was run for different sets of Trails.

##### JOB2

* **Input** - Latitude, Longitude, Altitude, Time-Stamp
* **Output** - Speed, Bearing, Time, Latitude, Longitude
* **Work** - Read, Processed and Parsed the input file to create output file with Latitude and Longitude 
also include unlike previous File. The Speed-Time and Bearing Time Plots were created using GNU 
Plot.

##### JOB 3

Separated the four sensors data of **Accelerometer, GPS, Gyroscope and Linear Accelerometer** into 
separate files from the main file. A lot of **landmarks** are also marked like Bus Stop, Bumper, Turns 
and Busy Road are also marked for each sensors.

##### JOB 4

* **Input** -All trails of Accelerometer, Gyroscope, GPS and Linear Accelerometer were taken as Input
* **Output** -For each of four Sensors, Separate GPS-Data related to landmarks like Broken Road, Bumper, 
Bus Stop, Busy Road, Junction, Pot-hole, Turn is created
* **Work** -For each of the Sensors, **Different files corresponding to all above Landmarks created** . The file 
has 225 lines (if exists) before and after all the data of a particular Landmark to study the behaviour 
of these Landmarks. For GPS, 3 Lines before and after data chosen.

##### JOB 5

Read, Cleaned and Modified Some Portions in Voting Algorithm. Unused Extra Variables were 
omitted. All different trails were also merged and trails marked accordingly.

##### JOB 6

* **Input** -Latitude, Longitude, Bus Stop
* **Output** -Central Point for each Bus Stop
* **Work** -The central Point was calculated with the help of 3D Geometry whose formula was proposed 
by me. 

##### JOB 7

To calculate Distance, Time, Start Time and between two Geographic Points which are given as 
INPUT.

##### JOB 8

* **Input** -Raw GPS Trails recorded by the Logger Unit
* **Output** - A file with zero Latitude Longitude Points. (Wait Time, Start Time, Bus Stop Number,
Latitude, Longitude, index)
* **Work** -An User INPUT threshold will display only those points which are zero Lat-Long Points and 
above the given threshold. Along with it a summary of all these trails in a single file was prepared for 
better comparison

![Alt text](https://cloud.githubusercontent.com/assets/7629815/9429791/64d7cfbe-49fa-11e5-8a02-8863b6b88e88.png)

##### JOB 9

* **Input** -Raw GPS Trails recorded by the Logger Unit
* **Output** - A file with zero Latitude Longitude Points. (Wait Time, Start Time, Bus Stop Number,
Latitude, Longitude, index)
* **Work** -An User INPUT threshold will display only those points which are zero Lat-Long Points and 
above the given threshold. Along with it a summary of all these trails in a single file was prepared for 
better comparison

![Alt text](https://cloud.githubusercontent.com/assets/7629815/9429792/6f2bde92-49fa-11e5-9f5e-7f6d7bc7b603.jpg)

##### JOB 10

* **Input** - Cluster Heads of All Groups of Each Trails
* **Output** - Second Level Clustering of Bus Stops.
* **Work** -The Cluster heads of different trails are combined according to a formula given by Sir ,a final 
threshold of more than 15% bus stops and the whole result is plotted in Google Maps.Implementing 
Second Level Clustering
