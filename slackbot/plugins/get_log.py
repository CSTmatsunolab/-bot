import requests

url = "https://slack.com/api/conversations.history"
token = "xoxb-234972346128-2826231709184-R6ZbOmiAacv3oSLpE45DM0ak"

header={
    "Authorization": "Bearer {}".format(token)
}

payload  = {
    "channel" : "C02N0T4SG2K",
    "limit" : "1",
    "ts" : "latest",
    "inclusive" : True
    }

res = requests.get(url, heade
rs=header, params=payload)

print(res.json())
print(res)