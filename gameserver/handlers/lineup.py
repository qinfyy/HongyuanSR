from proto import (
    ChangeLineupLeaderCsReq,
    ChangeLineupLeaderScRsp,
    GetAllLineupDataScRsp,
    GetCurLineupDataScRsp,
    LineupInfo,
    LineupAvatar,
    ExtraLineupType,
    SpBarInfo,
    AvatarType,
)
from ..handler import handler
from ..connection import Connection
from ..packet import Packet


@handler
async def on_change_lineup_leader(c: Connection, pkt: Packet) -> None:
    req = c.decode_packet(pkt, ChangeLineupLeaderCsReq)
    rsp = ChangeLineupLeaderScRsp(slot=req.slot)

    await c.send_packet(rsp)


@handler
async def on_get_all_lineup_data(c: Connection, pkt: Packet) -> None:
    rsp = GetAllLineupDataScRsp(
        cur_index=0,
        lineup_list=[
            LineupInfo(
                is_virtual=False,
                plane_id=20313,
                name="Yoshihide",
                mp=0,
                max_mp=5,
                index=0,
                extra_lineup_type=ExtraLineupType.LINEUP_NONE,
                avatar_list=[
                    LineupAvatar(
                        hp=10000,
                        id=8001,
                        slot=0,
                        sp_bar=SpBarInfo(
                            max_sp=10000,
                        ),
                        avatar_type=AvatarType.AVATAR_FORMAL_TYPE,
                    )
                ],
                leader_slot=0,
            )
        ],
    )

    await c.send_packet(rsp)


@handler
async def on_get_cur_lineup_data(c: Connection, pkt: Packet) -> None:
    rsp = GetCurLineupDataScRsp(
        lineup=LineupInfo(
            is_virtual=False,
            plane_id=20313,
            name="Yoshihide",
            mp=0,
            max_mp=5,
            index=0,
            extra_lineup_type=ExtraLineupType.LINEUP_NONE,
            avatar_list=[
                LineupAvatar(
                    hp=10000,
                    id=8001,
                    slot=0,
                    sp_bar=SpBarInfo(
                        max_sp=10000,
                    ),
                    avatar_type=AvatarType.AVATAR_FORMAL_TYPE,
                )
            ],
            leader_slot=0,
        )
    )

    await c.send_packet(rsp)
