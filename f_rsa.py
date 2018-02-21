import math
from math import exp

#s0 sequence starts with speaker randomly sending a true message
def s0(types, messages, interpretation):
    cond = dict([(t, dict([(m, 0) for m in messages])) for t in types])
    msg_t = dict([(t, set()) for t in types])
    for m in messages:
        for t in interpretation(m):
            msg_t[t].add(m)

    for t in types:
        msgs = msg_t[t]
        norm = len(msgs)
        for m in msgs:
                cond[t][m] = 1/float(norm)
                
    def _eval(t):
        def _cond_eval(m):
            return cond[t][m]
        return _cond_eval

    return _eval
"""
def l0(types, messages, interpretation, alpha):
    for(m in messages):
        j = 0
        if(t in lexicon[m]):
            j = exp(alpha*)
    

def nextL(types, lexicon, seq):

   """

messages = set(["m1","m2"])
types = set(["a","b","c"])

def lexicon(m):
    if(m == "m1"):
        return set(["a"])
    else:
        return set(["a","b"])

