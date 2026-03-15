import asyncio
from betterproto2 import Message
from proto.cmd import CmdRegistry
from .packet import Packet


class Connection:
    __slots__ = ("reader", "writer")

    def __init__(
        self,
        reader: asyncio.StreamReader,
        writer: asyncio.StreamWriter,
    ):
        self.reader = reader
        self.writer = writer

    async def read_packet(self) -> Packet:
        return await Packet.read_from(self.reader)

    def decode_packet(self, pkt: Packet, msg: Message) -> Message:
        return msg.parse(pkt.body)

    def _encode_packet(self, msg: Message) -> bytes:
        msg_name = msg.__class__.__name__
        cmd = CmdRegistry.get_id(msg_name)
        pkt = Packet(cmd=cmd, body=bytes(msg))
        return bytes(pkt)

    async def _send(self, buf: bytes) -> None:
        self.writer.write(buf)
        await self.writer.drain()

    async def send_packet(self, msg: Message) -> None:
        buf = self._encode_packet(msg)
        await self._send(buf)

    async def send_dummy(self, cmd: int) -> None:
        buf = bytes(Packet(cmd=cmd))
        await self._send(buf)

    async def close(self) -> None:
        self.writer.close()
        await self.writer.wait_closed()
