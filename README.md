# UT Dallas — Class Auto-Registration Bot

Automates the **Register → Continue** flow on the UT Dallas College Scheduler using your existing logged-in Brave browser session. Built for high-frequency retries when classes are full or registration opens early.

**Made by bibs** · Python 3.10+ · Playwright · Chrome DevTools Protocol

---

## Features

- Connects to your **already-logged-in Brave browser** via Chrome DevTools Protocol — no credentials stored in the script
- Automatically navigates to your cart, clicks **Register**, then **Continue**
- Detects whether registration succeeded or failed
- Saves a **screenshot** of every attempt
- Logs all results to a file
- Can loop automatically on a timer

---

## How It Works

1. You launch Brave in remote debug mode
2. You log in manually and add classes to your cart
3. The script connects to that browser session
4. It clicks through the registration flow
5. It detects the outcome (success, class full, or error)
6. It saves a screenshot and logs the result
7. It waits, then tries again

---

## Project Structure

```
class-autoreg/
├── brave_click_register.py     # Main automation script
├── start_brave_debug.cmd       # Launches Brave with remote debugging
├── rapid_test.cmd              # Run the script once (quick test)
├── run_click_register.cmd      # Single-execution wrapper
├── run_every_23min.cmd         # Loops the script every ~23 minutes
├── auto_reg.log                # All attempt results logged here
├── shots/                      # Screenshots from each attempt
└── user-data/                  # Persistent Brave profile (keeps you logged in)
```

---

## Requirements

- Python 3.10 or higher
- Playwright

Install dependencies:

```bash
pip install playwright
playwright install
```

---

## Setup

### 1. Start Brave in debug mode

Run:

```bash
start_brave_debug.cmd
```

This opens Brave with remote debugging on `127.0.0.1:9222` and loads your persistent profile from `user-data/`.

---

### 2. Log in and prepare your cart

In the Brave window that opens, go to:

```
https://utdallas.collegescheduler.com/terms/2026%20Spring/cart
```

Log in with your UTD account and add your desired classes to the cart.

> **Do not close this browser window while the script is running.**

---

### 3. Test run

Run:

```bash
rapid_test.cmd
```

The script will click Register → Continue, log the result, and save a screenshot in `/shots`.

---

### 4. Start the retry loop

Run:

```bash
run_every_23min.cmd
```

The script will execute, wait ~23 minutes, then repeat indefinitely.

---

## Logs & Output

All results are written to `auto_reg.log`. Example entry:

```
[auto-reg] 2026-03-29T01:23:45 - [OK] SUCCESS: Class added.
```

Screenshots in `/shots` are labeled by outcome: `success`, `full_or_error`, or `timeout`.

---

## Troubleshooting

| Problem | Fix |
|---|---|
| `ERROR: Could not connect to Brave at 127.0.0.1:9222` | Run `start_brave_debug.cmd` first and keep Brave open |
| Script does nothing | Confirm you're on the `/cart` page and buttons still say "Register" / "Continue" |
| Not logged in | Log in manually in the debug Brave window before running |
| Buttons not found | The scheduler UI may have changed — update selectors in the script: `page.get_by_role("button", name="Register")` |

---

## Ideas to Extend This

- **Discord or SMS alerts** — get notified the moment a class is registered
- **Shorter retry interval** — reduce the 23-minute wait for faster attempts
- **Multiple classes** — loop through several classes in one run
- **Headless mode** — run without a visible browser window

---

## Notes

- This uses a **real browser session**, not headless automation — lower detection risk
- The script never stores or transmits your credentials
- Keep the debug Brave window open while running

---

## Disclaimer

This script is for personal use only. Use responsibly and in accordance with UT Dallas's policies on automated access.
