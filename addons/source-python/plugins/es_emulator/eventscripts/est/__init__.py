
from collections.abc import Iterable

from commands.typed import TypedServerCommand
from entities.entity import Entity
from players.entity import Player

import es
import playerlib


def health(userid, iHealth):
    playerlib.getPlayer(userid).setHealth(int(iHealth))

def sethealth(userid, iHealth):
    health(userid, iHealth)

def speed(userid, multiplier):
    playerlib.getPlayer(userid).setSpeed(float(multiplier))

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
    player.setHealth(health - int(damage))

def setgravity(userid, gravityScale):
    Player.from_userid(int(userid)).gravity = float(gravityScale)

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
def on_est_spawn(command_info, userid):
    spawn(userid)

@TypedServerCommand("est_sethealth")
def on_est_sethealth(command_info, userid, iHealth):
    health(userid, iHealth)

@TypedServerCommand("est_RemoveWeapon")
def on_est_RemoveWeapon(command_info, userid, slot):
    player = playerlib.getPlayer(userid)

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
