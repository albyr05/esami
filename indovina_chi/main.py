from csv import DictReader
import os
os.chdir(os.path.dirname(__file__))

#* Returna una lista di dizionari, ognuno contenente le informazioni su ogni personaggi
def get_chararacters():
    chararacters= []
    f = open ("personaggi.txt", "r")
    properties = f.readline().strip().split(";")        #& salvo le caraatteristiche
    for line in f:
        char = {}
        data = line.strip().split(";")
        for i in range(len(properties)):
            char[properties[i]] = data[i]           #& Associa ad ogni caratteristica il suo valore
        chararacters.append(char)
    f.close()
    return chararacters

#* stampa i personaggi come richiesto nell'output
def print_char(characters):
    for char in characters:
        for k, v in char.items():
            if v not in "SINO":
                if k == "Nome":
                    print(f"{v} -", end= " ")
                print(f"{k}: {v}", end= ", ")
            elif v == "SI":
                if k == "Pelato":
                    print(k, end=" ")
                else:
                    print(k, end=", ")
        print()
    print()

#* mantiene i personaggi che rispettano la caratteristica della domanda
def game(prop, value, characters):
    return [char for char in characters if char[prop] == value]

def main():
    characters = get_chararacters()
    print("Personaggi del gioco")
    print_char(characters)
    f = open("domande1.txt", "r")
    line = f.readline()
    count = 1

    while line != "":
        question = line.strip().split("=")
        prop, value = question[0], question[1]
        print(f"Mossa {count} - domanda: {prop} = {value}")
        print("Personaggi selezionati: ")
        characters = game(prop, value, characters)
        print_char(characters)
        
        count += 1
        line = f.readline()

    if len(characters) == 1:
        print("Gioco terminato, hai vinto; è stato selzionato: ")
        print_char(characters)
    else:
        print("Peccato hai perso :-(")
    f.close()

main()
