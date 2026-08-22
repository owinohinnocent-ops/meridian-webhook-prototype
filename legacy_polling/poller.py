import time

from warehouse import get_stock
from cache import update_cache

while True:
    stock = get_stock()
    update_cache(stock)
    print("Latest stock:", stock)
    time.sleep(10)  # Poll every 10 seconds