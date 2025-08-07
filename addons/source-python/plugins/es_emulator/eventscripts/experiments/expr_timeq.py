
import es
import gamethread

#
# Just figuring out how gamethread and TimrSortedQueue work
#

def weapon_fire(ev):
    delayedCheck(1)
    gamethread.delayed(0.2, raiseError)
    delayedCheck(2)
    delayedCheck(3)
    gamethread.delayed(0.2, raiseError)
    delayedCheck(4)
    delayedCheck(5)
    gamethread.delayed(0.2, raiseError)
    delayedCheck(6)
    delayedCheck(7)
    gamethread.delayed(0.2, raiseError)
    delayedCheck(8)
    delayedCheck(9)
    gamethread.delayed(0.2, raiseError)
    delayedCheck(10)

    #
    # Check TimeSortedQuquq class
    #
    # timeq.remove should only remove the one node, not the all of the same gotime nodes.
    # -> RESULT: OK
    #
    q = gamethread.TimeSortedQueue()
    q.add(0.1, "1")
    q.add(0.1, "2")
    q.add(0, "3")
    q.add(0, "4")
    for node in q.nodes:
        print(f"BEFORE remove node: {node.cmd}, gotime: {node.gotime}")

    q.remove(q.getFirst())
    for node in q.nodes:
        print(f"AFTER remove node: {node.cmd}, gotime: {node.gotime}")

def delayedCheck(id):
    es.server.cmd(f"es_delayed 0.2 echo \"[EXPR] echo check {id}\"")
    gamethread.delayed(0.2, check, (id))

def check(id):
    print(f"[EXPR] check {id}")

def raiseError():
    # raise AssertionError("[EXPR] error")
    pass
