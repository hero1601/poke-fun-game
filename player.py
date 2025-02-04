class Player:
    def __init__(self, name):
        self.name = name
        self.cards = []

    def draw_card(self):
        return self.cards.pop(0)

    def add_cards(self, cards):
        self.cards.append(cards)

class AI(Player):
    def __init__(self, name):
        super().__init__(name)