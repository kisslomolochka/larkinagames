import random
import prompt

def main():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('Find the greatest common divisor of given numbers.')

    for i in range(3):
        num1 = random.randint(1, 100)
        num2 = random.randint(1, 100)

        a, b = num1, num2
        while b:
            a, b = b, a % b
        correct_answer = a

        print(f'Question: {num1} {num2}')
        user_answer = prompt.string('Your answer: ')

        if int(user_answer) == correct_answer:
            print('Correct!')
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return

    print(f'Congratulations, {name}')

if __name__ == "__main__":
    main()
