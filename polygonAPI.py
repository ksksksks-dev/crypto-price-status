apiKey = 

base = "https://api.polygon.io"

def getDailyOpenCloseUri(_from, to, date):
    uri = "/v1/open-close/crypto/{0}/{1}/{2}".format(_from, to, date)
    return uri


print(base + getDailyOpenCloseUri("BTC", "USD", "2021-10-01"))
