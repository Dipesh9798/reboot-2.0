#!/bin/bash

echo "Plz enter something:--"
#here echo is similar to printf in C and print in Python
sleep 2
read x
#here read is similar to scanf in C and input in Python
echo "you have entered $x"
sleep 3

#we can use another
read -p "Enter a number " y
sleep 4
echo $y





