# from level_one import level_1
# from level_two import level_2
from level_three import level_3
# from level_four import level_4
# from level_five import level_5

value = True


class Player:
    def __init__(self, exp, health, bounty, name):
        self.exp = exp
        self.health = health
        self.bounty = bounty
        self.item = []
        self.game = True
        self.name = name
        self.user_input = ''

    def change_health(self, num):  
        player1.health += num

    def change_bounty(self, bounty):  
        player1.bounty += bounty

    def change_exp(self, experience):  
        player1.exp += experience


player_name = input('Welcome to our adventure game. Please enter a name for your character ')

player1 = Player(exp=0, health=10, bounty=0, name=player_name)

# level_1(player1)

# if player1.game:
#     level_2(player1)

if player1.game:
    level_3(player1)

# if player1.game:
#     level_4(player1) 

# if player1.game:
#     level_5(player1)
