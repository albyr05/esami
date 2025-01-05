import os
os.chdir(os.path.dirname(__file__))

#* forma un dataset {Paese: {2013: {CO2: valore..}, 2014: {CO2: valore}...}, Paese2: {2013: {CO2: valore..}, 2014: {CO2: valore}...}}
def get_file(filename):
    dataset = dict()
    with open(filename, "r") as f:
        line = f.readline()
        values = line.strip().split(";")
        for line in f:
            info = line.strip().split(";")
            measures = {values[i]:int(info[i]) for i in range(2, len(values))}

            if info[0] not in dataset.keys():
                dataset[info[0]] = {info[1]: measures}
            else:
                dataset[info[0]][info[1]] = measures

        return dataset, values

#* Stampa i prima  dati richiesti
def first_task(dataset, values):
    print("Anni monitorati:", end= " ")
    country = list(dataset.keys())[0]               #& é il primo paese del dataset
    print(list(dataset[country].keys())[0], list(dataset[country].keys())[-1])          #& sono il primo e l'ultimo anno 
    print("Paesi monitorati:", end= " ")
    for k in dataset:
        print(k, end = " ")                 #& tutte le chiavi, quindi i paesi
    print()
    print("Valori monitorati: ", end = " ")
    for x in values [2:]:                           #& i valori monitorati, presi dalla prima riga del file  
        print(x, end = " ")
    print()

#* Soddisfa le richieste riguardanti l'operazione "paese"
def satisfy_query_country(query, dataset):
    output = dict()
    country, value = query["p1"], query["p2"]
    for year in dataset[country]:
        output[year] = dataset[country][year][value]                #& associa ad ogni anno il valore del parametro di emissione richiesto, creando il dizionario di return
    difference = (int(list(output.values())[-1]) - int(list(output.values())[0])) / int(list(output.values())[0]) * 100             #& calcola la differenza tra primo e ultimo 

    return output, difference
    
#* Soddisfa le richieste riguardanti l'operazione "paese"
def satisfy_query_max(query, dataset):
    year_ref, value_ref = query["p1"], query["p2"]
    maxcountry = max(dataset.items(), key = lambda x: x[1][year_ref][value_ref])            #& trova la coppia (Paese, suo dizionario) con il valore max/min nell'anno e nel parametro richiesto 
    mincountry = min(dataset.items(), key = lambda x: x[1][year_ref][value_ref])
    max_value = dataset[maxcountry[0]][year_ref][value_ref]                                 #& recupero anche il valore max/min 
    min_value = dataset[mincountry[0]][year_ref][value_ref]
    difference = (int(max_value) - int(min_value)) / int(min_value) * 100

    return max_value, maxcountry[0], difference
    

def main():
    filename = "GCB.csv"
    print(f"\nFile analizzato {filename}")
    dataset, values = get_file(filename)
    first_task(dataset, values)

    with open("queries.txt") as f:
        for line in f:
            print()
            op, par1, par2 = line.strip().split()
            query = {"op": op, "p1": par1, "p2": par2}
            if query["op"] == "paese":                                      
                output, difference = satisfy_query_country(query, dataset)
                print(f"Paese: {query["p1"]} - valore {query["p2"]}")               #& stampa dell'output
                for k in output.keys():
                    print(f"{k:7s}", end = " ")
                print()
                for v in output.values():
                    print(f"{str(v):7s}", end= " ")
                print()
                print(f"Differenza:  {difference:.2f}%")

            elif query["op"] == "massimo":
                maxvalue, max_country, difference = satisfy_query_max(query, dataset)
                print(f"Anno: {query["p1"]} - Valore: {query["p2"]}")
                print(f"Paese massimo: {max_country} ({maxvalue}, {difference:.2f}% rispetto al minimo)")


main()