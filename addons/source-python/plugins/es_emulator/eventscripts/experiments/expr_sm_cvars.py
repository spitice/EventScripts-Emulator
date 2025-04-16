
import random
import es

n_rounds = 0

def round_start(ev):
    global n_rounds

    #
    # Choose random hp
    #
    # REQ: Advanced Commands
    # https://forums.alliedmods.net/showthread.php?t=99300
    #
    es.server.cmd(f"es_delayed 2 sm_hp @all {random.randint(1, 19)}")

    #
    # EZ mode (rapid fire) or normal knife
    #
    # REQ: Weapon Mod
    # https://forums.alliedmods.net/showthread.php?p=1135688
    #
    firerate = -1.0  # normal firerate
    if n_rounds % 2 == 0:
        firerate = 0.0  # rapid firerate
    es.server.cmd(f"es_delayed 2 weaponmod knife firerate {firerate}")

    n_rounds += 1
