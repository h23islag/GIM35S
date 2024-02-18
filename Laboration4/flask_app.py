from flask import Flask, jsonify, request
import json

app = Flask(__name__)

filepath = 'cars.json'

try:
    with open(filepath, 'r', encoding='utf-8-sig') as json_file:
        cars = json.load(json_file)
except FileNotFoundError:
    cars = []

@app.route('/api/v1/home')
def main():
    welcome_message = 'Välkommen till Bilfirman Ruffel och Båg. Just nu befinner du dig /api/v1/home. Nedan finns samtliga tillgänliga sökvägar listade inklusive deras funktion:\n'
    get_cars = '/api/v1/cars - Hämtar en jsondict innehållande alla bilar och deras info\n'
    reg_get = '/api/v1/cars/<registration_number> [GET] - Hämtar en bils info baserat registreringsnummer\n'
    owner_get = '/api/v1/cars/<owner> [GET] - Hämtar en bils info baserat ägare\n'
    post_reg = '/api/v1/cars/<registration_number> [POST] - Hämtar en bils info baserat registreringsnummer\n'
    del_reg = '/api/v1/cars/<registration_number> [DELETE] - Tar bort registreringsnummer och sammanhängande info\n'
    put_reg = '/api/v1/cars/<registration_number> [PUT] - Updaterar en bils ägare baserat på registreringsnummer'
    formatted_message = (
        welcome_message 
        + get_cars
        + reg_get
        + owner_get
        + post_reg
        + del_reg
        + put_reg
    )
    return formatted_message

@app.route('/api/v1/cars', methods=['GET'])
def get_cars_jsonlist():
    return jsonify({'cars': cars})

@app.route('/api/v1/cars/<registration_number>', methods=['GET'])
def get_car_by_registration_number(registration_number):
    for car in cars:
        if(car['registration number'] == registration_number):
            return jsonify({'car': car})
    return jsonify({'Registration number not found!': car}), 404

@app.route('/api/v1/cars/<owner>', methods=['GET'])
def get_car_by_owner(owner):
    for car in cars:
        if(car['owner'] == owner):
            return jsonify({'car': car})
    return jsonify({'Car owner not found!': car}), 404

@app.route('/api/v1/cars/<registration_number>', methods=['POST'])
def add_car():
    try:
        registration_number = request.json['registration number']
        owner = request.json['owner']
        model = request.json['model']

    except KeyError as e:
        return jsonify({'Error': f'Missing key: {e} in the request body!'}), 400

    for car in cars:
        if(car['registration number'] == registration_number):
            return jsonify({'Error': 'Registration number already exists!'}), 409

    new_car = {'registration number': registration_number, 'model': model, 'owner': owner}
    cars.append(new_car)

    with open(filepath, 'w', 'utf-8-sig') as json_file:
        json.dump(cars, json_file, indent=2)

    return jsonify({'Message': 'Registration number added successfully!'}), 200

@app.route('/api/v1/cars/<registration_number>', methods=['DELETE'])
def delete_car(registration_number):
    for car in cars:
        if car['registration number'] == registration_number:
            cars.remove(car)
            with open(filepath, 'w', 'utf-8-sig') as json_file:
                json.dump(cars, json_file, indent=2)
            return jsonify({'Message': 'Registration number and coherent data deleted successfully!'}), 200
        return jsonify({'Error': 'Registration number not found!'}), 404

@app.route('/api/v1/cars/<registration_number>', methods=['PUT'])
def update_owner(registration_number):
    new_owner = request.json.get('new_owner')

    if new_owner is None:
        return jsonify({'Error': 'Owner must be provided!'}), 400

    updated = False
    for car in cars:
        if car['registration number'] == registration_number:
            car['owner'] = new_owner
            updated = True
            break

    if not updated:
        return jsonify({'Error': 'Registration number not found!'}), 404

    with open(filepath, 'r+', encoding='utf-8-sig') as json_file:
        json.dump(cars, json_file, indent=2)

    return jsonify({'Message': 'Owner updated successfully!'}), 200




