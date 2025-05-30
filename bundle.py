


# vybere náhodnou barvičku (barvy jsou vyjádřeny pomocí čísel)
def randColor() -> int:
    from config import pocet_barev
    from config import random
    return random.randint(0, pocet_barev)

# vytvoří nový řádek náhodných barev
def randBundle():
    from config import pocet_policek
    from config import opakovani_barev
    bundle = list()
    for i in range(pocet_policek):
        color = randColor()

        # vybere náhodnou barvičku ale pokud se opakuje a je zakázáno opakování barev vybere novou
        while color in bundle and not opakovani_barev:
            color = randColor()
        bundle.append(color)

    return bundle

class inputLenghtException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


# vytvoří nový řádek podle vstupu uživatele (příklad formátu "2 3 4 5 6")
def newBundle(user_input:str):
    from config import pocet_policek
    bundle = [int(i) for i in user_input.split(" ")]
    if len(bundle) != pocet_policek:
        raise inputLenghtException("Wrong number or arguments")
    return bundle


# porovná/vyhodnotí dva řádky a vrátí řádek, který ukazuje co bylo správně (bíle a černe barvičky)
# 0 = žádná shoda, 1 = někde shoda (bílá), 2 = přesná shoda (černá)
def compareBundles(guess, hidden):
    from config import pocet_policek
    from config import presne_hodnoceni
    answer_bundle = [0]*pocet_policek
    

    isValid = True
    used_index = 0
    index = 0
    for i in guess:
        # zkontroluje jestli je to přesná shoda
        if i == hidden[index]:
            answer_bundle[index] = 2
           

        # kdyz ne, tak se koukne jestli to je nepřesná shoda 
        else:
            isValid = False
            for j in hidden:
                if i == j:
                    answer_bundle[index] = 1
                    break
        index += 1

    if not presne_hodnoceni:
        answer_bundle = sorted(answer_bundle, reverse=True)
    return isValid, answer_bundle