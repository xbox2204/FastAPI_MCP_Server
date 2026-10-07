from fastapi import FastAPI
from fastapi_mcp import FastApiMCP
from pydantic import BaseModel

app = FastAPI(title="My REST API & MCP Server")

# 1. Define your standard FastAPI REST endpoints
class Product(BaseModel):
    name: str
    price: float

@app.get("/products/{product_id}")
async def get_product(product_id: int):
    """Fetch product details by ID."""
    return {"product_id": product_id, "name": "Premium Widget", "price": 49.99}

@app.post("/products")
async def create_product(product: Product):
    """Create a new product."""
    return {"status": "success", "data": product}

# 2. Initialize and mount the MCP adapter to the app
mcp = FastApiMCP(app)
mcp.mount()  # This exposes the MCP server at /mcp

if __name__ == "__main__":
    import uvicorn
    # Run the combined app
    uvicorn.run(app, host="127.0.0.1", port=8000)