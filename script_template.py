"""
WaterkoofAI x [PROJECT NAME] Airdrop Script Kit v1.0
======================================================
COVERAGE DECLARATION:
- Project: [Project Name]
- Portal URL: [https://...]
- Total airdrop tasks: [X]
- Tasks automated by this Kit: [X / X] ([X]%)
- Manual tasks remaining: [list them]
- Estimated points from this Kit: [~X pts] (estimated / confirmed)
- Tested on: [macOS / Windows / Linux] on [date]

SECURITY NOTICE:
- This script is open source and fully auditable
- Your private keys are NEVER collected or uploaded
- MetaMask signing steps require manual approval
- For educational purposes only. Use at your own risk.

HOW TO USE:
1. Drop STEP1_Drop_me_to_any_AI.md into any AI chat for guided setup
2. Fill in STEP2_Fill_your_wallet_info.json with your wallet details
3. Start Chrome with remote debugging (see If_you_dont_use_AI_read_me.txt)
4. Run: python project_auto.py

Powered by WaterkoofAI | t.me/WaterkoofAI_Bot
"""

import json
import time
import sys
import os
import platform
from playwright.sync_api import sync_playwright

# ── Replace these with the actual project URLs ──
PORTAL_URL  = "https://portal.yourproject.xyz"
APP_URL     = "https://app.yourproject.xyz"
CONFIG_FILE = "STEP2_Fill_your_wallet_info.json"


# ─────────────────────────────────────────────
#  Chrome debug command (auto-detects OS)
#  Do not modify this function.
# ─────────────────────────────────────────────

def get_chrome_debug_command():
    system = platform.system()
    home   = os.path.expanduser("~")
    if system == "Darwin":
        data_dir = os.path.join(home, "Library", "Application Support", "Google", "Chrome-Debug")
        return f'/Applications/Google\\ Chrome.app/Contents/MacOS/Google\\ Chrome --remote-debugging-port=9222 --no-first-run --user-data-dir="{data_dir}"'
    elif system == "Windows":
        data_dir = os.path.join(os.environ.get("LOCALAPPDATA", ""), "Google", "Chrome-Debug")
        return f'"C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe" --remote-debugging-port=9222 --no-first-run --user-data-dir="{data_dir}"'
    else:
        data_dir = os.path.join(home, ".config", "google-chrome-debug")
        return f'google-chrome --remote-debugging-port=9222 --no-first-run --user-data-dir="{data_dir}"'


# ─────────────────────────────────────────────
#  Helper functions
#  Do not modify these unless you know what you are doing.
# ─────────────────────────────────────────────

def load_config():
    if not os.path.exists(CONFIG_FILE):
        print(f"ERROR: {CONFIG_FILE} not found.")
        print("Please make sure STEP2_Fill_your_wallet_info.json is in the same folder.")
        sys.exit(1)
    with open(CONFIG_FILE, "r") as f:
        return json.load(f)


def wait_for_user(msg):
    """Pause the script and show a manual action prompt to the user."""
    print(f"\n{'='*50}")
    print(f"ACTION NEEDED: {msg}")
    print(f"Press ENTER when done...")
    print(f"{'='*50}")
    input()


def step(msg):
    """Print a step label."""
    print(f"\n> {msg}")


def success(msg):
    """Print a success message."""
    print(f"OK  {msg}")


def click_if_visible(page, selector, timeout=4000):
    """
    Click an element only if it is visible on the page.
    Returns True if clicked, False if not found.
    Use this for tasks that might already be completed.
    """
    try:
        el = page.locator(selector).first
        if el.is_visible(timeout=timeout):
            el.click()
            return True
    except Exception:
        pass
    return False


# ─────────────────────────────────────────────
#  Main wallet flow
#  THIS IS WHERE YOU BUILD YOUR AUTOMATION.
#  Follow the structure below for each task.
# ─────────────────────────────────────────────

def run_wallet(wallet, config, context):
    print(f"\n{'='*60}")
    print(f"Processing wallet: {wallet['address'][:10]}...")
    print(f"{'='*60}")

    page = context.new_page()

    # ── TASK 1: Open the project portal ──
    # Always start by navigating to the portal.
    step("Opening project portal...")
    page.goto(PORTAL_URL)
    page.wait_for_load_state("networkidle")
    time.sleep(2)
    success("Portal opened")

    # ── TASK 2: Connect wallet ──
    # Try to auto-click, then pause for manual MetaMask approval.
    step("Connecting wallet...")
    try:
        page.locator("text=Connect Wallet").first.click()
        time.sleep(1)
        page.locator("text=MetaMask").first.click()
        time.sleep(1)
    except Exception as e:
        print(f"  Auto-click failed: {e}")

    wait_for_user(
        "In Chrome / MetaMask:\n"
        "  1. Switch to the correct wallet\n"
        "  2. Click Connect in the MetaMask popup\n"
        "  3. Come back here and press ENTER"
    )

    # ── TASK 3: Example — fill a profile form ──
    # Use wait_for_user() for any form the user needs to fill manually.
    step("Profile setup check...")
    wait_for_user(
        "Check the browser:\n"
        "  - If you see a profile setup form:\n"
        "    1. Fill in your display name\n"
        "    2. Fill in your email\n"
        "    3. Click Save\n"
        "    4. Come back here and press ENTER\n"
        "  - If no form appears, just press ENTER to continue"
    )
    success("Profile step done")

    # ── TASK 4: Example — click a button that may already be done ──
    # Use click_if_visible() for tasks that might already be completed.
    step("Connecting GitHub...")
    if click_if_visible(page, "text=Connect GitHub"):
        wait_for_user(
            "In the GitHub popup:\n"
            "  1. Authorize the project\n"
            "  2. Come back here and press ENTER"
        )
        success("GitHub connected")
    else:
        print("  GitHub may already be connected")

    # ── TASK 5: Example — MetaMask network approval ──
    # Always use wait_for_user() for MetaMask approvals.
    step("Adding project network...")
    if click_if_visible(page, "text=Add Network"):
        wait_for_user(
            "In MetaMask:\n"
            "  1. Approve adding the network\n"
            "  2. Come back here and press ENTER"
        )
        success("Network added")
    else:
        print("  Network may already be added")

    # ── TASK 6: Example — faucet / token claim ──
    step("Claiming tokens...")
    if click_if_visible(page, "text=Get Tokens"):
        wait_for_user(
            "On the faucet page:\n"
            "  1. Complete the token claim\n"
            "  2. Come back here and press ENTER"
        )
        success("Tokens claimed")
    else:
        print("  Tokens may already be claimed")

    # ── ADD MORE TASKS HERE ──
    # Copy the pattern above for each additional task.
    # Always use:
    #   step()           to label the task
    #   click_if_visible() for buttons that might be done already
    #   wait_for_user()  whenever MetaMask or manual input is needed
    #   success()        to confirm completion

    # ── FINAL STEP: Close the tab ──
    wait_for_user("Press ENTER to finish this wallet and close the tab")
    page.close()
    print(f"\nWallet {wallet['address'][:10]}... DONE!")


# ─────────────────────────────────────────────
#  Entry point
#  Do not modify this section.
# ─────────────────────────────────────────────

def main():
    print("""
WaterkoofAI x [PROJECT NAME] Airdrop Script Kit v1.0
t.me/WaterkoofAI_Bot
--------------------------------------------------
This script NEVER collects private keys
Use at your own risk - For educational purposes only
--------------------------------------------------
    """)

    config  = load_config()
    wallets = config.get("wallets", [])

    if not wallets:
        print("ERROR: No wallets found in STEP2_Fill_your_wallet_info.json.")
        sys.exit(1)

    wallets = [w for w in wallets if not w["address"].startswith("0xYour")]
    if not wallets:
        print("ERROR: Please replace the placeholder wallet addresses in STEP2_Fill_your_wallet_info.json.")
        sys.exit(1)

    print(f"Found {len(wallets)} wallet(s) in config")
    print(f"Referral code: {config.get('referral_code', 'none')}")

    chrome_cmd = get_chrome_debug_command()

    print(f"""
{'='*60}
BEFORE YOU CONTINUE:
Make sure Chrome is already running with remote debugging.
Command to start Chrome (run in a separate terminal):

  {chrome_cmd}

If Chrome is already open and ready, just press ENTER.
{'='*60}
    """)
    input("Press ENTER when Chrome is open and ready...")

    with sync_playwright() as p:
        try:
            browser = p.chromium.connect_over_cdp("http://localhost:9222")
            context = browser.contexts[0]
            success("Connected to Chrome successfully")
        except Exception as e:
            print(f"\nERROR: Could not connect to Chrome.")
            print(f"Make sure Chrome is running with --remote-debugging-port=9222")
            print(f"Details: {e}")
            sys.exit(1)

        for i, wallet in enumerate(wallets):
            print(f"\n--- Wallet {i+1} of {len(wallets)} ---")
            run_wallet(wallet, config, context)
            if i < len(wallets) - 1:
                input("\nPress ENTER to continue to the next wallet...")

    print("""
--------------------------------------------------
All wallets processed!
Follow @WaterkoofAI_Bot for more airdrop scripts
--------------------------------------------------
    """)


if __name__ == "__main__":
    main()
