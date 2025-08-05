
from collections.abc import Callable
from collections.abc import Iterable

from commands.typed import TypedServerCommand
from entities.entity import Entity
from players.entity import Player

import es
import playerlib

def getEsPlayerByUserid(userid) -> playerlib.Player | None:
    try:
        return playerlib.getPlayer(userid)
    except playerlib.UseridError:
        return None

def getSpPlayerByUserid(userid) -> Player | None:
    try:
        return Player.from_userid(int(userid))
    except:
        return None

def doEsPlayer(userid, fn: Callable[[playerlib.Player], None]):
    player = getEsPlayerByUserid(userid)
    if player is not None:
        fn(player)

def doSpPlayer(userid, fn: Callable[[Player], None]):
    player = getSpPlayerByUserid(userid)
    if player is not None:
        fn(player)

def health(userid, iHealth):
    doEsPlayer(userid, lambda player: player.setHealth(int(iHealth)))

def sethealth(userid, iHealth):
    health(userid, iHealth)

def speed(userid, multiplier):
    doEsPlayer(userid, lambda player: player.setSpeed(float(multiplier)))

def noclip(userid, isEnabled):
    doEsPlayer(userid, lambda player: player.noclip(isEnabled))

def freeze(userid, isFrozen):
    doEsPlayer(userid, lambda player: player.freeze(isFrozen))

def give(userid, weaponName):
    es.give(userid, weaponName)

def spawn(userid, bForce = 0):
    #es.spawnplayer(userid)  # spawnplayer cannot specify bForce
    doSpPlayer(userid, lambda player: player.spawn(bForce))

def team(userid_or_userids, team):
    userids = userid_or_userids
    if not isinstance(userid_or_userids, Iterable):
        userids = [userid_or_userids]

    for userid in userids:
        doSpPlayer(userid, lambda player: player.switch_team(team))

def slay(userid):
    doEsPlayer(userid, lambda player: player.slay())

def damage(inflictorUserid, victimUserid, damage):
    player = getEsPlayerByUserid(victimUserid)
    if player is None:
        return

    health = player.getHealth()
    player.setHealth(health - int(damage))

def setgravity(userid, gravityScale):
    player = getSpPlayerByUserid(userid)
    if player is None:
        return

    player.gravity = float(gravityScale)

def deathadd(userid, numDeaths):
    player = getSpPlayerByUserid(userid)
    if player is None:
        return

    player.deaths += int(numDeaths)

def burn(userid, duration):
    #
    # playerlib's burn() won't work here
    # as they uses `es_fire` which is no longer working as of css2025
    #
    # playerlib.getPlayer(userid).burn()
    #
    doSpPlayer(userid, lambda player: player.call_input("IgniteLifetime", duration))

#
# Import this module from somewhere at least once to enable the following commands
#
@TypedServerCommand("est_spawn")
def on_est_spawn(command_info, userid):
    spawn(userid)

@TypedServerCommand("est_sethealth")
def on_est_sethealth(command_info, userid, iHealth):
    health(userid, iHealth)

@TypedServerCommand("est_RemoveWeapon")
def on_est_RemoveWeapon(command_info, userid, slot):
    player = getEsPlayerByUserid(userid)
    if player is None:
        return

    slot = int(slot)
    weaponName = None
    if slot == 1:
        weaponName = player.getPrimary()
    elif slot == 2:
        weaponName = player.getSecondary()
    elif slot == 3:
        weaponName = "knife"

    if weaponName is None or weaponName == '0':
        return

    weaponEntIndex = player.getWeaponIndex(weaponName)

    if weaponEntIndex == 0:
        return

    # Remove the weapon
    Entity(weaponEntIndex).call_input("Kill")

    #print(f"[est_RemoveWeapon] Removed weapon ({weaponName} at slot {slot}) from the player {userid}")

@TypedServerCommand("est_speed")
def on_est_speed(command_info, userid, multiplier):
    speed(userid, multiplier)
