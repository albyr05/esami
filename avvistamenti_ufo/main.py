import os 
os.chdir(os.path.dirname(__file__))

def main():
    state_dict = dict()
    max_durata = 0
    forma = None
    tipo = None
    with open("ufo_sightings.csv", "r") as f:
        for line in f:
            data = line.strip().split(",")
            if data[2] not in state_dict.keys():
                state_dict[data[2]] = 1
            else: 
                state_dict[data[2]] += 1
            if int(data[4]) > max_durata:
                max_durata = int(data[4])
                forma = data[3]
                tipo = data[-1]     
    
    sorted_dict = sorted(state_dict.items(), key = lambda x: x[1], reverse = True)
    print(f"Paese con il maggior numero di avvistamenti: {sorted_dict[0][0]}")
    print(f"Avvistamento di durata più lunga: {tipo} ({max_durata} secondi, Forma {forma})")

main()