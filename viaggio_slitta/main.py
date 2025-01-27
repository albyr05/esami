import os
import math

os.chdir(os.path.dirname(__file__))

def get_province():                 
    province = {}
    with open("province.csv", "r") as f:
        f.readline()
        for line in f:                                  
            data = line.strip().split(",")              
            province[data[-3]] = (data[-2], data[-1])           #& prendo la sigla della provincia e la sua longitudine e latitudine

    return province 

def get_children():
    province = get_province()
    children = []
    with open("bambini.csv", "r") as f:
        keys = f.readline().strip().split(",")      #& leggo le chiavi
        for line in f:
            child = {}
            data = line.strip().split(",")
            for i in range(len(keys)):
                child[keys[i]] = data[i]            #& associo ad ogni chiave un valore
            child["lat"] = float(province[data[-1]][0])             #& aggiungo latitudine e longitudine 
            child["long"] = float(province[data[-1]][1])
            children.append(child)          #& aggiungo il bimbo alla lista dei bambini
    return children

def find_nordest(children):
    nordest = max(children, key = lambda x: x["lat"])           #& trova il bimbo più a nord
    return nordest

def coordinates(a, b):
    lat_a = a["lat"] * math.pi / 180            #& trasformo le coordinate in radianti
    long_a = a["long"] * math.pi / 180
    lat_b = b["lat"] * math.pi / 180
    long_b = b["long"] * math.pi / 180
    h = (math.sin((lat_a-lat_b)/2)**2) + (math.cos(lat_a)*math.cos(lat_b)*(math.sin((long_a-long_b)/2)**2))
    distance = 2* 6731* math.asin(math.sqrt(h))         #& calcolo le distanza dal bimbo corrente agli altri
    return distance

def find_closest(children, child):
    _min = 9999999999999
    closest = None
    for c in children:  
        d = coordinates(child, c)           #& trova il bambino più vicino
        if d < _min:
            _min = d
            closest = c 
    return closest, _min
                  
def main():
    try:
        children = get_children()
    except FileNotFoundError:
        print("file not found")
    find_nordest(children)
    child = find_nordest(children)

    print(f"Consegnato {child["regalo"]} a {child["nome"]} {child["cognome"]} ({child["provincia"]})")
    children.remove(child)      #& rimuovo il bambino 
    while children:
        child, distance = find_closest(children, child)         #& stampo
        print(f"\tViaggio di {distance} km")
        print(f"Consegnato {child["regalo"]} a {child["nome"]} {child["cognome"]} ({child["provincia"]})")      
        
        children.remove(child)
    

main()

