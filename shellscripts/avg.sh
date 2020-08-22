#!/bin/bash
read N
for i in {1..N}
do
    read n
    var=$((n+var))
    echo $var
    
done

echo "scale=3;$((var/N))" | bc -l 
