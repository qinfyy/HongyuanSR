import asyncio
from config import GAMESERVER_ADDR
from .client import handle_client


async def start_server() -> None:
    host, port = GAMESERVER_ADDR
    server = await asyncio.start_server(handle_client, host, port)
    print(f"gameserver listening on {host}:{port}\n")

    async with server:
        await server.serve_forever()


if __name__ == "__main__":
    try:
        asyncio.run(start_server())
    except KeyboardInterrupt:
        pass
