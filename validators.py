def validate_inputs(symbol, side, order_type, quantity,price):
    if not symbol:
        raise ValueError("Symbol is required")
    
    side = side.upper()
    order_type = order_type.upper()

    if not symbol.endswith("USDT"):
        raise ValueError("Invalid symbol format")

    if side not in {'BUY', 'SELL'}:
        raise ValueError("Invalid Side")
    
    if order_type not in {'MARKET', 'LIMIT'}:
        raise ValueError("Invalid Type")
    
    if quantity <= 0:
        raise ValueError("Enter a valid quantity")
    
    if order_type == 'LIMIT' and price is None:
        raise ValueError("Please enter required price")

    if price is not None and price <= 0:
        raise ValueError("Price should be greater than zero")
    