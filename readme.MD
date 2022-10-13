# Github Checker
Simply checks GitHub for any new releases and notifies on Discord using webhooks.

## Installation
1. Install requirements using `pip install -r requirements.txt`
2. Create a `.env` file with the following key-value pairs:
   ```
    GIT_AUTH = "ghp auth code here"
    WEBHOOK = "discord webhook here"
    ```
3. Run the `main.py` file.
