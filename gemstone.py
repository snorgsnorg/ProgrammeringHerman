import random

score1 = 0

print("Målet med spelet är att du ska få maximalt 21 poäng. Du får poäng genom att kasta tärningen. Om du får över 21 poäng så förlorar du spelet. Lycka till!")

keep_playing = True

while keep_playing:
    choice = input("Vill du kasta tärningen? (Ja/Nej): ")
    if choice in ("nej", "n"):
        print("Du valde att stanna här. Hejdå!")
        keep_playing = False
        break
    elif choice in ("ja", "j"):
        roll = random.randint(1, 6)
        score1 += roll
        print(f"Poäng: {score1}/21")
        if score1 > 21:
            print("Din jävla apa! Du fick " + str(score1) + " poäng och förlorade spelet!")
            print("Spelet är över.")
            break
    else:
        print("Skriv 'Ja' eller 'Nej'.")

if score1 <= 21:
    print("Du fick " + str(score1) + " /21 poäng.")
    print("Du vann! Du är inte en jävla apa!")
