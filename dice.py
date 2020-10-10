print ("welcome")
import random
a = True
while a:
	x = random.randint(1,6)
	print(x)
	if input("press 1 to go again: ") != "1":
		a = False
