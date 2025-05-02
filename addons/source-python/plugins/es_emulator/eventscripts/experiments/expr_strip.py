
from entities.entity import Entity
import gamethread
from players.entity import Player
import es

#
# MOTIVATION:
# es.give/fire player_weaponstrip to remove player items are not working in CSS2025.
# Similar to expr_game_text.
#
# GOAL:
# Find a way to emulate strip (RemoveAllItems) player items,
# and override es.give/es.fire to apply the emulated strip mechanics.
#

def giveweapon(userid):
    es.give(userid, "weapon_m4a1")
    print("WEAPON has been given")

def strip(userid):
    #es.give(userid, "player_weaponstrip")
    #es.fire(userid, "player_weaponstrip", "strip", 1)

    entPlayer = Player.from_userid(int(userid))
    entStrip = Entity.create("player_weaponstrip")
    entStrip.spawn()
    entStrip.strip(1, entPlayer, entPlayer)
    entStrip.remove()

    print("WEAPON has been stripped")

def player_spawn(ev):
    userid = ev['userid']

    gamethread.delayed(0.01, giveweapon, (userid))
    gamethread.delayed(1, strip, (userid))
