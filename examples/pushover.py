import requests

# Pushover API URL: https://api.pushover.net/1/messages.json
# token - your application's API token (required)
# user - your user/group key (or that of your target user), viewable when logged into our dashboard; often referred to as USER_KEY in our documentation and code examples (required)
# message - your message (required)

# Def ine your Pushover API token and user key
strPushoverToken = ""
strPushoverUser = ""
strMessage = "Testing Pushover notification from Python script"

# Python script to send a Pushover notification
def send_pushover_notification(token, user, message):
    url = "https://api.pushover.net/1/messages.json"
    data = {
        "token": token,
        "user": user,
        "message": message
    }
    response = requests.post(url, data=data)
    return response.json()

send_pushover_notification(strPushoverToken, strPushoverUser, strMessage)