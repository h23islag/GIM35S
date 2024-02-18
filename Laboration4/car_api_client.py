import flask_app 
import json

# Create a test client to send requests
client = flask_app.app.test_client()

def get_main_page():
    response = client.get('/api/v1/home')
    print(response.text)

def get_cars_jsonlist():
    response = client.get('/api/v1/cars')
    data = json.loads(response.text)
    cars = data['cars']
    for car in cars:
        print("\nCar info:")
        for key, value in car.items():
            print(f"{key}: {value}")

def get_car_by_registration_number(registration_number):
    response = client.get(f'/api/v1/cars/{registration_number}')
    data = json.loads(response.text)
    print("\nCar info: ")
    for key, value in data["car"].items():
        print(f"{key}: {value}")

def get_car_by_owner(owner):
    response = client.get(f'/api/v1/cars/{owner}')
    data = json.loads(response.text)
    print("\nCar info: ")
    for key, value in data["car"].items():
        print(f"{key}: {value}")

# Send a POST request
def add_car(registration_number, owner, model):
    post_response = client.post(f'/api/v1/cars/{registration_number}', json={
        'registration number': f'{registration_number}',
        'owner': f'{owner}',
        'model': f'{model}'
    })
    print(post_response.get_json())

# Send a DELETE request
def delete_car(registration_number):
    delete_response = client.delete(f'/api/v1/cars/{registration_number}')
    print(delete_response.get_json())

def update_owner(registration_number, new_owner):
    put_response = client.put(f'/api/v1/cars/{registration_number}', json={'new_owner': f'{new_owner}'})
    print(put_response.get_json())


#get_main_page()

get_cars_jsonlist()

#get_car_by_registration_number("THW297")

#add_car("ABC123", "John Doe", "Toyota Corolla")

#delete_car("THW297")

#update_owner("ABC123", "Jane Doe")
