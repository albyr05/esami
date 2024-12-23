import os
os.chdir(os.path.dirname(__file__))  # Cambia directory al percorso del file corrente

def main():
    try:
        f = open("occupazione.txt", "r")
        line = f.readline()
        line = f.readline()
        while line != "":
            line = line.strip()
            info = get_info_client(line)
            line = f.readline()
            prices = get_price()
            calculate_price(info, prices)
            output(info)
    except FileNotFoundError as msg:
        print("File non trovato", msg)
    finally:
        f.close()

#* crea il dizionario con le info di ogni utente
def get_info_client(line):
    data = line.split(";")
    keys = ["id", "arrivo", "partenza", "tipo", "adulti", "bambini", "elettricità"]
    info = {k:v for k, v in zip(keys, data)}                       #& dict comprhension
    return info

#* crea un dizionario del tipo {(data_inizio, data_fine): {dettagli su quel periodo}}
def get_price():
    f = open("prezzi.txt", "r")
    prices = dict()
    line = f.readline()
    line = f.readline()
    keys = ["prezzo_tenda", "prezzo_camper", "prezzo_persona", "prezzo_elettricità"]
    while line != "":
        info_on_period = line.strip().strip(";").split(";")
        start = info_on_period[0]
        end = info_on_period[1]
        details = {k:v for k, v in zip(keys, info_on_period[2:])}
        prices[(start, end)] = details                             #& creazione del dizionario
        line = f.readline()
    f.close()
    return prices

#* crea il dizionario del tipo {data: giorno dell'anno}
def create_calendar():
    f = open("calendario.txt", "r")
    calendar = dict()
    n = 1
    for line in f:
        calendar[line.strip()] = n
        n += 1                                                     #& associazione progressiva dei numeri alla data
    f.close()
    return calendar

#* funzione sgravata per calcolare il prezzo della notte
def calculate_price(info, prices):
    calendar = create_calendar()
    camping_start = calendar[info["arrivo"]]                       #& risale ai giorni dell'anno di inzio/fine soggiorno tramite il dizionario
    camping_end = calendar[info["partenza"]]
    price = 0
    for day in range(camping_start, camping_end):                  #& cicla tante volte quanti sono i giorni del soggiorno
        for k in prices:
            if calendar[k[0]] <= day <= calendar[k[1]]:            #& se il giorno corrente è compreso tra quelli di inizio/fine di un periodo di prezzo
                price += (float(info["adulti"]) + float(info["bambini"])) * float(prices[k]["prezzo_persona"])                          #& aggiunge al prezzo il costo delle persone
                price += float(prices[k]["prezzo_camper"]) if info["tipo"] == "camper" else float(prices[k]["prezzo_tenda"])            #& aggiunge al prezzo il costo del tipo di abitazione
                price += float(prices[k]["prezzo_elettricità"]) if info["elettricità"] == "sì" else 0                                   #& aggiunge l'elettricità se c'è 
                break

    info["price"] = price                                          #& aggiunge al dizionario sulle info della prenotazione il prezzo complessivo per n notti
    info["numero notti"] = camping_end - camping_start - 1         #& aggiunge al dizionario sulle info della prenotazione il numero di notti


#* stampa tutte le info sulla stessa riga
def output(info):
    for k, v in info.items():
        if k == "numero notti":
            print(f" {k}: {v}")
        else:
            print(f" {k}: {v}", end = ",")
        



main()