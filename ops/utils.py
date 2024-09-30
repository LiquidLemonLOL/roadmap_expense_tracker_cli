import os
import json

file_path = 'expenses.json'

def read_expenses():
    if not os.path.exists(file_path):
        return [] #empty JSON
    try:
        with open(file_path, 'r') as file:
            expenses = json.load(file)
    except ValueError:
        print('Decoding JSON has failed, file may be corrupt')
    
def write__to_expenses(expenses):
    with open(file_path, 'w') as file:
        json.dump(expenses, file, indent=4)

def get_month(month):
    return['January', 'February', 'March', 'April', 'May', 'June', 'July', 
           'August', 'September', 'October', 'November', 'December'][month-1] if month else ""