
import experiments.expr_centermsg
import experiments.expr_game_text
import experiments.expr_sm_cvars

is_centermsg_enabled = False
is_game_text_enabled = False
is_sm_cvars_enabled = False

def round_start(ev):
    if is_centermsg_enabled:
        experiments.expr_centermsg.round_start(ev)
    if is_sm_cvars_enabled:
        experiments.expr_sm_cvars.round_start(ev)

def player_spawn(ev):
    if is_game_text_enabled:
        experiments.expr_game_text.player_spawn(ev)

def weapon_fire(ev):
    if is_game_text_enabled:
        experiments.expr_game_text.weapon_fire(ev)
