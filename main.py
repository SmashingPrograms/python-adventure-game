from level_one import level_1
from level_two import level_2
from level_three import level_3
from level_four import level_4
from level_five import level_5

value = True


class Player:
    def __init__(self, exp, health, bounty):
        self.exp = exp
        self.health = health
        self.bounty = bounty
        self.item = []
        self.game = True


player1 = Player(exp=0, health=10, bounty=0)

level_1(player1)

if player1.game:
    level_2(player1)

if player1.game:
    level_3(player1)

if player1.game:
    level_4(player1)

if player1.game:
    level_5(player1)
