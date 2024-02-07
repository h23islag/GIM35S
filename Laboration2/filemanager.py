import json
import csv
import Typewriter as tpwrite


def retrieve_user_data(filepath):
    with open(filepath, mode='r', encoding='utf-8-sig') as csv_file:
        users = []
        csv_object = csv.reader(csv_file)
        next(csv_object, None)
        for row in csv_object:
            data = []
            for field in row:
                data.append(field)
            users.append(data)
            # File is automatically closed when you exit the 'with' block
    return users
def export_to_json(data_set, filepath, indent):
    # Serializing json. Den process där en data struktur eller object konverteras till ett lätt förvarat format
    with open(filepath, mode='w', encoding='utf-8-sig') as json_file:
        json.dump(data_set, json_file, indent=indent, ensure_ascii=False)

def add_user_data(data_set, filepath, indent):
    with open(filepath, mode='r+', encoding='utf-8-sig') as json_file:
        json.dump(data_set, json_file, indent=indent, ensure_ascii=False)

def remove_user_data(username, filepath):
    with open(filepath, mode='r+', encoding='utf-8-sig') as json_file: # 'w' will truncate the file and remove all existing data. To modify the existing data without losing it, the file should be opened in read-write mode 'r+' instead.
        json_object = json.load(json_file)
        json_object.pop(username)
        json_file.seek(0) # Move the file cursor to the beginning of the file
        json_file.truncate()  # Truncate the file to remove content based on where the file cursors position
        json.dump(json_object, json_file, indent=2, ensure_ascii=False)

def print_data_set(filepath, indent):
    with open(filepath, mode='r', encoding='utf-8-sig') as json_file:
        json_object = json.load(json_file)
        for c in json.dumps(json_object, indent=indent, ensure_ascii=False):
            tpwrite.typewriter_effect(c)


def save_to_csv(json_filepath, csv_filepath):
    tpwrite.typewriter_effect("\nÖverför tillagd data till csv filen...")
    
    with open(json_filepath, mode='r', encoding='utf-8-sig') as json_file:
        new_data = json.load(json_file)
    
    # Write data to CSV file
    with open(csv_filepath, mode='w', encoding='utf-8-sig', newline='') as csv_file:
        csv_writer = csv.writer(csv_file) # Creates a csv writer object in Python.
        
        # Write headers
        csv_writer.writerow(['Användarnamn', 'Efternamn', 'Förnamn'])
        
        # Write data rows
        for username, [last_name, first_name] in new_data.items():
            csv_writer.writerow([username, last_name, first_name])
    
    tpwrite.typewriter_effect(f"\nDatan har uppdaterats och lagts till i {csv_filepath}")