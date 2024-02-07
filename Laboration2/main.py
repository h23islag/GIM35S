import os
import time
import Typewriter as tpwrite
import filemanager as fileman

SECS = 2

def menu():
    csv_filepath = "studenter.csv"
    json_filepath = "studenter.json"
    indent = 2
    running = True
    data_set = {}
    while(running):
        time.sleep(SECS)
        os.system('cls' if os.name == 'nt' else 'clear')
        tpwrite.typewriter_effect("*Meny*\n")
        tpwrite.typewriter_effect("Vilken av följande operationer skulle du vilja genomföra: "
            "\n1. Läs in orginalfil (.csv fil) och spara ner till .JSON fil\n2. Lägga till person (till .json filen)\n3. Ta bort person (till .JSON filen)"
            "\n4. Visa all data som finns i .JSON filen\n5. Spara .JSON filen till .csv filen\n6. Avsluta programmet")
        tpwrite.typewriter_effect("\nAnge alt: ")
        user_input = input()
        if(user_input == "1"):
            tpwrite.typewriter_effect("\nKonverterar datan...")
            time.sleep(SECS) # För uppnå en tidseffekt, dvs att det tar tid att konvertera datan
            users = fileman.retrieve_user_data(csv_filepath)
            for user in users:
                data_set[user[0]] = [user[1], user[2]]
            fileman.export_to_json(data_set, json_filepath, indent=indent)
        elif(user_input == "2"):
            try:
                tpwrite.typewriter_effect("\nAnge användarnamn till personen som önskas läggas till: ")
                username = input()
                if(username.isalnum() and not (username in data_set.keys())):
                    tpwrite.typewriter_effect("\nAnge förnamn till personen som önskas läggas till: ")
                    forename = input()
                    tpwrite.typewriter_effect("\nAnge efternamn till personen som önskas läggas till: ")
                    surname = input()
                    if(forename.isalpha() and surname.isalpha()):
                        data_set[username] = [surname, forename]
                        fileman.add_user_data(data_set, json_filepath, indent=indent)
                        tpwrite.typewriter_effect(f"\n{forename} {surname} med användarnamnet \"{username}\" har lagts till i {json_filepath}!")
                    else:
                        tpwrite.typewriter_effect("\nOgitligt format!")
                elif(username.isalnum() and username in data_set.keys()):
                    tpwrite.typewriter_effect(f"\nAnvändarnamnet \"{username}\" finns redan!")                
                else:
                    tpwrite.typewriter_effect(f"\nOgiltigt format!")
            except Exception as e:
                tpwrite.typewriter_effect(f"\nException message: {e}")
                data_set.pop(username)
                
        elif(user_input == "3"):
            try:
                tpwrite.typewriter_effect("\nAnge användarnamn på personen som önskas tas bort: ")
                username = input()
                if(username in data_set):
                    removed_user_data = data_set.pop(username)
                    fileman.remove_user_data(username, json_filepath)
                    tpwrite.typewriter_effect("\n" + removed_user_data[1] +  removed_user_data[0] + " med användarnamnet \"" + username + "\" har tagits bort från " + json_filepath + "!")#"{removed_user_data[1]} {removed_user_data[0]} med användarnamnet \"{username}\" har tagits bort från {json_filepath}!")
                else:
                    tpwrite.typewriter_effect(f"\nAnvändarnamnet \"{username}\" hittades inte!")
            except Exception as e:
                tpwrite.typewriter_effect(f"\nException message: {e}")
                data_set[username] = removed_user_data
        elif(user_input == "4"):
            try:
                fileman.print_data_set(json_filepath, indent=indent)
            except Exception as e:
                tpwrite.typewriter_effect(f"\nException message: {e}")
        elif(user_input == "5"):
            try:
                fileman.save_to_csv(json_filepath=json_filepath, csv_filepath=csv_filepath)
            except Exception as e:
                tpwrite.typewriter_effect(f"\nException message: {e}")
        elif(user_input == "6"):
            tpwrite.typewriter_effect("\nStänger ned...")
            time.sleep(1)
            exit()
        else: 
            tpwrite.typewriter_effect("Ogiltigt alternativ... Var god försök igen")


menu()