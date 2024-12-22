import os
from datetime import datetime
os.chdir(os.path.dirname(__file__))

def main():
    d = list()
    ref, parameter = get_paramater()
    f = open("manutenzione.txt", "r")
    for line in f:
        check_date(line, parameter, ref, d)
    f.close()
    output(d, parameter, ref)

#* ritorna le informazioni sulla data di riferimetno ed il parametro
def get_paramater():
    f = open("parametri.txt", "r")
    date, paramameter = tuple(f.readline().strip().split(","))
    f.close()
    return date, paramameter

#* popola la lista con le manutenzioni che rispettano il parametro
def check_date(line, parameter, ref, d):
    parts = line.strip().split(",")
    name, date, price = parts[0], parts[1], int(parts[2])
    date_f = datetime.strptime(date, "%d/%m/%Y")                #& converte la stringa della data in un formato confrotabile
    ref_date = datetime.strptime(ref, "%d/%m/%Y")               
    if parameter == "a":
        if date_f < ref_date:
            d.append({"name": name, "date": date, "price": price, "format": date_f})            #& aggiunge alla lista un dizionario con le info sulla manutenzione processata
    if parameter == "p":
        if date_f > ref_date:
            d.append({"name": name, "date": date, "price": price, "format": date_f})

#* stampa l'output
def output(d, parameter, date):
    sorted_d = sorted(d, key = lambda x: x ["format"])                      #& ordina il la lista secondo la chiave "format" del dizionario, quindi in ordina di data crescente
    max_price = max(d, key = lambda x: x ["price"])                         #& trova la manutenzione più costosa
    if parameter == "a":
        print(f"Le operazioni effettuate prima del {date} sono: \n")
        for m in sorted_d:
            print(f"{m["name"]} in data {m["date"]}, costo {m["price"]}")
        print(f"La manutenzione più costosa é stata {max_price["price"]}, in date {max_price["date"]}, prezzo {max_price["price"]}")

    elif parameter == "p":
        print(f"Le operazioni effettuate dopo il {date} sono: \n")
        for m in sorted_d:
            print(f"{m["name"]} in data {m["date"]}, costo {m["price"]}")
        print(f"La manutenzione più costosa da effettuare è {max_price["name"]}, in data {max_price["date"]}, prezzo {max_price["price"]}")

main()