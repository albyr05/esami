import os
os.chdir(os.path.dirname(__file__))

def get_prices():
    prices = {}
    with open("prices.dat", "r") as f:
        for line in f:
            info = line.strip().split(": ")
            prices[info[0]] = float(info[1])
    return prices

def get_offers():
    offers = []
    with open("offers.dat", "r") as f:
        for line in f:
            offert = {"needs": [], "quantity": [], "gift": ""}
            data = line.strip().split(": ")
            needed = data[0].split()
            for n in set(needed):
                offert["needs"].append(n)
                offert["quantity"].append(needed.count(n))
            offert["gift"] = data[1]
            offers.append(offert)
    return offers

def read_cart():
    cart = {}
    with open("cart.dat", "r") as f:
        for line in f:
            p = line.strip()
            if p not in cart.keys():
                cart[p] = 1 
            else:
                cart[p] += 1
    return cart

def main():
    cart, prices, offers = read_cart(), get_prices(), get_offers()        
    for offert in offers:
        valid = True
        stringa = ""
        for k in offert["needs"]:
            if k in cart.keys():
                pos = offert["needs"].index(k)
                stringa += f"{k} "*offert["quantity"][pos]
                try:
                    if cart[k] < offert["quantity"][pos]:
                        valid = False
                except KeyError:
                    continue
            else: 
                valid = False
        if valid:
            gift = offert["gift"]
            print(f"Acquistando {stringa}; hai ricevuto {gift}")
        
    total = sum(prices[k]*v for k,v in cart.items())
    print(f"Prezzo totale: {total} EUR")

main()

