# SHAUN
# Items include bannana, mushroom which refill health
def level_2(player1):
    user_input = ''

    print(f'{player1.name} Arrives in a weird colorful world with walking and flying turtles around. \r\n You see a rather big turltle in the distance who appraoches you and introduces himself as Bowser the King Koopa. \r\n He is looking for reliable help to kidnap the Princess, and offers info on a coin stash belonging to Mario. Bowser asks if you are interested.')

    user_input = input(f'Choose (A) To help Bowser, Choose (B) to decline ')

    if user_input == 'A':
        print("You arrive at Bowser's Castle. While in the castle waiting room you are approached by a koopa. He claims he is tired of working for Bowser and claims he has info on a huge stash in Bowser's chamber.")

        user_input = input('choose(A) to accept the offer. Choose (B) to decline')

        if user_input == 'A':
            print('A trap opens up beneath you and you fall in a pit of lava.\r\n GAME OVER!!')
            player1.game = False

        elif user_input == 'B':
            print("You passed the test. Now you and Bowser discuss your plans for the heist and head out to Mario's hideout. \r\n When you arrive at the hideout you approach Mario and Luigi to distract them. They offer you a giant mushroom.") 
            player1.exp += 5

            user_input = input('Choose (A) to accept the mushroom. Choose (B) to decline.')

            if user_input == 'A':
                print("You start to like Mario and Luigi and you decide to tell them Bowser's plan. \r\n Mario goes to stop Bowser,  Luigi offers you 15 coins for helping.")
                user_input = input("Choose (A) to accept. Choose (B) to decline and attempt to mug Luigi")

                if user_input == 'A':
                    print("You gain 15 coins but you lose 10exp for not attempting to steal")
                    player1.bounty += 15
                    player1.exp -= 10

                elif user_input =='B':
                    if player1.exp > 50:
                        print("You knock out Luigi and rob him of 50 coins. You gain 20exp")
                        player1.exp += 20
                    else:
                        print("Luigi jumps on your head for 10 damage and stuffs you in a nearby pipe")
                        player1.health -=10
                


            elif user_input == 'B':
                print("You hear screaming as Bowser is running out with the Princess. Mario and Luigi give chase leaving you alone. You locate the stash. You recieve 250 coins and jump in a near by tunnel to make your escapse")
                player1.bounty += 250
                player1.exp += 50

    elif user_input == 'B':
        print("Bowser hits you with a fireball for 5 damage, but luckily he gets hit with a barrel and knocked out. You are approached by Donkey Kong. \r\n Donkey asks for your help to find Diddy Kong who has been missing. It is assumed it is K-Rools doing. \r\n")
        player1.health -= 5

        user_input = 'Choose (A) to help. Choose (B) to decline'

        if user_input == 'A':
            print("You go with Donkey Kong to K-Rools hideout. After you execute your plan you begin to help Diddy escapse. He accidently reveals the location of their own stash of some sort, but he also mentions where he saw a stash in K-Rools hideout")

            user_input = input("To fight off Diddy and rob Donkey Kongs stash, choose (A). To go rob K-Rool choose (B).")

            if user_input == 'A':
                    print("You come across a huge stash but not exactly what you expected. You gain 50 bannanas")
                    # add 50 bannanas
            if user_input == 'B':
                if player1.exp < 40:
                    print("The henchman guarding the stash get the better of you, you take 10 damage and run to the nearest pipe to jump in and escape")
                    player1.health -= 10

                else:
                    print("You fight off a few henchman but you find a treasure of 50 coins and a bannana. Donkey Kong shows you to a pipe to get you out of this wacky world")
                    player1.bounty += 50
                    player1.exp += 30
                    #add bannana
        





        








        



        














