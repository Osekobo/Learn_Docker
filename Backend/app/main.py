from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Marq Kicks API")

# remove cors on nginx setup
# CORS setup - allows your React app to talk to this backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Your React frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Root endpoint - just to check if the API is alive
@app.get("/")
def read_root():
    return {"message": "Welcome to the Marq Kicks API!"}

# Sample data - simulating a database
shoes_db = [
    {"id": 1, "name": "Air Max 90", "price": 12000, "size": "42"},
    {"id": 2, "name": "Jordan 1 Retro", "price": 15000, "size": "43"},
    {"id": 3, "name": "Yeezy Boost 350", "price": 18000, "size": "41"},
]

# Endpoint to get all shoes
@app.get("/api/shoes")
def get_shoes():
    return {"shoes": shoes_db}

# Endpoint to get a specific shoe by ID
@app.get("/api/shoes/{shoe_id}")
def get_shoe(shoe_id: int):
    shoe = next((s for s in shoes_db if s["id"] == shoe_id), None)
    if shoe:
        return shoe
    return {"error": "Shoe not found"}, 404