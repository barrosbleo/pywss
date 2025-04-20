import sys
from websockets.sync.client import connect

def hello(message):
    with connect("ws://localhost:8765") as websocket:
        websocket.send(message)
        print(f"Sent message: {message}")
        response = websocket.recv()
        print(f"Received response: {response}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        message = sys.argv[1]
    else:
        message = "Hello, world!"
    hello(message)