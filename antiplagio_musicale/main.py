import os

os.chdir(os.path.dirname(__file__))


def get_songs():
    songs = dict()  
    with open("songs.txt") as f:
        for line in f:
            title, notes = line.strip().split(":")
            songs[title] = list(map(int, notes.split()))
    return songs                                            #& Ho un dizionario con chiave titolo e valore lista di note

def check_plagio(current, song):
    if current[1] == song:
        return True                                                 #& controllo se c'è plagio
    else:
        return False
    
def divide_groups(song):
    return [song[j:j+4] for j in range(len(song) - 3)]
   
def check_copiatura(groups1, groups2):
    for g1 in groups1:
        if g1 in groups2:                                               #& c'è una sequenza di 4 uguale 
            return True                                                 #& return true (la canzone corrente è copiatura di una precedente)
    
    return False                                                        #& non c'è copiatura

def check_sospetto(groups1, groups2):
    for g1 in groups1:
        for g2 in groups2:
            difference = g1[0] - g2[0]                              #& trovo la differenza tra i primi elementi di ogni sottogruppo
            if all((n1 - n2) == difference for n1, n2 in zip(g1, g2)):          #& se la differenza è uguale per tutti gli elementi di due sottogruppi
                return True                                                 #& return true (la canzone corrente è sospetto di quella precedente)
            
    return False                                    #& non è sospetto

def main():
    songs = list(get_songs().items())
    for i in range(len(songs)):
        current = songs[i]
        previous = songs[:i]            #& sono i (titoli, note) di tutte i brani precedenti a quello corrente 
        for title, song in previous:                        #& ciclo sulle coppie (titolo, canzone) precedenti a quelle corrente, questo mi permette di fare un confronto con ogni singola canzone precedente e vedere che rapporto c'è tra le due 
        
            if check_plagio(current, song):
                print(f"{current[0]} è PLAGIO di {title}")                  #& stampo in caso sia plagio
       
            else:
                groups1 = divide_groups(current[1])                 #& divido le note in sequenze da 4
                groups2 = divide_groups(song)

                if check_copiatura(groups1, groups2):                            #& se non era plagio controllo se è copiatura
                    print(f"{current[0]} è COPIATURA di {title}")

                elif check_sospetto(groups1, groups2):                             #& se non è nè plagio nè copiatura controllo se è sospetto
                    print(f"{current[0]} è SOSPETTO di {title}")
            

main()