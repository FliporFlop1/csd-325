"""Cho-Han, Modified by Jadon Argo
Original Author: Al Sweigart al@inventwithpython.com
The traditional Japanese dice game of even-odd, with custom rule updates.

Modifications:
- Input prompt changed to initials (ja:)
- House fee changed from 10% to 12%
- Added rule: if dice roll is 2 or 7, player receives a 10 mon bonus
- Bonus is added to purse if the bonus condition is met
"""

import random, sys

JAPANESE_NUMBERS = {1: 'ICHI', 2: 'NI', 3: 'SAN',
                    4: 'SHI', 5: 'GO', 6: 'ROKU'}

print('''Cho-Han, by Al Sweigart (Modified by Jadon Argo)

In this traditional Japanese dice game, two dice are rolled in a bamboo
cup by the dealer sitting on the floor. The player must guess if the
dice total to an even (cho) or odd (han) number.

BONUS RULE: If you roll a 2 or a 7, you receive a 10 mon bonus!
''')

purse = 5000
while True:  # Main game loop.
    # Place your bet:
    print('You have', purse, 'mon. How much do you bet? (or QUIT)')
    while True:
        pot = input('ja: ')
        if pot.upper() == 'QUIT':
            print('Thanks for playing!')
            sys.exit()
        elif not pot.isdecimal():
            print('Please enter a number.')
        elif int(pot) > purse:
            print('You do not have enough to make that bet.')
        else:
            pot = int(pot)
            break

    # Roll the dice
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)

    print('The dealer swirls the cup and you hear the rattle of dice.')
    print('The dealer slams the cup on the floor, still covering the')
    print('dice and asks for your bet.')
    print()
    print('    CHO (even) or HAN (odd)?')

    # Let the player bet cho or han:
    while True:
        bet = input('ja: ').upper()
        if bet not in ('CHO', 'HAN'):
            print('Please enter either "CHO" or "HAN".')
        else:
            break

    print('The dealer lifts the cup to reveal:')
    print('  ', JAPANESE_NUMBERS[dice1], '-', JAPANESE_NUMBERS[dice2])
    print('    ', dice1, '-', dice2)

    # Determine outcome
    rollTotal = dice1 + dice2
    rollIsEven = rollTotal % 2 == 0
    correctBet = 'CHO' if rollIsEven else 'HAN'
    playerWon = bet == correctBet

    # Display result
    if playerWon:
        print('You won! You take', pot, 'mon.')
        purse += pot

        # House takes 12%
        house_fee = int(pot * 0.12)
        print('The house collects a', house_fee, 'mon fee.')
        purse -= house_fee
    else:
        purse -= pot
        print('You lost!')

    # Bonus rule for rolling a 2 or 7
    if rollTotal == 2 or rollTotal == 7:
        print('Bonus! You rolled a', rollTotal, 'and receive a 10 mon bonus!')
        purse += 10

    # End condition
    if purse == 0:
        print('You have run out of money!')
        print('Thanks for playing!')
        sys.exit()


