"""
projekt_2.py: druhý projekt do Engento Online Python Akademie

autor: Markéta Fejtek
email: demura.m@seznam.cz
"""

import random
import time

pozdrav = "Hi there!"
informace_1 = "I've generated a random 4 digit number for you."
informace_2 = "Let's play bulls and cows game."
oddelovač = "-" * len(informace_1)



def generujeme_cislo():
    cislo = random.sample(range(1, 10), 4)
    if cislo[0] != 1:
        cislo[0], cislo[1] == cislo[1], cislo[0]
    return ("".join(map(str, cislo)))

def overeni_vstupu(hrac_hada):
    if hrac_hada.startswith("0"):
        print("Invalid input. Number cannot start with 0", oddelovač, sep="\n")
        return False
    elif not hrac_hada.isdigit():
        print("Invalid input. Please enter only digits", oddelovač, sep="\n")
        return False
    elif not len(set(hrac_hada)) == len(hrac_hada):
        print("The number must not contain duplicates!", oddelovač, sep="\n")
        return False
    elif len(hrac_hada) != 4 :
        print("Invalid input. Enter a 4-digit number.", oddelovač, sep="\n")
        return False
    return True




def analyza_typu(typ, hadane_cislo):
    bulls = sum(a == b for a, b in zip(typ, hadane_cislo))
    cows = len(set(typ) & set(hadane_cislo)) - bulls
    print(f"{bulls} bull{'s' if bulls != 1 else ''}, "
            f"{cows} cow{'s' if cows != 1 else ''}")
    print(oddelovač)
    return bulls, cows

  
def hra_bezi():
    print(pozdrav, oddelovač, informace_1, informace_2, oddelovač, sep="\n")
    print("Enter a number:", oddelovač, sep="\n")
    
    tajne_cislo = generujeme_cislo()
    print(tajne_cislo)
    zacatek_hry = time.time()
    pocet_pokusu = 0
    while True:
        hrac_hada = input(">>>")
        pocet_pokusu += 1
        if overeni_vstupu(hrac_hada):
            if hrac_hada == tajne_cislo:
                konec_hry = time.time()
                cas_hry = konec_hry - zacatek_hry
                minutes, seconds = divmod(cas_hry, 60)
                print(f"Correct, you've guessed the right number in {pocet_pokusu} guesses")
                print(oddelovač, "That's amazing!",oddelovač, sep="\n")
                print(f"Game time is {int(minutes)} minut{'s' if minutes > 1 else ''} and {seconds:.2f} seconds")
                break
            else:  
                analyza_bulls_cows = analyza_typu(hrac_hada, tajne_cislo)
        else:
            continue
      


if __name__ == "__main__":
    hra_bezi()
