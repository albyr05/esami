import os
import random
os.chdir(os.path.dirname(__file__))

def get_qualified():
    players = dict()
    with open("qualificati.txt", "r") as f:                 
        for line in f:
            data = line.strip().split(",")
            players[data[0]] = data[1]              #& salvo nel dizionario numero giocatore e nome 
    return players

def create_gironi(players):
    teste = list(players.keys())            
    red = [teste[0]]
    green = [teste[1]]
    options = [(teste[i], teste[i+1]) for i in range(2,len(teste), 2)]              #& creo tuple di due giocatori consecutivi
    for i, j in options:
        first = random.choice([i, j])           #& scelgo a caso tra uno dei due giocatori e lo metto nel girno rosso
        second = j if first == i else i         #& l'altro lo metto nel girone verde
        red.append(first)
        green.append(second)

    return red, green

def write_calendar(name, players, girone):
    with open("calendar.txt", "a") as f:
        f.write(f"GIRONE {name}\n")                 #& scrivo nel file il nome del girone

        girone_copy = girone.copy()                 #& copio il girone iniziale
        for i in range(1, 4):   
            f.write(f"Giornata{i}\n")               #& scrivo la giornata
            j = 0
            girone = list(girone_copy)
            while j < 2:
                p1 = random.choice(girone)              #& scelgo il primo giocatore
                p2 = random.choice(girone)              #& e il secondo
                while p2 == p1:                         #& se per caso sono uguali cambio il secondo
                    p2 = random.choice(girone)  
                
                f.write(f"{players[p1]} vs {players[p2]}\n" )           #& scrivo il match
                girone.remove(p1)                       #& elimino i due giocatori dalla giornata corrente, in modo che non possano fare un altro match
                girone.remove(p2)
                j +=1           #& scrivo 2 incontri per giornata 


def create_file(name, girone, players):             #& creo e scrivo i due file dei 2 gironi 
    filename = name + ".txt"
    f = open(filename, "w")
    for n in girone:
        f.write(f"{n} - {players[n]}\n")
    f.close()


def main():
    players = get_qualified()
    red, green = create_gironi(players)
    create_file("red", red, players)
    create_file("green", green, players)
    write_calendar("VERDE", players, green)
    write_calendar("ROSSO", players, red)
   


main()