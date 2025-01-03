import os
os.chdir(os.path.dirname(__file__))

def get_map():
    try:
        _map, output = [], []
        f = open("mappa.txt", "r")
        for line in f:
            output.append(line.strip().split())
            _map.append(list(map(int, line.strip().split())))
    except FileNotFoundError:
        print("file non trovato")

    f.close()
    
    return _map, output


def check_high(i, j, _map, directions):
    for d in directions:
        try:
            current = _map[i][j]
            n_x, n_y = i + d[0], j + d[1]
            _next = _map[n_x][n_y]
            if current <= _next: 
                return False                    #& Se un elemento nel quadrato è maggiore returna subito false
        
        except IndexError:                      #& Se l'elemento adiacente fosse fuori dalla lista passa al prossimo
            continue

    return True                                 #& vuol dire che è un massimo

def printoutput(output):
    for i in range(len(output)):
        for j in range(len(output)):
            if output[i][j] != "-":
                print(f"{output[i][j]}", end= "")
            else:
                print(f"{output[i][j]}", end= " ")
        print()

def main():
    _map, output = get_map()
    d = 2 
    directions = []
    for x in range(-d, d+1):
        for y in range(-d, d+1):
            if x == y == 0:
                pass
            else:
                directions.append((x, y))
    
    for i in range(len(_map)):
        for j in range(len(_map)):
            if not check_high(i, j, _map, directions):
                output[i][j] = "-"                  #& se non è un massimo sostituisce il valore con un trattino
    printoutput(output)

main()