
class Funcion:

    def __init__(self):
        print("Funcion")
        pass

    def encabezado(instruccion):
        titulo = instruccion.pop(0).value
        if titulo == "TituloPagina":
            instruccion.pop(0)
            titulo = instruccion.pop(0).value
            return titulo
        
    def Cuerpo(instruccion):
        contenido = ""
        css = "body {"
        atributos = {}  # Diccionario para almacenar los atributos del título
        
        # Procesar cada atributo del título
        while instruccion:
            funcion = instruccion.pop(0).value
            if funcion == 'Titulo':
                instruccion.pop(0)
                contenido += titulo(instruccion)
            elif funcion == "Fondo":
                instruccion.pop(0) 
                css += fondo(instruccion)
            elif funcion == "Parrafo":
                instruccion.pop(0)
                contenido += parrafo(instruccion)
            elif funcion == "Texto":
                instruccion.pop(0)
                css += texto(instruccion)
            elif funcion == "Codigo":
                instruccion.pop(0)
                contenido += codigo(instruccion)  
            elif funcion == "Negrita":
                instruccion.pop(0)
                contenido += negrita(instruccion)
            elif funcion == "Subrayado":
                instruccion.pop(0)
                contenido += subrayado(instruccion)
            elif funcion == "Tachado":
                instruccion.pop(0)
                contenido += tachado(instruccion)
            elif funcion == "Cursiva":
                instruccion.pop(0)
                contenido += cursiva(instruccion)
            elif funcion == "Salto":
                instruccion.pop(0)
                contenido += salto(instruccion)
            elif funcion == "Tabla":
                instruccion.pop(0)
                contenido += tabla(instruccion)

            # elif funcion == "tamano":
            #     instruccion.pop(0)
            #     css = instruccion.pop(0).value
            # elif funcion == "posicion":
            #     instruccion.pop(0)
            #     valor = instruccion.pop(0).value
            # elif funcion == "color":
            #     instruccion.pop(0)
            #     valor = instruccion.pop(0).value 
                
        css += "}"
            
        return css,contenido
  
def titulo(instruccion):
        contenido = ""
        atributos = {}  # Diccionario para almacenar los atributos del título
        # Procesar cada atributo del título
        while instruccion[0].value != '}':
            funcion = instruccion.pop(0).value
            if funcion == "texto":
                instruccion.pop(0) 
                valor = instruccion.pop(0).value
            elif funcion == "tamano":
                instruccion.pop(0)
                valor = instruccion.pop(0).value
                valor = valor.replace("t", "h")
            elif funcion == "posicion":
                instruccion.pop(0)
                valor = instruccion.pop(0).value
                if valor == "izquierda":
                    valor = "left"
                elif valor == "derecha":
                    valor = "right"
                elif valor == "centro":
                    valor = "center"    
            elif funcion == "color":
                instruccion.pop(0)
                valor = instruccion.pop(0).value
                if valor == "rojo":
                    valor = "red"
                elif valor == "amarillo":
                    valor = "yellow"
                elif valor == "azul":
                    valor = "blue"
            else:
                continue  # Ignorar atributos desconocidos
            atributos[funcion] = valor
                
        # Construir el fragmento HTML del título con sus atributos
        contenido += f"<{atributos.get('tamano')} style='text-align: {atributos.get('posicion')}; "
        contenido += f"color: {atributos.get('color')};'>"
        contenido += atributos.get('texto')
        contenido += f"</{atributos.get('tamano')}>"
            
        return contenido

def fondo(instruccion):
    contenido = ""
    atributos = {}

    while instruccion[0].value != '}':
            funcion = instruccion.pop(0).value
            if funcion == 'color':
                instruccion.pop(0)
                color = instruccion.pop(0).value
                if color == "rojo":
                    color = "red"
                elif color == "amarillo":
                    color = "yellow"
                elif color == "azul":
                    color = "blue"
                atributos[funcion] = color
    contenido += f"background-color: {atributos.get('color')};"
    return contenido

def parrafo(instruccion):
    contenido = ""
    atributos = {}  # Diccionario para almacenar los atributos del párrafo
    # Procesar cada atributo del párrafo
    while instruccion[0].value != '}':
        funcion = instruccion.pop(0).value
        if funcion == "texto":
            instruccion.pop(0) 
            valor = instruccion.pop(0).value
        elif funcion == "posicion":
            instruccion.pop(0)
            valor = instruccion.pop(0).value
            if valor == "izquierda":
                valor = "left"
            elif valor == "derecha":
                valor = "right"
            elif valor == "centro":
                valor = "center"    
        else:
            continue  # Ignorar atributos desconocidos
        atributos[funcion] = valor
            
    # Construir el fragmento HTML del párrafo con sus atributos
    contenido += f"<p style='text-align: {atributos.get('posicion')}; '>"
    contenido += atributos.get('texto')
    contenido += f"</p>"
    
    return contenido

def texto(instruccion):
    contenido = ""
    atributos = {}  # Diccionario para almacenar los atributos del párrafo
    # Procesar cada atributo del párrafo
    while instruccion[0].value != '}':
        funcion = instruccion.pop(0).value
        if funcion == "fuente":
            instruccion.pop(0) 
            valor = instruccion.pop(0).value
        elif funcion == "posicion":
            instruccion.pop(0)
            valor = instruccion.pop(0).value
            if valor == "izquierda":
                valor = "left"
            elif valor == "derecha":
                valor = "right"
            elif valor == "centro":
                valor = "center" 
        elif funcion == "color":
            instruccion.pop(0)
            valor = instruccion.pop(0).value
            if valor == "rojo":
                valor = "red"
            elif valor == "amarillo":
                valor = "yellow"
            elif valor == "azul":
                valor = "blue"   
        else:
            continue  # Ignorar atributos desconocidos
        atributos[funcion] = valor
            

    contenido += f"font-family: {atributos.get('fuente')};"
    contenido += f"font-size: {atributos.get('tamano')};"
    contenido += f"color: {atributos.get('color')};"
    return contenido

def codigo(instruccion):
    contenido = ""
    
    atributos = {}  # Diccionario para almacenar los atributos del párrafo
    # Procesar cada atributo del párrafo
    while instruccion[0].value != '}':
        funcion = instruccion.pop(0).value
        if funcion == "texto":
            instruccion.pop(0) 
            valor = instruccion.pop(0).value
        elif funcion == "posicion":
            instruccion.pop(0)
            valor = instruccion.pop(0).value
            if valor == "izquierda":
                valor = "left"
            elif valor == "derecha":
                valor = "right"
            elif valor == "centro":
                valor = "center"
        else:
            continue
        atributos[funcion] = valor

    contenido += f"<code style='text-align: {atributos.get('posicion')}; '>"
    contenido += atributos.get('texto')
    contenido += f"</code>"
    return contenido

def negrita(instruccion):
    contenido = ""
    atributos = {}  # Diccionario para almacenar los atributos del párrafo
    # Procesar cada atributo del párrafo
    while instruccion[0].value != '}':
        funcion = instruccion.pop(0).value
        if funcion == "texto":
            instruccion.pop(0) 
            valor = instruccion.pop(0).value
        else:
            continue
        atributos[funcion] = valor

    contenido += f"<strong>"
    contenido += atributos.get('texto')
    contenido += f"</strong>"
    return contenido

def cursiva(instruccion):
    contenido = ""
    atributos = {}  # Diccionario para almacenar los atributos del párrafo
    # Procesar cada atributo del párrafo
    while instruccion[0].value != '}':
        funcion = instruccion.pop(0).value
        if funcion == "texto":
            instruccion.pop(0) 
            valor = instruccion.pop(0).value
        else:
            continue
        atributos[funcion] = valor

    contenido += f"<em>"
    contenido += atributos.get('texto')
    contenido += f"</em>"
    return contenido

def subrayado(instruccion):
    contenido = ""
    atributos = {}  # Diccionario para almacenar los atributos del párrafo
    # Procesar cada atributo del párrafo
    while instruccion[0].value != '}':
        funcion = instruccion.pop(0).value
        if funcion == "texto":
            instruccion.pop(0) 
            valor = instruccion.pop(0).value
        else:
            continue
        atributos[funcion] = valor

    contenido += f"<u>"
    contenido += atributos.get('texto')
    contenido += f"</u>"
    return contenido

def tachado(instruccion):
    contenido = ""
    atributos = {}  # Diccionario para almacenar los atributos del párrafo
    # Procesar cada atributo del párrafo
    while instruccion[0].value != '}':
        funcion = instruccion.pop(0).value
        if funcion == "texto":
            instruccion.pop(0) 
            valor = instruccion.pop(0).value
        else:
            continue
        atributos[funcion] = valor

    contenido += f"<s>"
    contenido += atributos.get('texto')
    contenido += f"</s>"
    return contenido

def salto(instruccion):
    contenido = ""
    atributos = {}  # Diccionario para almacenar los atributos del párrafo
    # Procesar cada atributo del párrafo
    while instruccion[0].value != '}':
        funcion = instruccion.pop(0).value
        if funcion == "cantidad":
            instruccion.pop(0)
            valor = instruccion.pop(0).value
        else:
            continue

    contenido += f"<br>"*int(valor)
    return contenido

def tabla(instruccion):
    contenido = ""
    filas = 0
    columnas = 0
    elementos = []

    # Obtener atributos de la tabla
    for elem in instruccion:
        funcion = instruccion.pop(0).value
        if funcion == "filas":
            instruccion.pop(0)  # Eliminar el nombre del atributo
            filas = int(instruccion.pop(0).value)  # Obtener el valor de filas
        elif funcion == "columnas":
            instruccion.pop(0)  # Eliminar el nombre del atributo
            columnas = int(instruccion.pop(0).value)  # Obtener el valor de columnas
        elif funcion == "elemento":
            element = instruccion.pop(0).value # Eliminar el nombre del atributo
            elemento = {}
            while instruccion[0].value != "}":
                element = instruccion.pop(0).value
                if element == "fila":
                    instruccion.pop(0)
                    elemento["fila"] = int(instruccion.pop(0).value)
                elif element == "columna":
                    instruccion.pop(0)
                    elemento["columna"] = int(instruccion.pop(0).value)
                    instruccion.pop(0)
                    elemento["texto"] = instruccion.pop(0).value
            elementos.append(elemento)

    # Crear la tabla HTML
    contenido += "<table>"
    for i in range(1, filas + 1):
        contenido += "<tr>"
        for j in range(1, columnas + 1):
            contenido += "<td>"
            for elemento in elementos:
                if elemento.get("fila") == i and elemento.get("columna") == j:
                    contenido += elemento.get("texto")
                    break
            contenido += "</td>"
        contenido += "</tr>"
    contenido += "</table>"
    
    return contenido


