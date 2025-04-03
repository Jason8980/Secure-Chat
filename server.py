from fastapi import FastAPI, WebSocket, UploadFile, File
from pymongo import MongoClient
from datetime import datetime, timedelta
import asyncio, os

app = FastAPI()

# Database Setup – Replace the connection string with your MongoDB URI if needed
client = MongoClient("mongodb+srv://Filetolink:Jason8980@cluster0.pdjsv.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client["secure_chat"]
messages_collection = db["messages"]
media_collection = db["media"]

# Define valid users with fixed login credentials and their logos
connected_users = {}
valid_users = {"Aryan$8980": "H7&", "Parth#8012": "X*M"}

@app.websocket("/chat/{username}")
async def chat_endpoint(websocket: WebSocket, username: str):
    # Allow only the two valid users
    if username not in valid_users:
        await websocket.close()
        return

    await websocket.accept()
    connected_users[username] = websocket

    try:
        while True:
            data = await websocket.receive_text()
            # Save the message permanently in the database
            message = {
                "sender": username,
                "message": data,
                "timestamp": datetime.utcnow()
            }
            messages_collection.insert_one(message)

            # Broadcast the message to the other user with custom logo
            for user, connection in connected_users.items():
                if user != username:
                    sender_logo = valid_users[username]
                    await connection.send_text(f"{sender_logo}: {data}")
    except:
        # Remove user on disconnect
        del connected_users[username]

@app.post("/upload_media")
async def upload_media(file: UploadFile = File(...)):
    file_location = f"media/{file.filename}"
    with open(file_location, "wb") as f:
        f.write(file.file.read())

    media_collection.insert_one({
        "filename": file.filename,
        "timestamp": datetime.utcnow()
    })

    return {"message": "Media uploaded successfully", "url": file_location}

@app.on_event("startup")
async def cleanup_media():
    while True:
        expired_time = datetime.utcnow() - timedelta(hours=5)
        media_collection.delete_many({"timestamp": {"$lt": expired_time}})
        await asyncio.sleep(3600)  # Check every hour
