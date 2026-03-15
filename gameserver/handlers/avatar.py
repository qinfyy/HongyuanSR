import time
from proto import (
    GetAvatarDataScRsp,
    Avatar,
    AvatarPathData,
    AvatarPathSkillTree,
)
from ..handler import handler
from ..connection import Connection
from ..packet import Packet


@handler
async def on_get_avatar_data(c: Connection, pkt: Packet) -> None:
    t = int(time.time() * 1000)
    rsp = GetAvatarDataScRsp(
        is_get_all=True,
        avatar_list=[
            Avatar(
                first_met_time_stamp=t,
                level=80,
                promotion=6,
                base_avatar_id=8001,
                cur_multi_path_avatar_type=8002,
            )
        ],
        basic_type_id_list=[8001],
        avatar_path_data_info_list=[
            AvatarPathData(
                unlock_timestamp=t,
                avatar_id=8002,
                rank=6,
                avatar_path_skill_tree=[
                    AvatarPathSkillTree(
                        multi_point_id=i,
                        level=1,
                    )
                    for i in range(1, 10)
                ],
                unk_enhanced_id=0,
            )
        ],
    )

    await c.send_packet(rsp)
