
from entities.entity import Entity
from players.entity import Player

import es
from esc.monkeypatch import monkeypatch

def fire_strip(userid, command: str = "strip", removeSuit = 1):
    entPlayer = Player.from_userid(int(userid))
    entStrip = Entity.create("player_weaponstrip")
    entStrip.spawn()
    entStrip.strip(removeSuit, entPlayer, entPlayer)
    entStrip.remove()

def apply():
    @monkeypatch
    def give(*args):
        if len(args) >= 2:
            target = args[1]
            if target == "player_weaponstrip":
                es.dbgmsg(2, f"[css2025_win32] give_player_weaponstrip")
                # Just ignore es.give
                return
        give(*args)

    @monkeypatch
    def fire(*args):
        nArgs = len(args)
        if nArgs == 3 or nArgs == 4:
            target = args[1]
            if target == "player_weaponstrip":
                es.dbgmsg(2, f"[css2025_win32] fire strip on player")
                fire_strip(args[0], *args[2:])
                return
        fire(*args)
