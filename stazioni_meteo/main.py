import os 
os.chdir(os.path.dirname(__file__))

def read_file(filename: str) -> tuple[dict[str:dict[str:list[float]]], list]:
    dataset = dict()
    try:
        with open(filename, "r") as f:              #& apertura del file 
            keys = f.readline().strip().split(";")              #& salvo l'intestazione
            for line in f:  
                info = line.strip().split(";")
                date = info[0].split()[0]           #& salvo la data
                if date not in dataset:                 #& se la data non è nel dizionario 
                    dataset[date] = dict()              #& creo la chiave e le associo un valore
                    for i in range(1, len(keys)):
                        dataset[date][keys[i]] = []             #& per ogni parametro creo una lista vuota
                        dataset[date][keys[i]].append(float(info[i]))           #& aggiungo alla lista il valore
                else:                                                               #& se la data c'è già appendo solo i valori alle liste dei rispettivi parametri
                    for i in range(1, len(keys)):
                        dataset[date][keys[i]].append(float(info[i]))
    except FileNotFoundError:
        print("file not found")
        exit()
                
    return dataset, keys[1:]            #& ritorno il dizionario e l'intestazione 


def calculate_stats(date: dict[str:list]) -> dict[str:float]:
    all_stats = {}
    for k in date:
        moda_dict = dict()
        average = sum(date[k]) / len(date[k])           #& calcolo media per ogni parametro
        _max = max(date[k])                         #& calcolo max
        _min = min(date[k])                         #& calcolo min
        moda_dict = {el:date[k].count(el) for el in set(date[k])}           #& creo un dizionario con chiave un elemento e valore quante volte quell'elemento è ripetuto nella lista
        moda = sorted(moda_dict.items(), key = lambda x: x[1], reverse= True)[0][0]             #& ordino in ordine decrescente e poi prendo la prima chiave (el ripetuto più volte)
        all_stats[k] = {"media": average, "massimo": _max, "minimo": _min, "moda": moda}            #& salvo info in un dizionario
        
    return all_stats
    
def stampa(data):
    labels = ['media', 'massimo', 'minimo', 'moda']
    for label in labels:
        row = f"{label:>8}" + "".join([f"{data[key][label]:>11.2f}" for key in data])
        print(row)

def main():
    dataset, values = read_file("torino.csv")
    print(" "*8, end = " ")
    for k in values:
        print(f"{k:>10s}", end = "  ")          #& stampa l'intestazione (i parametri)
    print()
    for d in dataset:
        print(d)            #& stampo il giorno
        statistics = calculate_stats(dataset[d])
        stampa(statistics)          #& stampo le statistiche dopo averle calcolate per ogni giornata
        
        
main()