# -*- coding: utf-8 -*-

from Deck import *
from Player import *

class Game():
    def __init__(self):
        name1 = input("p1 name ")
        name2 = input("p2 name ")

        self.deck = Deck()
        self.p1 = Player(name1)
        self.p2 = Player(name2)
    
    def win(self, winner):
        """winner 获胜的玩家"""
        w = "{} wins this round"
        w = w.format(winner)
        print(w)

    def draw(self, p1n, p1c, p2n, p2c):
        d = "{} draw {} {} draw {} "
        d = d.format(p1n, p1c, p2n, p2c)
        print(d)
    
    def winner(self, p1, p2):
        if p1.wins > p2.wins:
            return p1.name
        if p1.wins < p2.wins:
            return p2.name
        return "It was a tie!"
    
    def play_game(self):
        cards = self.deck.cards
        print("beginning war")
        while len(cards) >= 2:
            m = "q to quit. Any " + " key to play: "
            response = input(m)
            if response == 'q':
                break
            p1c = self.deck.rm_card()
            p2c = self.deck.rm_card()
            p1n = self.p1.name
            p2n = self.p2.name
            self.draw(p1n, p1c, p2n, p2c)
            if p1c > p2c:
                self.p1.wins += 1
                self.win(self.p1.name)
            else:
                self.p2.wins += 1
                self.win(self.p2.name)
        win = self.winner(self.p1, self.p2)
        print("War is over. {} wins.".format(win))
