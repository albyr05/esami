import os
import random
os.chdir(os.path.dirname(__file__))

NUMBERS = ["7", "8", "9", "10", "J", "Q", "K", "A"]             
SEMI = ["♥", "♦", "♣", "♠"]                        
VALUES = [7, 8, 9, 10, 11, 12, 13, 14]
VALORI = {k:v for k, v in zip(NUMBERS, VALUES)}             #& associo ad ogni carta un valore numerico

def create_deck():
    cards = []
    deck = [(c,s) for c in NUMBERS for s in SEMI]           #& creo il mazzo con (valore, seme)
    random.shuffle(deck)                                    #& mescolo il mazzo
    with open("mazzo.txt", "w") as f:
        for c, s in deck:                       
            f.write(f"{c} {s}\n")           #& scrivo nel file le carte
    cards = [deck[i:i+5] for i in range(0, len(deck)-5, 5)]             #& divido le carte in gruppi di 5 (mani)
    return cards

def all_n(group):
    return[g[0] for g in group]         #& ritorna tutti i numeri delle carte di una mano

def check_couple_double_tris_full_poker(group):         
    couple, tris, poker = 0, 0, 0
    all_numbers = all_n(group)              
    set_number = set(all_numbers)
    for n in set_number:                    #& controllo se e quanti duplicati ci sono in una mano
        if all_numbers.count(n) == 2 :          #& coppia
            couple += 1
        elif all_numbers.count(n) == 3 :            #& tris
            tris += 1  
        elif all_numbers.count(n) == 4:         #& poker
            poker += 1 

    if couple == 1 and tris == 1:
        return "full"
    elif couple == 1:
        return "coppia"  
    elif couple == 2:
        return "doppia coppia" 
    elif tris == 1:
        return "tris"
    elif poker == 1:
        return "poker"
    
    return False                #& se non è entrato negli if precedenti ritorna False


def check_scale_color_royal(group):
    scala, colore = False, False
    all_numbers = all_n(group)
    converted = set([VALORI[n] for n in all_numbers])               #& così ho ad ogni carta un valore numerico corrispondente
    if len(converted) == 5 and ((max(converted) - min(converted)) == 4):            #& se non ci sono duplicati e la differenza è 4 allora le carte sono in scala
        scala = True                
    semi = set([g[1] for g in group])           #& salvo tutti i semi della mano 
    if len(semi) == 1:                  #& se c'è solo un seme ha fatto colore
        colore = True
    if scala and colore:                #& se ha fatto scala e colore --> scala reale
        return "scala reale"
    elif scala:                         #& ha fatto solo scala 
        return "scala"  
    elif colore:                    #& ha fatto solo colore
        return "colore"
    
    return False                #& non ha fatto né scala, né scala reale né colore


def main():
    cards = create_deck()
    for group in cards:
        result = check_scale_color_royal(group)         #& controllo prima se ha fatto scala, colore o scala reale 
        if result == False:                                 
            result = check_couple_double_tris_full_poker(group)             #& se ha ritornato false                                
        for n, v in group:
            print(f"{n}{v}", end= " ")                      #& printo tutta la mano 
        if result == False:
            result = "Niente.."             #&  se non ha fatto nulla
        print(f"{result}")

main()



              