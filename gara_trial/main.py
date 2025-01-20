import os
os.chdir(os.path.dirname(__file__))

def get_partecipants():
    ppl = dict()
    with open ("partecipanti.txt", "r") as f:
        for line in f:
            n, name = line.strip().split(":")
            ppl[n] = name           #& pettorina: nome
    return ppl

def get_penalties() -> dict[str:int]:
    ppl = get_partecipants()            #& recupero il primo dizionario
    pentalty = dict()
    with open("penalita.txt", "r") as f:
        for line in f:
            data = line.strip().split(":")
            pentalty[ppl[data[0]]] = list(map(int,data[1:]))            #& nome: lista con penalità
    return pentalty

def create_leadboard(penalty: dict[str:int]):
    penalty_sum = {k:sum(penalty[k]) for k in penalty}      #& nome: somma penalità
    s_penalty = dict(sorted(penalty_sum.items(), key = lambda x : x[1]))        #& ordino in ordine crescente 
    print("Classifica:")
    for k in s_penalty:     
        print(f"{k:17s} {s_penalty[k]:2d} penalità")        #& stampo la classifica


def find_best_streak(penalty):
    best = 0    
    top = None
    for k in penalty:       #& per ogni partecipante
        i = 0
        while i < len(penalty[k]):      #& ciclo su ogni penalità
            if penalty[k][i] == 0:      #& se è uguale a zero inizio una sequenza
                j = 0
                while i < len(penalty[k]):      
                    if penalty[k][i] == 0:          #& se l'elemento successivo è ancora uguale a 0 incremento di uno la sequenza e passo all'elemento dopo
                        j += 1 
                        i += 1 
                    else:           #& se no interrompo il ciclo interno
                        break
                if j >= best:       #& se la sequenza appena terminata è maggiore a quella che prima era la più lunga sovrescrivo il suo valore e anche quello dle partecipante 
                    best = j
                    top = k 
            i += 1 
        
    return top, best 

def main():
    penalty = get_penalties()
    create_leadboard(penalty)
    top_partecipant, record = find_best_streak(penalty)
    print(f"Ha realizzato la più lunga sequenza {top_partecipant} con {record} prove consecutive superate senza errori")

main()
            
    

    

