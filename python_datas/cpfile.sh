# !/bin/bash

#dog='find . -name "system.log*"'
#for i in $dog
#do
#echo $i
#done
#cao zuo hou de jieguo ruhe fuzhi yong qilai
genmu=$(pwd)
echo $genmu
rm -rf $genmu'/crashlog'
mkdir $genmu'/crashlog'

for((i=1; i<4; i++))
do
mkdir $genmu'/crashlog''/v'$i
dircmu=`echo $genmu'/crashlog''/v'$i'/'`
logfile=`echo $genmu'/v'$i'/system.log'`
echo $logfile
if [ -f "$logfile" ];then
     echo "file on"
     echo $dircmu
     echo $logfile
     cp $logfile $dircmu
fi
for((j=1; j<30; j++))
do
logfile=`echo $genmu'/v'$i'/system.log.'$j`
if [ -f "$logfile" ]; then
    echo "file on"
     echo $dircmu
     echo $logfile
     cp $logfile $dircmu
else
     break
fi
done

done