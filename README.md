# Facebook-Pokeback
Python-based bot for automatically sending pokes back to friends on Facebook. Designed for simplicity, efficiency, and easy setup using Selenium WebDriver.

---

## 🤖 Automated Facebook Poke Back Bot

This Python script automates the process of poking back friends on Facebook. It uses Selenium to interact with the Facebook UI, making it ideal for users who want to maintain their poke streaks without manual effort.

---

## 🛠️ Setup Instructions

Follow these steps to configure and run the bot:

### 1️⃣ Install Dependencies
Ensure you have Python 3.8+ installed. Then, install the required libraries:
```bash
pip install undetected-chromedriver
```
Note: You no longer need to manually download ChromeDriver if you use undetected_chromedriver; it handles much of that automatically. However, if you prefer, you can still set your own driver path in code.
---

2️⃣ Create a search_terms.txt File
Create a file named search_terms.txt in the same directory as pokeBack.py.
Each line in the file should contain a single term, for example:
```
back
back//InYourLanguage
```
If no file is found, the script will prompt you to create one.

---

## 🚀 How to Run

1. Run the script:
```python
python pokeBack.py
```
2. A Chrome browser will open; log into Facebook manually.
3. Once you’re logged in, return to the terminal and press Enter.
4. The script will navigate to the Facebook Poke page and:
   * Continuously find and click “poke back” buttons (or similar) based on the search terms.
   * Sleep and repeat in a loop to maintain your poke streaks.

---

## 🛡️ Error Handling

- If login fails, an error will be logged to the console.
- If the poke page URL changes, the script will provide instructions to update it.

---

## 📂 How It Works

1. **Login Automation**: The bot uses Selenium WebDriver to log into your Facebook account.
2. **Navigate to Poke Page**: It navigates to the Facebook poke page.
3. **Automated Poking**: All pending poke requests are processed in a single run.

---

## 🔧 Requirements
- Python 3.8+  
- Selenium  
- WebDriver for your browser (e.g., ChromeDriver, GeckoDriver)

---

## 🧰 Technologies Used
- **Python**: Core language for automation.
- **Selenium**: For browser interaction and automation.
- **WebDriver**: To control the browser and simulate user actions.

---

## 🌟 Features
- Automatic poking back of all pending requests.
- Lightweight and easy-to-configure script.
- Minimal dependencies for quick setup.

---

Feel free to contribute, raise issues, or suggest enhancements to this project!
