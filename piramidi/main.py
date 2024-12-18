import os 
os.chdir(os.path.dirname(__file__))

#* restituisce la mappa del file come una tabella
def create_table():
    f = open("mappa.txt", "r")
    table = []
    for line in  f:
        row = [int(el) for el in line.strip().split()]
        table.append(row)
    return table

#* controlla se la piramide corrente sia o meno una piramide
def check_high(_map:list, x, y):
    directions = [(0,1), (1,0), (-1,0), (0,-1), (1,1), (-1,-1), (1,-1), (-1,1)]         #& le possibili 8 direzioni, comprese le diagonali
    check = 0
    for d in directions:                                                                
        next_x, next_y = x + d[0], y+ d[1]                                              #& Sarà la posizione dell'elemento adiacente a quello della piramide nella direzione corrente
        if 0 <= next_x < len(_map) and 0 <= next_y < len(_map):
            if _map[next_x][next_y] < _map[x][y]:                                       #& controllo che l'altezza della pirramide adiciante sia minore di quella corrente
                check += 1                                                              #& l'elemento è valido e passo alla prossima direzione
            else:                                                                       
                break                                                                   #& se l'elemento non è valido vuol dire che la piramide non è una cima e quindi interrompo il ciclo
        else:
            check += 1                                                                  #& l'elemento esce dalla mappa e quindi posso considerare la piramide come cima in quella direzione perchè è sul bordo

    if check == 8:                                                                      #& Se la piramide è cima in tutte le direzioni sarà cima completa
        return True
    else:
        return False
    
#* Stampa l'output desiderato
def print_output(highs:list):
    for h in highs:
        for el in h:
            print(el, end = " ")
        print()
    average_high = sum(h[0] for h in highs) / len(highs)            #& calcola l'altezza media
    print(f"\nAltezza madia {average_high:.2f} ")

def main():
    highs = []
    _map = create_table()
    for i in range(len(_map)):
        for j in range(len(_map)):
            if check_high(_map, i, j):                  #& controllo se è una cima e mi salvo le informazioni in una lista
                highs.append((_map[i][j], i, j))
    print_output(highs)

main()
