import requests
import json
import re
import http.client
import urllib
import os

URL = "https://developer.woot.com/feed/All"
HEADERS = {
    "Accept": "application/json",
    "x-api-key": os.environ["WOOT_API_KEY"],  # Ensure you have set this environment variable
}

def main():
    response = requests.get(URL, headers=HEADERS)
    response.raise_for_status()
    data = response.json()

    #print(json.dumps(data, indent=2))

    # Search for regex "magic.*gathering" in the results
    pattern = re.compile(r"magic.*gathering", re.IGNORECASE)
    matches = []

    for item in data.get("Items", []):
        title = item.get("Title", "")
        if pattern.search(title):
            matches.append(item)

    if matches:
        print(f'Found {len(matches)} results matching regex "magic.*gathering":')
        send_pushover_notification()
        for match in matches:
            print(f"- {match.get('Title')} ({match.get('Url')})")
    else:
        print('No results found matching regex "magic.*gathering".')

def send_pushover_notification():

    strPushoverToken = os.environ["PUSHOVER_WOOT_TOKEN"]
    strPushoverUser = os.environ["PUSHOVER_USER"]
    strMessage = "Woot Match: Magic The Gathering"

    objConn = http.client.HTTPSConnection("api.pushover.net:443")
    objConn.request("POST", "/1/messages.json",
    urllib.parse.urlencode({
        "token": strPushoverToken,
        "user": strPushoverUser,
        "message": strMessage,
    }), { "Content-type": "application/x-www-form-urlencoded" })
    objConn.getresponse()

if __name__ == "__main__":
    main()