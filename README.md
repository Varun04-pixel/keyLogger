# Python Keylogger with Email Reporting (Educational Project)

## 📌 Overview
This project is a **Python-based keylogger**.  
It logs keystrokes with timestamps into a file and **automatically emails the log file** when the `ESC` key is pressed.

⚠️ **This project is strictly for educational purposes only.**  😂
Use it only on systems you own or have explicit permission to test. 

---

## ✨ Features
- Logs keyboard input with date & time
- Saves logs to a file (`data.txt`)
- Stops execution on pressing **ESC**
- Automatically emails the log file as an attachment
- Uses environment variables for sensitive data

---

## 🛠️ Technologies Used
- Python 3
- `pynput` (keyboard listener)
- `smtplib` (email sending)
- `python-dotenv` (environment variable management)

---

## 📁 Project Structure
project-folder/
│
├── keylog.py # Main keylogger script
├── data.txt # Generated log file
├── .env # Environment variables (not committed)
├── README.md # Project documentation

---

## 🔐 Environment Variables (`.env`)
Create a `.env` file in the project root:

```env
SENDER_EMAIL = "your_email@gmail.com"
RECEIVER_EMAIL = "receiver_email@gmail.com"
PASSWORD = "your_app_password"

🔑 Note:

For Gmail, use an App Password, not your normal password.

Enable 2-Step Verification in your Google account.

---

📦 Installation
1️⃣ Clone the repository
git clone <repo-url>
cd project-folder

2️⃣ Install dependencies
pip install pynput python-dotenv

▶️ Usage

Run the script:

python keylog.py