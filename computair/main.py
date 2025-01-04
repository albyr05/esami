import os
os.chdir(os.path.dirname(__file__))

def get_weather():
    f = open("weather.txt", "r")
    city_weather = dict()
    for line in f:
        city, weather = line.strip().split(";")
        city_weather[city] = weather
    f.close()
    return city_weather

def get_flights():
    f = open ("flight.txt", "r")
    flights = dict()
    for line in f:
        _id, city, n_passengers = line.strip().split(";")
        if city not in flights:
            flights[city] = {_id: int(n_passengers)}
        else:
            flights[city][_id] = int(n_passengers)     
    return flights 

def print_bad_conditions(flights, weather):
     print("Codice dei voli verso città con condizione meteorologica Rainy o Stormy: ")
     for city in flights:
        if city in weather.keys():
            if weather[city] in ["Stormy", "Rainy"]:
                for k in flights[city]:
                    print(f"{k} verso {city}: {weather[city]}")

def print_city(flights, weather):
    print("Condizione meteorologica delle città che sono destinazione di almeno un volo:")
    total_passengers, count = 0,0 
    for city in flights:
        passengers_city = 0
        for k, v in flights[city].items():
            total_passengers += v 
            passengers_city += v
            count +=  1
        print(f"{city}: {weather[city]}. {passengers_city} passeggeri in arrivo")
    average = total_passengers / count 
    print()
    print(f"Numero medio di passeggeri {average:.1f}")

def main():
    flights, weather = get_flights(), get_weather()
    print_city(flights, weather)
    print()
    print_bad_conditions(flights, weather)

main()