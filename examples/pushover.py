import http.client, urllib

# Pushover API URL: https://api.pushover.net/1/messages.json
# token - your application's API token (required)
# user - your user/group key (or that of your target user), viewable when logged into our dashboard; often referred to as USER_KEY in our documentation and code examples (required)
# message - your message (required)

# Def ine your Pushover API token and user key
strPushoverToken = ""
strPushoverUser = ""
strMessage = "Testing Pushover notification from Python script"

# function to send Pushover notification
def send_pushover_notification():
    objConn = http.client.HTTPSConnection("api.pushover.net:443")
    objConn.request("POST", "/1/messages.json",
    urllib.parse.urlencode({
        "token": strPushoverToken,
        "user": strPushoverUser,
        "message": strMessage,
    }), { "Content-type": "application/x-www-form-urlencoded" })
    objConn.getresponse()

# call the function to send the notification
send_pushover_notification()