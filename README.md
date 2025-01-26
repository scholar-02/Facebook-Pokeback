
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
#### Note: With `undetected_chromedriver`, ChromeDriver setup is handled automatically.

---

### 2️⃣ Create a search_terms.txt File
Create a file named `search_terms.txt` in the same directory as `pokeBack.py`.
Each line in the file should contain a single term. Example:
```
back
backInYourLanguage
```
If the file is not found, the script will prompt you to create one.

---

## 🚀 How to Run

1. Run the script:
```python
python pokeBack.py
```
2. A Chrome browser will open; log into Facebook manually.
3. Once you’re logged in, return to the terminal and press Enter.
4. The script will navigate to the Facebook Poke page and:
   * Dynamically find and click "poke back" buttons based on the search terms.
   * Mimic human-like scrolling and clicking behavior.
   * Sleep and repeat in a loop to maintain your poke streaks.

---

## 🛡️ Error Handling

- If the `search_terms.txt` file is missing, the script will notify you.
- Console logs provide updates on progress and any errors encountered.
- The script handles interruptions gracefully. Press `Ctrl + C` to stop it at any time.

---

## 📂 How It Works

1. **Search Terms**: Dynamically builds an XPath based on terms from `search_terms.txt`.
2. **Login Automation**: Prompts you to log in manually for added security.
3. **Navigate to Poke Page**: Automatically navigates to the Facebook Poke page.
4. **Human-Like Behavior**: Mimics human-like scrolling and random clicking within the browser.
5. **Continuous Operation**: Runs in a loop, ensuring consistent poke-back activity.

---

## 🔧 Requirements
- Python 3.8+  
- Selenium  
- `undetected_chromedriver`

---

## 🧰 Technologies Used
- **Python**: Core language for automation.
- **Selenium**: For browser interaction and automation.
- **undetected_chromedriver**: To control the browser and avoid detection.

---

## 🌟 Features
- Automatically pokes back all pending requests.
- Handles dynamic Facebook UI changes with custom XPath logic.
- Mimics human-like interactions to avoid detection.
- Gracefully stops with `Ctrl + C`.
- Lightweight and easy to configure.

---

Feel free to contribute, raise issues, or suggest enhancements to this project!
