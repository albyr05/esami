from operator import itemgetter
def get_info(line):
    parts = line.strip().split()
    return parts 

def calculate_points(parts):
    points = list(map(float, parts[4:]))
    score = sum(points) - min(points) - max(points)
    return score

def add_athletes(nations, parts):
    if parts[3] not in nations:
        nations[parts[3]] = calculate_points(parts)
    else:
        nations[parts[3]] += calculate_points(parts)

def print_best_nations(nations):
    punteggi = sorted(nations.items(), key = itemgetter(1), reverse = True)
    for i in range(3):
        print(f"{i+1}°) {punteggi[i][0]} - Punteggio Totale {punteggi[i][1]:.1f}")

def main():
    file = open("/Users/albertoreano/Documents/Documenti - MacBook Air di Alberto/vscode/python_uni/esami/testo.txt/input.txt", "r")
    nations = {}
    score = 0
    for line in file:
        parts = get_info(line)
        add_athletes(nations, parts)
        if parts[2] == "F":
            temp = calculate_points(parts)
            if temp > score:
                score = temp
                name_winner, nation = parts[0] + parts[1], parts[3]

    print("vincitrice femminile")
    print(f"{name_winner}, {nation} - Punteggio: {score:.1f}")
    print("classifica delle nazioni")
    print_best_nations(nations)

main()


