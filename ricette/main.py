import os
os.chdir(os.path.dirname(__file__))

def read_recipe():
    ingredients = dict()
    with open("polenta_concia.txt", "r") as f:
        line = f.readline()
        line = f.readline()
        while line != "\n":
            ingredient, grams = line.strip().split(";")
            ingredients[ingredient] = grams
            line = f.readline()
    return ingredients

def read_food():
    foods = dict()
    foods.setdefault
    try:
        with open("cibi.txt", "r") as f:
            for line in f:
                ingredient, price, calories = line.strip().split(";")
                foods[ingredient] = (price, calories)
    except FileNotFoundError:
        print("file not found")
    return foods
            
def main():
    recipe = read_recipe()
    foods = read_food()
    total_price, total_calories = 0, 0
    print("Ingredienti:")
    for k, v in recipe.items():
        print(k, "-", v )
        total_price += float(foods[k][0]) * (float(v)/1000) 
        total_calories += float(foods[k][1]) * (float(v)/1000) 
    print(f"Numero di ingredienti: {len(recipe)}")
    print(f"Costo ricetta {total_price:.2f}")
    print(f"calorie ricetta {total_calories:.2f}")

main()
