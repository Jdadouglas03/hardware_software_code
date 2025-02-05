def conversation():
	print("Do you like coding in python? Answer yes or no")
	answer = input().lower().strip()
	if answer == "yes":
		print("You answered {}, That's good - the united states needs more coders!!!." .format(answer))
	elif answer == "no":
		print("perhaps you will change your mind")
	else:
		print("I don't undertand?")
		conversation()

def main():
	print("Welcome to my conversation program")
	conversation()
	print("Thanks for chatting with me")

if __name__ == "__main__":
	main()