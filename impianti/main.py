import os 
os.chdir(os.path.dirname(__file__))


def read_impianti():
    impianti = dict()
    with open("impianti.txt", "r") as f :
        line = f.readline()
        for line in f:
            data = line.strip().split(";")
            impianti[data[0]] = {"dim": float(data[1]), "eta": float(data[2])}
    return impianti

def read_meteo():
    meteo = dict()
    with open("meteo.txt", "r") as f:
        line = f.readline()
        for line in f:
            data, ora, ghi = line.strip().split(";")
            if data not in meteo:
                meteo[data] = {ora: float(ghi)}
            else:
                meteo[data][ora] = float(ghi)
    return meteo

def calcola_consumi(abitazione, meteo, impianti):
    energia_prodotta = impianti[abitazione["ID_Abitazione"]]["eta"] * impianti[abitazione["ID_Abitazione"]]["dim"] * meteo[abitazione["Data"]][abitazione["Ora"]]
    energia_consumata = float(abitazione["Consumo_energetico"])
    energia_immessa_inrete = energia_prodotta - energia_consumata if energia_prodotta >= energia_consumata else 0
    energia_autoconsumata = energia_consumata if energia_prodotta >= energia_consumata else energia_prodotta

    return energia_prodotta, energia_consumata, energia_immessa_inrete, energia_autoconsumata

def main():
    abitazione = dict()
    meteo = read_meteo()
    impianti = read_impianti()
    energia_totale_consumata = 0
    energia_totale_prodotta = 0
    energia_totale_immessa = 0
    energia_totale_autoconsumata = 0
    complesso = dict()
    with open("consumi.txt", "r") as f:
        keys = f.readline().strip().split(";")
        line = f.readline()
        while line != "":
            data = line.strip().split(";")
            for i in range(len(keys)):
                abitazione[keys[i]] = data[i]
            info = list(calcola_consumi(abitazione, meteo, impianti))
            energia_totale_prodotta += info[0]
            energia_totale_consumata += info[1]
            energia_totale_immessa += info[2]
            energia_totale_autoconsumata += info[3]
            if abitazione["ID_Abitazione"] not in complesso.keys():
                complesso[abitazione["ID_Abitazione"]] = {"Energia_prodotta": 0, "energia_consumata": 0, "energia_immessa": 0, "energia_autoconsumata": 0}

            for k, v  in zip(list(complesso[abitazione["ID_Abitazione"]]), info):
                complesso[abitazione["ID_Abitazione"]][k] += v

            line = f.readline()


    for _id in complesso:
        complesso[_id]["autosufficienza"] = (complesso[_id]["energia_autoconsumata"] / complesso[_id]["energia_consumata"])
        complesso[_id]["autoconsumo"] = (complesso[_id]["energia_autoconsumata"] / complesso[_id]["Energia_prodotta"]) 
        
    complesso_sorted_by_autoconsumo = sorted(complesso.items(), key = lambda x : x[1]["autoconsumo"], reverse = True)
    complesso_sorted_by_autosufficienza = sorted(complesso.items(), key = lambda x : x[1]["autosufficienza"], reverse=True)
    

    print(f"Energia totale prodotta {energia_totale_prodotta:.2f} KWh")
    print(f"Energia totale consumata {energia_totale_consumata:.2f} KWh")
    print(f"Energia totale immssa {energia_totale_immessa:.2f} KWh")
    print(f"Energia totale autoconsumata {energia_totale_autoconsumata:.2f} KWh")
    print(f"Totale autoconsumo {(energia_totale_autoconsumata / energia_totale_prodotta)*100:.2f}%")
    print(f"Totale autosufficienza {(energia_totale_autoconsumata / energia_totale_consumata)*100:.2f}%")
    print(f"Le tre abitazioni con il più alto autoconsumo sono:", end = " ")
    for i in range(3):
        print(complesso_sorted_by_autoconsumo[i][0], end = " ")
    print()
    print(f"Le tre abitazioni con il più alta autosufficienza sono:", end = " ")
    for i in range(3):
        print(complesso_sorted_by_autosufficienza[i][0], end = " ")
    

main()


