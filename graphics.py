import color as c
from config import *

# převede číslo na barvičku
def choseColor(i, colorfull):
    if colorfull:
        match i:
            case 1:
                return c.Red
            
            case 2:
                return c.Green
            
            case 3:
                return c.Yellow
            
            case 4:
                return c.Blue
            
            case 5:
                return c.Magenta
            
            case 6:
                return c.Cyan
            
            case 7:
                return c.White
            
            case 8:
                return c.Black
            
            case _:
                return c.RESET 
    else:
        match i:
            case 1:
                return c.White
            
            case 2:
                return c.Black

            case _:
                return c.RESET 


        
# převést řádek na textovou formu
def toString(bundle, colorfull) -> str:
    out = ""
    if bundle == None:
        out = "_ "*pocet_policek
    else:
        for i in bundle:
            out+=choseColor(i, colorfull)+str(i)+c.RESET+" "
    return out

# vypsat hlavní TUI
def printGame(hidden, guesses, answers, valid):

    spliter = "  |  "

    print(c.CLEAR)
    if valid:
        print(toString(hidden, True))
    else:
        print(c.B_Yellow+"X "*pocet_policek+c.RESET)

    print()
    for i in range(pocet_pokusu):
        try:
            print(toString(guesses[9-i], True) + spliter + toString(answers[9-i], False))
        except IndexError:
            print(toString(None, True) + spliter + toString(None, False))