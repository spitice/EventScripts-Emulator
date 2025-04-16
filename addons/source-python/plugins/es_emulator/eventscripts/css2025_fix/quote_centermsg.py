
from typing import List

def quote_args(args: List[str]):
    args_str = " ".join(args)

    # Checks if already quoted
    if args[0].startswith("\"") and args[-1].endswith("\""):
        return args_str

    return f"\"{args_str}\""

def quote_centermsg(command_str: str):
    args = command_str.split(" ")
    pre_commands = []
    centermsg_args = None

    # es.server.cmd("es_centermsg foo bar")
    if args[0] == "es_centermsg" and len(args) >= 2:
        centermsg_args = args[1:]

    # es.server.cmd("es_delayed 43 es_centermsg foo bar")
    elif args[0] == "es_delayed" and args[2] == "es_centermsg" and len(args) >= 4:
        pre_commands = args[0:2]
        centermsg_args = args[3:]

    if centermsg_args == None:
        # Not found valid es_centermsg command
        return command_str

    quoted_msg = quote_args(centermsg_args)

    return " ".join([*pre_commands, "es_centermsg", quoted_msg])
