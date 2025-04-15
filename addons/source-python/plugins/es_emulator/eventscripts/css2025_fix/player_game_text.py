
from colors import Color
from messages import HudMsg
from players.helpers import index_from_userid

__all__ = [
    "give_gametext",
    "fire_gametext",
]

def apply_addoutput_to_hudmsg(hudMsg, params: str):
    args = params.split(" ")
    attr = args[0].lower()

    match attr:
        case "message":
            hudMsg.message = params[len("message "):]
        case "x":
            hudMsg.x = float(args[1])
        case "y":
            hudMsg.y = float(args[1])
        case "color":
            # Convers "255 255 255" to Color(int("255"), int("255"), int("255"))
            hudMsg.color1 = Color(*[int(v) for v in args[1:4]])
        case "color2":
            hudMsg.color2 = Color(*[int(v) for v in args[1:4]])
        case "effect":
            hudMsg.effect = int(args[1])
        case "fadein":
            hudMsg.fade_in = float(args[1])
        case "fadeout":
            hudMsg.fade_out = float(args[1])
        case "holdtime":
            hudMsg.hold_time = float(args[1])
        case "fxtime":
            hudMsg.fx_time = float(args[1])
        case "channel":
            hudMsg.channel = int(args[1])
        case _:
            print(f"[apply_addoutput_to_hudmsg] Invalid command: {params}")

class PlayerGameText:
    def __init__(self, userid):
        self.player_index = index_from_userid(int(userid))
        self.hudmsg = HudMsg(message="")

player_gametext_map = {}

def give_gametext(userid):
    gametext = PlayerGameText(userid)
    player_gametext_map[userid] = gametext

def fire_gametext(userid, inputName: str, params: str = ""):
    userid = str(userid)

    gametext = None
    if userid in player_gametext_map:
        gametext = player_gametext_map[userid]
    else:
        gametext = give_gametext(userid)

    inputName = inputName.lower()
    match inputName:
        case "addoutput":
            apply_addoutput_to_hudmsg(gametext.hudmsg, params)
        case "display":
            gametext.hudmsg.send(gametext.player_index)
        case "kill":
            player_gametext_map.pop(userid)
        case "_":
            print(f"[fire_gametext] Invalid input name: {inputName}")
