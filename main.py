import config
import game

# hlavní game loop
while True:
    print("""Výtej ve hře logik

    použij jednu z možností:
    1: hrát
    2: nastavení obtížnosti
    3: odejít""")

    option = input()

    match option:
        case "1":
            game.start()
        case "2":
            config.setConfig()
        case "3":
            break

