print("Welcome")
ch = True
while ch:
	a1 = str(input("Enter an adjective: "))
	a2 = str(input("Enter an adjective: "))
	n = str(input("Enter an noun: "))
	print("They saw my school is haunted; my" + " " +a1 + " friend says she saw a" + " " + a2 + " " + n + " at the end of the cafeteria.")
	while True:
		end = input("play again? YES/NO:")
		if end == "NO" or end =="no":
			ch = False
			break
		elif end == "yes" or end =="YES":
			ch = True
			break
		else:
			print("wrong choice")

