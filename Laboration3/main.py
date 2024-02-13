import os
from time import sleep
import usermanager as userman
import moviemanager as mvman
import Typewriter as tpwrite

SECS = 2

def login_menu():
    running = True
    while(running):
        sleep(SECS)
        os.system('cls' if os.name == 'nt' else 'clear')
        tpwrite.typewriter_effect("*Meny*\n")
        tpwrite.typewriter_effect("Vilken av följande operationer skulle du vilja genomföra: "
            "\n1. Logga in\n2. Skapa konto\n3. Avsluta programmet")
        tpwrite.typewriter_effect("\nAnge alt: ")
        user_input = input()
        if(user_input == "1"):
            if(userman.load_user_data()):
                username = userman.login()
                if(username != None):
                    mv_menu(username)
        elif(user_input == "2"):
            userman.create_user()
        elif(user_input == "3"):
            tpwrite.typewriter_effect("\nLoggar ut...")
            sleep(SECS)
            exit()
        else:
            tpwrite.typewriter_effect("\nOgiltigt alternativ... Var god försök igen")

def mv_menu(username):
    running = True
    while(running):
        sleep(SECS)
        os.system('cls' if os.name == 'nt' else 'clear')
        tpwrite.typewriter_effect("*Meny*\n")
        tpwrite.typewriter_effect("Vilken av följande operationer skulle du vilja genomföra: "
            "\n1. Sök efter fullständing titel\n2. Sök efter fullständig titel med IMDB id"
            "\n3. Sök efter tillgängliga filmer\n4. Visa sök historik"
            "\n5. Rensa användarhistorik\n6. Logga ut\n7. Avsluta programmet")
        tpwrite.typewriter_effect("\nAnge alt: ")
        user_input = input()
        if(user_input == "1"):
            tpwrite.typewriter_effect("\nAnge fullständig titel: ")
            movie = mvman.lookup_title(input(), False)
            if(movie):
                userman.update_user_history(username, movie)
        elif(user_input == "2"):
            tpwrite.typewriter_effect("\nAnge fullständig IMDB id: ")
            movie = mvman.lookup_title(False, input())
            if(movie):
                userman.update_user_history(username, movie)
        elif(user_input == "3"):
            tpwrite.typewriter_effect("\nVar god och ange en sök fras: ")
            movie = mvman.lookup_titles(input())
            if(movie):
                userman.update_user_history(username, movie)
        elif(user_input == "4"):
            userman.print_user_history(username)
        elif(user_input == "5"):
            userman.clear_user_history(username)
        elif(user_input == "6"):
            return login_menu()
        elif(user_input == "7"):
            tpwrite.typewriter_effect("\nStänger ned...")
            sleep(SECS)
            exit()
        else: 
            tpwrite.typewriter_effect("\nOgiltigt alternativ... Var god försök igen")

login_menu()