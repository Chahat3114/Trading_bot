from binance.client import Client

class BinanceClient:
    def __init__(self, api_key, api_secret, testnet=True):
        self.client = Client(api_key, api_secret)
        if testnet:
            self.client.FUTURES_URL = "https://testnet.binancefuture.com/fapi"

API_KEY = "my_api_key"
API_SECRET = "my_api_secret"
client = BinanceClient(API_KEY, API_SECRET).client
