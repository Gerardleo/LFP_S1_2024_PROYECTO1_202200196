from Funciones.Funcion import Funcion as f
from Clases.Html import Html as ht
from Clases.htmlErrores import htmlErrores as he
from Clases.htmlTokens import htmlTokens as htkn
from collections import namedtuple
Token = namedtuple("Token", ["identificador","value", "line", "col"])

line = 1
col = 1
tokens = []
errores = []
html = ht()
htmlErrores = he()
htmlTokens = htkn()


def tokenize_string(input_str, i):
    token = ""
    for char in input_str:
        if char in [':','"',";","="]:
            return [token, i]
        token += char
        i += 1
    error = {
        "N.": len(errores) + 1,
        "mensaje": "String no cerrado",
        "linea": line,
        "columna": col,
    }
    errores.append(error)
    print("String no cerrado", token)



def tokenize_number(input_str, i):
    token = ""
    isDecimal = False
    for char in input_str:
        if char.isdigit():
            token += char
            i += 1
        elif char == ".":
            token += char
            i += 1
            isDecimal = True
        else:
            break
    if isDecimal:
        return [float(token), i]

    return [int(token), i]


def tokenize_input(input_str):
    global line, col, tokens

    i = 0
    while i < len(input_str):
        char = input_str[i]
        if char.isspace():
            if char == "\n":
                line += 1
                col = 1
            elif char == "\t":
                col += 4
            i += 1
        elif char.isupper():
            string, pos = tokenize_string(input_str[i:], i)
            col += len(string) + 1
            i = pos
            identificador = "Palabra Reservada"
            token = Token(identificador,string, line, col)
            tokens.append(token)
        elif char.islower():
            string, pos = tokenize_string(input_str[i:], i)
            col += len(string) + 1
            i = pos
            identificador = "Palabra Reservada"
            token = Token(identificador,string, line, col)
            tokens.append(token)
        elif char == '"':
            string, pos = tokenize_string(input_str[i+1:], i)
            col += len(string) + 1
            i = pos + 2
            identificador = "Cadena"
            token = Token(identificador,string, line, col)
            tokens.append(token)
        elif char in ["{", "}", "[", "]", ",", ":", ";", "="]:
            col += 1
            i += 1
            identificador = ""
            if char == "{":
                identificador = "Llave Abierta"
            elif char == "}":
                identificador = "Llave Cerrada"
            elif char == "[":
                identificador = "Corchete Abierto"
            elif char == "]":
                identificador = "Corchete Cerrado"
            elif char == ",":
                identificador = "Coma"
            elif char == ":":
                identificador = "Dos Puntos"
            elif char == ";":
                identificador = "Punto y Coma"
            elif char == "=":
                identificador = "Igual"
            token = Token(identificador,char, line, col)
            tokens.append(token)
        elif char.isdigit():
            number, pos = tokenize_number(input_str[i:], i)
            col += pos - i
            i = pos
            identificador = "Numero"
            token = Token(identificador,number, line, col)
            tokens.append(token)
        else:
            error = {
                "N.": len(errores) + 1,
                "mensaje": "Error: caracter desconocido",
                "caracter": char,
                "linea": line,
                "columna": col,
            }
            errores.append(error)
            i += 1
            col += 1

def get_instruction():
    global tokens, errores
    if not tokens:
        return None
    else:
        htmlTokens.createHtml(tokens)
        htmlTokens.generateHtml()
    while tokens:
        token = tokens.pop(0)
        if token.value == "Encabezado":
            tokens.pop(0)
            tokens.pop(0)
            titulo = f.encabezado(tokens)
            html.encabezado(titulo)
        if token.value == "Cuerpo":
            tokens.pop(0)
            tokens.pop(0)
            css,cuerpo = f.Cuerpo(tokens)
            html.agregar_estilo(css)
            html.cuerpo(cuerpo)            
    HTML = html.generarArchivo()
    htmlErrores.createHtml(errores)
    htmlErrores.generateHtml()

    return HTML

def create_instructions():
    global tokens
    instrucciones = []
    while tokens:
        instruccion = get_instruction()
        if instruccion:
            instrucciones.append(instruccion)
    return instrucciones

def inicializador(entrada):
    limpia()
    lectura = open(entrada, "r").read()
    tokenize_input(lectura)
  
    for i in tokens:
        print(i)

   
    instrucciones = create_instructions()
    print(instrucciones)
    if errores:
        for i in errores:
            print(i)
        return None
    return instrucciones
    

def limpia():
    tokens.clear()
    errores.clear()

     