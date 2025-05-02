import config
import game
import tutorial
from color import CLEAR

# hlavní game loop
while True:
    print(CLEAR+"""Welcome to the game logik

    Chose one of the options:
    1: play
    2: settings
    3: tutorial
    3: exit""")

    option = input()

    match option:
        case "1":
            game.start()
        case "2":
            config.setConfig()
        case "3":
            tutorial.play()
        case "4":    
            break