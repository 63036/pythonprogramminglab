import random
l={'r':"rock",'p':"paper",'s':"scissor"}
while True:
#take input from user
	u=input("enter your choice")

#input from computer
	c=random.choice('rps')
	print("computer chooses",c)

#compare the user and computer choice
	if u==c:
		print("tie")
	elif u=="r"and c=="p":
		print("com wins")	

	if u==c:
		print("tie")
	elif u=="p"and c=="s":
		print("com wins")

	if u==c:
		print("tie")
	elif u=="s"and c=="r":
		print("com wins")

	if u==c:
		print("tie")
	elif u=="r"and c=="s":
		print("u wins")

	if u==c:
		print("tie")
	elif u=="s"and c=="p":
		print("u wins")

	if u==c:
		print("tie")
	elif u=="p"and c=="r":
		print("u wins")


