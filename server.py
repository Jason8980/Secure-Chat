import gc
import uvicorn
import logging
from fastapi import FastAPI
from pymongo import MongoClient

# Initialize FastAPI app
app = FastAPI()

# Optimize MongoDB connection (limit connection pool)
client = MongoClient("mongodb+srv://Megasaver:9nLFTisTq3uj53Il@cluster0.iqcva.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0", maxPoolSize=5)
db = client["your_database"]

# Reduce logging level to save memory
logging.basicConfig(level=logging.WARNING)

@app.get("/")
def read_root():
    return {"message": "Server is running"}

# Enable garbage collection to free up memory
@app.on_event("startup")
async def startup_event():
    gc.collect()

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, workers=1)
