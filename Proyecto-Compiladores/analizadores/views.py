from django.shortcuts import render

from .analizador_lexico import *
from .analizador_sintactico import *

def Index(request):
    global codigoEjemplo
    errores = []
    datos = {'code': codigoEjemplo }

    if request.POST:
        datos['code'] = request.POST['code']
        datos['analizado'] = True

        errores = analizar(datos['code'])

        datos['n_errores'] = len(errores)
        errores = "\n".join(errores)
        datos['errores'] = errores
        

    return render(request, 'index.html', datos)


codigoEjemplo = """
var :: 24
num :: var + 1

Ver num

Sil [var < num] ( Ver var ) El ( Ver num )

RF [a::1 ; a<100] ( Ver a ) 

DoMi ( var :: var + 2 ) Mi [var != 50] 

Mi [var != 50] ( var :: var + 2 )"""