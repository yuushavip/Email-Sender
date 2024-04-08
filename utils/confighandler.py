import configparser
import yaml
import os

def get_config():
    config = configparser.ConfigParser()
    file_name = 'email_sender_config.ini'
    file_path = f"config/{file_name}"
    
    if os.environ.get('CONFIG_DIR_PATH'):
        file_path = f"{os.environ['CONFIG_DIR_PATH']}{file_name}"
        
    config.read(file_path)
    
    return config

def get_info():
    file_name = 'email_sender_info.yaml'
    file_path = f"config/{file_name}"
    
    if os.environ.get('CONFIG_DIR_PATH'):
        file_path = f"{os.environ['CONFIG_DIR_PATH']}{file_name}"
    
    with open(file_path, 'r') as file:
        config = yaml.safe_load(file)
    
    return config

def get_info_from_session(session):
    info = get_info()
    info_session = info[session]
    info_data = {}
    
    for key, item in info_session.items():
        info_data[key] = item
        
    return info_data

def get_config_from_session(session):
    config = get_config()
    config_session = config[session]
    config_data = {}
    
    for key, item in config_session.items():
        config_data[key] = item
        
    return config_data

def get_email_tasks():
    config = get_info_from_session('settings')
    email_tasks = config.get('email_tasks', {})
    
    return email_tasks

def get_info_recipient_list(session):
    info = get_info_from_session(session)
    
    return info['recipient_list']

def get_info_email_subject(session):
    info = get_info_from_session(session)
    
    return info['email_subject']

def get_info_email_html(session):
    info = get_info_from_session(session)
    
    return info['email_html']

def get_config_auth():
    config = get_config_from_session('AUTH')
        
    return config

def get_config_smtp():
    config = get_config_from_session('SMTP')
        
    return config