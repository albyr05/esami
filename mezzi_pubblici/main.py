import os
os.chdir(os.path.dirname(__file__))

def get_database():
    autisti, fermate = {}, {}
    with open("database.csv", "r") as f:
        for line in f:
            data = line.strip().split(": ")
            if data[0].startswith("A"):
                autisti[data[0]] = data[1]
            else:
                fermate[data[0]] = data[1]
    return autisti, fermate

def get_mezzi():
    _id_autisti = {}
    
    with open("mezzi.csv", "r") as f:
        keys = f.readline().strip().split(",")
        key = keys[2:]
        mezzi = {k:{} for k in key}
        for k in mezzi:
            mezzi[k]["saliti"] = 0
            mezzi[k]["scesi"] = 0
        for line in f:
            data = line.strip().split(",")
            stopped = data[2:]
            for i in range(len(stopped)):
                if stopped[i] == "--":
                    n, m = 0, 0
                elif stopped[i].startswith("-"):
                    n = 0
                    m = -int(stopped[i])
                elif "/" in stopped[i]:
                    n = int(stopped[i].split("/")[0])
                    m = int(stopped[i].split("/")[1])
                else:
                    n = int(stopped[i])
                    m = 0

                if data[0] not in _id_autisti:
                    _id_autisti[data[0]] = n
                else:
                    _id_autisti[data[0]] += n

                mezzi[key[i]]["scesi"] += m
                mezzi[key[i]]["saliti"] += n


    _max_saliti = max(mezzi.items(), key = lambda x: x [1]["saliti"])
    _max_scesi = max(mezzi.items(), key = lambda x: x [1]["scesi"])
    s_id = dict(sorted(_id_autisti.items(), key = lambda x: x[1], reverse=True))
    
    return _max_saliti, _max_scesi, s_id

def main():

    
    autisti, fermate = get_database()
    _max_saliti, _max_scesi, s_id = get_mezzi()
    print(f"La fermata in cui salgono più passeggeri ({_max_saliti[1]["saliti"]}) è {fermate[_max_saliti[0]]}")
    print(f"La fermata in cui scendono più passeggeri ({_max_scesi[1]["scesi"]}) è {fermate[_max_scesi[0]]}")
    print("Lista di autisti ordinata in base al numero di passeggeri:")
    for k, v in s_id.items():
        print(f"{autisti[k]} con {v} passeggeri")


main()
        

                


            



            