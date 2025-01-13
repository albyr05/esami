import os
os.chdir(os.path.dirname(__file__))

#* Stampa la griglia 
def print_grid(grid):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            print(grid[i][j], end = " ")
        print()

    print()

#* assegna la prima posizione disponibile nella colonna selezionata
def position(grid, move, column):
    row = len(grid)-1           #& parto dall'ultima riga
    found = False
    while row >= 0 and not found:       
        if grid[row][column] == "-":            #& se è libera metto lì la pedina 
            grid[row][column] = move
            found = True
        else:
            row -= 1        #& altrimenti decremento di uno la riga
    return row

#* data la posizione dell'ultimo elemento returno True se rispecchia le condizioni richieste, gestisco i limiti della grglia con le eccezioni 
def check_tris(grid,i, j):         
    last = grid[i][j]
    try:
        if grid[i+1][j] == grid[i+2][j] == grid[i+3][j] == last:            #& elementi verso il basso
            return True
    except IndexError:
        pass

    try:
        if grid[i][j+1] == grid[i][j+2] == grid[i][j+3] == last:                #& elementi a destra
            return True
    except IndexError:
        pass

    try:
        if grid[i][j-1] == grid[i][j-2] == grid[i][j-3] == last:        #& elementi a sinistra
            return True
    except IndexError:
        pass

    try:    
        if grid[i+1][j-1] == grid[i+2][j-2] == grid[i+3][j-3] == last:      #& elementi sulla diagonale in basso a sx
            return True 
    except IndexError:
        pass
    
    try: 
        if grid[i+1][j+1] == grid[i+2][j+2] == grid[i+3][j+3] == last:           #& elementi sulla diagonale in basso a dx
            return True
    except IndexError:
        pass

    return False            #& altrimenti False

def main():
    grid = [["-"]*7 for _ in range(6)]
    print_grid(grid)
    try:
        with open("mosse.txt", "r") as  f:
            line = f.readline()
            tris = False
            counter = 0
            while line != "" and not tris:              #& leggo le mosse fino alla fine del file o finchè non c'è un tris
                player, column = line.strip().split()
                move = "0" if player == "G1" else "X"           #& assegno la mossa in base al giocatore
                print(f"Gioca il giocatore {player}")

                row = position(grid, move, int(column))         #& oltre a modificare la griglia mi salvo anche la riga, così ho le coordinate della posizione 
                print_grid(grid)                                #& stampo la nuova griglia ad ogni mossa

                if check_tris(grid, row, int(column)):              #& controllo il tris
                    tris = True

                counter += 1 
                line = f.readline()

        print(f"Ha vinto il giocatore {player} in {counter} mosse")

                
    except FileNotFoundError:
        print("file not found")
        exit()


main()