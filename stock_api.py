from fastapi import FastAPI
from cache import get_cached_stock

app = FastAPI()

@app.get("/stock/{product_id}")
def get_stock(product_id: str):
    stock = get_cached_stock()

    if product_id not in stock:
        return {
            "message": "Product not found"
        }

    return {
        "product_id": product_id,
        "quantity": stock[product_id]
        }