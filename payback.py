# This is for educational usage only.
# If you get a message from a scammer pretending to be a bank,
# just adapt the url and data to the form on their website.

import requests
url = 'https://www.putTheUrlOfTheScammersRequestHere.com/'
data={
    "data": "value"
    }
def bullyScammer():   
    response = requests.post(url, data=data).text
    print(response)

while True:
    bullyScammer()