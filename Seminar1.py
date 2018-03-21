Cypher_Control_Loop_Variable = 1
while Cypher_Control_Loop_Variable == 1:
	print(" Welcome")
	print(" Menu")
	User_Input = input(" Enter your choice, or type 'quit': ")
	if User_Input.lower() == 'quit':
		return 1
	elif User_Input.lower() == 'exit':
		return 0
	elif User_Input == "1":
		Instructions
	elif User_Input == "2":
		Encode
	elif User_Input == "3":
		Decode
	else:
		print(" Please enter an option on the list or type 'quit'.")