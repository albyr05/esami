from csv import DictReader
import os
os.chdir(os.path.dirname(__file__))

#* restituisce una lista di dizionari di auto
def get_all_autos():
    autos = []
    try:
        f = open("auto.csv", "r")
        keys = f.readline().strip().split(",")              #& legge la prima riga
        for line in f:
            data = line.strip().split(",")
            car = {}
            for i in range(len(keys)):  
                car[keys[i]] = data[i]                      #& per ogni riga crea un dizionario che associa un corrispettivo valore alla chaive presente nella prima riga
            autos.append(car)                               #& aggiunge ogni auto ad una lista
    except FileNotFoundError as msg:
        print("file non trovato :(", msg)
        exit()

    return autos

#* gestisce la richiesta e modifica i valori del dizionario
def get_request(_inp, autos):
    num_to_day = {k: v for k,v in zip([x for x in range (1, 8)], ["Lunedì","Martedì","Mercoledì","Giovedì","Venerdì","Sabato","Domenica"])}                 #& associa ad un numero il corrsipettivo giorno della settimana 
    car_type, days = _inp.split()[0], list(map(int,_inp.split()[1:]))                  
    selected = []
    if car_type not in ["utilitaria", "media", "lusso", "sportiva", "furgone"]:
        raise KeyError
    for car in autos:
        if car["Categoria"] == car_type:
            count = 0
            for d in days:
                if car[num_to_day[d]] == "L":
                    count += 1 
            if count == len(days):                      #& se tutti i giorni richiesti sono liberi la macchina è candidata per la scelta
                selected.append(car)                    
    if len(selected) == 0:                      
        print("Non ci sono macchine che possano soddisfare le richeste")

    else:
        for i, auto in enumerate(selected):
            print(f"{i+1}) {auto["Marca"]} {auto["Modello"]} colore {auto["Colore"]}")                  #& stampa le inforazioni relative alle auto disponibili
        choose = int(input("Quale quoi prenotare? "))
        chosen_car = selected[choose-1]
        for car in autos:
            if car == chosen_car:
                for d in days:
                    car[num_to_day[d]] = "A"                                                    #& sovrascrive il valore dei giorni richiesti della macchina scelta come affittata
    print()

#* Stampa tutte le auto
def printauots(autos):
    keys = " ".join(autos[0].keys())                                    #& stampa l'intestazione 
    print(keys)
    for auto in autos:                          
        for k,v in auto.items():
            if k != "Domenica":
                print(f"{v}", end= ", ")
            else:
                print(v)
    print()
    
def main():
    autos = get_all_autos()
    printauots(autos)
    _inp = input("Scegli categoria e giorni: ").lower()
    while _inp != "":
        try:
            get_request(_inp, autos)
            printauots(autos)
        except KeyError:                    #& se viene sollevata un'eccezione di tipo keyerror stampo che l'input è incorretto e ripeto il ciclo
            print("Input incorretto")
            _inp = input("Scegli categoria e giorni: ").lower()             
            continue

        _inp = input("Scegli categoria e giorni: ").lower()

main()
