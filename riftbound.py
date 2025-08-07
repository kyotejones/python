import os
import requests
from bs4 import BeautifulSoup
import http.client, urllib

strUrl = "https://www.gamenerdz.com/riftbound-league-of-legends-tcg-origins-booster-box-sealed-case-preorder"
strPushoverToken = os.environ["PUSHOVER_TOKEN"]
strPushoverUser = os.environ["PUSHOVER_USER"]
strMessage = "Riftbound is available for order"

def send_pushover_notification():
    objConn = http.client.HTTPSConnection("api.pushover.net:443")
    objConn.request("POST", "/1/messages.json",
    urllib.parse.urlencode({
        "token": strPushoverToken,
        "user": strPushoverUser,
        "message": strMessage,
    }), { "Content-type": "application/x-www-form-urlencoded" })
    objConn.getresponse()

response = requests.get(strUrl)
soup = BeautifulSoup(response.text, "html.parser")
availability = soup.find(string="Set Restock Notification")

print(availability)
# Possible outputs
# "Set Restock Notification"
# None

if availability == None:
    print("Product is available for order")
    send_pushover_notification()
    print("Pushover notification sent")
else:
    print("Produict is not available for order")