import modules as m
import os
from random import randint

def menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    running = True
    while(running):
        print("Vilken av följande två program skulle du vilja köra?\n1. Modulo operation\n2. Gissa ett nummer\n3. Avsluta programemt")
        user_input = input("Ange ett alt: ")
        if(user_input == "1"):
            print("\nAnge två nämnare:")
            denominator1 = input("Nämnare ett : ")
            if (denominator1.isdigit()):
                denominator2 = input("Nämnare två : ")
                if(denominator2.isdigit()):
                    denominator1 = int(denominator1)
                    denominator2 = int(denominator2)
                    print(f"Nämnarna {denominator1} och {denominator2} angavs!\n")
                    dict = m.divider(denominator1, denominator2)
                    print(f"\nMedelvärdet för antalet tal med rest 0 för {denominator1} är: {dict[denominator1][1]} där antalet tal motsvarar = {len(dict[denominator1][0])}")
                    print(f"Medelvärdet för antalet tal med rest 0 för {denominator2} är: {dict[denominator2][1]} där antalet tal motsvarar = {len(dict[denominator2][0])}\n")
                else:
                    print("Ogiltig nämnare! Var god försök igen")
            else:
                print("Ogiltig nämnare! Var god försök igen")
        elif(user_input == "2"):
            rnd = randint(1,60)
            m.guessing_game(rnd)
        elif(user_input == "3"):
            print("Avslutar...")
            running = False
        else:     
            print("\nOgiltigt alternativ. Var god försök igen!\n")

menu()