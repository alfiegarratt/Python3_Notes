from random import randint
loopy2 = True
loopy = True
while loopy:
	random_number = randint(1,10)
	print("number is:", random_number)
	while loopy2:
		user_choice =input("Pick a number between 1 and 10: ")
		user_choice = int(user_choice)
		if user_choice < random_number:
			print("too low try again")
			loopy = False
			loopy2 = True
		elif user_choice > random_number:
			print("too high try again")
			loopy = False
			loopy2 = True
		else:
			print("Bang on! Go again (y/n)")
			go_again = input()
			if go_again == "y":
				loopy = True
				random_number = randint(1,10)
			else:
				loopy = False
				loopy2 = False
