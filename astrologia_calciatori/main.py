import csv
import os
from operator import itemgetter
os.chdir(os.path.dirname(__file__))
def get_soccer_info():
    f = open("sportivi.csv", "r")
    data = csv.reader(f, delimiter="\t")    
    return data

# Abe Lenstra	710	Netherlands	27/11/1920
def get_zodiacal_info():
    f = open("zodiacali.csv", "r")
    data = csv.reader(f, delimiter= "\t")
    zodiacal = {}
    for row in data:
        start = "".join(row[1].split("/")[::-1])  
        end = "".join(row[2].split("/")[::-1])
        zodiacal[row[0]] = [start, end]
    f.close()
    return zodiacal

def get_sign(row, zodiacal, final_dic):
    birth = "".join(row[-1].split("/")[1::-1])
    
    for k, v in zodiacal.items():
        if v[0] <= birth <= v[1]:
            if k in final_dic:
                final_dic[k] += int(row[1])
            else:
                final_dic[k] = int(row[1])

def print_output(d):
    sorted_d = dict(sorted(d.items(), key=itemgetter(1), reverse=True))
    topvalue = max(d.values())
    for k in sorted_d:
        x = int((d[k]/topvalue)*50)
        value = str(d[k])
        ist = "*"*x
        print(f"{k:10s} ({value:4s}) {ist}")

def main():
    data = get_soccer_info()
    zodiacal = get_zodiacal_info()
    output_info = dict()
    for row in data:
        get_sign(row, zodiacal, output_info)
    print_output(output_info)
main()