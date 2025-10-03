from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None
    price_with_tax: Optional[float] = None


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello, FastAPI World"}

@app.get("/items/{item_id}")
async def read_item(item_id: int) -> dict[str, int]:
    return {"item_id": item_id}


@app.post("/items")
async def create_item(item: Item):
    updated_item = None
    if item.tax:
        price_with_tax = item.price * (1 + (item.tax / 100.))
        update_data = {"price_with_tax": price_with_tax}
        item_dict = item.model_dump()
        item_dict.update(update_data)
        updated_item = Item(**item_dict)
    print(updated_item if updated_item else item)
    return updated_item if updated_item else item
