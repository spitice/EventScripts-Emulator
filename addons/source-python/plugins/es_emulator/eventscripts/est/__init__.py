
import es
import playerlib

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

def spawn(userid, unknownArg = 0):
    es.spawnplayer(userid)
