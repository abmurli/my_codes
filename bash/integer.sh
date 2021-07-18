line='2 41 -15 2'
eval "arr=($line)"
count=0
for x in "${arr[@]}"; do
    let s="(x<0?-x:x)"
    count=$(expr "$count" + $x)
done
echo $count
