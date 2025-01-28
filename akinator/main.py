import os
import random
import string
os.chdir(os.path.dirname(__file__))

def choose_level():
    levels = ["facile", "medio", "difficile"]
    chosen = random.choice(levels)
    filename = chosen + ".txt"
    with open(filename, "r") as f:
        words = f.read().splitlines()
        word = random.choice(words)
    return chosen, word 

def game(chosen_word):
    points = 10
    word = list(chosen_word)
    current = ["_"]*len(word)
    letters = list(string.ascii_lowercase)
    while points != 0 and current != word:
        print(f"Punti {points} - La parola da indovinare è: {" ".join(current)}")
        random_letter = random.choice(letters)
        print(f"\tLettera scelta dal bot {random_letter}")
        if random_letter in word:
            for i in range(len(word)):
                if word[i] == random_letter:
                    current[i] = random_letter
            print(f"\tLettera '{random_letter}' presente: {" ".join(current)}")        
        else:
            print(f"\tLettera '{random_letter}' non presente")
            points -= 1 
    if points == 0:
        print(f"\nPeccato, il bot ha peerso! la parola da indovinare era {"".join(chosen_word)}")
        win = 0
        lose = 1
    else: 
        print(f"\nComplimenti, il bot ha vinto la parola {"".join(chosen_word)} è stata indovinata correttamente")
        lose = 0 
        win = 1
    return win , lose

def main():
    n_game = 1
    play = "s"   
    n_win, n_lose = 0,0 
    while play.lower() == "s": 
        print()
        level, chosen_word = choose_level()
        print(f"Partita {n_game}")
        print(f"Il bot seleziona la difficoltà: {level}")
        win, lose = game(chosen_word)
        n_win += win
        n_lose += lose
        play = input("Vuoi effettuare un' altra partita [s][n]: ")
        n_game += 1 

    print("\nSessione terminata")
    print(f"Il bot ha vinto {n_win} partite")
    print(f"Il bot ha perso {n_lose} partite")

main()