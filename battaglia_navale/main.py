import os 
os.chdir(os.path.dirname(__file__))

ROWS = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]                   #& sono le lettere delle righe
CONVERTED = {r:n for r, n in zip(ROWS, [_ for _ in range(10)])}             #& converte la lettera della riga in un indice della lista

#* crea una tabella dal file in lettura
def read_data(filename: str) -> list[list[str]]:
    table = []
    with open(filename, "r") as f:              
        for line in f:         
            line = line.strip()
            row = [c for c in line]         #& creo una lista con i singoli caratteri di ogni linea  
            table.append(row)               #& la aggiungo alla matrice

    return table

#* creo due tabelle vuote, sono quelle che verranno stampati ad ogni turno e man mano vengono aggiornate
def create_table() -> list[list[str]] :
    return [["  "]*10 for i in range(10)]           #& lista con elementi vuoti

#* stampa l'output della tabella ad ogni turno
def print_table(table: list[list[str]]): 
    print(f"    ", end = "")                
    column = "|  ".join([str(x) for x in range(1,11)])      #& è l'intestazione della tabella con il numero delle colonne
    print(column)                           
    for i in range(len(table)):             #& ciclo sulle righe
        print("-"*42)               #& stampa i trattini per separare le righe 
        for j in range(len(table)-1):           #& ciclo sulle colonne
            if j == 0:                      #& se è la prima colonna stampo anche la lettera della riga
                print(ROWS[i], end = "| ")  
                print(table[i][j], end = "| ")              
            else:
                print(table[i][j], end = "| ")                  #& stampo l'elemento della tabella 
        print()
    print("-"*42)

def game(t: list[list[str]], current: list[list[str]], row: str, column: str) -> str:
    i = CONVERTED[row]          #& trasformo la lettera della della mossa in un indice
    j = int(column) - 1         #& gli indici partono scalano di uno così partono da zero
    if t[i][j] != ",":          #& controllo se c'è una nave
        current[i][j] = "* "            #& rimpiazzo il valore della lista con l'asterisco (colpito)
        t[i][j] = ","                   #& "elimino" la nave colpita così posso poi controllare se ha vinto
        return "colpito"        
    
    else:       
        current[i][j] = "° "            #& se non c'è la nave ho preso acqua e quindi metot il pallino vuoto
    return "acqua"
    
#* controllo se la tabella non ha più navi, ritorno true --> qualcuno ha vinto
def check_win(t: list[list[str]]) -> bool:           
    for row in t:
        if row.count(",") != 10:
            return False
    return True

def main():
    current1 = create_table()           #& creo le due tabelle vuote
    current2 = create_table()
    t1, t2 = read_data("navi1.txt"), read_data("navi2.txt")         #& creo le due tabelle dal file
    play = True                                 
    player = True
    with open("mosse.txt", "r") as f:
        line = f.readline()         #& leggo la linea del file
        while line != "" and play:          #& il gioco continua fino a quando qualcuno ha vinto o finiscono le mosse
            move = line.strip().split(",")          #& è la mossa letta
            if player:
                print("E' il turno del giocatore 1")            
                print(f"Coordinate dell'attacco: {move[0]}, {move[1]}")
                esito = game(t2, current2, move[0], move[1])            #& controllo la tabella dell'avversario e printo "colpito" e "acqua", la funzione modifica anche la lista current dell'avversario
                print(esito)
                print_table(current2)

                if check_win(t2):
                    print("Ha vinto il giocatore 1")
                    play = False                #& se la tabella del giocatore 2 non ha più navi, il giocatore 1 ha vinto, si interrompe il ciclo

            else:                               #& stessa cosa di prima ma ora gioca il giocatore 2, quindi è tutto invertito
                print("E' il turno del giocatore 2")
                print(f"Coordinate dell'attacco: {move[0]}, {move[1]}")
                esito = game(t1, current1, move[0], move[1])
                print(esito)
                print_table(current1)

                if check_win(t1):
                    print("Ha vinto il giocatore 2")
                    play = False

            print()         

            line = f.readline()         #& leggo riga dopo

            player = not player             #& mi permette di alternare i due giocatori
    
main()   
