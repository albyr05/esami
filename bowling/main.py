import os
os.chdir(os.path.dirname(__file__))

def main():
    f = open("bowling.txt", "r")
    all_dataset = []
    for line in f:
        all_dataset.append(get_info_on_player(line))
    all_dataset.sort(key = lambda x: x ["total_score"], reverse= True)              #& Ordina i dati secondo la chiave "total score"
    print_output(all_dataset)
    find_best_zeros_and_strikes(all_dataset)

#* aggiunge ad una lista un diozionario per ogni giocatore con le relative informazioni 
def get_info_on_player(line):
    data = line.strip().split(";")
    name = data[1] 
    surname = data[0]
    points = list(map(int, data[2:]))           #& trasforma direttamente in intero tutti i punteggi
    info_d = {"name": name, "surname": surname, "score": points, "total_score": sum(points)}
    return info_d

#* stampa l'output per ogni giocatore
def print_output(info):     
    for player in info:
        print(f"{player["name"]:10s}{player["surname"]:10s} {player["total_score"]:5d}")

#* Trova il giocatore che ha fatto più strikes e più zeri in tutta la partita e ne stampa il nome (se esiste)
def find_best_zeros_and_strikes(dataset):
    best_zeros, best_strikes = 0, 0
    best_player, worst_player = None, None
    for player in dataset:
        n_strikes = player["score"].count(10)
        n_zeros = player["score"].count(0)
        if n_strikes > best_strikes:
            best_strikes = n_strikes
            best_player = f"{player["name"]} {player["surname"]}"
        if n_zeros > best_zeros:
            best_zeros = n_zeros
            worst_player = f"{player["name"]} {player["surname"]}"
        
    if best_player == None:
        print("Nessun giocatore ha effettuato strikes")
    else:
        print(f"{best_player} ha effettuato {best_strikes} strikes")
    if worst_player == None:
        print("Nessun giocatore ha mancato tutti i birilli")
    else:
        print(f"{worst_player} ha mancato tutti i birilli {best_zeros} volta/e")



main()