#!/bin/bash
read -p 'Enter first decimal number:' num1
read -p 'Enter second decimal number:' num2
echo "$num1 + $num2" | bc
echo "$num1 - $num2" | bc
echo "$num1 * $num2" | bc
echo "scale=2; $num1 / $num2" | bc
echo "$num1 % $num2" | bc

read -p 'Enter a number for square root:' num

echo "scale=2;sqrt($num)" | bc -l

read -p 'Enter number for exponent:' var
echo "scale=2;$var^2" | bc -l
