import asyncio
from websockets.asyncio.server import serve

async def echo(websocket, path):
    async for message in websocket:
        print(f"Received message: {message}")
        await websocket.send(f"Echo: {message}")

async def main():
    async with serve(echo, "localhost", 8765) as server:
        print("WebSocket server started on ws://localhost:8765")
        await server.serve_forever()

if __name__ == "__main__":
    asyncio.run(main())