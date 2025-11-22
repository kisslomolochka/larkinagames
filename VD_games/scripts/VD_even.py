import random
import prompt

def main():
	print("welcome to the BRAIN GAMES!")
	name = prompt.string("May I have your name? ")
	print(f"hello, {name}")
	print('answer "yes" if the number is even, otherside answer "no".')

	for i in range(3):
		number = random.randint(1, 100)
		print(f"Question: {number}")
		answer = prompt.string("your answer: ")
	
		if number % 2 == 0:
			correct = "yes"
		else:
			correct = "no"

		if answer == correct:
			print("CORRECT!")
		else:
			print(f"Your answer - '{answer}' is wrong answer (haha loh). Correct answer was '{answer}'. ")
			print(f"Let's try again!, {name}")
			return

	print(f"Congrats, {name}!")

if __name__ == "__main__":
	main()
