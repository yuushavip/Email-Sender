from utils import confighandler

def read_html_file(info_session):
    info = confighandler.get_info_email_html(info_session)
    file_path = f"html/{info}"
    
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()