import os
os.chdir(os.path.dirname(__file__))

def main():
    safe = []
    unique_name, unique_output = set(), set()
    known_gate= ["and", "nand", "or", "nor", "xor", "xnor", "not", "buf"]           #& Gates validi
    filename =  "c5315.txt" #input("Insert the name of the file: ")
    f = open(filename, "r")
    row = 1
    error_count = 0
    for line in f:
        ok, error = task1(line, known_gate, unique_name, unique_output)             
        if ok:                                                                      #& se la riga non ha errori, la salvo
            safe.append(line)
        else:
            for k in error:
                print(f"Riga {row}: {k} ({error[k]})")                              #& Se ha errori printo il numero di riga ed il tipo di errore
            error_count +=1 
        row += 1 
    print("Numero errori", str(error_count))

    global_input, global_output = get_global_input_output(safe)                     #& Cerca gli output e input globali 
    print(f"\nInput globali: {len(global_input)}")                              
    print(f"\nOutput globali: {len(global_output)}")

    info_on_gates = get_number_of_gates(safe)                                       
    gates_num = sum(valore for k in info_on_gates for valore in info_on_gates[k].values())          #& numero di gates totali
    print(f"\nNumero di gates: {gates_num}")                    
    for k, v in info_on_gates.items():                                                              #& stampa l'output del terzo punto, come richiesto
        for m in v.keys():
            print(f"{v[m]} {k} con {m} input")
            
#* controlla se ci sono errori
def task1(line, know_gate, unique_name, unique_output): 
    error = {}
    check = True
    data = line.strip().split()
    try:
        gate_type, gate_name, output, input_net = data[0], data[1], data[2], data[3:]
    except IndexError:                                                                    #& caso in cui la riga non sia completa segnala subito l'errore
        check = False
        error["Numero di net non valdio"] = 0
        return check, error
    
    if gate_name in unique_name:                                                    
        check = False
        error["Nome già utilizzato"] = gate_name
    elif gate_name not in unique_name:
        unique_name.add(gate_name)                                                        #& Se non è già presente aggiunge al set il nome del gate

    if output in unique_output:                                                           #& unicità degli output
        check = False
        error["Net collegata a più output"] = output
    elif output not in unique_output:
        unique_output.add(output)

    if gate_type not in know_gate:                                                        #& Gate sconosciuto
        check = False
        error["Gate sconosciuto"] = gate_type
        
    elif gate_type in know_gate[0:6] and len (input_net) < 2:                             #& net input incongruenti
        check = False 
        error["Numero di net non valdio"] = len(input_net)
        
    elif gate_type in know_gate[6:8] and len (input_net) != 1:
        check = False 
        error["Numero di net non valdio"] = len(input_net)
        
    return check, error

#* Cerca gli output/input globali ignorando le linee con errori                 (non funziona correttamente)
def get_global_input_output(safe):
    input_set = set()                                           #& contiene tutti gli input
    output_set = set()                                          #& contiene tutti gli output
    for line in safe:
        _output = line.strip().split()[2]                          
        output_set.add(_output)
        _inp = line.strip().split()[3:]
        for x in _inp:
            input_set.add(x)
    global_output = output_set.difference(input_set)
    global_input = input_set.difference(output_set)
    return global_input, global_output

#* restituisce d = {gate_type: {lunghezza_input: quanti ce ne sono}}           
def get_number_of_gates(safe):
    d = dict()
    for line in safe:
        data = line.strip().split()
        gate_type, input_net = data[0], len(data[3:])
        if gate_type not in d:
            d[gate_type] = {}
        if input_net not in d[gate_type]:
            d[gate_type][input_net] = 1
        else:
            d[gate_type][input_net] += 1
    return d

main()



