
from colors import Color
import gamethread
from messages import HudMsg
from players.helpers import index_from_userid

import es
from esc.monkeypatch import monkeypatch

#
# game_text entity in css2025 seems to be broken so we are using our own implementation:
# Leveraging HudMsg from Source.Python to emulate game_text's behavior controlled via give/ent_fire.
#

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
    global player_gametext_map

    gametext = PlayerGameText(userid)
    player_gametext_map[userid] = gametext

def fire_gametext(userid, inputName: str, params: str = ""):
    global player_gametext_map

    userid = str(userid)

    gametext = None
    if userid in player_gametext_map:
        gametext = player_gametext_map[userid]
    #else:
    if gametext is None:
        gametext = give_gametext(userid)

    inputName = inputName.lower()
    match inputName:
        case "addoutput":
            apply_addoutput_to_hudmsg(gametext.hudmsg, params)
        case "display":
            #
            # Fix hud message in the first round of beachvolley not showing
            # since round_start (calls Display) would be called before player_spawn.
            # Just add a small delay to send hudmsg to mitigate this issue.
            # However, you cannot send hudmsg via `fire` to different channels at the same tick.
            # In this case, don't rely on `fire` and create HudMsg by your own.
            #
            # gametext.hudmsg.send(gametext.player_index)
            gamethread.queue(gametext.hudmsg.send, gametext.player_index)
        case "kill":
            player_gametext_map.pop(userid)
        case "_":
            print(f"[fire_gametext] Invalid input name: {inputName}")

def apply():
    @monkeypatch
    def give(*args):
        if len(args) >= 2:
            target = args[1]
            if target == "game_text":
                es.dbgmsg(2, f"[css2025_win32] give_gametext")
                give_gametext(args[0])
                return
        give(*args)

    @monkeypatch
    def fire(*args):
        if len(args) >= 3:
            target = args[1]
            if target == "game_text":
                es.dbgmsg(2, f"[css2025_win32] fire_gametext {args[2]}")
                fire_gametext(args[0], *args[2:])
                return
        fire(*args)
