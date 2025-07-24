
from collections.abc import Iterable

import es
import playerlib

from commands.typed import TypedServerCommand
from players.entity import Player


def health(userid, iHealth):
    playerlib.getPlayer(userid).setHealth(iHealth)

def sethealth(userid, iHealth):
    health(userid, iHealth)

def speed(userid, multiplier):
    playerlib.getPlayer(userid).setSpeed(multiplier)

def noclip(userid, isEnabled):
    playerlib.getPlayer(userid).noclip(isEnabled)

def freeze(userid, isFrozen):
    playerlib.getPlayer(userid).freeze(isFrozen)

def give(userid, weaponName):
    es.give(userid, weaponName)

def spawn(userid, bForce = 0):
    #es.spawnplayer(userid)  # spawnplayer cannot specify bForce
    Player.from_userid(int(userid)).spawn(bForce)

def team(userid_or_userids, team):
    userids = userid_or_userids
    if not isinstance(userid_or_userids, Iterable):
        userids = [userid_or_userids]

    for userid in userids:
        Player.from_userid(int(userid)).switch_team(team)

def slay(userid):
    playerlib.getPlayer(userid).slay()

def damage(inflictorUserid, victimUserid, damage):
    player = playerlib.getPlayer(victimUserid)
    health = player.getHealth()
    player.setHealth(health - damage)

def setgravity(userid, gravityScale):
    Player.from_userid(int(userid)).gravity = gravityScale

def deathadd(userid, numDeaths):
    Player.from_userid(int(userid)).deaths += int(numDeaths)

def burn(userid, duration):
    #
    # playerlib's burn() won't work here
    # as they uses `es_fire` which is no longer working as of css2025
    #
    # playerlib.getPlayer(userid).burn()
    #
    Player.from_userid(int(userid)).call_input("IgniteLifetime", duration)

#
# Import this module from somewhere at least once to enable the following commands
#
@TypedServerCommand("est_spawn")
def on_est_spawn(command_info, userid:int):
    spawn(userid)
