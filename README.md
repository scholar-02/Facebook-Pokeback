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
pip install selenium
```

---

### 2️⃣ Download WebDriver

- Download the correct WebDriver for your browser and OS. For example:
  - [ChromeDriver](https://sites.google.com/chromium.org/driver/)
  - [GeckoDriver](https://github.com/mozilla/geckodriver) (for Firefox)
- Place the WebDriver executable in your system's PATH or in the script directory.

---

### 3️⃣ Update Configuration

Modify the script to include your Facebook login credentials and WebDriver path:
```python
EMAIL = "your-email@example.com"
PASSWORD = "your-password"
WEBDRIVER_PATH = "/path/to/your/webdriver"
```

---

### 4️⃣ Customize Facebook Poke URL

Update the `POKE_URL` in the script with the correct Facebook poke page URL:
```python
POKE_URL = "https://www.facebook.com/pokes"
```

---

## 🚀 How to Run

1. Run the script:
   ```bash
   python pokeBack.py
   ```
2. The bot will:
   - Log into your Facebook account.
   - Navigate to the Facebook Poke page.
   - Automatically poke back all pending requests.

---

## ⚙️ Customizations

- **Run Frequency**  
  You can schedule the bot to run periodically using a task scheduler (e.g., Cron for Linux or Task Scheduler for Windows).
  
- **Browser Options**  
  Modify Selenium WebDriver settings for headless mode:
  ```python
  options.add_argument("--headless")
  ```

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
- Customizable login and browser settings.
- Minimal dependencies for quick setup.

---

Feel free to contribute, raise issues, or suggest enhancements to this project!
