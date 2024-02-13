import json
from time import sleep

import keyboard
import Typewriter as tpwrite

SECS = 2

users = {}

def create_user():
    tpwrite.typewriter_effect("\nAnge användarnamn: ")
    username = input()
    if(username.isalnum()):
        if(username not in users.keys()):
            tpwrite.typewriter_effect("\nAnge lösenord: ")
            user_pwd = input()
            users[username] = [user_pwd, []] # Där [] är en tom lista tänkt att förvara filmer
            tpwrite.typewriter_effect("\nSparar ned användare...")
            sleep(SECS)
            save_user_data()
            tpwrite.typewriter_effect(f"\nAnvändare sparad!")
        else:
            tpwrite.typewriter_effect(f"{username} finns redan!")
    else:
        tpwrite.typewriter_effect("Ogiltigt format på användarnamn!")
        return

def login():
    running = True
    while running:
        tpwrite.typewriter_effect("\nAnge användarnamn: ")
        username = input()
        if(check_username(username)):
            tpwrite.typewriter_effect("\nAnge lösenord: ")
            user_pwd = input()
            if(check_pwd(user_pwd)):
                tpwrite.typewriter_effect("\nLoggar in...")
                return username
            else:
                user_input = input(f"\nLösenordet matchar inte användaren {username}! Vill du: \n1.Försöka igen\n2.Gå tillbaka?")
                if(user_input == "2"):
                    return None
                elif(user_input != "1"):
                    tpwrite.typewriter_effect("\nOgiltigt alternativ!")
                    return None
        else:
            tpwrite.typewriter_effect(f"\nAnvändaren \"{username}\" hittades inte! Vill du: \n1.Försöka igen\n2.Gå tillbaka?")
            user_input = input()
            if(user_input == "2"):
                return False
            elif(user_input != "1"):
                tpwrite.typewriter_effect("\nOgiltigt alternativ!")
                return False

def check_username(username):
    if(username in users.keys()):
        return True
    return False

def check_pwd(user_pwd):
    for user in users:
        if(user_pwd == users[user][0]):
            return True
    return False

def save_user_data():
    with open("users", mode='w', encoding='utf-8-sig') as json_file:
        json.dump(users, json_file, indent=1, ensure_ascii=False)

def load_user_data():
    try:
        global users
        with open("users", mode='r+', encoding='utf-8-sig') as json_file:
            users = json.load(json_file)
        return True
    except FileNotFoundError:
        tpwrite.typewriter_effect("\nIngen användare skapad!")

def update_user_history(username, movie):
    for user in users.keys():
        if(username == user):
            users[user][1].append(movie)
    save_user_data()

def clear_user_history(username):
    for user in users.keys():
        if(username == user):
            users[user][1] = []
            tpwrite.typewriter_effect("\nHistorik rensad!")
    save_user_data()

def print_user_history(username):
    for user in users.keys():
        if(username == user):
            for movie in users[user][1]:
                print()
                for key, value in movie.items():
                    if not isinstance(value, list):
                        tpwrite.typewriter_effect(str(key) + ": " + str(value) + "\n")
    while True:
        tpwrite.typewriter_effect("\nKlicka backspace för att återgå till menyn!")
        if(keyboard.read_key('backspace')):
            break



