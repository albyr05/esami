import os
os.chdir(os.path.dirname(__file__))

def get_athlets():
    athlets = {"5km": {}, "10km": {}, "15km": {}, "40km": {}}
    run_type = {"0": "5km", "1": "10km", "2": "15km", "3": "40km"}
    with open("atleti.txt", "r") as f:
        for line in f:
            code, competion, times = line.strip().split(";")
            if run_type[competion] not in athlets.keys():
                athlets[run_type[competion]] = {code: list(map(float, times.split(",")))}
            else: 
                athlets[run_type[competion]][code] = list(map(float, times.split(",")))

    return athlets

def get_average_times(athlets):
    av = dict()
    athlet_av = dict()
    for k in athlets:
        total = 0
        divided = len(list(athlets[k]))
        for a in athlets[k]:
            av_partial = (sum(athlets[k][a])/len(athlets[k][a]))
            if k not in athlet_av:
                athlet_av[k] = {a:av_partial}
            else:
                athlet_av[k][a] = av_partial
            total += av_partial
        av[k] = round(total/divided, 2)
    return av, athlet_av

def find_qualified(athlet_av, av, g):
    qualified = 0
    for a in athlet_av[g]:
        if abs((athlet_av[g][a] - av[g]) / av[g]) * 100 < 10:

            qualified += 1 

    return qualified    

def find_top_last(athlets, av, g):
    top_last = []
    for a in athlets[g]:
        last_time_av = sum(athlets[g][a][-3:]) / 3
        if abs((last_time_av - av[g]) / av[g]) * 100 < 3:
            top_last.append(a)
    return top_last
      
def main():
    athlets = get_athlets()
    av, athlet_av = get_average_times(athlets)
    total_qualified, total_athlets = 0, 0
    print("tempi per gara:")
    for k in av:
        print(f"{k}: tempo medio {av[k]}")
    print()
    for g in athlets:
        qualified = find_qualified(athlet_av, av, g)
        total_qualified += qualified
        print(f"Gli atleti per la gara {g} sono: {qualified}")
        top_last = find_top_last(athlets, av, g)
        print(f"Gli atleti nel 3% sono: {top_last}")
        print()
        total_athlets += len(athlets[g].keys())
    
    print(f"In totale gli atleti selezionati sono {total_qualified} su {total_athlets} ({(total_qualified / total_athlets)*100:.2f}%)")

    
main()