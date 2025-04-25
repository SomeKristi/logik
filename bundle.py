from config import *


# vybere náhodnou barvičku (barvy jsou vyjádřeny pomocí čísel)
def randColor() -> int:
    return random.randint(0, pocet_barev)

# vytvoří nový řádek náhodných barev
def randBundle():
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
    bundle = [int(i) for i in user_input.split(" ")]
    if len(bundle) != pocet_policek:
        raise inputLenghtException("Wrong number or arguments")
    return bundle


# porovná/vyhodnotí dva řádky a vrátí řádek, který ukazuje co bylo správně (bíle a černe barvičky)
# 0 = žádná shoda, 1 = někde shoda (bílá), 2 = přesná shoda (černá)
def compareBundles(guess, hidden):
    answer_bundle = [0]*pocet_policek
    

    isValid = True
    used_index = 0
    index = 0
    for i in guess:
        # pokud je zaplé přsené hodnocení bude aktualizovat index na stejné místo jako kontrolujeme
        # pokud ne tak se bude used_index teprve posouvat když na políčko už zapsal 
        if presne_hodnoceni:
            used_index = index

        # zkontroluje jestli je to přesná shoda
        if i == hidden[index]:
            answer_bundle[used_index] = 2
            used_index+=1

        # kdyz ne, tak se koukne jestli to je nepřesná shoda 
        else:
            isValid = False
            for j in hidden:
                if i == j:
                    answer_bundle[used_index] = 1
                    used_index+=1
                    break
        index += 1

        if not presne_hodnoceni:
            answer_bundle = sorted(answer_bundle, reverse=True)
    return isValid, answer_bundle