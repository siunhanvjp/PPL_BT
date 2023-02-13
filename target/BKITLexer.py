# Generated from main/mt22/parser/BKIT.g4 by ANTLR 4.11.1
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *


def serializedATN():
    return [
        4,0,5,42,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,1,
        0,1,0,1,0,3,0,17,8,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,
        4,2,30,8,2,11,2,12,2,31,1,2,1,2,1,3,1,3,1,3,1,4,1,4,1,5,1,5,0,0,
        6,1,0,3,1,5,2,7,3,9,4,11,5,1,0,3,1,0,49,57,1,0,48,57,3,0,9,10,13,
        13,32,32,43,0,3,1,0,0,0,0,5,1,0,0,0,0,7,1,0,0,0,0,9,1,0,0,0,0,11,
        1,0,0,0,1,16,1,0,0,0,3,20,1,0,0,0,5,29,1,0,0,0,7,35,1,0,0,0,9,38,
        1,0,0,0,11,40,1,0,0,0,13,14,7,0,0,0,14,17,7,1,0,0,15,17,7,0,0,0,
        16,13,1,0,0,0,16,15,1,0,0,0,16,17,1,0,0,0,17,18,1,0,0,0,18,19,7,
        1,0,0,19,2,1,0,0,0,20,21,3,1,0,0,21,22,5,46,0,0,22,23,3,1,0,0,23,
        24,5,46,0,0,24,25,3,1,0,0,25,26,5,46,0,0,26,27,3,1,0,0,27,4,1,0,
        0,0,28,30,7,2,0,0,29,28,1,0,0,0,30,31,1,0,0,0,31,29,1,0,0,0,31,32,
        1,0,0,0,32,33,1,0,0,0,33,34,6,2,0,0,34,6,1,0,0,0,35,36,9,0,0,0,36,
        37,6,3,1,0,37,8,1,0,0,0,38,39,9,0,0,0,39,10,1,0,0,0,40,41,9,0,0,
        0,41,12,1,0,0,0,3,0,16,31,2,6,0,0,1,3,0
    ]

class BKITLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    IP_ADDR = 1
    WS = 2
    ERROR_CHAR = 3
    UNCLOSE_STRING = 4
    ILLEGAL_ESCAPE = 5

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
 ]

    symbolicNames = [ "<INVALID>",
            "IP_ADDR", "WS", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    ruleNames = [ "IP", "IP_ADDR", "WS", "ERROR_CHAR", "UNCLOSE_STRING", 
                  "ILLEGAL_ESCAPE" ]

    grammarFileName = "BKIT.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.11.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[3] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            raise ErrorToken(self.text)
     


