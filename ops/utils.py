import os
import json
import csv

file_path = 'expenses.json'
csv_path = 'expenses.csv'
def read_expenses():
    if not os.path.exists(file_path):
        return [] #empty JSON
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except ValueError:
        print('Decoding JSON has failed, file may be corrupt')

    
def write__to_expenses(expenses):
    with open(file_path, 'w') as file:
        json.dump(expenses, file, indent=4)

def get_month_name(month):
    return['January', 'February', 'March', 'April', 'May', 'June', 'July', 
           'August', 'September', 'October', 'November', 'December'][month-1] if month else ""

def json_to_csv():
    with open(file_path, 'r') as json_file:
        json_data = json.load(json_file)
    
    with open(csv_path, 'w+', newline='') as csv_file:

        csv_writer = csv.writer(csv_file)

        if isinstance(json_data, list):

            header = json_data[0].keys()
            csv_writer.writerow(header)

            for item in json_data:
                csv_writer.writerow(item.values()) 


