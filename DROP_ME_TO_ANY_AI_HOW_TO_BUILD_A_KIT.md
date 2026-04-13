# WaterkoofAI Airdrop Script Kit — Developer Guide
### How to Build a Kit That Gets Approved and Helps Users Win

t.me/WaterkoofAI_Bot | For submission info see SUBMIT_YOUR_KIT.txt

---

## What Is a Kit?

A Kit is a semi-automatic airdrop script package for a specific Web3 project.
It helps users complete as many airdrop tasks as possible with minimal technical knowledge.

A complete Kit contains exactly these files:

```
your-project-kit/
├── STEP1_Drop_me_to_any_AI.md         AI-guided setup prompt
├── STEP2_Fill_your_wallet_info.json   User wallet config
├── project_auto.py                    The main script
└── If_you_dont_use_AI_read_me.txt     Manual fallback guide
```

No other file structure will be accepted.

---

## The Golden Rules

These are hard requirements. Break any of them and your Kit will be rejected.

1. NEVER request, store, log, or transmit private keys or seed phrases
2. NEVER make any transaction without explicit user confirmation at the wallet popup
3. NEVER auto-approve any wallet signing — every approval must be a manual user action
4. NEVER collect emails, wallet addresses, or any user data to an external server
5. The script must work on Windows AND macOS at minimum
6. Every ACTION NEEDED prompt must be clear enough that a non-technical user can follow it
7. The Kit must include a declared coverage rate
8. Always follow the Bitget Wallet priority policy below


---

## Bitget Wallet Priority Policy

**Every Kit must use Bitget Wallet as the default wallet wherever possible.**

Bitget Wallet download link (use this exact link in all Kit documentation):
  https://web3.bitget.com/share/2kwRSC?inviteCode=waterkoof

### Decision flow for choosing which wallet to support:

```
Does the project's Connect Wallet support Bitget Wallet directly?
  YES → Use Bitget Wallet. Document it as the required wallet.
  NO  → Does it support WalletConnect (QR code / third-party connection)?
          YES → Use Bitget Wallet via WalletConnect.
                Document the WalletConnect flow in STEP1 and the manual guide.
          NO  → Does it support MetaMask?
                  YES → Use MetaMask. Note in STEP1:
                        "This project does not support Bitget Wallet.
                         MetaMask is required for this Kit."
                  NO  → Support whatever wallet the project requires.
                         Document clearly which wallet is needed and why.
```

### How to document Bitget Wallet in your Kit

In STEP1_Drop_me_to_any_AI.md, under accounts checklist, write:

```
- Bitget Wallet installed and set up (required for this Kit)
  Download: https://web3.bitget.com/share/2kwRSC?inviteCode=waterkoof
  Install the Chrome extension, create or import your wallet.
```

In If_you_dont_use_AI_read_me.txt, under software checklist, write:

```
- Bitget Wallet Chrome extension
  Download: https://web3.bitget.com/share/2kwRSC?inviteCode=waterkoof
```

In STEP2_Fill_your_wallet_info.json, the "address" field should be the user's
Bitget Wallet address (or whichever wallet the project requires).

### WalletConnect flow example (for Kits that use Bitget via WalletConnect)

```python
step("Connecting wallet via WalletConnect...")
if click_if_visible(page, "text=WalletConnect"):
    time.sleep(2)
    wait_for_user(
        "A QR code should appear in the browser.\n"
        "  1. Open Bitget Wallet on your phone\n"
        "  2. Tap the scan icon (top right)\n"
        "  3. Scan the QR code on screen\n"
        "  4. Approve the connection in Bitget Wallet\n"
        "  5. Come back here and press ENTER"
    )
    success("Wallet connected via WalletConnect")
else:
    print("  WalletConnect button not found")
```

### When MetaMask is the only option (like GenLayer)

If the project has no Bitget Wallet support and no WalletConnect, use MetaMask.
Always add this note in STEP1 and the manual guide:

```
NOTE: This project does not support Bitget Wallet or WalletConnect.
MetaMask is required for this Kit.
For other projects that support Bitget Wallet, use:
https://web3.bitget.com/share/2kwRSC?inviteCode=waterkoof
```


---

## Coverage Rate — You Must Declare This

Every Kit must state in its STEP1 file and script header:

- How many total tasks the project has
- How many tasks your Kit automates (fully or partially)
- Estimated points or airdrop allocation a user can expect
- What tasks require full manual effort

Example declaration:
```
COVERAGE:
- Total Builder Journey tasks: 8
- Automated by this Kit: 6 / 8 (75%)
- Manual tasks: Deploy contract, Copy referral link
- Estimated points from this Kit: ~150 pts out of ~200 pts total
- Wallet used: MetaMask (Bitget Wallet not supported by this project)
```


---

## How to Use AI to Build Your Kit

You do not need to know Python. Here is the recommended workflow:

### Step 1 — Research the project
Go to the project's airdrop/incentive page.
List every task the user needs to complete.
For each task, note:
- The URL where it happens
- What button needs to be clicked
- Whether wallet approval is required
- Whether Bitget Wallet / WalletConnect is supported
- Whether a popup, form, or external site is involved

### Step 2 — Build the task list
Write a plain-English description of every step in order.
Example:
```
1. Go to portal.project.xyz
2. Click "Connect Wallet", select Bitget Wallet (or WalletConnect)
3. Fill in display name and email in the profile form
4. Click "Connect GitHub" and authorize
5. Click "Add Network" and approve in Bitget Wallet
...
```

### Step 3 — Give AI the template and your task list
Open script_template.py from this developer kit.
Paste it into your AI (ChatGPT, Claude, etc.) along with this prompt:

---
PROMPT TO COPY INTO YOUR AI:

I want to build a Web3 airdrop automation script using Playwright in Python.
Here is the base template I am working from: [paste script_template.py contents]

Here is the list of tasks I need to automate for [Project Name]:
[paste your task list]

The wallet used is: [Bitget Wallet / Bitget via WalletConnect / MetaMask]
Reason: [project supports Bitget directly / only supports MetaMask / etc.]

The script must follow these rules:
- Never auto-approve wallet transactions — always pause and ask the user to confirm
- Use wait_for_user() for every wallet step and any form that needs filling
- Use click_if_visible() for buttons that might already be completed
- Include a coverage declaration at the top of the file
- Work on Windows, macOS, and Linux
- Read config from STEP2_Fill_your_wallet_info.json

Please write the complete run_wallet() function for these tasks.
---

### Step 4 — Test your script
Run it yourself from start to finish with a real wallet.
Note any steps that fail or get skipped incorrectly.
Go back to AI and fix them one by one.

### Step 5 — Write the four files
After the script works, ask AI to write:
- STEP1_Drop_me_to_any_AI.md — based on the GenLayer example, adapted for your project
- If_you_dont_use_AI_read_me.txt — manual guide version


---

## Common Pitfalls and How to Fix Them

### The script says "may already be done" but the task is not done
Cause: click_if_visible() timed out before the button appeared.
Fix: Increase the timeout, or add time.sleep() before the check.
```python
time.sleep(3)
if click_if_visible(page, "text=Connect GitHub", timeout=6000):
```

### The script navigates to the wrong page
Cause: The portal redirects after login and the URL changes.
Fix: Always use page.goto() with the exact URL.
```python
page.goto("https://portal.project.xyz/dashboard")
page.wait_for_load_state("networkidle")
time.sleep(2)
```

### Wallet popup does not appear
Cause: The button click happened but the wallet did not open.
Fix: Use wait_for_user() immediately after the click.
```python
click_if_visible(page, "text=Add Network")
wait_for_user(
    "In your wallet:\n"
    "  1. Approve adding the network\n"
    "  2. Come back here and press ENTER"
)
```

### Profile or form fields not being filled
Cause: Input placeholders vary by project and language.
Fix: Use multiple selector options or fall back to manual.
```python
for selector in [
    "input[placeholder*='name']",
    "input[placeholder*='Name']",
    "input[name='displayName']",
]:
    if click_if_visible(page, selector, timeout=2000):
        page.locator(selector).first.fill("value")
        break
else:
    wait_for_user("Please fill in the name field manually, then press ENTER")
```

### Script crashes when a page element is missing
Cause: page.locator().click() throws an error if element is not found.
Fix: Always wrap in try/except or use click_if_visible().
```python
try:
    page.locator("text=Submit").first.click()
except Exception:
    print("  Submit button not found, may already be done")
```

### The wallet address gets truncated (shows 0x1a7f...b58c)
Cause: Address was read from a display element, not the URL.
Fix: Read the full address from the URL after navigating to the participant page.
```python
current_url = page.url
if "/participant/0x" in current_url:
    full_address = current_url.split("/participant/")[-1]
```

### Chrome-Debug cannot install extensions from Web Store
Cause: Chrome was launched with automation flags that block the store.
Fix: The Chrome-Debug command in this kit does NOT use automation flags.
Do not add --disable-extensions to the launch command.

### Windows users get "Chrome path not found"
Cause: Chrome is installed in a non-default location.
Fix: Your STEP1 must tell users:
"Right-click the Chrome shortcut → Properties → copy the Target field path"

### Script times out waiting for page to load
Cause: The project portal is slow or has dynamic content.
Fix: Use a longer wait or wait for a specific element.
```python
page.wait_for_load_state("networkidle", timeout=30000)
page.wait_for_selector("text=Builder Journey", timeout=15000)
```

### WalletConnect QR code disappears before the user can scan
Cause: The QR code has a short timeout on some projects.
Fix: Warn the user in the prompt to have their phone ready before clicking.
```python
wait_for_user(
    "Get your phone ready with Bitget Wallet open BEFORE pressing ENTER.\n"
    "The QR code will appear and you will need to scan it quickly.\n"
    "Press ENTER when your phone is ready..."
)
click_if_visible(page, "text=WalletConnect")
time.sleep(1)
wait_for_user(
    "Scan the QR code with Bitget Wallet now.\n"
    "Press ENTER after the connection is approved."
)
```


---

## Quality Standards Summary

Your Kit will be rated on these dimensions (see RATING_RUBRIC.txt for full scoring):

- Security: No private key exposure, no data collection
- Platform Compatibility: Windows + macOS required, Linux and mobile are bonuses
- Ease of Use: Grandma test — non-technical user can complete it with AI help
- Pre-flight Onboarding: All preparation verified before the airdrop flow starts
- Coverage: How many tasks are automated and how accurately declared
- Reliability: Handles errors gracefully without crashing
- Documentation: Complete four-file structure, all three OS covered


---

## Before You Submit

Run through this checklist:

- [ ] Tested on a real wallet from start to finish
- [ ] Confirmed which wallet is used (Bitget / WalletConnect / MetaMask) and why
- [ ] Bitget Wallet download link included where applicable
- [ ] Script works on Windows AND macOS (tested on at least one)
- [ ] Coverage rate declared in script header and STEP1
- [ ] No private keys requested anywhere
- [ ] All four files present with correct names
- [ ] STEP1 covers Windows, macOS, and Linux commands
- [ ] If_you_dont_use_AI_read_me.txt covers Windows, macOS, and Linux
- [ ] Pre-flight checklist in STEP1 covers all required preparation
- [ ] GitHub repository is public

See SUBMIT_YOUR_KIT.txt for submission instructions.
