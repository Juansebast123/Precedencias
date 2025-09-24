grammar LabeledExpr2;

prog:   stat+ ;

stat:   expr NEWLINE                # printExpr
    |   ID '=' expr NEWLINE         # assign
    |   NEWLINE                     # blank
    ;
    
// Se cambia el orden y lee primero la suma y resta, luego multiplicacion y division

expr:   expr op=('+'|'-') expr      # AddSub
    |   expr op=('*'|'/') expr      # MulDiv
    |   FLOAT                       # float
    |   INT                         # int
    |   ID                          # id
    |   '(' expr ')'                # parens
    |   func=ID '(' expr ')'        # function
    |   expr '!'                    # factorial
    ;

MUL : '*' ;
DIV : '/' ;
ADD : '+' ;
SUB : '-' ;

ID    : [a-zA-Z]+ ;
FLOAT : [0-9]+ '.' [0-9]+ ;
INT   : [0-9]+ ;
NEWLINE:'\r'? '\n' ;
WS    : [ \t]+ -> skip ;
