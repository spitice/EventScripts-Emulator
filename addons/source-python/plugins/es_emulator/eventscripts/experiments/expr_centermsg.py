
import es

#
# MOTIVATION:
# Parenthesis put in `es_centermsg` would be double-quoted.
#
# GOAL:
# Find a way to eliminate redundant quotation in centermsg command.
#

def round_start(ev):
    #
    # Not quoted
    #
    # "don't quote (parenthesis) [] {}"
    #
    es.centermsg('don\'t quote (parenthesis) [] {}')
    es.server.cmd('es_centermsg \"don\'t quote (parenthesis) [] {}\"')

    #
    # Quoted because it is parsed as es command first.
    #
    # don "'" t quote "(" parenthesis ")" [] "{" "}"
    #
    es.server.cmd('es_centermsg don\'t quote (parenthesis) [] {}')
    es.server.cmd('es_delayed 0.1 es_centermsg don\'t quote (parenthesis) [] {}')
