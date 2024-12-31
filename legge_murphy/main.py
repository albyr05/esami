import os
os.chdir(os.path.dirname(__file__))
LAWS = "leggi.txt"
TOPICS =  "argomenti.txt"

def get_laws(filename):
    laws = dict()
    try:
        f = open(filename, "r")
        n = False
        for line in f:
            if line == "\n":
                n = False
                continue
            if not n:
                title = line
                laws[title.strip()] = [] 
                n = True
            else:
                laws[title.strip()].append(line.strip())
        f.close()
    except FileNotFoundError:
        print("file non trovato")

    return laws
        
def find_topic(topic, laws, saved_laws):
    found_laws = []
    for k, v in laws.items():
        for el in v:
            for word in el.split():
                if word.lower().strip("-,.;?!'") == topic and (k,el) not in saved_laws and (k,el) not in found_laws:            #& evita le ripetizioni 
                    found_laws.append((k, el))
    return found_laws

def main():
    laws = get_laws(LAWS)
    f = open(TOPICS, "r")
    saved_laws = []
    for line in f:
        topic = line.strip()
        found_laws = find_topic(topic, laws, saved_laws)
        for l in found_laws:
            saved_laws.append(l)                #& salvo tutte le leggi e gli enunciati già salvati
        if found_laws != []:
            for el in found_laws:
                if len(el[1]) <= 50:
                    print(f"{el[0]} - {el[1]}")
                else: 
                    print(f"{el[0]} - {el[1][0:50]}...")
main()

        
