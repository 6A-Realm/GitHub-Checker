# Github Checker
Simply checks GitHub for any new releases and notifies on Discord using webhooks.

## Setup
1. Fork the respositiory
2. Create a `settings.json` file with the following structure:
   ```
   {

    "repositories": {
        "Author\repo-name": "random number",
        "olliz0r\sys-botbase": "random number"
    }
   }
    ```
3. On your fork, go to `Settings > Secrets > Actions > New repository secret` and add the following:
   ```
   1.
        Name: GIT_AUTH
        Value: <Your GitHub access token here>
   2.
        Name: WEBHOOK
        Value: <Your Discord webhook link here>
  ```
