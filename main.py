import random

coins = 250
chance = 5
# start
print('''Welcome...\nyou have 250 coins.\nyou have 5 chance to win.\njust guess number between 1-50.\n''')


def game():
    global coins, chance
    # random number
    random_number = random.randint(1, 50)
    # checks valid betting
    while True:
        bet = int(input('How much you want played? '))
        if bet <= coins:
            coins -= bet
            break
        elif bet > coins:
            print('You don\'t have enough coins')
            continue
    # guessing number loop
    while chance != 0:
        guess = int(input('Guess a number between 1-50: '))
        # coin balance checking
        if coins < 0:
            print('You ran out of coins...')
            break
        # valid number checking
        if guess > 50:
            print('just guess between 1-50')
            continue
        # correct number checking
        else:
            if guess == random_number:
                coins += bet * 2
                print(f'congratulations! You Win...,Now you have {coins} coins')
                break
            # guessing checking
            if guess > random_number:
                coins -= bet
                chance -= 1
                print(f'Guess a smaller number.You have {chance} chance.')
            # guessing checking
            if guess < random_number:
                print(f'Guess a bigger number.You have {chance} chance.')
                coins -= bet
                chance -= 1
        if chance == 0:
            print('You lose!,\nyou have no other chance')


if __name__ == '__main__':
    game()
