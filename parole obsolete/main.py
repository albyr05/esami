def main():
    try:
        obsolete_dic = create_obsolete_dic()
        f = open("output.txt", "w")
        total_words = read_text(obsolete_dic, f)
        print(f"Il numero di parole presenti nel testo è: {total_words}")
        print_count_words(obsolete_dic)
        f.close()
    except FileNotFoundError as msg:
        print("qualcosa è andato storto", msg)
    

def read_text(dic, f): 
    text = open("input.txt", "r")
    word_counter = 0
    for line in text:
        line_list = [word for word in line.split()]
        word_counter += len(line_list)
        for i in range(len(line_list)):
            punctuation = ""
            if line_list[i] in dic.keys():

                if line_list[i][-1] in ",;:.?!":
                    punctuation = line_list[i][-1]
                    line_list[i] = line_list[i].strip(",;?!:")

                dic[line_list[i]]["count"] += 1
                line_list[i] = dic[line_list[i]]["new"] + punctuation 
                
        f.write(f"{" ".join(line_list)}\n")
    text.close()
    return word_counter

def create_obsolete_dic():
    words = open("obsoleto.txt", "r")
    d = dict()
    for line in words:
        parts = line.strip().split()
        info = {"new": parts[1], "count": 0}
        d[parts[0]] = info
    words.close()
    return d 

def print_count_words(dic):
    for key in sorted(dic):
        print(f"{key}: {dic[key]["count"]}")
main()

