import time
import requests
import re
import http.client
import urllib
import os
import json

str_woot_api_key = os.environ["WOOT_API_KEY"]
str_pushover_token = os.environ["PUSHOVER_WOOT_TOKEN"]
str_pushover_user = os.environ["PUSHOVER_USER"]

URL = "https://developer.woot.com/feed/All"
HEADERS = {
    "Accept": "application/json",
    "x-api-key": str_woot_api_key,  # Ensure you have set this environment variable
}

def main():
    response = requests.get(URL, headers=HEADERS)
    response.raise_for_status()
    data = response.json()

    # Troubleshooting
    #print(json.dumps(data, indent=2))

    # Search for regex "magic.*gathering" in the results
    pattern = re.compile(r"magic.*gathering", re.IGNORECASE)
    matches = []
    str_message = ""

    for item in data.get("Items", []):
        title = item.get("Title", "")
        if pattern.search(title):
            matches.append(item)

    if matches:
        print(f'Found {len(matches)} results matching regex "magic.*gathering":')
        for match in matches:
            print(f"- {match.get('Title')} ({match.get('Url')})")
            str_message += f"- {match.get('Title')} ({match.get('Url')})\n"
        send_pushover_notification(str_message)

        # store data in a file under /tmp/
        with open(f"/tmp/woot_results_{int(time.time())}.json", "w") as f:
            json.dump(data, f)
    else:
        print('No results found matching regex "magic.*gathering".')

def send_pushover_notification(str_message):

    objConn = http.client.HTTPSConnection("api.pushover.net:443")
    objConn.request("POST", "/1/messages.json",
    urllib.parse.urlencode({
        "token": str_pushover_token,
        "user": str_pushover_user,
        "message": str_message,
    }), { "Content-type": "application/x-www-form-urlencoded" })
    objConn.getresponse()

if __name__ == "__main__":
    main()