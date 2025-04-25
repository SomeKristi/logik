import random
import color as c

pocet_barev = 5 # 5-7
opakovani_barev = True # boolean
pocet_policek:int = 5 # 4-5
presne_hodnoceni = True # boolean
pocet_pokusu = 10

# zmněna nastavení
def setConfig():
    global pocet_barev
    global opakovani_barev
    global pocet_policek
    global presne_hodnoceni
    global pocet_pokusu
    try:
        while True:
            print("tvoje nastavení:")
            print("pocet_barev = " + str(pocet_barev))
            print("opakovani_barev = " + str(opakovani_barev))
            print("pocet_policek = " + str(pocet_policek))
            print("presne_hodnoceni = " + str(presne_hodnoceni))
            print("pocet_pokusu = " + str(pocet_pokusu))
            print("pokud chceš něco změnit tak to napiš stejně jako nahoře ale s jinou hodnotou")
            print("pokud nechceš níc mněnit tak dej enter")
            option = input()

            # odejít pokud nic nezadal
            if option == "":
                return
            
            try:
                key, value = option.split(" = ")

                # nastavit hodnotu
                if key == "pocet_barev":
                    pocet_barev = int(value)
                elif key == "opakovani_barev":
                    opakovani_barev = value
                elif key == "pocet_policek":
                    pocet_policek = int(value)
                elif key == "presne_hodnoceni":
                    presne_hodnoceni = value
                elif key == "pocet_pokusu":
                    pocet_pokusu = int(value)
                else:
                    print(c.Red+"Něco jsi zadal špatně"+c.RESET)
            except ValueError:
                print(c.Red+"Něco jsi zadal špatně"+c.RESET)
            print()
            

    except KeyboardInterrupt:
        print("Odešel jsi z nastavení")

