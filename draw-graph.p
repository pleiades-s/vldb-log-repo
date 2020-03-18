# Scale font and line width (dpi) by changing the size! It will always display stretched.
set terminal svg size 400,300 enhanced fname 'arial'  fsize 10 butt solid
set output 'out.svg'

# Key means label...
set key inside bottom right
set xlabel 'Time (sec)'
set ylabel 'Compaction (sec)'
set title 'Zipfian'
plot  "data.txt" using 1:2 title 'L0' with lines, "data.txt" using 1:3 title 'L1' with lines, "data.txt" using 1:4 title 'L2' with lines,

# http://gnuplot.respawned.com/