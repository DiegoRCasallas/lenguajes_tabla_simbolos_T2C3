grammar PythonGrammar;

program: (statement | function_def)* EOF;

statement: 
    assignment
    | expression
    | if_statement
    | while_statement
    | return_statement
    ;

assignment: ID '=' expression;

expression:
    expression op=('*' | '/') expression
    | expression op=('+' | '-') expression
    | expression op=('==' | '!=' | '<' | '>') expression
    | '(' expression ')'
    | ID
    | NUMBER
    | STRING
    ;

if_statement: 'if' expression ':' block ('elif' expression ':' block)* ('else' ':' block)?;

while_statement: 'while' expression ':' block;

function_def: 'def' ID '(' parameters? ')' ':' block;

parameters: ID (',' ID)*;

block: NEWLINE INDENT statement+ DEDENT | statement;

return_statement: 'return' expression?;

ID: [a-zA-Z_][a-zA-Z_0-9]*;
NUMBER: [0-9]+ ('.' [0-9]+)?;
STRING: '"' .*? '"' | '\'' .*? '\'';
NEWLINE: '\r'? '\n';
INDENT: '    ';
DEDENT: ; // Manejo especial en el listener
WS: [ \t]+ -> skip;