import os
import requests
from bs4 import BeautifulSoup

url = "https://www.gamenerdz.com/riftbound-league-of-legends-tcg-origins-booster-box-sealed-case-preorder"
#url = "https://www.gamenerdz.com/magic-the-gathering-innistrad-crimson-vow-set-booster-box"
strPushoverToken = os.environ["PUSHOVER_TOKEN"]
strPushoverUser = os.environ["PUSHOVER_USER"]
strMessage = "Riftbound is available for order"

def send_pushover_notification(token, user, message):
    url = "https://api.pushover.net/1/messages.json"
    data = {
        "token": token,
        "user": user,
        "message": message
    }
    response = requests.post(url, data=data)
    return response.json()

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
availability = soup.find(string="Set Restock Notification")

print(availability)
# Possible outputs
# "Set Restock Notification"
# None

if availability == None:
    print("Product is available for order")
    send_pushover_notification(strPushoverToken, strPushoverUser, strMessage)
    print("Pushover notification sent")
else:
    print("Produict is not available for order")