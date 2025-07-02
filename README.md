# 🔐 AI Password Strength & Leak Checker

A smart and secure web app that checks how strong your password is and whether it's been exposed in known data breaches. Built using Python and Streamlit, it gives real-time strength analysis, visual feedback, and safe password suggestions.

👉 **[Live Demo](https://ai-password-strength-leak-checker-nr5.streamlit.app/)**  
📂 **[Source Code](https://github.com/devvsingh/AI-Password-Strength-Leak-Checker)**

---

## ✨ Features

- ✅ Password strength check with regex rules
- 🔋 Strength meter (Very Weak → Strong)
- 🔍 Leak detection using [HaveIBeenPwned API](https://haveibeenpwned.com/API/v3#SearchingPwnedPasswordsByRange)
- 🔐 Strong password generator (random & secure)
- 📱 Mobile-friendly Streamlit interface
- 🔒 Fully private – passwords never stored or shared

---

## 🛠 Tech Stack

| Tool           | Purpose                      |
|----------------|-------------------------------|
| Python         | Backend logic                 |
| Streamlit      | Web UI                        |
| Requests       | API communication             |
| Regex          | Pattern-based validation      |
| Hashlib        | SHA-1 hashing                 |
| Secrets        | Secure password generation    |
| HaveIBeenPwned | Public data breach database   |

---

## 🧠 How It Works

1. **Strength Check** – Regex verifies:
   - Length ≥ 8
   - Uppercase, lowercase, digit, and special characters
2. **Visual Feedback** – Progress bar shows strength (red → green)
3. **Leak Checker** – Password is hashed → API returns match count if leaked
4. **Password Suggestions** – Strong alternatives auto-generated using secure random

---

## 📦 Installation

### 1. Clone the Repository
```
git clone https://github.com/devvsingh/AI-Password-Strength-Leak-Checker.git
cd AI-Password-Strength-Leak-Checker
```
### 2. Install Requirements
```
pip install -r requirements.txt
```
### 3. Run the App
```
streamlit run app.py
```
### 📌 Use Cases
Students checking password security

Educating users on good password practices

Pre-check before signing up on websites

### 🔐 Why It’s Secure
Your password is never sent to the server

Uses k-anonymity principle (only 5 hash characters sent)

Open-source and privacy-first

### 🧑‍💻 Author
Dev Raj Singh.

Feel free to connect or contribute!

### ⭐ Show Your Support
If you like the project:

⭐ Star this repo

📣 Share the app

🔁 Contribute ideas or improvements


