from random import randint

def divider(denominator1, denominator2):
    size = 1600
    numerators1 = []
    numerators2 = []
    for i in range(1, size):
        if(i%denominator1 == 0):
            numerators1.append(i)
        elif(i%denominator2 == 0):
            numerators2.append(i)
    print(f"\nNedan följer alla delbara tal med {denominator1} i intervallet 1 til 1600: ")
    print(numerators1) # Hade alternativt kunna loopa igenom värdena för snyggare utskrift
    print(f"\nNedan följer alla delbara tal med {denominator2} i intervallet 1 til 1600: ")
    print(numerators2) # Hade alternativt kunna loopa igenom värdena för snyggare utskrift
    dict = {}
    print(denominator1)
    dict[denominator1] = (numerators1, sum(numerators1)/len(numerators1))
    dict[denominator2] = (numerators2, sum(numerators2)/len(numerators2))
    return dict

def guessing_game(rnd):
    guesses = input("\nHur många gissningar vill du ha: ")
    if (not(guesses.isdigit())):
        print("\nOgiltigt alternativ!")
        guessing_game(rnd)
        return
    guesses = int(guesses)
    index = 0
    while index < guesses:
        predicted_val = input("\nGissa vilket tal jag tänker på (1-60): ")
        if (predicted_val.isdigit() and (1 < int(predicted_val) <= 60)):
            predicted_val = int(predicted_val)
            if(predicted_val == rnd):
                print("Du svarade korrekt! Grattis!")
                index = guesses
            elif(predicted_val < rnd):
                print("Du svarade fel. Talet är större än ditt gissade tal.")
                index += 1
            elif(predicted_val > rnd):
                print("Du svarade fel. Talet är mindre än ditt gissade tal.")
                index += 1
            else:
                print("Ogiltigt alternativ! Du får tillbaka ditt försök.")
        else:
            print("Ogiltigt alternativ! Du får tillbaka ditt försök.")
        
    print("\nTyvärr men dina gissningar är slut... Talet var: " + str(rnd) + "\n")
