import requests
import json

domain = "https://api.wazirx.com/"

tickerUri = "/api/v2/market-status"

url = domain + tickerUri

res = requests.get(url)

print(res.json()["markets"])
