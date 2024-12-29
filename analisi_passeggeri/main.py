import os 
from operator import itemgetter
os.chdir(os.path.dirname(__file__))

FILE = "passeggeri.csv"

def get_average_age_per_city(city_average_age, p):
    if p["origine"] not in city_average_age.keys():
        city_average_age[p["origine"]] = [int(p["età"])]            #& salvo l'età in una lista relativa all'origine
    else:
        city_average_age[p["origine"]].append(int(p["età"]))        

#* salva il conteggio di volte che è stato preso un volo e da chi 
def find_popular_flight(flight_numbers, p):
    if p["numero_volo"] not in flight_numbers.keys():
        flight_numbers[p["numero_volo"]] = {"count": 1, "female": 0,  "male": 0}      #& salvo le info riguardanti il numero di volo
    else:
        flight_numbers[p["numero_volo"]]["count"] += 1 
                                                                                    #& Aggiorno il conteggio di maschi e femmine
    if p["sesso"] == "M":
        flight_numbers[p["numero_volo"]]["male"] += 1                           
    else:
        flight_numbers[p["numero_volo"]]["female"] += 1

#* Stampa output
def output(city_average_age, flight_numbers):
    for k in city_average_age.keys():
        average = sum(city_average_age[k]) / len(city_average_age[k])               #& calcola la media delle età
        city_average_age[k] = average
    s_d = dict(sorted(city_average_age.items(), key = itemgetter(1), reverse=True))             #& ordino il dizionario per media decrescente
    for k in s_d:
        print(f"Origine: {k}, media età {round(s_d[k], 1)}")
    
    pop_flight = max(flight_numbers.items(), key = lambda x: x[1]["count"])                 #& trovo il volo più popolare in base al conteggio di ogni volo (c'era metodo più intelligente?!)
    print(f"volo più popolare {pop_flight[0]} , M: {pop_flight[1]["male"]}, F : {pop_flight[1]["female"]}")

def main():
    f = open(FILE, "r")
    prop = f.readline().strip().split(",")
    city_average_age = dict()               #& dizionari man mano popolati dalle funzioni
    flight_numbers = dict()
    for line in f:
        data = line.strip().split(",")
        passenger = {}
        for i in range(len (prop)):
            passenger[prop[i]] = data[i]                #& dizionario con info su ogni passegero
        find_popular_flight(flight_numbers, passenger)
        get_average_age_per_city(city_average_age, passenger)

    output(city_average_age, flight_numbers)
        
main()

            
