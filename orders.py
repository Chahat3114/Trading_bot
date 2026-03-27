from client import client
from logging_config import logger

def place_order(side, symbol, order_type, quantity, price=None):
    side = side.upper()
    order_type = order_type.upper()

    try:
        client.futures_change_leverage(symbol=symbol, leverage=10)
        logger.info(f"Leverage set to 10x for {symbol}")

        try:
            client.futures_change_margin_type(symbol=symbol, marginType='ISOLATED')
            logger.info(f"Margin type changed to ISOLATED for {symbol}")

        except Exception as e:
            pass   

        if order_type == "MARKET":
            order = client.futures_create_order(
                symbol=symbol,
                side=side,
                type='MARKET',
                quantity=quantity
            )

        elif order_type == "LIMIT":
            order = client.futures_create_order(
                symbol = symbol,
                side = side,
                type ='LIMIT',
                quantity=quantity,
                price = price,
                timeInForce='GTC'
            )

        else:
            raise ValueError("unsupported Order Type")
        
        print("Order placed successfully!")
        print("Order ID:", order.get("orderId"))
        print("Status:", order.get("status"))
        print("Executed Qty:", order.get("executedQty"))
        print("Avg Price:", order.get("avgPrice", "N/A"))

    except Exception as e:
        print("Order failed:", e)


