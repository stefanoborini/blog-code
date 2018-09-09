# creates the initial guess. grossly wrong

python ./piechart.py 100 400 iter_0.pdf
convert -geometry 210x158 iter_0.pdf iter_0.png 
echo "step w   h  white black"
step=1
while true; 
do
    data=`python imagedata.py iter_$(($step-1)).png`
    echo "$step - $data"
    python ./piechart.py `echo $data|awk '{print $3}'` `echo $data|awk '{print $4}'`  iter_$step.pdf
    convert -geometry 210x158 iter_$step.pdf iter_$step.png 
    step=$(($step+1))
done
