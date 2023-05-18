# What does this piece of code do?
# Answer: randomly pick 10 numbers in (1,100),and get the largest one.

# Import libraries
# randint allows drawing a random number,
# e.g. randint(1,5) draws a number between 1 and 5
from random import randint #importing a fuction

# ceil takes the ceiling of a number, i.e. the next higher integer.
# e.g. ceil(4.2)=5
from math import ceil #importing a fuction

progress=0
stored_random_number=0
while progress<10:
	progress+=1 #10 times to do the actions
	n = randint(1,100)
	if n > stored_random_number:
		stored_random_number = n #get the biggest one

print(stored_random_number)
