from .ply import yacc as yacc
from .analizador_lexico import tokens, resultado_lexema

resultado_gramatica = []
linea_actual = 0

precedence = (
    ('right','ASIGNAR'),
    ('left', 'SUMA', 'RESTA'),
    ('left', 'MULT', 'DIV'),
)

nombres = {}

def p_statement_assign(p):
    '''
    statement : IDENTIFICADOR ASIGNAR expression 
        | IDENTIFICADOR ASIGNAR CADENA 
    '''
    nombres[p[1]] = p[3]

def p_statement_expr(p):
    'statement : expression'
    p[0] = p[1]

def p_expression_operation(p):
    '''
    expression  :   expression SUMA expression
        |   expression RESTA expression
        |   expression MULT expression
        |   expression DIV expression
    '''

def p_expression_group(p):
    '''
    expression  : PARIZQ expression PARDER
        | LLAIZQ expression LLADER
        | CORIZQ expression CORDER
    '''
    p[0] = p[2]

def p_expression_logical(p):
    '''
    expression : expression MENORQUE expression 
        | expression MAYORQUE expression 
        | expression MENORIGUAL expression 
        | expression MAYORIGUAL expression 
        | expression IGUAL expression 
        | expression DIFERENTE expression
    '''

def p_expression_boolean(p):
    '''
    expression : expression AND expression 
        | expression OR expression 
        | expression NOT expression 
        | PARIZQ expression AND expression PARDER
        | PARIZQ expression OR expression PARDER
        | PARIZQ expression NOT expression PARDER
    '''

def p_expression_number(p):
    'expression : ENTERO'
    p[0] = p[1]

def p_expression_cadena(p):
    'expression : COMDOBLE expression COMDOBLE'
    p[0] = p[2]

def p_expression_id(p):
    'expression : IDENTIFICADOR'
    try:
        p[0] = nombres[p[1]]
    except LookupError:
        msj = "Error. Variable indefinida \"{}\" en la linea {}".format(str(p[1]), str(linea_actual))
        resultado_gramatica.append(msj)

def p_expression_print(p):
    'expression : PRINT IDENTIFICADOR'
    try:
        p[0] = nombres[p[2]]
    except LookupError:
        msj = "Error. Variable indefinida \"{}\" en la linea {}".format(str(p[2]), str(linea_actual))
        resultado_gramatica.append(msj)
        

def p_expression_condicional(p):
    '''
    expression : IF CORIZQ expression CORDER PARIZQ expression PARDER
        |  IF CORIZQ expression CORDER PARIZQ expression PARDER ELSE PARIZQ expression PARDER
    '''

def p_expression_ciclo(p):
    ''' 
    expression : WHILE CORIZQ expression CORDER PARIZQ expression PARDER
        | WHILE CORIZQ expression CORDER PARIZQ statement PARDER
        | DO PARIZQ expression PARDER WHILE CORIZQ expression CORDER
        | DO PARIZQ statement PARDER WHILE CORIZQ expression CORDER
        | FOR CORIZQ statement PUNTOCOMA expression CORDER PARIZQ expression PARDER
    '''

def p_error(p):
    global resultado_gramatica
    if p:
        msj = "Error sintactico de tipo {} en el valor \" {} \" en la linea {}.".format( str(p.type),str(p.value), str(linea_actual))
    else:
        msj = "Error sintactico de tipo ({}) Indefinido en la linea {}.".format(p, str(linea_actual))
    resultado_gramatica.append(msj)


# instancia del analizador sistactico
parser = yacc.yacc()

def analizar(code):
    global linea_actual
    global resultado_gramatica
    global nombres 
    nombres = {}
    linea_actual = 0
    resultado_gramatica.clear()
    resultado_lexema.clear()
    salida_parser = []

    for linea in code.splitlines():
        linea_actual = linea_actual + 1
        if linea:
            result = parser.parse(linea)
            if result:
                salida = "Linea {} -> {}".format(str(linea_actual), str(result))
                salida_parser.append(salida)

    return resultado_gramatica