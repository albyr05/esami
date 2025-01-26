import os 
os.chdir(os.path.dirname(__file__))

def read_file():
    inventory = {}
    with open("Inventario_old.csv", "r") as f:
        for line in f:
            data = line.strip().split(";")
            if data[1] not in inventory.keys():
                inventory[data[1]] = {"titolo": data[2], "autore": data[3], "copie": [data[0]]}         #& salvo l'isbn univoco e i dati realativi a quel libro
            else:
                inventory[data[1]]["copie"].append(data[0])                                 #& aggiungo il codice copia
    s_inventory = dict(sorted(inventory.items()))                   #& ordino il dizionario per isbn alfabetico
    return s_inventory

def check_for_school(inventory):
    gifts, total_copies = 0, 0
    with open("Inventario_scuola.csv", "w") as f:
        for k in inventory:
            l = len(inventory[k]["copie"])              #& vedo quante copie ci sono 
            if l >= 3:
                gifts += 1                  #& se sono più di 3 sto regalando un libro alla scuola
                total_copies += (l -3)              #& regalo tutte le copie in eccesso rispetto a 3 
                copies = ";".join(inventory[k]["copie"][l-1:2:-1])              #& sono le ultime copie in eccesso che regalo alla scuola

                for i in range(l-1, 2, -1):
                    inventory[k]["copie"].pop(i)            #& rimuovo dall'inventario le copie regalate
                    
                f.write(f"{k};{inventory[k]["autore"]};{inventory[k]["titolo"]};{copies}\n")            #& scrivo nel file

        
    return  gifts, total_copies

def print_new(new_inventory):
    with open("Inventario_new.csv", "w") as f:
        for k in new_inventory:                             
            copies = ";".join(new_inventory[k]["copie"])            #& sono tutte le copie che mi sono rimaste
            f.write(f"{k};{new_inventory[k]["autore"]};{new_inventory[k]["titolo"]};{copies}\n")            #& scrivo il nuovo inventario

def main():
    inventory = read_file()
    gifts, total_copies = check_for_school(inventory)
    print_new(inventory)
    print(f"Numero libri da regalare: {gifts}, copie totali: {total_copies}")

main()
