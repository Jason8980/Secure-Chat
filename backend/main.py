from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from starlette.responses import FileResponse
from typing import Dict

app = FastAPI()

# CORS setup so frontend can communicate
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace "*" with your frontend domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Serve static files from the React build folder
# This makes all files in frontend/build/static accessible via /static
app.mount("/static", StaticFiles(directory="frontend/build/static"), name="static")

# Update the root endpoint to serve the built React app's index.html
@app.get("/")
async def read_index():
    return FileResponse("frontend/build/index.html")

# Only two users allowed
valid_users = ["Aryan$8980", "Parth8012"]

# Connected clients dictionary
clients: Dict[str, WebSocket] = {}

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
            # Determine the other user
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
