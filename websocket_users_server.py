import asyncio

import websockets
from websockets import ServerConnection


async def handle_connection(websocket: ServerConnection):
    async for message in websocket:
        print(f"Получено сообщение от пользователя: {message}")

        for number in range(1, 6):
            response = f"{number} Сообщение пользователя: {message}"
            await websocket.send(response)


async def main():
    server = await websockets.serve(handle_connection, "localhost", 8765)
    print("WebSocket сервер запущен на ws://localhost:8765")
    await server.wait_closed()


if __name__ == "__main__":
    asyncio.run(main())
