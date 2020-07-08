#!/usr/bin/python
import random 
hidden = random.randrange(1, 1000)
# print hidden
count=0 
guess = int(input("Please enter your guess: "))

while(guess!=hidden):
    if guess < hidden:
        count+=1
        guess=int(input("Your guess is too low thoda zyada soche:--"))
    else:
        count+=1
        guess=int(input("Your guess is too high thoda kam soche:--"))

print ("YES YOU GOT IT CORRECT IN {} ATTEMPT:::::))))))".format(count))
