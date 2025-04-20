import sys
import asyncio
from websockets.asyncio.server import serve

async def echo(websocket):
    async for message in websocket:
        print(f"Received message: {message}")
        if message == "generate_ws_key":
            print("Generate the websocket key")
            await websocket.send("Key generated")
            print("Closing the connection")
            await websocket.close()

            sys.exit()
            break
        await websocket.send(f"Echo: {message}")

async def main():
    async with serve(echo, "localhost", 8765) as server:
        print("WebSocket server started on ws://localhost:8765")
        await server.serve_forever()

if __name__ == "__main__":
    asyncio.run(main())