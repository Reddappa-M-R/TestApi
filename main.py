from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost:3000",  # Your frontend's local development origin
    "https://salary-management-app-oflt.vercel.app/"  # Your production frontend domain
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Replace with specific domains if needed
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI app deployed on Vercel!"}

@app.get("/items/")
def get_items(id: int = None):
    data = [
        {"id": 1, "name": "Item 1", "description": "This is the first item."},
        {"id": 2, "name": "Item 2", "description": "This is the second item."},
        {"id": 3, "name": "Item 3", "description": "This is the third item."},
    ]
    if id is not None:
        item = next((item for item in data if item["id"] == id), None)
        if item is None:
            return {"detail": "Item not found"}
        return item
    return data

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=5000)
