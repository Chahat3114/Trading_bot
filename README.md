# Binance Futures Testnet Trading Bot

## Description
A simplified Python trading bot for Binance Futures Testnet (USDT-M).  
Supports placing MARKET and LIMIT orders via CLI with input validation, logging, and error handling.

---

## Setup

1. Clone the repository:

```bash
git clone <your-repo-url>
cd trading_bot
Install dependencies:
pip install -r requirements.txt
Set your Binance Testnet API keys in bot/client.py:
API_KEY = "YOUR_API_KEY"
API_SECRET = "YOUR_API_SECRET"

You can create a Binance Futures Testnet account and generate API credentials at: https://testnet.binancefuture.com/

How to Run
MARKET Order
python cli.py --symbol BTCUSDT --side BUY --order_type MARKET --quantity 0.01
LIMIT Order
python cli.py --symbol BTCUSDT --side SELL --order_type LIMIT --quantity 0.01 --price 78050

Note: For LIMIT orders, make sure the price is close to the current Testnet market price.

Logs

All API requests, responses, and errors are logged in trading.log.

Assumptions
The bot only supports USDT-M futures.
Leverage is set to 10x and margin type to ISOLATED by default.
User inputs are validated (symbol format, side, order type, quantity, price).
MARKET orders execute immediately; LIMIT orders execute when the market reaches the specified price.