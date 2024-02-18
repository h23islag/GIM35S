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
    response = client.get(f'/api/v1/cars/registration_numbers/{registration_number}')
    data = json.loads(response.text)
    car = data['car']
    print("\nCar info:")
    for key in car:
        print(f"{key}: {car[key]}")

def get_car_by_owner_req(owner):
    try:
        response = client.get(f'/api/v1/cars/owners/{owner}')
        data = json.loads(response.text)
        car = data['car']
        print("\nCar info:")
        for key in car:
            print(f"{key}: {car[key]}")
    except:
        print("Owner not found!")

# Send a POST request
def add_car_req(registration_number, owner, model):
    post_response = client.post(f'/api/v1/cars/registration_numbers/{registration_number}', json={
        'registration number': f'{registration_number}',
        'owner': f'{owner}',
        'model': f'{model}'
    })
    data = post_response.get_json()
    for key in data:
        print(data[key])

# Send a DELETE request
def delete_car_req(registration_number):
    delete_response = client.delete(f'/api/v1/cars/registration_numbers/{registration_number}')
    data = delete_response.get_json()
    for key in data:
        print(data[key])

def update_owner_req(registration_number, new_owner):
    put_response = client.put(f'/api/v1/cars/owners/{registration_number}', json={'new_owner': f'{new_owner}'})
    data = put_response.get_json()
    for key in data:
        print(data[key])


os.system('cls' if os.name == 'nt' else 'clear')

#get_main_page_req()

#get_cars_jsonlist_req()

#get_car_by_registration_number_req("NZX348")

#get_car_by_owner_req("Michael Schumacher")

#add_car_req("ABC123", "John Doe", "Toyota Corolla")

#update_owner_req("ABC123", "Jane Doe")

delete_car_req("ABC123")