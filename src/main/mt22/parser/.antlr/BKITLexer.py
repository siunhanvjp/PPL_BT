# Generated from c:\Users\Admin\Desktop\PPL\exercise\src\main\mt22\parser\BKIT.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\7")
        buf.write("\66\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t")
        buf.write("\7\4\b\t\b\4\t\t\t\3\2\3\2\3\2\3\2\3\2\5\2\31\n\2\3\2")
        buf.write("\3\2\3\3\3\3\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3")
        buf.write("\6\6\6*\n\6\r\6\16\6+\3\6\3\6\3\7\3\7\3\7\3\b\3\b\3\t")
        buf.write("\3\t\2\2\n\3\2\5\2\7\2\t\3\13\4\r\5\17\6\21\7\3\2\b\3")
        buf.write("\2\62\67\3\2\63\63\3\2\62;\3\2\63;\3\2c|\5\2\13\f\17\17")
        buf.write("\"\"\2\66\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3")
        buf.write("\2\2\2\2\21\3\2\2\2\3\30\3\2\2\2\5\34\3\2\2\2\7\36\3\2")
        buf.write("\2\2\t \3\2\2\2\13)\3\2\2\2\r/\3\2\2\2\17\62\3\2\2\2\21")
        buf.write("\64\3\2\2\2\23\24\7\64\2\2\24\31\t\2\2\2\25\26\t\3\2\2")
        buf.write("\26\31\t\4\2\2\27\31\t\5\2\2\30\23\3\2\2\2\30\25\3\2\2")
        buf.write("\2\30\27\3\2\2\2\30\31\3\2\2\2\31\32\3\2\2\2\32\33\t\4")
        buf.write("\2\2\33\4\3\2\2\2\34\35\t\6\2\2\35\6\3\2\2\2\36\37\t\4")
        buf.write("\2\2\37\b\3\2\2\2 !\5\3\2\2!\"\7\60\2\2\"#\5\3\2\2#$\7")
        buf.write("\60\2\2$%\5\3\2\2%&\7\60\2\2&\'\5\3\2\2\'\n\3\2\2\2(*")
        buf.write("\t\7\2\2)(\3\2\2\2*+\3\2\2\2+)\3\2\2\2+,\3\2\2\2,-\3\2")
        buf.write("\2\2-.\b\6\2\2.\f\3\2\2\2/\60\13\2\2\2\60\61\b\7\3\2\61")
        buf.write("\16\3\2\2\2\62\63\13\2\2\2\63\20\3\2\2\2\64\65\13\2\2")
        buf.write("\2\65\22\3\2\2\2\5\2\30+\4\b\2\2\3\7\2")
        return buf.getvalue()


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

    ruleNames = [ "IP", "Letter", "Digit", "IP_ADDR", "WS", "ERROR_CHAR", 
                  "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    grammarFileName = "BKIT.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[5] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            raise ErrorToken(self.text)
     


