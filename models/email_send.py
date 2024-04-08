from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import formataddr
from utils import confighandler, htmlhandler, recipienthandler
import smtplib
import ssl

def send_email(info_session):
    config_auth = confighandler.get_config_auth()
    config_smtp = confighandler.get_config_smtp()
    
    sender_name = config_auth['sender_name']
    sender_username = config_auth['username']
    sender_password = config_auth['password']
    smtp_server = config_smtp['smtp_server']
    smtp_port = config_smtp['smtp_port']
    email_subject = confighandler.get_info_email_subject(info_session)
    from_addr = formataddr((sender_name, sender_username))
    
    recipients_list = recipienthandler.get_recipients_list(info_session)
    
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls(context=ssl.create_default_context())
        server.login(sender_username, sender_password)
        
        for recipient_item in recipients_list:
            original_html_content = htmlhandler.read_html_file(info_session)
            msg = MIMEMultipart("alternative")
            msg['From'] = from_addr
            msg['To'] = recipient_item['recipient']
            msg['Subject'] = email_subject
                
            for key, value in recipient_item.items():
                value = str(value).replace('\n', '<br>')
                original_html_content = original_html_content.replace(f'{{{key}}}', value)
                
            msg.attach(MIMEText(original_html_content, 'html'))
            server.sendmail(from_addr, msg['To'], msg.as_string())
            
            print(f'Sent email to {msg["To"]} with subject "{msg["Subject"]}"')
