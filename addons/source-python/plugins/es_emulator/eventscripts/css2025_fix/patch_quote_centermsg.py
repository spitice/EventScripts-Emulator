
from messages import TextMsg

import es
from esc.monkeypatch import monkeypatch

from .quote_centermsg import quote_centermsg

class FakeSplitCmds:
    def __init__(self, splitcmds):
        self._splitcmds = splitcmds

    def findall(self, command):
        orig_splitter = self._splitcmds.findall(command)

        # Apply quote_centermsg for each command
        new_splitter = [quote_centermsg(cmd) for cmd in orig_splitter]

        # Just checking if any commands are modified for debugging purpose
        for [orig_cmd, new_cmd] in zip(orig_splitter, new_splitter):
            if orig_cmd != new_cmd:
                es.dbgmsg(2, f"[css2025_win32] Quoted centermsg: {new_cmd}")

        return new_splitter

def apply():
    es.server.splitcmds = FakeSplitCmds(es.server.splitcmds)

    @monkeypatch
    def centermsg(*argv):
        if len(argv) == 1:
            # @command decorator would make things messy...
            # You'll get special characters quoted or the entire line gets quoted.
            # To prevent this, we manually create TextMsg here and send the string as is.
            message: str = argv[0]
            TextMsg(message).send()

        else:
            centermsg(*argv)
