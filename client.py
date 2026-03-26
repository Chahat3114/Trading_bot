from binance.client import Client

class BinanceClient:
    def __init__(self, api_key, api_secret, testnet=True):
        self.client = Client(api_key, api_secret)
        if testnet:
            self.client.FUTURES_URL = "https://testnet.binancefuture.com/fapi"

API_KEY = "G4nM5oEBFiey7fscTTZh7IOEE2yxAZeFhSWujJaYNoWMlXwaidwMuk6KTyZuMyeY"
API_SECRET = "lfFzPNugIzryX7Ftj2vML1VFGESqAt8Lp5gRYBIDyUzmp39DCca1D9QnHpL3Q1o6"
client = BinanceClient(API_KEY, API_SECRET).client
