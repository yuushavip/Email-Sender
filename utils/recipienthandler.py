from utils import confighandler
import csv

def get_recipients_list(info_session):
    info = confighandler.get_info_recipient_list(info_session)
    file_path = f"recipients/{info}"
    
    with open(file_path, 'r', newline='', encoding='utf-8') as file:
        dict_reader = csv.DictReader(file)
        data = [row for row in dict_reader]
        
    return data