
import requests

url = "https://slack.com/api/chat.getPermalink"
token = "xoxb-234972346128-2826231709184-R6ZbOmiAacv3oSLpE45DM0ak"

header={
    "Authorization": "Bearer {}".format(token)
}

payload  = {
    "channel" : "C02N0T4SG2K",
    "message_ts" : "latest",
    }

res = requests.get(url, headers=header, params=payload)

print(res.json())