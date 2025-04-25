import bundle
import graphics
from time import sleep
import color as c


def start():
    import config
    hidden = bundle.randBundle()

    guesses = list()
    answers = list()

    guess = ""
    show = False
    valid = False
    try:
        for i in range(config.pocet_pokusu):
            guessing = True
            while guessing:
                graphics.printGame(hidden, guesses, answers, show)
                print("Prosím zadejte váš odhad:")
                try:
                    option = input()

                    # Pokud bude nutno podvádět, tak se tímto zobrazí kombinace
                    if option == "X":
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
    except KeyboardInterrupt:
        print(c.Red+"Ukoncil jsi hru"+c.RESET)
        sleep(2)

    if not valid:
        graphics.printGame(hidden, guesses, answers, True)
        print(c.Red+"Prohrál jsi"+c.RESET)