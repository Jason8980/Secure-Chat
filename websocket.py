from fastapi import WebSocket, WebSocketDisconnect
from fastapi import APIRouter

router = APIRouter()

@router.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    try:
        async for message in websocket.iter_text():
            await websocket.send_text(f"Message received: {message}")
    except WebSocketDisconnect:
        pass  # Prevents memory leaks by handling disconnections properly.
