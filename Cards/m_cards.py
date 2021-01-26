# Dyson Smith
# Dec 17-2020
# Cards starting module


class Card(object):
    RANKS = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', ]
    SUITS = ['♥', '♦', '♣', '♠']

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        rep = str.format("""
        +----------+
        | {0:<2}{1}      |
        |          |
        |          |
        |          |
        |          |
        |      {1}{0:>2} |
        +----------+
        """, self.rank, self.suit)
        return rep


class Pos_Card(Card):

    def __init__(self, rank, suit, face_up=True):
        super(Pos_Card, self).__init__(rank, suit)
        self.is_face_up = face_up

    def __str__(self):
        if self.is_face_up:
            rep = str.format("""
            +----------+
            | {0:<2}{1}      |
            |          |
            |          |
            |          |
            |      {1}{0:>2} |
            +----------+
            """, self.rank, self.suit)
        else:
            rep = str.format("""
            +----------+
            |##########|
            |##########|
            |##########|
            |##########|
            |##########|
            +----------+
            """)
        return rep

    def flip(self):
        self.is_face_up = not self.is_face_up


class Hand(object):
    def __init__(self):
        self.cards = []

    def __str__(self):
        rep = ''
        if self.cards:
            for card in self.cards:
                rep += str(card)
        else:
            rep = '< EMPTY >'
        return rep

    def clear(self):
        self.cards = []

    def add(self, card):
        self.cards.append(card)

    def give(self, card, other_hand):
        self.cards.remove(card)
        other_hand.add(card)


class Deck(Hand):
    def shuffle(self):
        import random
        random.shuffle(self.cards)

    def deal(self, handslist, per_hand=1):
        for rounds in range(per_hand):
            for hand in handslist:
                if self.cards:
                    topcard = self.cards[0]
                    self.give(topcard, hand)
                else:
                    print("Out of cards")
                    for hand in handslist:
                        hand.clear()
                    self.clear()
                    self.populate()
                    self.shuffle()
                    self.deal(handslist, per_hand)

    def populate(self):
        for suit in Card.SUITS:
            for rank in Card.RANKS:
                self.add(Card(rank, suit))


if __name__ == "__main__":
    print("This is a modal with playing cards. This is not meant to be run on its own.")
    input("\n\nPress the enter key to exit")
