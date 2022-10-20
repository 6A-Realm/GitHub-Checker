
from github import Github
from json import load, dumps
from requests import post
from time import sleep


# Opening JSON file and return as dictionary
with open("settings.json") as f:
    initial = load(f)

    # Access GitHub API using access token
    git = Github(initial["settings"]["GIT_AUTH"])
    f.close


def search():
    f2 = open("settings.json")
    data = load(f2)

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
            post(data["settings"]["WEBHOOK"], json = discord)


    # Write to file
    with open("settings.json", "w") as outfile:
        outfile.write(dumps(data, indent = 4, default = str))

# Start code
if __name__ == "__main__":
    while True:
        search()

        # Loop every 30 mins
        sleep(5)
