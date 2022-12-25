from os import environ
from github import Github
from json import load, dumps
from requests import post


# Load env variables
git_token = environ["GIT_AUTH"]
webhook = environ["WEBHOOK"]


# Connect to API
git = Github(git_token)

# Opening settings file
with open("settings.json") as f:
    data = load(f)

    for key in data["repositories"].copy():

        value = data["repositories"][key]
        # Fetch repository from GitHub
        try:
            repo = git.get_repo(key)
        except:
            print(f"{key} does not exist on GitHub and will be removed. Example name: 6A-Realm/GitHub-Checker")
            del data["repositories"][key]
            continue

        # Check latest release if any
        try:
            created = repo.get_latest_release().created_at
        except:
            print(f"{repo.full_name} does not have any releases and will be removed.")
            del data["repositories"][key]
            continue

        # Check if last tag name is most currently documented
        if str(created) != value:
            data["repositories"][key] = created

            # Get other data
            tag = repo.get_latest_release().tag_name
            about = repo.get_latest_release().body

            # Create a discord webhook
            discord = {
                "username": "GitHub Release Checker",
                "avatar_url": "https://media.discordapp.net/attachments/955988110892732467/1029981559199109130/unknown.png",
                "embeds": [{
                    "title": f"New release {tag} detected for {key}!",
                    "url": f"https://github.com/{key}/releases/latest",
                    "description": f"New release created on {created}.\n{about}",
                    "color": 0x00FF00
                }]
            }

            # Send to Discord
            post(webhook, json = discord)


# Write to file
with open("settings.json", "w") as outfile:
    outfile.write(dumps(data, indent = 4, default = str))
