
from esc.monkeypatch import monkeypatch

from .player_game_text import fire_gametext
from .player_game_text import give_gametext

#
# game_text entity in css2025 seems to be broken so we are using our own implementation:
# Leveraging HudMsg from Source.Python to emulate game_text's behavior controlled via give/ent_fire.
#

@monkeypatch
def give(*args):
    if len(args) >= 2:
        target = args[1]
        if target == "game_text":
            give_gametext(args[0])
            return

    give(*args)

@monkeypatch
def fire(*args):
    if len(args) >= 3:
        target = args[1]
        if target == "game_text":
            fire_gametext(args[0], *args[2:])
            return
    fire(*args)

print("Eventscripts css2025_fix patch has been loaded")
