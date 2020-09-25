import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven',
         'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8,
          'Nine': 9, 'Ten': 10, 'Jack': 11, 'Queen': 12, 'King': 13, 'Ace': 14}


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return f'{self.rank} of {self.suit}'


class Deck:
    def __init__(self):
        self.all_cards = []
        for suit in suits:
            for rank in ranks:
                self.all_cards.append(Card(suit, rank))

    def shuffle_deck(self):
        random.shuffle(self.all_cards)

    def pick_one(self):
        return self.all_cards.pop()


class Player:
    def __init__(self, name):
        self.all_cards = []
        self.name = name

    def add_cards(self, cards):
        if type(cards) == type([]):
            self.all_cards.extend(cards)
        else:
            self.all_cards.append(cards)

    def remove_card(self):
        return self.all_cards.pop(0)

    def shuffle(self):
        random.shuffle(self.all_cards)

    def __str__(self):
        return f'Player {self.name} has {len(self.all_cards)} cards.'


# Game initialization
game = True
gameround = 0

player_one = Player("ONE")
player_two = Player("TWO")

deck = Deck()
deck.shuffle_deck()  # Shuffle the deck before splitting

# Distribute cards among players
for x in range(26):
    player_one.add_cards(deck.pick_one())
    player_two.add_cards(deck.pick_one())

while game:
    if len(player_one.all_cards) == 0:
        print("Player 1 has no cards ! Player 2 wins")
        game = False
        break
    if len(player_two.all_cards) == 0:
        print("Player 2 has no cards ! Player 1 wins")
        game = False
        break
    gameround += 1
    print(f'Round No: {gameround}')

    player_one_game_cards = []
    player_two_game_cards = []
    # Removing one card from players deck to compare
    player_one_game_cards.append(player_one.remove_card())
    player_two_game_cards.append(player_two.remove_card())

    gamewar = True

    while gamewar:
        if player_one_game_cards[-1].value > player_two_game_cards[-1].value:
            player_one.add_cards(player_one_game_cards)
            player_one.add_cards(player_two_game_cards)
            # Shuffling cards after adding new cards
            player_one.shuffle()
            gamewar = False

        elif player_two_game_cards[-1].value > player_one_game_cards[-1].value:
            player_two.add_cards(player_one_game_cards)
            player_two.add_cards(player_two_game_cards)
            # Shuffling cards after adding new cards
            player_two.shuffle()
            gamewar = False

        else:
            print("Players at war")
            if len(player_one.all_cards) < 3:
                print('Player 1 dont have cards to be at war')
                print('Player 2 wins!')
                game = False
                break
            elif len(player_two.all_cards) < 3:
                print('Player 2 dont have cards to be at war')
                print('Player 1 wins!')
                game = False
                break
            else:
                # adding three cards in case of war.

                for num in range(3):
                    # Shuffling cards before removing
                    player_one.shuffle()
                    player_two.shuffle()
                    # Adding cards for the next round
                    player_one_game_cards.append(player_one.remove_card())
                    player_two_game_cards.append(player_two.remove_card())
