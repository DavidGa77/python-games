import random

options = ('Rock', 'Paper', 'Scissors')


def start_game():
    rand_no = random.randint(0, len(options) - 1)
    user_choice = input('Make a choice of Rock, Paper or Scissors: ').capitalize()
    comp_choice = options[rand_no]
    print(f'Computer chooses {comp_choice}.')
    play_game(user_choice, comp_choice)


def play_game(user: str, comp: str):
    if user in options:
        file = open("rpsCombos.txt", "r")
        for combination in file.readlines():
            winner = combination.split(' ')[0]
            loser = combination.split(' ')[1].strip('\n')
            if user == comp:
                print("It's a draw!")
                start_game()
                break
            elif user == winner and comp == loser:
                print('You Win!')
                break
            elif comp == winner and user == loser:
                print('You Lose!')
                break


def main():
    start_game()


if __name__ == '__main__':
    main()
