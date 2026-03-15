from proto import (
    GetCurSceneInfoScRsp,
    SceneInfo,
    SceneEntityGroupInfo,
    SceneEntityInfo,
    SceneActorInfo,
    AvatarType,
    MotionInfo,
    Vector,
)
from ..handler import handler
from ..connection import Connection
from ..packet import Packet


@handler
async def on_get_cur_scene_info(c: Connection, pkt: Packet) -> None:
    rsp = GetCurSceneInfoScRsp(
        scene=SceneInfo(
            plane_id=20313,
            entry_id=2031301,
            floor_id=20313001,
            game_mode_type=1,
            leader_entity_id=sum(b"Shiomi Yoru") << 3,
            entity_group_list=[
                SceneEntityGroupInfo(
                    # state=1,
                    entity_list=[
                        SceneEntityInfo(
                            entity_id=sum(b"Shiomi Yoru") << 3,
                            actor=SceneActorInfo(
                                base_avatar_id=8001,
                                avatar_type=AvatarType.AVATAR_FORMAL_TYPE,
                                map_layer=2,
                                uid=333,
                            ),
                            motion=MotionInfo(
                                pos_index=Vector(
                                    x=40748,
                                    y=192819,
                                    z=439218,
                                ),
                                rot_index=Vector(),
                            ),
                        )
                    ],
                )
            ],
        )
    )

    await c.send_packet(rsp)
