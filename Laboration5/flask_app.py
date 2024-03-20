import os
from flask import Flask, jsonify
from bs4 import BeautifulSoup
import requests
import json
import datetime

app = Flask(__name__)

def get_categories():
    try:
        url = 'https://books.toscrape.com/'
        response = requests.get(url)
        # Check if the request was successful
        response.raise_for_status()
        # Extract the HTML content from the response
        html_doc = response.text

        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(html_doc, 'html.parser')

        # Find all <ul> tags with class "nav-list"
        nav_lists = soup.find_all('ul', class_='nav-list')

        # Initialize a list to store categories
        categories = []

        # Iterate over each <ul> tag
        for nav_list in nav_lists:
            # Find all <a> tags within the <ul> tag
            category_links = nav_list.find_all('a')

            # Iterate over each <a> tag to create a dictionary for each book
            for link in category_links[1:]:
                category_url = 'https://books.toscrape.com/' + link.get('href')
                category_title = link.get_text(strip=True)

                response = requests.get(category_url)
                if response.status_code == 200:
                    # Extract the HTML content from the response
                    html_doc = response.text
                    
                    # Parse the HTML content using BeautifulSoup
                    soup = BeautifulSoup(html_doc, 'html.parser')
                    # Find all <li> tags with class "col-xs-6 col-sm-4 col-md-3 col-lg-3"
                    results = soup.find_all('li', class_='col-xs-6 col-sm-4 col-md-3 col-lg-3')

                categories.append({'title': category_title, 'url': category_url, 'results': len(results)})

        filename = f'categories_{datetime.date.today()}.json'
        with open(filename, mode='w', encoding='utf-8-sig') as json_file:
            json.dump(categories, json_file, indent=4)
        
        print(f"Categories saved to {filename}")
        return categories
    except requests.exceptions.HTTPError as err:
        print("Failed to retrieve data from the URL with the following error:", err)

def get_book(category, full_title):
    if(check_date("categories")):
        with open(f'categories_{datetime.date.today()}.json', mode='r', encoding='utf-8-sig') as json_file:
            categories = json.load(json_file)
    else:
        categories = get_categories()
    for cat in categories:
        if cat['title'] == category:
            response = requests.get(cat['url'])
            if response.status_code == 200:
                # Extract the HTML content from the response
                html_doc = response.text
                
                # Parse the HTML content using BeautifulSoup
                soup = BeautifulSoup(html_doc, 'html.parser')
                # Find all <li> tags with class "col-xs-6 col-sm-4 col-md-3 col-lg-3"
                li_tags = soup.find_all('li', class_='col-xs-6 col-sm-4 col-md-3 col-lg-3')
                books = []
                for li_tag in li_tags:
                    # Extract book information
                    if full_title != None:
                        try:
                            title = li_tag.find('h3').find('a')['title']
                            price = li_tag.find('p', class_='price_color').get_text(strip=True)
                            # Decode Unicode escape sequences to proper characters
                            price = price.encode().decode('unicode-escape')
                            rating = li_tag.find('p', class_='star-rating')['class'][1]
                            books.append({'title': title, 'price': price, 'rating': rating})
                            filename = f'{category}_{title}_{datetime.date.today()}.json'
                            with open(filename, mode='w', encoding='utf-8-sig') as json_file:
                                json.dump(books, json_file, indent=4)
                            print(f'Book saved to {filename}')
                            return books
                        except:
                            print(f"Book by the titlename {full_title} not found!")
                            return
                    else:
                        title = li_tag.find('h3').find('a')['title']
                        price = li_tag.find('p', class_='price_color').get_text(strip=True)
                        rating = li_tag.find('p', class_='star-rating')['class'][1]
                        books.append({'title': title, 'price': price, 'rating': rating})

                filename = f'{category}_books_{datetime.date.today()}.json'
                # Save books to JSON file
                with open(filename, mode='w', encoding='utf-8-sig') as json_file:
                    json.dump(books, json_file, indent=4)
                print(f"Books saved to {filename}")
                return books

def get_books(category):
    return get_book(category, None)

@app.route('/api/v1/books/categories', methods=['GET'])
def fetch_categories():
    if check_date('categories'):
        with open(f'categories_{datetime.date.today()}.json', mode='r', encoding='utf-8-sig') as json_file:
            categories = json.load(json_file)
        return jsonify(categories)
    else:
        categories = get_categories()
        return jsonify(categories)

@app.route('/api/v1/books/<category>', methods=['GET'])
def fetch_books(category):
    if check_date(category+"_books"):
        with open(f'{category}_books_{datetime.date.today()}.json', mode='r', encoding='utf-8-sig') as json_file:
            books = json.load(json_file)
        return jsonify(books)
    else:
        books = get_books(category)
        return jsonify(books)

@app.route('/api/v1/books/<category>/<book_title>', methods=['GET'])
def fetch_book(category, book_title):
    if check_date(f'{category}_{book_title}'):
        with open(f'{category}_{book_title}_{datetime.date.today()}.json', mode='r', encoding='utf-8-sig') as json_file:
            book = json.load(json_file)
        return jsonify(book)
    else:
        book = get_book(category, book_title)
        return jsonify(book)

def check_date(partial_filename):
    today_date = datetime.date.today()
    
    # Get the directory of the current script
    script_directory = os.path.dirname(os.path.abspath(__file__))
    
    # Construct the file path for the JSON file
    json_file_path = os.path.join(script_directory, f'{partial_filename}_{today_date}.json')
    
    # Check if the JSON file exists and if its name matches the current date
    if os.path.exists(json_file_path):
        return True
    else:
        return False

if __name__ == '__main__':
    app.run(debug=True)