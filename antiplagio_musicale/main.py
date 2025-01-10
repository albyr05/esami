import os

os.chdir(os.path.dirname(__file__))

def get_songs():
    songs = dict()  
    with open("songs.txt") as f:
        for line in f:
            title, notes = line.strip().split(":")
            songs[title] = list(map(int, notes.split()))
    return songs                                            #& Ho un dizionario con chiave titolo e valore lista di note


def check_plagio(current, previous):
    plagi = list()                          #& mi salvo nella lista i titoli di cui la canzone è plagio
    for title, notes in previous:
        
        if current[1] == notes:                     #& le canzoni sono identiche e salvo il titolo nella lista
            if title not in plagi:
                plagi.append(title)

    return plagi
   

def check_copiatura(current, previous, plagi):
    groups1 = [current[1][i:i+4] for i in range(len(current[1]) - 3)]                   #& divido in gruppi di quattro le note la canzone corrente
    copiature = list()
    for title, notes in previous:
        if title in plagi:                                      #& balzo i titoli delle canzoni che sono plagi 
            continue

        groups2 = [notes[j:j+4] for j in range(len(notes) - 3)]             #& divido in gruppi di 4 le note del brano che sto confrontando
        for g1 in groups1:
            if g1 in groups2:                                               #& c'è una sequenza di 4 uguale 
                if title not in copiature:
                    copiature.append(title)                 #& salvo i titoli delle copiature
    return copiature



def check_sospetto(current, previous, plagi, copiature):
    sospetti = list()
    groups1 = [current[1][i:i+4] for i in range(len(current[1]) - 3)]
    
    for title, notes in previous:
        if title in plagi or title in copiature:                #& balzo i titoli che sono già plagi o copiature
            continue

        groups2 = [notes[j:j+4] for j in range(len(notes) - 3)]

        for g1 in groups1:
            for g2 in groups2:
                difference = g1[0] - g2[0]                              #& trovo la differenza tra i primi elementi di ogni sottogruppo
                if all((n1 - n2) == difference for n1, n2 in zip(g1, g2)):          #& se la differenza è uguale per tutti gli elementi di due sottogruppi
                    if title not in sospetti:
                        sospetti.append(title)                  #& salvo i titoli di sospetti
    return sospetti


def main():
    songs = list(get_songs().items())
    for i in range(len(songs)):
        current = songs[i]
        previous = songs[:i]            #& sono i (titoli, note) di tutte i brani precedenti a quello corrente 
        
        plagi = check_plagio(current, previous)             #& sono tutti i titoli dei plagi
        for i in range(len(plagi)):
            print(f"{current[0]} è PLAGIO di {plagi[i]}")

        copiature = check_copiatura(current, previous, plagi)            #& sono tutti i titoli delle copiature 
        for i in range(len(copiature)):
            print(f"{current[0]} è COPIATURA di {copiature[i]}")

        sospetti = check_sospetto(current, previous, plagi, copiature)            #& sono tutti i titoli dei sospetti 
        for i in range(len(sospetti)):
            print(f"{current[0]} è SOSPETTO di {sospetti[i]}")

main()
