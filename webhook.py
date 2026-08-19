from fastapi import FastAPI
from pydantic import BaseModel

class StockUpdate(BaseModel):
    product_id: str
    quantity: int

app = FastAPI()

@app.post("/webhook")
def receive_stock_update(stock: StockUpdate):
    print(stock)
    return {
        "message": "Stock update received",
        "product_id": stock.product_id,
        "quantity": stock.quantity
    }