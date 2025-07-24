
import est

def weapon_fire(ev):
    userid = ev['userid']
    est.burn(userid, 1)
