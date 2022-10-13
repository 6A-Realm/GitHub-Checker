from dotenv import load_dotenv
from os import getenv
from github import Github
from json import load, dumps
from requests import post
from time import sleep


# Load system variables
load_dotenv()
git_auth = getenv("GIT_AUTH")
webhook = getenv("WEBHOOK")

# Access GitHub API using access token
git = Github(git_auth)

# Opening JSON file and return as dictionary
with open("repositories.json") as f:
    data = load(f)

def search():
    for key, value in data.items():

        # Fetch repository from GitHub
        try:
            repo = git.get_repo(key)
        except:
            print(f"{key} does not exist on GitHub. Example name: 6A-Realm/GitHub-Checker")

        # Check latest release if any
        try:
            tag = repo.get_latest_release().tag_name
        except:
            print(f"No releases found for {repo.full_name}")
            continue

        # Check if last tag name is most currently documented
        if tag != value:
            data[key] = tag

            # Get other data
            published = repo.get_latest_release().published_at
            about = repo.get_latest_release().body

            # Create a discord webhook
            discord = {
                "username": "GitHub Release Checker",
                "avatar_url": "https://media.discordapp.net/attachments/955988110892732467/1029981559199109130/unknown.png",
                "embeds": [{
                    "title": f"New release {tag} detected for {key}!",
                    "url": f"https://github.com/{key}/releases/latest",
                    "description": f"New release {tag} published {published}.\n{about}",
                    "color": 0x00FF00
                }]
            }

            # Send to Discord
            post(webhook, json = discord)

    # Write to file
    with open("repositories.json", "w") as outfile:
        outfile.write(dumps(data, indent = 4))

# Start code
if __name__ == "__main__":
    while True:
        search()

        # Loop every 30 mins
        sleep(108000)
