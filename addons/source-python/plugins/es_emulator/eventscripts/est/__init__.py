
import es
import playerlib

from commands.typed import TypedServerCommand
from players.entity import Player
from players.helpers import index_from_userid


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
    index = index_from_userid(int(userid))
    Player(index).spawn(bForce)

#
# Import this module from somewhere at least once to enable the following commands
#
@TypedServerCommand("est_spawn")
def on_est_spawn(command_info, userid:int):
    spawn(userid)
