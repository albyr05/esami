import os 
from operator import itemgetter

os.chdir(os.path.dirname(__file__))

def main():
    role_dictionary = read_file("statistiche.txt")
    request_dict(role_dictionary)

#* Crea il dizionario del tipo {roulo: {calciatore: punteggio}} secondo le informazioni nel file
def read_file(f):
    infile = open (f, "r")
    role_d = dict()
    for line in infile:
        parts = line.strip().split()
        name = parts[0] + " " + parts[1]
        role = parts[2]
        punteggio = calculate_performance(list(map(float, parts[3:])))
        if role not in role_d:
            players = {name: punteggio}                         #& Crea la nuova chiave con associato un dizionario contenente il giocatore che sta leggendo
            role_d[role] = players
        else: 
            role_d[role][name] = punteggio                      #& Aggiunge al dizionario associato al ruolo del giocatore corrente il nuovo giocatore
    infile.close()

    return role_d

#* Calcola il punteggio di performance secondo la formula fornita
def calculate_performance(_list):
    performance = _list[0] * (_list[1]*0.5 + _list[2]*0.5 - _list[3]*0.2 - _list[4]*0.4)
    return performance 

#* gestisce le varie richieste
def request_dict(role_d):
    request = input("What do tou wanna do? (C/R/Q) ")
    while request.upper() in "RC":  

        if request.upper() == "R":                              #? Caso in cui vengano richiesti i 3 migliori giocatori di un ruolo
            role = input("Which role [A/D/P/C] ")
            if role.upper() in role_d.keys():
                players = role_d[role]                          #& Contiene tutti i giocatori che giocano in quel ruolo
                best_players = sorted(players.items(), key= itemgetter(1), reverse = True)              #& ordina gli elementi del dizionario secondo il valore (punteggio di performance)
                print("here are the best player in the asked role")
                for i in range(min(3, len(best_players))):                                              #& Stampa i 3 migliori giocatori di quel ruolo 
                    player = best_players[i]
                    print(f"{player[0]} {player[1]:.2f}")               
                    
        if request.upper() == "C":                              #? Caso in cui venga richiesto un confornto tra 2 giocatori
            p1 = input("Insert the first player ")
            p2 = input("Insert the second player ")
            role_match = False
            for role in role_d:
                if p1 in role_d[role] and p2 in role_d[role]:       #& controlla che i 2 giocatori siano nello stesso ruolo
                    role_match = True                     
                    if role_d[role][p1] > role_d[role][p2]:
                        print(f"The best is {p1}")
                    else: 
                        print(f"The best one is {p2}")
                    

            if not role_match:                                      #& i due giocatori giocano in ruoli diversi
                print("Can't compare 2 players in different roles")

        request = input("\nWhat do tou wanna do? (C/R/Q) ")

main()