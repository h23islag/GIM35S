import modules as m
import time
import os
from random import randint

RND = randint(1,60)
SECS = 1

def menu():
    running = True
    while(running):
        print("Vilken av följande två program skulle du vilja köra?\n1. Modulo operation\n2. Gissa ett nummer\n3. Avsluta programemt")
        user_input = input("Ange ett alt: ")
        if (user_input.isdigit()):
            user_input = int(user_input)
            if(user_input == 1):
                print("\nAnge två nämnare:")
                denominator1 = input("Nämnare ett : ")
                if (denominator1.isdigit()):
                    denominator2 = input("Nämnare två : ")
                    if(denominator2.isdigit()):
                        denominator1 = int(denominator1)
                        denominator2 = int(denominator2)
                        dict = m.divider(int(denominator1), int(denominator2))
                        print(f"\nMedelvärdet för antalet tal med rest 0 för {denominator1} är: {dict[denominator1][1]} där antalet tal motsvarar = {len(dict[denominator1][0])}")
                        print(f"Medelvärdet för antalet tal med rest 0 för {denominator2} är: {dict[denominator2][1]} där antalet tal motsvarar = {len(dict[denominator2][0])}\n")
            elif(user_input == 2):
                m.guessing_game(RND) # Importerar och genererar ett slumpmässigt tal i program för att ge använder möjlighet att gissa på samma tal flera gånger.
                #OBS! Om så behövts för att få godkännt på uppgiften hade importeringen kunnat lega i modules och genergeringen kunnat genomföras med en global variabel i modules.
            elif(user_input == 3):
                print("Avslutar...")
                running = False
            else:
                print("\nOgiltigt alternativ. Var god försök igen!\n")
                time.sleep(SECS)
                os.system('cls' if os.name == 'nt' else 'clear')
        else:     
            print("\nOgiltigt alternativ. Var god försök igen!\n")
            time.sleep(SECS)
            os.system('cls' if os.name == 'nt' else 'clear')

menu()