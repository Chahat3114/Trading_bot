from orders import place_order
from validators import validate_inputs
import argparse
parser = argparse.ArgumentParser()

parser.add_argument("--side", type=str, required = True)
parser.add_argument("--symbol", type=str, required = True)
parser.add_argument("--order_type", type=str, required = True)
parser.add_argument("--quantity", type=float, required = True)
parser.add_argument("--price", type=float)

args = parser.parse_args()

try:
    validate_inputs(args.symbol, args.side, args.order_type, args.quantity, args.price)
except ValueError as e:
    print(e)
    exit()

place_order(args.side, args.symbol, args.order_type, args.quantity, args.price)