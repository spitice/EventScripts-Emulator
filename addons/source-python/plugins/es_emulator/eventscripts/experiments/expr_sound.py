
import es
from engines.sound import Sound
from players.helpers import index_from_userid

def player_hurt(ev):
    userid = ev["userid"]
    attacker = ev["attacker"]

    play_sound_via_sp(attacker, "surfpvparena/_hitsound.mp3")

def play_sound_via_es(userid, soundPath):
    volume = 1.0
    es.playsound(userid, soundPath, volume)

def play_sound_via_sp(userid, soundPath):
    sound = Sound(soundPath)
    sound.play(index_from_userid(int(userid)))
