import time, random, sys
from datetime import datetime
from pathlib import Path
from playwright.sync_api import sync_playwright, TimeoutError as PWTimeoutError

CDP_ENDPOINT = "http://127.0.0.1:9222"
CART_URL     = "https://utdallas.collegescheduler.com/terms/2026%20Summer/cart"
SHOT_DIR     = Path(__file__).resolve().parent / "shots"
LOG_PREFIX   = "[auto-reg]"

SUCCESS_PHRASE = "Success: This class has been added to your schedule."
FAIL_HEADER_1  = "Registration Results"
FAIL_PHRASE_1  = "You are not registered for the following courses."
FAIL_PHRASE_2  = "Choose another class."

def log(msg):
    print(f"{LOG_PREFIX} {datetime.now().isoformat(timespec='seconds')} - {msg}", flush=True)

def pick_cart_page(contexts):
    # Look for an existing tab on collegescheduler
    for ctx in contexts:
        for pg in ctx.pages:
            u = (pg.url or "").lower()
            if "collegescheduler.com" in u:
                return pg
    # Else open a new tab in the first context
    if contexts:
        return contexts[0].new_page()
    return None

def main():
    SHOT_DIR.mkdir(exist_ok=True)
    # For production you can use: time.sleep(random.randint(0, 90))
    time.sleep(1)  # fast while testing

    with sync_playwright() as p:
        try:
            browser = p.chromium.connect_over_cdp(CDP_ENDPOINT)
        except Exception:
            log(f"ERROR: Could not connect to Brave at {CDP_ENDPOINT}. Is the debug Brave window running?")
            sys.exit(1)

        contexts = browser.contexts
        if not contexts:
            log("ERROR: No contexts found in Brave.")
            sys.exit(1)

        page = pick_cart_page(contexts)
        if page is None:
            log("ERROR: Could not open/find a page context.")
            sys.exit(1)

        try:
            # If not already on cart, go there
            if "collegescheduler.com" not in (page.url or ""):
                page.goto(CART_URL, timeout=120_000, wait_until="domcontentloaded")
            else:
                # Ensure we're on the cart path
                if "/cart" not in page.url:
                    page.goto(CART_URL, timeout=120_000, wait_until="domcontentloaded")

            page.wait_for_load_state("networkidle")
            page.wait_for_timeout(1200)  # lazy-load cushion

            log("[STEP] Finding Register button...")
            register = page.get_by_role("button", name="Register")
            register.wait_for(state="visible", timeout=20_000)

            log("Clicking Register…")
            register.click()

            log("[STEP] Looking for Continue (confirm)...")
            continue_btn = page.get_by_role("button", name="Continue")
            continue_btn.wait_for(state="visible", timeout=20_000)

            log("[STEP] Clicking Continue...")
            continue_btn.click()

            log("[STEP] Waiting for result...")
            page.wait_for_timeout(1000)

            deadline = time.time() + 25
            outcome = "unknown"
            shot_path = None

            while time.time() < deadline:
                html = page.content()

                # ----- SUCCESS -----
                if SUCCESS_PHRASE in html:
                    outcome = "success"
                    # brief delay so the success dialog is visible in the screenshot
                    page.wait_for_timeout(750)
                    break

                # ----- FAILURE / FULL -----
                if (FAIL_HEADER_1 in html) or (FAIL_PHRASE_1 in html) or (FAIL_PHRASE_2 in html):
                    outcome = "full_or_error"
                    # wait so the popup is clearly visible
                    page.wait_for_timeout(750)

                    # take screenshot BEFORE we dismiss OK
                    shot_path = SHOT_DIR / f"{int(time.time())}_{outcome}.png"
                    try:
                        page.screenshot(path=str(shot_path), full_page=True)
                    except Exception:
                        pass

                    # now dismiss the popup so next run is clean
                    try:
                        ok_btn = page.get_by_role("button", name="OK")
                        if ok_btn.is_visible():
                            ok_btn.click()
                    except Exception:
                        pass
                    break

                page.wait_for_timeout(600)

            # If we didn't already take a screenshot above, take a generic one now
            if shot_path is None:
                shot_path = SHOT_DIR / f"{int(time.time())}_{outcome}.png"
                try:
                    page.screenshot(path=str(shot_path), full_page=True)
                except Exception:
                    pass

            if outcome == "success":
                log("[OK] SUCCESS: Class added.")
            elif outcome == "full_or_error":
                log("[WARN] No seat/waitlist. Not registered.")
            else:
                log("[INFO] Clicked through; no clear message found.")

        except PWTimeoutError:
            log("ERROR: Timeout.")
            try:
                page.screenshot(path=str(SHOT_DIR / f"{int(time.time())}_timeout.png"), full_page=True)
            except Exception:
                pass
        except Exception as e:
            log(f"ERROR: {e!r}")
            try:
                page.screenshot(path=str(SHOT_DIR / f"{int(time.time())}_exception.png"), full_page=True)
            except Exception:
                pass
        finally:
            # Do NOT close the browser; it’s your Brave instance (this only closes the CDP connection)
            try:
                browser.close()
            except Exception:
                pass

if __name__ == "__main__":
    main()
