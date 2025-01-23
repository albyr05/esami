import os 
os.chdir(os.path.dirname(__file__))

POINTS = {"Rosso": 5, "Verde": 3, "Giallo": 1}

def read_deck() -> tuple[list[str], list[str]]:
    p1, p2 = [], []             
    with open("mazzo.txt", "r") as f:
        i = 0
        line = f.readline()
        while line != "":
            card = line.strip()
            if i % 2 == 0:          #& assegno le carte ai 2 giocatori in modo alternato
                p1.append(card)
            else:
                p2.append(card)
            i += 1 
            line = f.readline()
    return p1, p2

def result(card1: str, card2: str) -> int:
    if POINTS[card1] == POINTS[card2]:          #& controllo le condizioni di vittoria 
        return 0
    elif POINTS[card1] > POINTS[card2]:
        return 1
    else:
        return -1

def game(p1: list[str], p2: list[str]):
    j = 0
    table = []
    points_1, points_2 = 0, 0
    print(f"Punteggio giocatore 1: {points_1}")
    print(f"Punteggio giocatore 2: {points_2}")
    while j < len(p1):
        print()
        print(f"Mano n. {j+1}")
        card1, card2 = p1[j], p2[j]             #& sono le carte giocate dai 2 giocatori
        print(f"Carta giocatore1: {card1}")             
        print(f"Carta giocatore2: {card2}")

        if result(card1, card2) == 0:
            print("Risultato: Pareggio")
            table.extend([card1, card2])        #& se c'è stato pareggio aggiungo salvo le carte che sono rimaste sul tavolo

        elif result(card1, card2) == 1:
            print("Risultato: Vince la mano il giocatore 1")
            table.extend([card1, card2])           
            points_1 += sum(POINTS[c] for c in table)           #& sommo tutte le carte che c'erano sul tavolo e assegno il punteggio al giocatore 
            table.clear()                           #& svuoto il tavolo 
            
        else: 
            print("Risultato: Vince la mano il giocatore 2")
            table.extend([card1, card2])
            points_2 += sum(POINTS[c] for c in table)
            table.clear()

        print(f"Punteggio giocatore 1: {points_1}")
        print(f"Punteggio giocatore 2: {points_2}")

        j += 1 

    if points_2 > points_1:
        print(f"\nVince il giocatore 2 con {points_2}.")
    elif points_1 > points_2:
        print(f"\nVince il giocatore 1 con {points_1}")
    else: 
        print("\nPartita finita in pareggio")
    
def main():
    try:
        p1, p2 = read_deck()
    except FileNotFoundError:
        print("file not found")
    game(p1, p2)

main()

