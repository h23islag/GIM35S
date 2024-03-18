from random import randint

def divider(denominator1, denominator2):
    numerators = []
    for i in range(1, 1601):
        if(i%denominator1 == 0 and i%denominator2 == 0):
            numerators.append(i)
    print(f"\nNedan följer alla delbara tal med {denominator1} och {denominator2} i intervallet 1 til 1600: ")
    print(numerators) # Hade alternativt kunna loopa igenom värdena för snyggare utskrift
    print()
    dict = {}
    dict[denominator1] = (numerators, sum(numerators)/len(numerators))
    dict[denominator2] = (numerators, sum(numerators)/len(numerators))
    return dict

def guessing_game(rnd):
    guesses = input("\nHur många gissningar vill du ha: ")
    if (not(guesses.isdigit())):
        print("\nOgiltigt alternativ!")
        guessing_game(rnd)
        return
    guesses = int(guesses)
    while 0 < guesses:
        predicted_val = input("\nGissa vilket tal jag tänker på (1-60): ")
        if (predicted_val.isdigit() and (1 <= int(predicted_val) <= 60)):
            predicted_val = int(predicted_val)
            if(predicted_val == rnd):
                print("Du svarade korrekt! Grattis!")
                guesses = 0
            elif(predicted_val < rnd):
                print("Du svarade fel. Talet är större än ditt gissade tal.")
                guesses -= 1
                print(f"Du har {guesses} antal försök kvar!")
            elif(predicted_val > rnd):
                print("Du svarade fel. Talet är mindre än ditt gissade tal.")
                guesses -= 1
                print(f"Du har {guesses} antal försök kvar!")
        else:
            print("Ogiltigt alternativ! Du får tillbaka ditt försök.")
    if(predicted_val != rnd):
        print("\nTyvärr men dina gissningar är slut... Talet var: " + str(rnd) + "\n")
