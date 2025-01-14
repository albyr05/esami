import os 

os.chdir(os.path.dirname(__file__))

def get_source():
    all_sources = dict()
    with open("risorse.txt", "r") as f:
        source = f.readline().split()
    types = ["A", "B", "C", "D", "E"]
    for el, t in zip(source, types):
        all_sources[t] = int(el)
    for t in types:
        if t not in all_sources.keys():             #& quelli che non hanno valori dal file partonocon 0
            all_sources[t] = 0 
        else:
            pass
    return all_sources

def find_limit(all_sources, types, maxs):
    _all_ingredients = {}
    for t in types:
        if all_sources[t] // maxs[t] >= 1:
            _all_ingredients[t] = all_sources[t] // maxs[t]             #& salvo i rapporti interi
        else:
            return 0                                            #& se non ci sono abbastanza risorse return 0
    limit = min(_all_ingredients[t] for t in types)         #& cerco il valore minimo che dovrei prendere, quindi quello limita 
    return limit

def nuclear(maxs, all_sources):
    types = ["A", "B", "C"]
    limit = find_limit(all_sources, types, maxs)
    for t in types:
        all_sources[t] -= maxs[t] * limit               #& sottraggo i multipli del limite di ogni reagente 
    all_sources["D"] += 10*limit
    all_sources["E"] += 15*limit            #& aggiungo i prodotti
    return limit                    #& è il valore dell'energia prodotta

#* analogog a nuclear
def anular(maxs, all_sources):
    types = ["D", "E"]
    limit = find_limit(all_sources, types, maxs)
    for t in types:
        all_sources[t] -= maxs[t] * limit
    all_sources["A"] += 5*limit
    all_sources["B"] += 7*limit
    all_sources["C"] += 11*limit
    return 2*limit
    

def main():
    all_sources = get_source()
    maxs = {"A": 10, "B": 3, "C": 7, "D": 6, "E": 5}            #& sono i valori consumati ad ogni ciclo
    energy_tot = 0                  
    end = False
    cycle = 0
    max_production, most_productive_cycle = 0, 0                

    while cycle < 1000 and not end:             #& faccio reagire fino a 1000 cicli o se finiscono le risorse

        n_energy_cycle = nuclear(maxs, all_sources)
        energy_tot += n_energy_cycle                    #& sommo all'energia totale quella del ciclo nucleare
        if n_energy_cycle == 0:                 #& se è zero vuol dire che sonon finite le risorse necessarie 
            end = True

        else:                       #& alrimenti procedo con la fase anulare 
            a_energy_cycle = anular(maxs, all_sources)
            energy_tot+= a_energy_cycle
            if a_energy_cycle == 0:
                end = True

        if a_energy_cycle + n_energy_cycle >= max_production:           #& ricerca del ciclo pù produttivo           
            max_production = a_energy_cycle + n_energy_cycle
            most_productive_cycle = cycle
        
        cycle += 1 
    
    print(f"Energia totale {energy_tot}MW")

    print(f"Ciclo più produttivo {most_productive_cycle}")


main()