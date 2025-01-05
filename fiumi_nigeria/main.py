import os
os.chdir(os.path.dirname(__file__))


def get_info(filename):
    
    with open(filename,  "r") as f:
        keys = f.readline().split()
        info = f.readline().split()
        place = {keys[i]: info[i] for i in range(len(keys))}            #& salva le informazioni sul luogo 
        line = f.readline()
        values = f.readline().split()
        measures = {values[i]: [] for i in range(len(values))}          #& creo un dizionario di default con parametro e lista vuota
        for line in f:
            data = line.strip().split()
            for i in range(len(values)):
                measures[values[i]].append(float(data[i]))             #& associa ad ogi parametro una lista contenente tutti i vlaori misurati durante l'anno

    return place, measures

#* stampa la prima parte dell'output
def calculate_output(measures):
    avg_humidity = sum(measures["Humidity"]) / len(measures["Humidity"])
    max_windspeed = max(measures["Windspeed"])
    avg_temperature = sum(measures["Tair"]) / len(measures["Tair"])
    max_temperature = max(measures["Tair"]) 
    print(f"Avg. humidity: {avg_humidity:.2f}%")
    print(f"Max wind speed: {max_windspeed}m/s")
    print(f"Avg. temperature: {avg_temperature:.2f}°C (max: {max_temperature:.2f}°C)")

#* incremento ad ogni fiume letto il valore settimanale della pioggia
def calculate_average_rainfall(measures, av):
    for i in range(len(measures["Rainfall"])):
        av[i] += measures["Rainfall"][i]

def main():
    
    with open("rivers.txt", "r") as f:
        n_rivers = 0
        av = [0]*52                     #& la lista parte con 52 zeri
        for line in f:
            print()
            river = line.strip()
            associated_file = river + ".dat"

            try:
                place, measures = get_info(associated_file)
                print(f"{river.upper():10s} measured in {place["Station"]:10s} ({place["Lat"]} {place["Long"]})")           #& stampo le inof sul luogo
                calculate_output(measures)
                n_rivers += 1 
                calculate_average_rainfall(measures,av)

            except FileNotFoundError:
                print(f"{river:5s} file not found")
                continue

    for i in range(len(av)):
        av[i] = av[i]/n_rivers              #& Divido ogni valore delle misurazioni per il numero di fiumi letti, in modo da avere la media
    print("\nAverage weekly rain (mm):")
    i, k = 0, 0
    while i < len(av):                      #& stampa la tabella formattata
        k += 1
        while i < 7*k and i < len(av): 
            print(f"{str(round(av[i], 2)):8s}", end=" ")
            i += 1
        print()
    print(f"\nYearly average: {sum(av)/len(av):.2f}mm")             #& calcola le precitazioni annuali medie 


main()