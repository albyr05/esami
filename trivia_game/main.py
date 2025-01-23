import os
import random
os.chdir(os.path.dirname(__file__))

def read_question() -> dict[int:list[dict]]:
    all_file = dict()
    with open("domande.txt", "r") as f:
        line = f.readline()
        dic = {0: "domanda", 1: "difficoltà", 2: "corretta", 3: "opzioni", 4: "opzioni", 5: "opzioni"}
        while line != "":
            i = 0           
            question = dict()
            while i <= 5:                   #& inizio un ciclo ogni volta che c'è una nuova domanda (legge le cinque righe successive)
                if i not in [3, 4, 5]:
                    question[dic[i]] = line.strip()         #& la domanda è nella prima riga 
                    if i == 2:
                        corretta = line.strip()             #& salvo la risposta corretta
                elif i == 3:
                    question[dic[i]] = [line.strip(), corretta]         #& inizializzo la lista delle opzioni
                else:
                    question[dic[i]].append(line.strip())           #& aggiungo tutte le opzioni 
            
                i+= 1           #& incremento e leggo la riga dopo
                line = f.readline()
   
            if int(question["difficoltà"]) not in all_file.keys():          
                all_file[int(question["difficoltà"])] = [question]          #& aggiungo la domanda alla lista delle domande del livello corrsipondente
            else:
                all_file[int(question["difficoltà"])].append(question)

            line = f.readline()             #& balzo la riga vuota

    return all_file

def game(all_question: dict[int:list[dict]] , points_d: dict[str:float], nickname: str):
    level = 0
    points = 0 
    game = True
    while level <= list(all_question.keys())[-1] and game:              #& il gioco continua fino a quando il giocatore non sbaglia o non arriva al livello massimo
        print()
        question = random.choice(all_question[level])               #& sceglie una domanda casuale da quelle possibili del livello corrente 
        print(f"Livello {level}) {question["domanda"]}")
        random.shuffle(question["opzioni"])                 #& mescolo le opzioni
        for i in range(len(question["opzioni"])):
            print(f"{i+1:>7d}) {question["opzioni"][i]}")           #& stampo le 4 opzioni
    
        risposta = input("inserisci la risposta: ")         
        while risposta not in ["1", "2", "3", "4"]:             #& inserimento della risposta e validazione dell'input
            risposta = input("inserisci la risposta: ")     
        risposta = int(risposta)
        if question["opzioni"][risposta-1] == question["corretta"]:             #& verifico la correttezza della risposta
            print("Risposta corretta!")
            level += 1                  #& incremento il livello e aumento di uno i punti del giocatore
            points += 1 
        else: 
            print(f"Risposta sbagliata. La risposta corretta era {question["corretta"]}")           #& se ha sbagliato stampo la risposta corretta
            game = False                        #& il gioco finisce

    print(f"\nHai totalizzato {points} punti")
    
    if nickname not in points_d:
        points_d[nickname] = points         #& aggiorno il punteggio del giocatore
    else:
        points_d[nickname] += points
        
def read_points() -> dict[str:int]:
    points = {}
    with open("points.txt", "r") as f:
        for line in f:
            if line != "\n":                #& salvo i punteggi dei giocatori se la linea non è vuota
                name, point = line.strip().split()
                points[name] = int(point)
            else:
                continue
    return points 

def change_points(points_d):
    points_d = dict(sorted(points_d.items(), key= lambda x: x[1], reverse= True))           #& ordino i giocatori per punteggio decrescente 
    with open("points.txt", "w") as f:
        for n, p in points_d.items():               #& scrivo i nuovi punteggi nel file 
            f.write(f"{n} {p} \n")
    
def main():
    all_question = read_question()
    nickname = input("Inserisci il tuo nickname: ")
    points_d = read_points()
    game(all_question, points_d, nickname)
    change_points(points_d)   

main()            

                        

