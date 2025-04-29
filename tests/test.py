from main import *

class MockWebSocket:
        def __init__(self):
            self.messages = []

        async def send(self, message):
            self.messages.append(message)

        async def close(self):
            pass

        async def __aiter__(self):
            return self

        async def __anext__(self):
            if self.messages:
                return self.messages.pop(0)
            raise StopAsyncIteration

def test_echo():
    websocket = MockWebSocket()

    asyncio.run(echo(websocket))

    assert "Echo: test message" in websocket.messages

def test_generate_ws_key():
    websocket = MockWebSocket()

    asyncio.run(echo(websocket))

    assert "Key generated" in websocket.messages
    assert "Closing the connection" in websocket.messages