# Generated from main/mt22/parser/BKOOL.g4 by ANTLR 4.9.2
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\26")
        buf.write("p\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\3\3")
        buf.write("\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4\3\5\6\5>\n\5\r\5\16")
        buf.write("\5?\3\6\3\6\3\7\3\7\3\b\3\b\3\t\3\t\3\n\3\n\3\13\3\13")
        buf.write("\3\f\3\f\3\r\3\r\3\16\3\16\3\17\3\17\3\20\3\20\3\21\3")
        buf.write("\21\3\22\3\22\3\22\3\22\3\23\6\23_\n\23\r\23\16\23`\3")
        buf.write("\24\6\24d\n\24\r\24\16\24e\3\24\3\24\6\24j\n\24\r\24\16")
        buf.write("\24k\3\25\3\25\3\25\2\2\26\3\3\5\4\7\5\t\6\13\7\r\b\17")
        buf.write("\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23")
        buf.write("%\24\'\25)\26\3\2\5\6\2\62;C\\aac|\5\2\13\f\17\17\"\"")
        buf.write("\3\2\62;\2s\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3")
        buf.write("\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2")
        buf.write("\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2")
        buf.write("\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2")
        buf.write("#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\3+\3\2\2\2")
        buf.write("\5\62\3\2\2\2\7\66\3\2\2\2\t=\3\2\2\2\13A\3\2\2\2\rC\3")
        buf.write("\2\2\2\17E\3\2\2\2\21G\3\2\2\2\23I\3\2\2\2\25K\3\2\2\2")
        buf.write("\27M\3\2\2\2\31O\3\2\2\2\33Q\3\2\2\2\35S\3\2\2\2\37U\3")
        buf.write("\2\2\2!W\3\2\2\2#Y\3\2\2\2%^\3\2\2\2\'c\3\2\2\2)m\3\2")
        buf.write("\2\2+,\7t\2\2,-\7g\2\2-.\7v\2\2./\7w\2\2/\60\7t\2\2\60")
        buf.write("\61\7p\2\2\61\4\3\2\2\2\62\63\7k\2\2\63\64\7p\2\2\64\65")
        buf.write("\7v\2\2\65\6\3\2\2\2\66\67\7h\2\2\678\7n\2\289\7q\2\2")
        buf.write("9:\7c\2\2:;\7v\2\2;\b\3\2\2\2<>\t\2\2\2=<\3\2\2\2>?\3")
        buf.write("\2\2\2?=\3\2\2\2?@\3\2\2\2@\n\3\2\2\2AB\7.\2\2B\f\3\2")
        buf.write("\2\2CD\7=\2\2D\16\3\2\2\2EF\7*\2\2F\20\3\2\2\2GH\7+\2")
        buf.write("\2H\22\3\2\2\2IJ\7}\2\2J\24\3\2\2\2KL\7\177\2\2L\26\3")
        buf.write("\2\2\2MN\7?\2\2N\30\3\2\2\2OP\7-\2\2P\32\3\2\2\2QR\7/")
        buf.write("\2\2R\34\3\2\2\2ST\7,\2\2T\36\3\2\2\2UV\7\61\2\2V \3\2")
        buf.write("\2\2WX\7\'\2\2X\"\3\2\2\2YZ\t\3\2\2Z[\3\2\2\2[\\\b\22")
        buf.write("\2\2\\$\3\2\2\2]_\t\4\2\2^]\3\2\2\2_`\3\2\2\2`^\3\2\2")
        buf.write("\2`a\3\2\2\2a&\3\2\2\2bd\t\4\2\2cb\3\2\2\2de\3\2\2\2e")
        buf.write("c\3\2\2\2ef\3\2\2\2fg\3\2\2\2gi\7\60\2\2hj\t\4\2\2ih\3")
        buf.write("\2\2\2jk\3\2\2\2ki\3\2\2\2kl\3\2\2\2l(\3\2\2\2mn\13\2")
        buf.write("\2\2no\b\25\3\2o*\3\2\2\2\7\2?`ek\4\b\2\2\3\25\2")
        return buf.getvalue()


class BKOOLLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    INT = 2
    FLOAT = 3
    ID = 4
    CM = 5
    SEMI = 6
    LB = 7
    RB = 8
    LCB = 9
    RCB = 10
    EQ = 11
    Add = 12
    Sub = 13
    Mul = 14
    Div = 15
    Mod = 16
    WS = 17
    INTLIT = 18
    FLOATLIT = 19
    ERROR_CHAR = 20

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'return'", "'int'", "'float'", "','", "';'", "'('", "')'", 
            "'{'", "'}'", "'='", "'+'", "'-'", "'*'", "'/'", "'%'" ]

    symbolicNames = [ "<INVALID>",
            "INT", "FLOAT", "ID", "CM", "SEMI", "LB", "RB", "LCB", "RCB", 
            "EQ", "Add", "Sub", "Mul", "Div", "Mod", "WS", "INTLIT", "FLOATLIT", 
            "ERROR_CHAR" ]

    ruleNames = [ "T__0", "INT", "FLOAT", "ID", "CM", "SEMI", "LB", "RB", 
                  "LCB", "RCB", "EQ", "Add", "Sub", "Mul", "Div", "Mod", 
                  "WS", "INTLIT", "FLOATLIT", "ERROR_CHAR" ]

    grammarFileName = "BKOOL.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[19] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            raise ErrorToken(self.text)
     


