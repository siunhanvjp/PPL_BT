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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\b")
        buf.write("A\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\3\2\3\2\3\2\5\2\31\n\2\3\2\3")
        buf.write("\2\3\3\3\3\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\6")
        buf.write("\3\6\3\6\3\6\7\6-\n\6\f\6\16\6\60\13\6\3\6\3\6\3\7\6\7")
        buf.write("\65\n\7\r\7\16\7\66\3\7\3\7\3\b\3\b\3\b\3\t\3\t\3\n\3")
        buf.write("\n\2\2\13\3\2\5\2\7\2\t\3\13\4\r\5\17\6\21\7\23\b\3\2")
        buf.write("\7\3\2\63;\3\2\62;\3\2c|\3\2))\5\2\13\f\17\17\"\"\2B\2")
        buf.write("\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21")
        buf.write("\3\2\2\2\2\23\3\2\2\2\3\30\3\2\2\2\5\34\3\2\2\2\7\36\3")
        buf.write("\2\2\2\t \3\2\2\2\13(\3\2\2\2\r\64\3\2\2\2\17:\3\2\2\2")
        buf.write("\21=\3\2\2\2\23?\3\2\2\2\25\26\t\2\2\2\26\31\t\3\2\2\27")
        buf.write("\31\t\2\2\2\30\25\3\2\2\2\30\27\3\2\2\2\30\31\3\2\2\2")
        buf.write("\31\32\3\2\2\2\32\33\t\3\2\2\33\4\3\2\2\2\34\35\t\4\2")
        buf.write("\2\35\6\3\2\2\2\36\37\t\3\2\2\37\b\3\2\2\2 !\5\3\2\2!")
        buf.write("\"\7\60\2\2\"#\5\3\2\2#$\7\60\2\2$%\5\3\2\2%&\7\60\2\2")
        buf.write("&\'\5\3\2\2\'\n\3\2\2\2(.\7)\2\2)-\n\5\2\2*+\7)\2\2+-")
        buf.write("\7)\2\2,)\3\2\2\2,*\3\2\2\2-\60\3\2\2\2.,\3\2\2\2./\3")
        buf.write("\2\2\2/\61\3\2\2\2\60.\3\2\2\2\61\62\7)\2\2\62\f\3\2\2")
        buf.write("\2\63\65\t\6\2\2\64\63\3\2\2\2\65\66\3\2\2\2\66\64\3\2")
        buf.write("\2\2\66\67\3\2\2\2\678\3\2\2\289\b\7\2\29\16\3\2\2\2:")
        buf.write(";\13\2\2\2;<\b\b\3\2<\20\3\2\2\2=>\13\2\2\2>\22\3\2\2")
        buf.write("\2?@\13\2\2\2@\24\3\2\2\2\7\2\30,.\66\4\b\2\2\3\b\2")
        return buf.getvalue()


class BKOOLLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    IP_ADDR = 1
    STRING = 2
    WS = 3
    ERROR_CHAR = 4
    UNCLOSE_STRING = 5
    ILLEGAL_ESCAPE = 6

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
 ]

    symbolicNames = [ "<INVALID>",
            "IP_ADDR", "STRING", "WS", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    ruleNames = [ "IP", "Letter", "Digit", "IP_ADDR", "STRING", "WS", "ERROR_CHAR", 
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
            actions[6] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            raise ErrorToken(self.text)
     


