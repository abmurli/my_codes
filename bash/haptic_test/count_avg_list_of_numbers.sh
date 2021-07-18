count=0; total=0; for i in $( awk '{ print $1; }' file.txt );do total=$(echo $total+$i | bc ); ((count++)); done; echo "scale=5; $total / $count" | bc
