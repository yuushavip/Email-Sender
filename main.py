from utils import confighandler
from models import email_send

def main():
    email_tasks = confighandler.get_email_tasks()
    
    for task in email_tasks:
        if task:
            print("Task: ", task)
            email_send.send_email(task)

if __name__ == "__main__":
    main()