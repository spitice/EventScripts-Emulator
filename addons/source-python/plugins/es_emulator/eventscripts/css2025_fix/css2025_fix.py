
import css2025_fix.patch_player_gametext
import css2025_fix.patch_player_strip
import css2025_fix.patch_quote_centermsg
#import css2025_fix.patch_server_commands

css2025_fix.patch_player_gametext.apply()
css2025_fix.patch_player_strip.apply()
css2025_fix.patch_quote_centermsg.apply()
#css2025_fix.patch_server_commands.apply()

#
# "patch_server_commands" is no longer required
# since I directly modified the original ES function.
#

print("Eventscripts css2025_fix patch has been loaded")
