from random import randint

def play():
    lower_num, higher_num = 1, 10
    random_number = randint(lower_num, higher_num)
    print(f'Guess the number from {lower_num} to {higher_num}.')
    guesses = 0

    while guesses < 3:
        try:
            if guesses == 2:
                print('Last guess!!')
            user_guess = int(input('Guess: '))
            guesses += 1
        except ValueError as e:
            print('Please enter a valid number.')
            continue

        if user_guess > random_number:
            print('The number is lower.')
        elif user_guess < random_number:
            print('The number is higher')
        else:
            print('You guessed it!')
            break

def main():
    play()


if __name__ == '__main__':
    main()
