# Github Checker
Simply checks GitHub for any new releases and notifies on Discord using webhooks.

## Installation
1. Install requirements using `pip install -r requirements.txt`
2. Create a `settings.json` file with the following structure:
   ```
   {
    "settings": {
        "GIT_AUTH": "",
        "WEBHOOK": ""
    },
    "repositories": {
        "Author\repo-name": "random number",
        "olliz0r\sys-botbase": "random number"
    }
   }
    ```
3. Click on the Microsoft Windows logo.
4. Search for `Task Scheduler`.
5. Click on `Create task` found on the right hand side.
6. Set a name and description.
7. Toggle `Run whether user is loged on or not`.
8. Click on the `Triggers` tab and click `New`.
9. Set a repeat task of your choosing and click `OK`.
10. Click on the `Actions` tab and click `New`.
11. Set action to `Start a program`.
12. Open a command prompt and locate python.exe using `where py` and paste into location.
13. Add `main.py` text to `Add arguments (optional)`.
14. Add the file path in `Start in (optional)`.
15. Click `OK` and enter password.
