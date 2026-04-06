# 📚 Class Auto Registration Bot (UT Dallas)

Automates clicking the **Register → Continue** flow on the UT Dallas College Scheduler site using a real Brave browser session.

Designed for high-frequency retry attempts when classes are full.

---

## 🚀 Features

- Uses your **existing logged-in browser session**
- Connects via **Chrome DevTools Protocol (CDP)**
- Automatically:
  - Navigates to cart
  - Clicks Register and Continue
  - Detects success or failure
- Saves screenshots of outcomes
- Logs every attempt
- Can run repeatedly on a timer

---

## 🧠 How It Works

1. Launch Brave in debug mode  
2. Script connects to that browser session  
3. Finds your scheduler tab or opens one  
4. Clicks through registration flow  
5. Detects result:
   - Success → class added
   - Failure → class full or error  
6. Saves screenshot and logs result  

---

## 📂 Project Structure

```
class-autoreg/
│
├── brave_click_register.py     # Main automation script
├── start_brave_debug.cmd       # Launch Brave with remote debugging
├── rapid_test.cmd              # Run script once (quick test)
├── run_click_register.cmd      # Single execution wrapper
├── run_every_23min.cmd         # Loop script every ~23 minutes
├── auto_reg.log                # Log output
├── shots/                      # Screenshots of attempts
└── user-data/                  # Persistent Brave profile
```

---

## ⚙️ Requirements

- Python 3.10+
- Playwright

Install dependencies:

```bash
pip install playwright
playwright install
```

---

## 🧪 Setup

### 1. Start Brave in Debug Mode

Run:

```bash
start_brave_debug.cmd
```

This launches Brave with:
- Remote debugging on `127.0.0.1:9222`
- Persistent profile (`user-data/`)

---

### 2. Log In Manually

In the opened Brave window:

1. Go to:
   https://utdallas.collegescheduler.com/terms/2026%20Spring/cart
2. Log into your account
3. Make sure your desired classes are in the cart

---

### 3. Test Run

Run:

```bash
rapid_test.cmd
```

Expected behavior:
- Clicks Register → Continue
- Logs result in terminal
- Saves screenshot in `/shots`

---

## 🔁 Continuous Auto-Retry

To run repeatedly:

```bash
run_every_23min.cmd
```

This will:
- Execute the script
- Wait ~23 minutes
- Repeat indefinitely

---

## 🧾 Logs & Output

### Log File

```
auto_reg.log
```

Example:

```
[auto-reg] 2026-03-29T01:23:45 - [OK] SUCCESS: Class added.
```

---

### Screenshots

Saved in:

```
/shots/
```

Types:
- success
- full_or_error
- timeout

---

## ⚠️ Troubleshooting

### Cannot connect to browser

```
ERROR: Could not connect to Brave at 127.0.0.1:9222
```

Fix:
- Run `start_brave_debug.cmd` first

---

### Not logged in

Fix:
- Log in manually in the debug Brave window

---

### Script does nothing

Fix:
- Make sure you're on `/cart` page
- Ensure buttons still say:
  - Register
  - Continue

---

### Selectors broken

If UI changes, update selectors in:

```python
page.get_by_role("button", name="Register")
```

---

## 🔒 Notes

- This uses a **real browser session**, not headless automation
- Lower detection risk compared to bots that log in automatically
- Do not close the debug browser while running

---

## 🛠️ Customization Ideas

- Add Discord or SMS alerts on success
- Reduce retry interval
- Add multiple class attempts
- Headless fallback mode
- GUI dashboard

---

## 📌 Disclaimer

This script is for personal automation. Use responsibly and in accordance with your institution’s policies.
