set terminal x11
set datafile separator ','
set nokey

splot [10.7:11.7] [44.4:45.2]  'quakes-simple.txt' u 2:1:(-$3):($4/4) with points pt 7 ps var, 'quakes-strong.txt' u 2:1:(-$3) with points lt 4 pt 7 ps 2, 'cities.txt' u 2:1:(0):3 w points lt 3 pt 5 ps var, 'cities.txt' using 2:1:(0):4 with labels notitle point pt 0 lw .1 left offset 1,0 font "Arial,12"



