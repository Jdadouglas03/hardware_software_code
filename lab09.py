def print_lyrics():
	print("Im a programmer, and im okay.")
	print("I code all night, and I code all day.")

def repeat_lyrics(count = 1):
	for number in range(count):
		print("{}############" .format(number), end=".")
		print_lyrics()
		print("############")

	

def main():
	repeat_lyrics()
	repeat_lyrics(4)

if __name__ == "__main__":
	main()


