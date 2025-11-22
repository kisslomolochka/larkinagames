import random
import prompt

def main():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('What is the result of the expression?')

    for i in range(3):
        a = random.randint(1, 20)
        b = random.randint(1, 20)
        operation = random.choice(['+', '-', '*'])

        if operation == '+':
            correct = a + b
        elif operation == '-':
            correct = a - b
        else:
            correct = a * b

        print(f'Question: {a} {operation} {b}')
        answer = prompt.string('Your answer: ')

        if int(answer) == correct:
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct}'.")
            print(f"Let's try again, {name}!")
            return

    print(f'Congratulations, {name}!')

if __name__ == "__main__":
    main()
