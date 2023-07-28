import random
print("KAMIEN, PAPIER, NOZYCZE \n")

options = ["papier", "kamien", "nozyce"]
bot = random.choice(options)
print(bot)
print("1. papier\n 2. kamien\n 3. nozyce")
you = input("podaj numer:")

if(you == "1"):
    player = "papier"
elif(you == "2"):
    player = "kamien"
else:
    player = "nozyce"

print("komputer: ", bot, "vs ", player, " :Ty")

if(bot == "papier" and player =="papier"):
    print("remis")
elif(bot == "kamien" and player =="kamien"):
    print("remis")
elif(bot == "nozyce" and player =="nozyce"):
    print("remis")
elif(bot == "papier" and player =="kamien"):
    print("komputer wygrywa")
elif(bot == "kamien" and player =="nozyce"):
    print("komputer wygrywa")
elif(bot == "nozyce" and player =="papier"):
    print("komputer wygrywa")
elif(bot == "papier" and player =="nozyce"):
    print("wygrywasz")
elif(bot == "kamien" and player =="papier"):
    print("wygrywasz")
elif(bot == "nozyce" and player =="kamien"):
    print("wygrywasz")
else:
    print("idk")

w = input()