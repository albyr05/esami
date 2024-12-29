from operator import itemgetter
import os
os.chdir(os.path.dirname(__file__))

#* restituisce un dizionario per giorno {#hashtag: counter}
def get_hashtags():
    f = open("hashtag.csv", "r")
    first_day, second_day = dict(), dict()
    line = f.readline()
    info = line.strip().split()
    date = info[0]                  #& salva la data del primo giorno
    while line != "":
        info = line.strip().split()
        if info[0] == date:                         #& aggiunge gli hastags relativi alla prima giornata nel primo dizionario
            for h in info[2:]:
                if h not in first_day.keys():
                    first_day[h] = 1
                else:
                    first_day[h] += 1
        else:                                         #& aggiunge gli hashtags relativi al secondo giorno al secondo dizionario
            for h in info[2:]:
                if h not in second_day.keys():
                    second_day[h] = 1
                else:
                    second_day[h] += 1                          #& incrementa il valore se la hastags è già stato usato in quella giornata

        line = f.readline()
    f.close()
    
    return first_day, second_day

#* Stampa l'output come richiesto
def printout(popular):
    if len(popular) == 0:
        print("nessun hastag ha ottenuto tendenza nelle ultime 24 ore")
    else:
        s_pop = dict(sorted(popular.items(), key = itemgetter(1), reverse = True))              #& ordina il dizionario per valori decrescenti 
        for k in s_pop:
            print(f"{k}, con un incremento del {s_pop[k]}%")

def main():
    first_day, second_day = get_hashtags()
    popular = dict()
    for k, v in second_day.items():
        try:                                            #& se l'hashtag è presente in tutti e due i dizionari calcola l'icremento
            increase = (v-first_day[k])/first_day[k]
            if increase >= 0.5:
                popular[k] = int(round(increase*100, 0))            #& salvo solo gli hashtag con un incremento maggiore di 50%
        except KeyError:
            continue                                        #& se un hastag manca nella prima giornata, non sarà confrontabile e quindi passa al prossimo 
    printout(popular)

main()


