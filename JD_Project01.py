def main():
	print("This program will ask you a series of questions like your name and education history")
	name = input("What is your name?")
	college_name = input("What college do you go to?")
	highschool_name = input("What highschool did you go to?")
	print(" Hello {}, so you went to highschool at {} and you go to college at {}." .format(name, highschool_name, college_name))
	print("Thank you for answering my questions!")
	institution_morefun = input("Hey! one last question, which institution you think is the most fun?")
	institution_lessfun = input("which institution do you think is the least fun?")
	print("So... you think {} is more fun than {}" .format(institution_morefun, institution_lessfun))
	print("Thank you so much for your time. Goodbye!")
	


if __name__ == "__main__":
	main()  
