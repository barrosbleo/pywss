from websockets.sync.client import connect

def hello():
    with connect("ws://localhost:8765") as websocket:
        websocket.send("Hello, world!")
        print(f"Sent message: Hello, world!")
        response = websocket.recv()
        print(f"Received response: {response}")

hello()