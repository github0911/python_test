# -*- coding: utf-8 -*-
from random import shuffle
from Card import *

class Deck():
    def __init__(self):
        self.cards = list()
        for i in range(2, 15):
            for j in range(4):
                self.cards.append(Card(i, j))
        shuffle(self.cards)
    def rm_card(self):
        if len(self.cards) == 0:
            return
        return self.cards.pop()
