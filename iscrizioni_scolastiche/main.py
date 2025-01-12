import os
import csv

os.chdir(os.path.dirname(__file__))

def get_students():
    infant_students = 0
    dataset = dict()
    first = True
    try: 
        with open("studenti.csv", "r") as f :
            x = csv.reader(f, delimiter=",")
            for line in x:    
                if first:
                    keys = line             #& salvo la prima linea come chiavi
                    first = False

                else:
                    data = dict()

                    for i in range(len(keys)):          #& creo un dizionario a cui associo ad ogni chaive della prima il corrispondente valore della riga corrente
                        data[keys[i]] = line[i]

                    if data["Provincia"] not in dataset.keys():
                        dataset[data["Provincia"]] = int(data["Numtotaleiscritti"])             #& sommo il totale di studenti di ogni provincia 
                    else:
                        dataset[data["Provincia"]] += int(data["Numtotaleiscritti"])
                    
                    if data["GradoScolastico"] == "1 - Scuola dell'infanzia":           #& controllo se la riga riguarda la scuola dell'infanzia, in caso aggiungo gli studenti 
                        infant_students += int(data["Numtotaleiscritti"])

    except FileNotFoundError:
        print("file not found")
        exit()

    return dataset, infant_students

def main():
    dataset, infant_student = get_students()
    sorted_dict = dict(sorted(dataset.items(), key = lambda x: x[0]))           #& ordino in ordine alfabetico per chiave 
    print("Le province per le quali vengono fornite le statistiche sono: ")
    for k in sorted_dict:
        print(k)
    print()
    for k, v in sorted_dict.items():
        print(f"Totale studenti iscritti: {k:20s} {v}")
    print(f"Gli studenti iscritti alla scuola dell'infanzia in Piemonte sono: {infant_student}")

main()