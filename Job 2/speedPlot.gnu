#set dgrid3d

set xlabel "time"
#set xrange [1:5]
set ylabel "speed"

#set zlabel "% of outliers"
#set zrange [0:1]
#set ztic auto  
set term png enhanced 
set datafile separator ","
set output "speed_time.png"
set grid

plot "outputGPSLogger_latlng1.txt" using 3:1 title 'lat,long' with linespoints lw 2
#"turn.txt" using 2:1 title 'Turn(lat,long)' with points  lw 2
#"OBearing3.txt" using 1:2 title 'Bearing3(Fixed)' with linespoints lw 2,\
#"OBearing4.txt" using 1:2 title 'Bearing4(Fixed)' with linespoints lw 2
set output "speed_time2.png"
set grid

plot "outputGPSLogger_latlng2.txt" using 3:1 title 'lat,long' with linespoints lw 2
set output "speed_time3.png"
set grid

plot "outputGPSLogger_latlng3.txt" using 3:1 title 'lat,long' with linespoints lw 2
#plot "Bearing4.txt" using 1:2 title 'Bearing(GPS)' with linespoints  lw 2,\
#"CBearing4.txt" using 1:2 title 'Bearing(Consecutive)' with linespoints lw 2,\
#"OBearing4.txt" using 1:2 title 'Bearing(Fixed)' with linespoints lw 2

