
from colors import Color
from messages import HudMsg
from players.helpers import index_from_userid

import es

#
# MOTIVATION:
# game_text seems to be broken in CSS2025 so nothing would be shown.
#
# GOAL:
# Find a way to emulate the hud message via UserMessages,
# and override es.give/es.fire to apply the emulated game_text mechanics.
#

def player_spawn(ev):
    userid = ev['userid']
    index = index_from_userid(int(userid))

    # es.give(userid, 'game_text')
    # es.fire(userid, 'game_text', 'addoutput', 'channel 2')
    # es.fire(userid, 'game_text', 'addoutput', 'color 049 182 042')
    # es.fire(userid, 'game_text', 'addoutput', 'color2 255 255 255')
    # es.fire(userid, 'game_text', 'addoutput', 'effect 2')
    # es.fire(userid, 'game_text', 'addoutput', 'fadein 0.08')
    # es.fire(userid, 'game_text', 'addoutput', 'fadeout 1.2')
    # es.fire(userid, 'game_text', 'addoutput', 'holdtime 1000')
    # es.fire(userid, 'game_text', 'addoutput', 'x 0.01')
    # es.fire(userid, 'game_text', 'addoutput', 'y 0.24')
    # es.fire(userid, 'game_text', 'addoutput', 'fxtime 0.25')

    # es.fire(userid, 'game_text', 'addoutput', 'message [RandomSettings] 120% Ball Speed [Bomb ON]')
    # es.fire(userid, 'game_text', 'Display')

    HudMsg(
        channel=2,
        effect=2,
        fade_in=0.08,
        fade_out=1.2,
        color1=Color(49, 182, 42),
        color2=Color(255, 255, 255),
        hold_time=1000,
        x=0.01,
        y=0.24,
        fx_time=0.25,
        message="[RandomSettings] Beach ni ikuwayo!"
    ).send(index)

def weapon_fire(ev):
    userid = ev['userid']
    index = index_from_userid(int(userid))

    HudMsg(
        "BOTTOM TEXT",
        x=-1.0, y=1.0, channel=1
    ).send(index)
