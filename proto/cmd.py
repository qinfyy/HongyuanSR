import json

with open("CmdId.json", "r", encoding="utf-8") as f:
    COMMAND_NAME_TO_ID = json.load(f)

COMMAND_ID_TO_NAME = {v: k for k, v in COMMAND_NAME_TO_ID.items()}


class CmdRegistry:
    @staticmethod
    def get_id(name: str) -> int:
        if cmd_id := COMMAND_NAME_TO_ID.get(name):
            return cmd_id
        raise ValueError(f"invalid cmd name: {name}")

    @staticmethod
    def get_name(cmd_id: int) -> str:
        if name := COMMAND_ID_TO_NAME.get(cmd_id):
            return name
        raise ValueError(f"invalid cmd id: {cmd_id}")
