import os
import requests
from bs4 import BeautifulSoup
import http.client, urllib
import syslog

# Price: 539.97 (08/14/2025)

strUrl = "https://www.gamenerdz.com/riftbound-league-of-legends-tcg-origins-booster-box-sealed-case-preorder"
#strUrl = "https://www.gamenerdz.com/magic-the-gathering-innistrad-crimson-vow-set-booster-box"
strPushoverToken = os.environ["PUSHOVER_TOKEN"]
strPushoverUser = os.environ["PUSHOVER_USER"]
strMessage = "Riftbound is available for order"

syslog.openlog(ident="riftbound", logoption=syslog.LOG_PID, facility=syslog.LOG_USER)

def log_info(message):
    syslog.syslog(syslog.LOG_INFO, message)

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

# print(availability)
# Possible outputs
# "Set Restock Notification"
# None

if availability == None:
    log_info("Product is available for order")
    send_pushover_notification()
    log_info("Pushover notification sent")
else:
    log_info("Produict is not available for order")