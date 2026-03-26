# bot/logging_config.py
import logging

# Configure logging
logging.basicConfig(
    filename="trading.log",            
    level=logging.INFO,                 
    format="%(asctime)s - %(levelname)s - %(message)s"
    )


logger = logging.getLogger("trading_bot")