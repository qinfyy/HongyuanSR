import json
import re

if __name__ == "__main__":
    with open("unclean.proto", "r", encoding="utf-8") as f:
        content = f.read()

    cmd_id_pattern = re.compile(r"//\s*CmdID:\s*(\d+)")
    msg_name_pattern = re.compile(r"message\s+(\w+)\s*\{")

    results = {}

    lines = content.splitlines()
    last_cmd_id = None

    for line in lines:
        cmd_match = cmd_id_pattern.search(line)
        if cmd_match:
            last_cmd_id = int(cmd_match.group(1))
            continue

        msg_match = msg_name_pattern.search(line)
        if msg_match and last_cmd_id is not None:
            msg_name = msg_match.group(1)
            results[msg_name] = last_cmd_id
            last_cmd_id = None

    with open("CmdId.json", "w", encoding="utf-8") as f:
        json.dump(results, f, indent=4)
