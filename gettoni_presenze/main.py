import os 
os.chdir(os.path.dirname(__file__))

def read_file() -> dict[str: dict[str:list[float], str: float]]:
    ppl = dict()
    with open("presenza.txt", "r") as f:
        f.readline()
        for line in f:
            data = line.strip().split(";")
            if data[0] not in ppl.keys():
                ppl[data[0]] = {"presence": [int(data[-2])], "income": float(data[-1])}         
            else:   
                ppl[data[0]]["presence"].append(int(data[-2]))          #& salvo in una lista le presenze mensili 
                ppl[data[0]]["income"] += float(data[-1])               #& sommo lo stipendio
    return ppl

def main():
    ppl = read_file()
    zero_presence = []
    for p in ppl:
        if sum(ppl[p]["presence"]) == 0:            
            zero_presence.append(p)         #& salvo i consiglieri che non hanno mai partecipato ad una seduta comunale
            ppl[p]["average"] = 0
        else:
            average_presence = sum(ppl[p]["presence"]) / len (ppl[p]["presence"])           
            ppl[p]["average"] = average_presence                    #& salvo la presenza media annuale
    top_five = sorted (ppl.items(), key = lambda x: x[1]["average"], reverse=True)          #& ordino i consiglieri in ordine di maggior numero di presenze 
    
    for c in zero_presence:
        print(f"Il consigliere {c} non ha mai partecipato a sedute del Consiglio Comunale nel 2023 \n")             #& stampo i consiglieri che hanno 0 presenze

    for i in range(5):
        print(f"{top_five[i][0]:30s} {top_five[i][1]["average"]:10.2f} {top_five[i][1]["income"]:10.2f}")               #& stampo i primi 5 consiglieri

main()