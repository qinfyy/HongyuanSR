import asyncio
from proto.cmd import CmdRegistry
from .handler import HANDLER_MAP, DUMMY_MAP
from .connection import Connection


async def handle_client(
    reader: asyncio.StreamReader, writer: asyncio.StreamWriter
) -> None:
    addr = writer.get_extra_info("peername")
    c = Connection(reader, writer)

    try:
        while True:
            try:
                pkt = await c.read_packet()
                cmd = pkt.cmd
            except EOFError:
                break

            try:
                cmd_name = CmdRegistry.get_name(cmd)
                print(f"got {cmd_name} ({cmd}) from {addr}\n")
            except ValueError:
                print(f"got UnregisteredCmd ({cmd}) from {addr}\n")
                continue

            if handler := HANDLER_MAP.get(cmd):
                await handler(c, pkt)
            elif rsp_cmd := DUMMY_MAP.get(cmd):
                await c.send_dummy(rsp_cmd)
            else:
                print(f"unhandled cmd: {cmd_name} ({cmd})\n")

    except Exception as e:
        print(f"err handling client {addr}: {e}\n")
    finally:
        await c.close()
        print(f"client {addr} disconnected.\n")
