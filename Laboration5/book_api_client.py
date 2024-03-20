import json
import os
import flask_app

# Create a test client to send requests
client = flask_app.app.test_client()

def get_categories():
    response = client.get(f'/api/v1/books/categories')
    categories = json.loads(response.text)
    for category in categories:
        print("\nCategory info:")
        for key in category:
            print(f"{key}: {category[key]}")

def get_books(category):
    response = client.get(f'/api/v1/books/{category}')
    books = json.loads(response.text)
    for book in books:
        print("\nBook info:")
        for key in book.keys():
            if key == "rating":
                print(f"{key}: {book[key]}/Five")
            else:
                print(f"{key}: {book[key]}")

def get_book(category, title):
    response = client.get(f'/api/v1/books/{category}/{title}')
    book = json.loads(response.text)
    print("Book info:")
    for key in book[0].keys():
        if key == "rating":
            print(f"{key}: {book[0][key]}/Five")
        else:
            print(f"{key}: {book[0][key]}")

def get_book_price(category, title):
    response = client.get(f'/api/v1/books/{category}/{title}')
    book = json.loads(response.text)
    print("Book info:")
    for key in book[0].keys():
        if key == "price":
            print(f"{key}: {book[0][key]}")

def get_book_rating(category, title):
    response = client.get(f'/api/v1/books/{category}/{title}')
    book = json.loads(response.text)
    print("Book info:")
    for key in book[0].keys():
        if key == "rating":
            print(f"{key}: {book[0][key]}/Five")

os.system('cls' if os.name == 'nt' else 'clear')

#get_categories()

#get_books("Health")

get_book("Mystery", "Sharp Objects")

#get_book_price("Thriller", "Behind Closed Doors")

#get_book_rating("Thriller", "Behind Closed Doors")