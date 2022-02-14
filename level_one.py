# BILLY

def level_1(player1):
    prompts = [
        {
            'prompt': 'You\'re in the electronics aisle.',
            'answers': [
                'Bargain $10 from a frail old man walking by.',
                'Break the glass, steal a computer, and run.',
                'Take something off the shelf; doesn\'t look like there\'s a camera there!'
            ],
            'consequences': [
                {
                    'description': 'It worked! His brain ain\'t working so well in his old age, so he was easy to cheat out of math.',
                    'health': 3,
                    'bounty': 1,
                    'experience': 3,
                },
                {
                    'description': 'Oh no! A security guard caught you! Off to jail!',
                    'health': -10000,
                    'bounty': 2,
                    'experience': 0,
                },
                {
                    'description': 'Agh! Someone almost saw you, so you lost your chance. Almost got caught... Phew, that was close!',
                    'health': 0,
                    'bounty': 1,
                    'experience': 0,
                },
            ]
        },
        {
            'prompt': 'You\'re at the checkout line...',
            'answers': [
                'Bargain $10 from an experienced cashier.',
                'Slip an item out of someone else\'s cart and walk off with it after checking out',
                'Impulse buy some gum'
            ],
            'consequences': [
                {
                    'description': 'Bad move, the cashier knows his math and knows your game. The cops were called to the scene so you better hit the road!',
                    'health': -1,
                    'bounty': 5,
                    'experience': 1,
                },
                {
                    'description': 'You were quite sneaky enough. You stole a watch from the shopping cart. Looks like it could be pawned for some money!',
                    'health': 3,
                    'bounty': 1,
                    'experience': 3,
                },
                {
                    'description': 'What were you even thinking!!! For shame, a thief impulse buying something so useless.',
                    'health': -5,
                    'bounty': 0,
                    'experience': -1,
                },
            ]
        },
        {
            'prompt': 'You\'re in the produce section.',
            'answers': [
                'Take one banana off of a stem of them when no one is looking.',
                'Sneak up and pickpocket the lady in front of you.',
                'Pull the fire alarm to distract everyone so you can loot.'
            ],
            'consequences': [
                {
                    'description': 'Success! No one saw you!',
                    'health': 3,
                    'bounty': 1,
                    'experience': 1,
                },
                {
                    'description': 'Eek! She yells! Now you\'re REALLY in trouble!',
                    'health': -10000,
                    'bounty': 2,
                    'experience': 1,
                },
                {
                    'description': 'It worked! No one knows what happened! You take lots of food, but you need to run, because now your bounty\'s gonna be pretty high!',
                    'health': 10,
                    'bounty': 10,
                    'experience': 5,
                },
            ]
        },
    ]

    choices = ['A', 'B', 'C']

    print(prompts)
    print("Setting: 2000 AD. You walk into a Wal-Mart shopping center. People. People everywhere! Shoppers, mall cops, everybody! So much that could be stolen, so many people that could be robbed or manipulated. But so much danger!")

    for p in prompts:
        print("Player health: ", player1.health, "\nPlayer bounty: ", player1.bounty, "\nPlayer experience: ", player1.exp)

        prompt_string = "\n\n\n" + p["prompt"] + "\n" + "Choices: A) " + p["answers"][0] + " B) " + p["answers"][1] + " C) " + p["answers"][2] + " "
        prompt = input(prompt_string)

        prompt = prompt.upper()

        if prompt == "":
            print("Please type something")
            exit()
        elif prompt not in choices:
            print("Please enter A, B, or C...")
            exit()
        
        choice = choices.index(prompt)

        consequence = p["consequences"][choice]

        print("\n\n" + consequence["description"])
        player1.health += consequence["health"]
        player1.bounty += consequence["bounty"]
        player1.exp += consequence["experience"]
        if player1.health <= 0:
            print("You have no health left! You're dead!")
            exit()