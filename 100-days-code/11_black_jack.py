############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

################################################################

import random
from os import system, name

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

class Player:

    def __init__(self, name) -> None:
        self.reset(name)
    
    def reset(self, name) -> None:
        # Resets to initial values of a hand
        self.hand = []
        self.name = name

    def draw_card(self) -> None:
        _ = random.choice(cards)

        # Accounting for an ace
        if _ == 11 and sum(self.hand) + _ > 21:
            _ = 1
        self.hand.append(_)

    def score(self) -> None:
        print(f'{self.name}\'s score: {sum(self.hand)}')

    def show_hand(self) -> None:
        print(f'{self.name}\'s hand: {self.hand}')

def clear():
    # To clear screen

    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


def play_game(user, dealer):
    # Game with one dealer(computer) and one player(user)

    dealer.draw_card()
    user.draw_card()
    dealer.draw_card()
    user.draw_card()

    user.show_hand()
    user.score()
    print(f'Dealer\'s first card: {dealer.hand[0]}')

    if sum(user.hand) == 21:

        while sum(dealer.hand) < 17:
            dealer.draw_card()
            if sum(dealer.hand) > 21:
                break

        dealer.show_hand()
        dealer.score()

        if sum(dealer.hand) == 21:
            print('It\'s a draw!')
        else:
            print('You win!')

    else:
        while sum(user.hand) < 21:
            _ = input('Draw another card? (y/n): ')
            if _.lower() == 'y':
                user.draw_card() 
                user.show_hand()
                user.score()
                print(f'Dealer\'s first card: {dealer.hand[0]}')
            else:
                break

        user.show_hand()
        user.score()

        while sum(dealer.hand) < 17:
            dealer.draw_card()
            if sum(dealer.hand) > 21 or sum(user.hand) < sum(dealer.hand):
                break
            

        dealer.show_hand()
        dealer.score()
        
        if sum(user.hand) > sum(dealer.hand) and sum(user.hand) <= 21 or sum(dealer.hand) > 21:
            print('You win!')
        elif sum(user.hand) < sum(dealer.hand) and sum(dealer.hand) <= 21 or sum(user.hand) > 21:
            print('You lose!')
        else:
            print('It\'s a draw!')

if __name__ == '__main__':

    user = Player('Player')
    dealer = Player('Dealer')
    
    while True:
        print("""
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
""")
        play_game(user, dealer)
        _ = input('Play another round? (y/n): ')
        if _.lower() == 'y':
            user.reset('Player')
            dealer.reset('Dealer')
            clear()
        else:
            break
        

        
