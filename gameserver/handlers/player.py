import time
from proto import (
    PlayerGetTokenScRsp,
    PlayerHeartBeatCsReq,
    PlayerHeartBeatScRsp,
    PlayerLoginScRsp,
    PlayerBasicInfo,
    GetBasicInfoScRsp,
    PlayerSettingInfo,
    GetPlayerBoardDataScRsp,
    HeadFrameInfo,
    DisplayAvatarVec,
    HeadIconData,
)
from ..handler import handler
from ..connection import Connection
from ..packet import Packet


@handler
async def on_player_get_token(c: Connection, pkt: Packet) -> None:
    rsp = PlayerGetTokenScRsp(
        uid=333,
    )

    await c.send_packet(rsp)


@handler
async def on_player_heart_beat(c: Connection, pkt: Packet) -> None:
    t = int(time.time() * 1000)
    req = c.decode_packet(pkt, PlayerHeartBeatCsReq)
    rsp = PlayerHeartBeatScRsp(
        client_time_ms=req.client_time_ms,
        server_time_ms=t,
    )

    await c.send_packet(rsp)


@handler
async def on_player_login(c: Connection, pkt: Packet) -> None:
    t = int(time.time() * 1000)
    rsp = PlayerLoginScRsp(
        basic_info=PlayerBasicInfo(
            nickname="Araya",
            level=67,
            stamina=240,
            world_level=5,
        ),
        server_timestamp_ms=t,
        stamina=240,
    )

    await c.send_packet(rsp)


@handler
async def on_get_basic_info(c: Connection, pkt: Packet) -> None:
    rsp = GetBasicInfoScRsp(
        cur_day=1,
        player_setting_info=PlayerSettingInfo(),
        is_gender_set=True,
        gender=2,
    )

    await c.send_packet(rsp)


@handler
async def on_get_player_board_data(c: Connection, pkt: Packet) -> None:
    rsp = GetPlayerBoardDataScRsp(
        signature="三生縁分 三千世界 三世因果",
        current_head_icon_id=200143,
        unlocked_head_icon_list=[
            HeadIconData(id=200143),
            HeadIconData(id=200001),
        ],
        head_frame_info=HeadFrameInfo(
            head_frame_item_id=226004,
            head_frame_expire_time=int(time.time() * 1000) + 86400000,
        ),
        current_personal_card_id=253001,
        unlocked_personal_card_list=[253001],
        display_avatar_vec=DisplayAvatarVec(is_display=False),
    )

    await c.send_packet(rsp)
