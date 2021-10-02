import requests

apikey = ""
mockkey = "b54bcf4d-1bca-4e8e-9a24-22ff2c3d462c"

domain = "pro-api.coinmarketcap.com"
testDomain = "sandbox-api.coinmarketcap.com"

uri = "/v1/cryptocurrency/listings/latest"
params = {
    "start": "1",
    "limit": "5000",
    "convert": "USD",
}
headers = {
    "Accepts": "application/json",
    "X-CMC_PRO_API_KEY": mockkey,
}

url = "https://" + testDomain + uri

res = requests.get(
    url=url,
    params=params,
    headers=headers,
)

print(res.json())
