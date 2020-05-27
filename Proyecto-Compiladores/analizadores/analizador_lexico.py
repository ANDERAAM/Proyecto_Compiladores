from .ply import lex as lex

# resultado del analisis
resultado_lexema = []

reservada = (
    'PRINT',
    'CADENA',
    'IDENTIFICADOR',
    'ENTERO',
    'ASIGNAR',

    #Condiones
    'IF',
    'ELSE',
    #Ciclos
    'WHILE',
    'FOR',
    'DO',
)
tokens = reservada + (
    
    # Operaciones basicas
    'SUMA',
    'RESTA',
    'MULT',
    'DIV',

    # Logica
    'AND',
    'OR',
    'NOT',
    'MENORQUE',
    'MENORIGUAL',
    'MAYORQUE',
    'MAYORIGUAL',
    'IGUAL',
    'DIFERENTE',

    # Agrupadores
    'PARIZQ',
    'PARDER',
    'CORIZQ',
    'CORDER',
    'LLAIZQ',
    'LLADER',

    'PUNTOCOMA',
    'COMA',
    'COMDOBLE',
)

t_SUMA = r'\+'
t_RESTA = r'-'
t_MULT = r'\*'
t_DIV = r'/'
t_ASIGNAR = r'::'
t_NOT = r'\!'
t_MENORQUE = r'<'
t_MAYORQUE = r'>'
t_PUNTOCOMA = ';'
t_COMA = r','
t_PARIZQ = r'\('
t_PARDER = r'\)'
t_CORIZQ = r'\['
t_CORDER = r'\]'
t_LLAIZQ = r'{'
t_LLADER = r'}'
t_COMDOBLE = r'\"'

def t_PRINT(t):
    r'Ver'
    return t

def t_ELSE(t):
    r'El'
    return t

def t_IF(t):
    r'Sil'
    return t

def t_WHILE(t):
    r'Mi'
    return t

def t_DO(t):
    r'DoMi'
    return t

def t_FOR(t):
    r'RF'
    return t

def t_ENTERO(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_IDENTIFICADOR(t):
    r'\w+(_\d\w)*'
    return t

def t_CADENA(t):
   r'\"?(\w+ \ *\w*\d* \ *)\"?'
   return t

def t_AND(t):
    r'yy'
    return t

def t_OR(t):
    r'oo'
    return t

def t_MENORIGUAL(t):
    r'<='
    return t

def t_MAYORIGUAL(t):
    r'>='
    return t

def t_IGUAL(t):
    r'=='
    return t

def t_DIFERENTE(t):
    r'!='
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

t_ignore =' \t'

def t_error( t):
    global resultado_lexema
    msj = "Token no valido en la Linea {:4} Valor {:16} Posicion {:4}".format(
        str(t.lineno), str(t.value), str(t.lexpos))
    resultado_lexema.append(msj)
    t.lexer.skip(1)


# instancia de plylex
lexer = lex.lex()
