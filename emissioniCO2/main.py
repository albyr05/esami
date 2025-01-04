import os
os.chdir(os.path.dirname(__file__))

def get_file():
    dataset = dict()
    with open("GCB.csv") as f:
        line = f.readline()
        values = line.strip().split(";")
        for line in f:
            info = line.strip().split(";")
            if info[0] not in dataset.keys():
                dataset[info[0]] = {info[1]: {"Totale": int(info[2]), "Carbone": int(info[3]), "Petrolio": int(info[4]), "Gas": int(info[5])}}
            else:
                dataset[info[0]][info[1]] = {"Totale": info[2], "Carbone": info[3], "Petrolio": info[4], "Gas": info[5]}

        return dataset, values
    
def first_task(dataset, values):
    print("\nAnni monitorati:", end= " ")
    country = list(dataset.keys())[0]
    print(list(dataset[country].keys())[0], list(dataset[country].keys())[-1])
    print("Paesi monitorati:", end= " ")
    for k in dataset:
        print(k, end = " ")
    print()
    print("Valori monitorati: ", end = " ")
    for x in values [2:]:
        print(x, end = " ")
    print()


def satisfy_query_country(query, dataset):
    output = dict()
    country, value = query["p1"], query["p2"]
    for year in dataset[country]:
        output[year] = dataset[country][year][value]
    difference = (int(list(output.values())[-1]) - int(list(output.values())[0])) / int(list(output.values())[0]) * 100
    return output, difference
    
def satisfy_query_max(query, dataset):
    year_ref, value_ref = query["p1"], query["p2"]
    maxcountry = max(dataset.items(), key = lambda x: x[1][year_ref][value_ref])
    mincountry = min(dataset.items(), key = lambda x: x[1][year_ref][value_ref])
    max_value = dataset[maxcountry[0]][year_ref][value_ref]
    min_value = dataset[mincountry[0]][year_ref][value_ref]
    difference = (int(max_value) - int(min_value)) / int(min_value) * 100
    return max_value, maxcountry[0], difference
    

def main():
    dataset, values = get_file()
    first_task(dataset, values)

    with open("queries.txt") as f:
        for line in f:
            print()
            op, par1, par2 = line.strip().split()
            query = {"op": op, "p1": par1, "p2": par2}
            if query["op"] == "paese":
                output, difference = satisfy_query_country(query, dataset)
                print(f"Paese: {query["p1"]} - valore {query["p2"]}")
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