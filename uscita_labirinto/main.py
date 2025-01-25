import os 
import random
os.chdir(os.path.dirname(__file__))

def get_map():
    with open("labirinto.txt") as f:
        start = f.readline().strip().split(",")             #& salvo la posizione iniziale
        target = f.readline().strip().split(",")                #& salvo l'uscita
        _map = [list(line.strip()) for line in f]           #& creo una matrice della mappa
        return start, target, _map

def next_move(i, j, directions, _map, movements):
    possible = False
    p_mov = []
    for dx, dy in directions:
        
        nx, ny = i + dx, j + dy
        if _map[nx][ny] not in ["X", "V"]:                  
            possible = True             #& se ci sono mosse possibili metto un flag
            p_mov.append((nx, ny))  
        

    if possible:
        new_x, new_y = random.choice(p_mov)             #& scelgo causualmente una mossa tra quelle possibili
        _map[new_x][new_y] = "V"                #& marco la posizione visitata
        movements.append((new_x, new_y))
    else:                   
        new_x, new_y = movements.pop(len(movements)-1)          #& non ci sono posizioni possibili e quindi torno indietro
    
    return new_x, new_y
        


def main():
    start, target, _map = get_map()
    directions = [(1, 0), (-1, 0), (0,1), (0,-1)]
    print(f"Posizione iniziale {start[0]} {start[1]}")
    movements = []
    _map[int(start[0])][int(start[1])] = "V"                #& marco la posizione iniziale
    current_x, current_y = next_move(int(start[0]), int(start[1]), directions, _map, movements)
    i = 1
    print(f"Movimento{i} : ({current_x}, {current_y})")
    while not(current_x == int(target[0]) and current_y == int(target[1])):             #& il ciclo va avanti fino all'uscita
        current_x, current_y = next_move(current_x, current_y, directions, _map, movements)         
        print(f"Movimento {i}: ({current_x}, {current_y})")
        i += 1

    
main()
