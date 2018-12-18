class Table:
    def __init__(self):
        self.name = str
        self.cards = list()

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def add_card(self, card):
        self.cards.append(card)

    def remove_card(self, card):
        for index, card_item in enumerate(self.cards):
            if card.matchUser(card_item):
                self.cards.pop(index)
                break

    def move_card(self, card, table, order):
        pass

    def reorder_card(self, card, index):
        pass
