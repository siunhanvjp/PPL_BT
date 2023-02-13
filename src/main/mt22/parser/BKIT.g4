grammar BKIT;

@lexer::header {
from lexererr import *
}

options{
	language=Python3;
}

program:  EOF ;

fragment IP : ([1-9][0-9] | [1-9]) ? [0-9];
IP_ADDR : IP '.' IP '.' IP '.' IP;
WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines


ERROR_CHAR: . {raise ErrorToken(self.text)} ;
UNCLOSE_STRING: .;
ILLEGAL_ESCAPE: .;