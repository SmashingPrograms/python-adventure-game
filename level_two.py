# SHAUN

def level_2(player1):
    user_input = ''

    print(f'{player1.name} Arrives in a weird colorful world with walking and flying turtles around. \r\n You see a rather big turltle in the distance who appraoches you and introduces himself as Bowser the King Koopa. \r\n He is looking for relable help to kidnap the Princess, and offers info on a coin stash belonging to Mario. Bowser asks if you are interested.')

    user_input = input(f'Choose (A) To help Bowser, Choose (B) to decline ')

    if user_input == 'A':
        print("You arrive at Bowser's Castle. While in the castle waiting room you are approached by a koopa. He claims he tired of working for Bowser and claims he has info on a huge stash in Bowser's chamber.")

        user_input = input('choose(A) to accept the offer. Choose (B) to decline')

        if user_input == 'A':
            print('You trap opens up beneath you and you fall in a pit of lava.\r\n GAME OVER!!')
            player1.game = False

        elif user_input == 'B':
            print("You passed the test. Now you and Bowser discuss your plans for the heist and head out to Mario's hideout. \r\n When you arrive at the hideout you approach Mario and Luigi to distract them. They offer you a giant mushroom.") 

            user_input = input('Choose (A) to accept the mushroom. Choose (B) to decline.')

            if user_input == 'A':
                print("You start to like Mario and Luigi and you decide to tell them Bowser's plan. \r\n   Luigi offers you 25 coins for helping.")
                user_input = input("Choose (A) to accpet. Choose (B) to decline and attempt to mug Luigi")

                if user_input == 'A':
                    player1.bounty += 25
                elif user_input =='B':
                    pass
                    #battle with Luigi
                #another scenario?


            elif user_input == 'B':
                print("You hear screaming as Bowser is running out with the Princess. Mario and Luigi give chase leaving you alone. You locate the stash. You recieve 250 coins and jump in a near by tunnel to make your escapse")
                player1.bounty += 250

    elif user_input == 'B':
        print("Bowser hits you with a fireball for 5 damage, but luckily he gets hit with a barrel and knocked out. You are approached by Donkey Kong. \r\n Donkey asks for your help to find Diddy Kong who has been missing. It is assumed it is K-Rools doing. \r\n")

        user_input = 'Choose (A) to help. Choose (B) to decline'

        if user_input == 'A':
            print("You go with Donkey Kong to K-Rools hideout. After you execute your plan you begin to help Diddy escapse. He accidently reveals the location of their own stash of some sort, but he also mentions where he saw a stash in K-Rools hideout")

            user_input = input("To fight off Diddy and rob Donkey Kongs stash, choose (A). To go rob K-Rool choose (B).")

            if user_input == 'A':
                    print("You come across a huge stash but not exactly what you expected. You gain 50 bannanas")
                    ##possibly another scenario
            if user_input == 'B':
                    print("You fight off a few henchman but you find a treasure of 50 coins and a bannana")
                    ##take damage based on exp
                    #possibly another scenario
        





        








        



        














