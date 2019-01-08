Q = True
while Q:
	print("Welcome")
	print("You are in the castle.") 
	b=1
	p=1
	def roomo():
		print("It is a dark room. There are two doors: one on the north and other on the west ")
		a = str(input("Where would you like to go "))
		if a == "north" or a == "NORTH":
			roomtw()
		elif a == "west" or a == "WEST":
			roomf()

	def roomtw():
		print("It is another room in the castle, with a small window on the left wall.")
		global b
		if b == 1:
			print(" There is a bottle lying on the floor")
			b1 = str(input("Would you like to examine the bottle "))
			if b1 == "Yes" or b1 == "yes":
				print("This is a black color bottle. It contains water. This might help you on your journey")
				b2 = str(input("Would you like to keep it? "))
				if b2 == "yes" or b2 == "YES":
					print("You got it")
					b = b-1
				else:
					print("As your wish")
			else:
				print("Okay")		
		print("There are three doors: one on the west, one on the north and one on the south ")
		a = str(input("Where would you like to go "))
		if a == "west" or a == "WEST":
			roomth()
		elif a == "south" or a == "SOUTH":
			roomo()
		else:
			print("oops! it was a trap, you are freezed.")

	def roomth():
		print("This is another room in the castle, it's pretty dark in here.")
		global p
		if p == 1:
			print(" There is a packet lying on the floor")
			p1 = str(input("Would you like to examine the packet "))
			if p1 == "Yes" or p1 == "yes":
				print("This is a wrapped packet. It contains some food items. This might help you on your journey")
				p2 = str(input("Would you like to keep it? "))
				if p2 == "yes" or p2 == "YES":
					print("You got it")
					p = p-1
				else:
					print("As your wish")
			else:
				print("Okay")		
		print("There are two doors: one on the east and other on the south")
		a = str(input("Where would you like to go "))
		if a == "east" or a == "EAST":
			roomtw()
		elif a == "SOUTH" or a == "south":
			roomf()

	def roomf():
		print("There is a strange smell in this room, it would be better if you move from here fast. There are three doors: one on the south, one on the east and one on the west ")
		a = str(input("Where would you like to go "))
		if a == "SOUTH" or a == "south":
			print("Woah!! You managed to find the exit. YOU ARE FREE")
		elif a == "west" or a == "WEST":
			print("oops! it was a trap, you are freezed.")
		elif a == "east" or a == "EAST":
			roomo()

	roomo()
	while True:
		end = input("play again? YES/NO:")
		if end == "NO" or end =="no":
			Q = False
			break
		elif end == "yes" or end =="YES":
			Q = True
			break
		else:
			print("wrong choice")