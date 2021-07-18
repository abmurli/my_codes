#!/bin/bash

#a=0
#while [ "$a" -lt 10 ]    # this is loop1
#do
#   b="$a"
#   while [ "$b" -ge 0 ]  # this is loop2
#   do
#      echo -n "$b"
#      b=`expr $b - 1`
#   done
#   echo
#   a=`expr $a + 1`
#done

#!/bin/sh

#a=0
#
#until [ $a -gt 10 ]
#do
#   echo $a
#   a=`expr $a + 1`
#done

#!/bin/sh

for var1 in 1 2 3
do
   for var2 in 0 5
   do
      if [ $var1 -eq 2 -a $var2 -eq 0 ]
      then
         break 2
      else
         echo "$var1 $var2"
      fi
   done
done