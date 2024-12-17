import os
from operator import itemgetter
os.chdir(os.path.dirname(__file__))


def main():
    artistfile_to_code = get_artists()
    dataset = dict()                                    #& Il dataset viene inizializzato come un dict vuoto
    for key in artistfile_to_code.keys():               #& per ogni artista letto apre il file e aggiunge le canzoni secondo la funzione read_song
        read_songs(key, dataset, artistfile_to_code)

    print_output(dataset)                               


#* legge il file degli artisti e returna un dizionario {filename: artist_code}
def get_artists():
    artistfile_to_code = dict()
    try:
        f = open("artisti.txt", "r")
        for line in f:
            parts = line.strip().split(";")
            artistfile_to_code[parts[1]] = parts[0]
        f.close()

    except FileNotFoundError as msg:
        print("file non trovato", msg)

    return artistfile_to_code                   #& {file: code}


#* Legge le canzoni di ogni artista dal file annesso e le aggiunge in un dizionario d, viene popolato senza bisogno di return
def read_songs(file, d, artistfile_to_code):
    try:
        f = open(file, "r")
        for line in f:
            parts = line.strip().split(";")
            year, song = int(parts[0]), parts[1]
            if year not in d.keys():                        
                d[year] = {song: artistfile_to_code[file]}          #& Aggiunge al dizionario d una chiave (anno) e gli associa un dizionario contente la canzone (chiave) e il codice dell'artista (valore)
            else:
                d[year][song] = artistfile_to_code[file]            #& Se l'anno è già stato incontrato, aggiunge al suo dizionario una nuova canzone con associato il codice dell'artista
        f.close()

    except FileNotFoundError as msg:
        print(f"file {file} non trovato", msg)

    #& d = {year1: {song1: code1, song2: code2}, year2: {song3: code3, song4, code4}}
    

#* stampa l'output richiesto
def print_output(dataset):
    s_dataset = dict(sorted(dataset.items(), key = itemgetter(0)))          #& ordina il dizionario in modo da avere gli anni in ordine crescente
    for year in s_dataset.keys():
        print(f"{year}: ")
        for song, code in s_dataset[year].items():
            print(f"{song:35s} {code}")
        print()

  
main()

