import os
import flask_app 
import json

# Create a test client to send requests
client = flask_app.app.test_client()

def get_main_page_req():
    response = client.get('/api/v1/home')
    print(response.text)

def get_cars_jsonlist_req():
    response = client.get('/api/v1/cars')
    data = json.loads(response.text)
    cars = data['cars']
    for car in cars:
        print("\nCar info:")
        for key in car:
            print(f"{key}: {car[key]}")

def get_car_by_registration_number_req(registration_number):
    response = client.get(f'/api/v1/cars/{registration_number}')
    data = json.loads(response.text)
    print("\nCar info:")
    for key, value in data["car"].items():
        print(f"{key}: {value}")

def get_car_by_owner_req(owner):
    response = client.get(f'/api/v1/cars/{owner}')
    data = json.loads(response.text)
    print("\nCar info: ")
    for key, value in data["car"].items():
        print(f"{key}: {value}")

# Send a POST request
def add_car_req(registration_number, owner, model):
    post_response = client.post(f'/api/v1/cars/{registration_number}', json={
        'registration number': f'{registration_number}',
        'owner': f'{owner}',
        'model': f'{model}'
    })
    print(post_response.get_json())

# Send a DELETE request
def delete_car_req(registration_number):
    delete_response = client.delete(f'/api/v1/cars/{registration_number}')
    print(delete_response.get_json())

def update_owner_req(registration_number, new_owner):
    put_response = client.put(f'/api/v1/cars/{registration_number}', json={'new_owner': f'{new_owner}'})
    print(put_response.get_json())


os.system('cls' if os.name == 'nt' else 'clear')

#get_main_page()

get_cars_jsonlist_req() # Soterars i alfabetisk ordning pga items

#get_car_by_registration_number("THW297")

#add_car_req("ABC123", "John Doe", "Toyota Corolla")

#delete_car_req("THW297")

#update_owner("ABC123", "Jane Doe")
