import color as c
def play():
    for i in scenes:
        print(i)
        input()
        print(c.CLEAR)



scenes = [
    """Welcome to the tutorial
to continue press enter...""",

    """In this game you are given a random set of numbers that represent colors.\n
And your job is to guess the combination with the hints you get after each guess.\n
A black color (the number 2) tells you the number you guessed is an exact match.\n
A white color (the number 1) tells you the number you guessed is apart of the hidden combination.""",



"""This is an example playing field

X X X X X
_ _ _ _ _ | _ _ _ _ _
_ _ _ _ _ | _ _ _ _ _
_ _ _ _ _ | _ _ _ _ _
_ _ _ _ _ | _ _ _ _ _
_ _ _ _ _ | _ _ _ _ _
_ _ _ _ _ | _ _ _ _ _
_ _ _ _ _ | _ _ _ _ _
_ _ _ _ _ | _ _ _ _ _
_ _ _ _ _ | _ _ _ _ _
_ _ _ _ _ | _ _ _ _ _""",



"""X X X X X ←─ This is the hidden combination, it will reveal at the end of the game.
_ _ _ _ _ | _ _ _ _ _
_ _ _ _ _ | _ _ _ _ _
_ _ _ _ _ | _ _ _ _ _
_ _ _ _ _ | _ _ _ _ _
_ _ _ _ _ | _ _ _ _ _
_ _ _ _ _ | _ _ _ _ _
_ _ _ _ _ | _ _ _ _ _
_ _ _ _ _ | _ _ _ _ _
_ _ _ _ _ | _ _ _ _ _
_ _ _ _ _ | _ _ _ _ _
1 2 3 3 1 ←─ here you enter your guess (each number seperated by a space).""",




"""X X X X X
_ _ _ _ _ | _ _ _ _ _
_ _ _ _ _ | _ _ _ _ _
_ _ _ _ _ | _ _ _ _ _
_ _ _ _ _ | _ _ _ _ _
_ _ _ _ _ | _ _ _ _ _
_ _ _ _ _ | _ _ _ _ _
_ _ _ _ _ | _ _ _ _ _
_ _ _ _ _ | _ _ _ _ _
_ _ _ _ _ | _ _ _ _ _
1 2 3 3 1 | 1 2 0 0 1

    ↑           ↑
    │           │
    │           │
    │           └ In this column you have your hints.
    │           
    │
    └ In this column are your guesses.""",



    
"""X X X X X
_ _ _ _ _ | _ _ _ _ _
_ _ _ _ _ | _ _ _ _ _
_ _ _ _ _ | _ _ _ _ _
_ _ _ _ _ | _ _ _ _ _
_ _ _ _ _ | _ _ _ _ _
_ _ _ _ _ | _ _ _ _ _
_ _ _ _ _ | _ _ _ _ _
_ _ _ _ _ | _ _ _ _ _
_ _ _ _ _ | _ _ _ _ _
1 2 3 3 1 | 1 2 0 0 1
↑           ↑
│           │
└───┬─────┘
This means the number 1 you guessed is somewhere in the combination.""",


    
"""X X X X X
_ _ _ _ _ | _ _ _ _ _
_ _ _ _ _ | _ _ _ _ _
_ _ _ _ _ | _ _ _ _ _
_ _ _ _ _ | _ _ _ _ _
_ _ _ _ _ | _ _ _ _ _
_ _ _ _ _ | _ _ _ _ _
_ _ _ _ _ | _ _ _ _ _
_ _ _ _ _ | _ _ _ _ _
_ _ _ _ _ | _ _ _ _ _
1 2 3 3 1 | 1 2 0 0 1
  ↑           ↑
  │           │
  └───┬─────┘
  This means the number 2 you guessed exactly matches the number in the hidden combonatio.""",




"""X X X X X
_ _ _ _ _ | _ _ _ _ _
_ _ _ _ _ | _ _ _ _ _
_ _ _ _ _ | _ _ _ _ _
_ _ _ _ _ | _ _ _ _ _
_ _ _ _ _ | _ _ _ _ _
_ _ _ _ _ | _ _ _ _ _
_ _ _ _ _ | _ _ _ _ _
_ _ _ _ _ | _ _ _ _ _
_ _ _ _ _ | _ _ _ _ _
1 2 3 3 1 | 1 2 0 0 1
    ↑           ↑
    │           │
    └───┬─────┘
    This means the number 3 you guessed is not in the hidden combination.""",




"""That's all you need to know to play
It would be cool of you to star the repository on git and give me feedback or suggestions via git too."""
]