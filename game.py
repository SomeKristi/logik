import bundle
from config import *
import graphics
from time import sleep


def start():
    hidden = bundle.randBundle()

    guesses = list()
    answers = list()

    guess = ""
    show = False
    try:
        for i in range(pocet_pokusu):
            guessing = True
            while guessing:
                graphics.printGame(hidden, guesses, answers, show)
                print("Prosím zadejte váš odhad:")
                try:
                    option = input()

                    # Pokud bude nutno podvádět, tak se tímto zobrazí kombinace
                    if option == "X X X X X":
                        show = True

                    # Když zadá uživatel špatné hodnoty, tak to hodí chybu a ta je odchycena
                    guess = bundle.newBundle(option)
                    guessing = False
                except bundle.inputLenghtException:
                    print(c.Red+"napsal jsi špatný počet políček zkus to znovu"+c.RESET)
                    sleep(2)
                    
                except ValueError:
                    print(c.Red+"napsal jsi nečíselné hodnoty zkus to znovu"+c.RESET)
                    sleep(2)


            valid, answer_bundle = bundle.compareBundles(guess, hidden)

            guesses.append(guess)
            answers.append(answer_bundle)

            if valid:
                graphics.printGame(hidden, guesses, answers, True)
                print(c.Green+"Vyhrál jsi"+c.RESET)
                break
    except InterruptedError:
        print("Ukoncil jsi hru")

    if not valid:
        print(c.Red+"Prohrál jsi"+c.RESET)
        print("schovaný řádek byl: ", end="")
        print(hidden)