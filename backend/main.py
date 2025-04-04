from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware
from typing import Dict

app = FastAPI()

# CORS setup so frontend can communicate
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Use specific domain if deploying securely
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Only two users allowed
valid_users = ["Aryan$8980", "Parth8012"]

# Connected clients
clients: Dict[str, WebSocket] = {}

@app.get("/")
def root():
    return {"message": "Server is running"}

@app.websocket("/ws/{username}")
async def websocket_endpoint(websocket: WebSocket, username: str):
    if username not in valid_users:
        await websocket.close()
        return

    await websocket.accept()
    clients[username] = websocket
    try:
        while True:
            data = await websocket.receive_json()
            event = data.get("event")
            content = data.get("content")
            to_user = "Parth8012" if username == "Aryan$8980" else "Aryan$8980"

            if event == "message":
                if to_user in clients:
                    await clients[to_user].send_json({
                        "event": "message",
                        "from": username,
                        "content": content
                    })

            elif event == "typing":
                if to_user in clients:
                    await clients[to_user].send_json({
                        "event": "typing",
                        "from": username
                    })

    except WebSocketDisconnect:
        if username in clients:
            del clients[username]
