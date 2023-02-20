grammar BKOOL;

@lexer::header {
from lexererr import *
}

options{
	language=Python3;
}

program: decl EOF; // write for program rule here using vardecl and funcdecl

decl: (vardecl | funcdecl) decl | (vardecl | funcdecl);


vardecl: typ idlist SEMI ;

idlist: ID CM idlist | ID;

funcdecl: typ ID paradecl body ;

paradecl: LB paralist RB ;

paralist: paralist1 | ;

paralist1: para SEMI paralist1 | para;

para: typ paralistid;

paralistid: ID CM paralistid | ID;

body: LCB bodylist RCB;

bodylist: (vardecl | stmt) bodylist | ;

stmt: (asm | call | return_) SEMI;

asm: ID EQ expr;

call: ID LB exprlist RB;

exprlist: exprlist1 | ;
exprlist1: expr CM exprlist1 | expr;

return_: 'return' expr;

expr: expr1 Add expr | expr1 ;
expr1: expr2 Sub expr2 | expr2;
expr2: expr2 (Mul | Div) expr3 | expr3;
expr3: (LB expr RB) | INTLIT | FLOATLIT | ID | call;

typ: INT | FLOAT ;

INT: 'int';
FLOAT: 'float';
ID: [a-zA-Z0-9_]+;
CM: ',';
SEMI: ';';
LB: '(';
RB: ')';
LCB: '{';
RCB: '}';
EQ: '=';
Add : '+';
Sub : '-';
Mul : '*';
Div : '/';
Mod : '%';
WS: [ \t\r\n] -> skip;
INTLIT: [0-9]+;
FLOATLIT: [0-9]+ '.' [0-9]+ ; 

ERROR_CHAR: . {raise ErrorToken(self.text)};
