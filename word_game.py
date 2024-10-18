import random


def guess_word():
    words = ["hello", "science", "broom", "ship", "jigsaw", "table", "tennis", "money", "window", "house"]
    answer = words[random.randint(0, len(words) - 1)]
    clue = f"_{answer[1:4]}" + "_" * len(answer[4:])
    guess = input(f"Guess the {len(answer)} letter word: {clue} ")
    if guess == answer:
        print("Correct!")
    else:
        print(f"Too bad! The answer was {answer}.")


def main():
    guess_word()


if __name__ == '__main__':
    main()
