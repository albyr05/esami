import os 
from math import sqrt
os.chdir(os.path.dirname(__file__))

def get_oasis():
    f = open ("desert.csv", "r")
    safety = []
    for line in f:
        parts = line.strip().split()
        if parts[2] in "oasis":
            safety.append((int(parts[0]), int(parts[1])))  
    f.close()
    return safety

def get_survivors(line):
    person = dict()
    parts = line.strip().split(",")
    person = {"id": parts[0], "position": (int(parts[1]), int(parts[2])), "km": float(parts[3])*float(parts[4]), "visited": []}
    return person 


def check_exit(start, km):
    exit = False
    x, y = start[0], start[1]
    if y+km > 500:
        exit = True
    elif x+km > 500:
        exit = True
    elif y-km < 0:
        exit = True
    elif x-km < 0:
        exit = True
    
    return exit


def look_for_oasis(person, oasis):
    km = person["km"]
    start = person["position"]
    found_oasis = False
    for pos in oasis:
        distance = sqrt(((start[0]-pos[0])**2) + ((start[1]-pos[1])**2))
        if distance <= km and pos not in person["visited"]:
            person["position"] = pos
            person["visited"].append(pos)
            found_oasis = True
        if found_oasis:
            break
        
def print_output(count, not_survived):
    percetage_survived = 100 - (len(not_survived)/count * 100)
    print(f"Sopravvissuti: {percetage_survived}")
    for p in not_survived:
        print(f"<{p["id"]}>: {p["visited"][-1]}")

def main():
    f = open("survivors.txt", "r")
    line = f.readline()
    line = f.readline()  
    oasis = get_oasis()
    not_survived = []
    count_people = 0

    while line != "":
        person = get_survivors(line)
        prev_position = None
        out = False
        while not out:
            
            if check_exit(person["position"], person["km"]):
                out = True
            else:
               
                prev_position = person["position"]
                look_for_oasis(person, oasis)

                if person["position"] == prev_position:
                    break  

        if not out:
            not_survived.append(person)

        count_people += 1
        line = f.readline()

    print_output(count_people, not_survived)

main()

