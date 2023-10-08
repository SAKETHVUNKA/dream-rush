import ply.lex as lex
import ply.yacc as yacc
tokens=['if','else','condition','statements','next','normalopenbracket','normalclosebracket','curlyopenbracket','curlyclosebracket','semicolon',];
t_ignore = ' \t';
t_next = ' \\n';
t_curlyopenbracket = r'\{';
t_curlyclosebracket = r'\}';
t_normalopenbracket = r'\(';
t_normalclosebracket = r'\)';
t_semicolon = r';';
t_if=r'if';
t_else=r'else';
t_condition=r'condition';
t_statements=r'statements';

##################################################
'''
-------------------CFG--------------------------
S -> if E | if E else A
E -> C A
C -> (condition)
A -> {statements;} | {S}

'''
##################################################

def p_if(p):
    '''assign : if expr
    | if expr next else statementsub
    | if expr else statementsub'''
    print("Syntax is correct .");

def p_expr(p):
    '''expr : conditionsub next statementsub
            | conditionsub statementsub'''
            

def p_conditionsub(p):
    '''conditionsub : normalopenbracket condition normalclosebracket '''

def p_statementsub(p):
    '''statementsub : curlyopenbracket next statements semicolon next curlyclosebracket
                        | curlyopenbracket next assign next curlyclosebracket'''
  

def p_error(p):
  print("Syntax error x_x, try again lol :p");

def t_error(p):
    print("Token error , try again");

lex.lex();
yacc.yacc();

data='''if(condition)
{
   statements;
}else{
    statements;
}''';


yacc.parse(data)