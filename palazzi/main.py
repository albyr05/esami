import os
os.chdir(os.path.dirname(__file__))
# funzione per leggere la mappa: mi restituisce un matrice rappresentativa del file già con i valori in intero
def read_map():
    mappa = []
    with open("mappa.txt", "r") as f:           # apro il file
        for line in f:                  # ciclo sulle righe
            row = []                    # lista della riga vuota
            line = line.strip()             # tolgo il \n
            for el in line:         
                row.append(int(el))         #aggiungo alla row l'elemento intero 
            mappa.append(row)           # aggiungo la riga alla matrice

    return mappa


# funzione che mi permette di torvare la sommatoria del valore della vista, directions è una lista di tuple
def calculate_sight(i, j, mappa, directions):
    rows = len(mappa)           # salvo i limiti della tabella
    column = len(mappa[i])
    sommatory = 0               
    current = mappa[i][j]           # è l'elemento di cui sto calcolando la sommatoria
    for dx, dy in directions:
        n_x, n_y = i + dx, j + dy           # mi sposto all'elemento successivo
        if 0 <= n_x < rows and 0 <= n_y < column:           # controllo se l'elemento adiacente è nei bordi della lista
            adjacent = mappa[n_x][n_y]
            delta = current - adjacent              # calcolo la differenza di altezza
        else:
            delta = current             # se è fuori dai bordi

        sommatory += delta          # aggiungo il delta alla sommatoria

    return sommatory            # ritorno la sommatoria

# printa l'output richiesto
def print_output(sights):
    sorted_sights = sorted(sights.items(), key = lambda x :x[1], reverse=True)          # ordino il dizionario in base al valore della vista decrescente
    for i in range(len(sorted_sights)):
        print(f"{i+1} {sorted_sights[i][0]}: valore = {sorted_sights[i][1]}")           # printo l'output


def main():
    try:
        mappa = read_map()              # recupero la mappa
        directions = []
        sights = dict()         # è un dizionario che avrà per chiave la tupla con la posizione nella mappa e valore la sommatoria
        # creo una lista di tuple che mi permetta di controllare tutti gli elementi adiacenti
        for x in range(-1,2):
            for y in range(-1, 2):
                if x == y == 0:         # escludo la tupla (0,0) perchè vorrebbe dire rimanere sullo stesso elemento
                    pass
                else:
                    directions.append((x, y))

        for i in range(len(mappa)):             # ciclo su ogni elemento della matrice
            for j in range(len(mappa[i])):
                sommatory = calculate_sight(i, j , mappa, directions)           # calcolo la sommatorie delle viste
                sights[(i, j)] = sommatory              # aggiungo al dizionario
        print_output(sights)

    except FileNotFoundError:
        print("file not found")
main()


