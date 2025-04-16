
from commands import Command

import es
from esc.monkeypatch import monkeypatch

def apply():
    #
    # Sometimes using `con_command.dispatch` on cvars by managed by SourceMod plugins
    # won't be updated. seems to be a little bit weird...
    #
    # Apparently, there is a bug on `Command` class. (need to invesitage in some day)
    # For now, let's just use `insesrt_command_string` for everything.
    # (which seems to be less performant I guess.)
    #
    @monkeypatch
    def ForceServerCommand(command_str):
        if not isinstance(command_str, str):
            raise TypeError

        c = Command()
        if not c.tokenize(command_str):
            return 1

        es.insert_command_string(command_str)
        return 1
