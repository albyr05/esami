import os
os.chdir(os.path.dirname(__file__))

def read_data():
    allarms = {}
    max_severity, top_id = 0, []            
    with open("robot.csv") as f:
        f.readline()
        for line in f: 
            _id, severity, description = line.strip().split(";")
            if _id not in allarms.keys():           
                allarms[_id] = 1                    #& conto gli allarmi associati ad ogni robot 
            else:
                allarms[_id] += 1

            if int(severity) > max_severity:            #& se c'è un nuovo max di severità svuoto la lista e ci appendo l'id corrente, aggiorno il nuovo max
                max_severity = int(severity)
                top_id.clear()
                top_id.append(_id)

            elif int(severity) == max_severity:         #& se invece è uguale al massimo aggiungo solo l'id corrente
                top_id.append(_id)
    return allarms, max_severity, top_id

def main():
    allarms, max_severity, top_id = read_data()
    s_allarms = sorted(allarms.items(), key= lambda x: x[1], reverse=True)          #& ordino per numero di allarmi decresecente
    for k, v in s_allarms:
        print(f"Per il robot {k} si sono verificati {v} allarmi")

    print(f"Il livello massimo di severità {max_severity} è stato raggiunto dai seguenti robot:")
    for r in top_id:                #& printo tutti gli id che hanno raggiunto il max 
        print(r)
    
main()