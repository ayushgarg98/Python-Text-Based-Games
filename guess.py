print ("welcome")
import random
a = True
while a:
	r = random.randint(1,3)
	e = input("Enter your guess: ")
	if(e.isdigit() == True):
		if (int(e)==r):
			print("Woah!!")
		elif(int(e)>r):
			print("Too high")
		else:
			print("Too small")
		print("Answer is",r)
	else:
		 print("That's not an int!")
	if input("press 1 to go again: ") != "1":
			a = False
