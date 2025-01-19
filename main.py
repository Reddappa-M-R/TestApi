from fastapi import FastAPI, HTTPException
from typing import Optional

app = FastAPI()

# Sample data (for demonstration purposes)
data = [
    {"id": 1, "name": "Item 1", "description": "This is the first item."},
    {"id": 2, "name": "Item 2", "description": "This is the second item."},
    {"id": 3, "name": "Item 3", "description": "This is the third item."},
]

# Root endpoint
@app.get("/")
def read_root():
    return {"message": "Welcome to the API!"}

# GET endpoint to retrieve all items or filter by id
@app.get("/items/")
def get_items(id: Optional[int] = None):
    if id is not None:
        item = next((item for item in data if item["id"] == id), None)
        if item is None:
            raise HTTPException(status_code=404, detail="Item not found")
        return item
    return data
