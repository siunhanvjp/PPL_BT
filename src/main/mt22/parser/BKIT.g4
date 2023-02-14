grammar BKIT;

@lexer::header {
from lexererr import *
}

options{
	language=Python3;
}

program:  EOF ;

fragment IP : ('2'[0-5] | [1][0-9] | [1-9]) ? [0-9];
fragment Letter: [a-z];
fragment Digit: [0-9];
// bai 1
IP_ADDR : IP '.' IP '.' IP '.' IP;
// // bai 2
// Identifier: Letter (Digit | Letter) +;
//bai 3
// fragment Dec: '.' Digit+;
// fragment Exp: [eE] [+-] ? [1-9] Digit *;
// REAL: Digit+ (Dec | Exp | Dec Exp); 

//bai 5
// Int: ('0' | [1-9] [0-9_] *) {self.text = self.text.replace('_','')};

//bai 4
// STRING: '\'' (~['] | '\'\'')* '\'' ; 

WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines


ERROR_CHAR: . {raise ErrorToken(self.text)} ;
UNCLOSE_STRING: .;
ILLEGAL_ESCAPE: .;