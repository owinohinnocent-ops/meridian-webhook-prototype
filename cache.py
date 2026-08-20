import json

CACHE_FILE = "stock_cache.json"

def update_cache(stock):
    with open(CACHE_FILE, "w") as file:
        json.dump(stock, file)

def get_cached_stock():
    try:
        with open(CACHE_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}
