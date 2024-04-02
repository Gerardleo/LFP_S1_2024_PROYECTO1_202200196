import json
from collections import namedtuple

Token = namedtuple("Token", ["type", "value"])

def tokenize_input(input_str):
    tokens = []
    input_str = input_str.replace("\n", "").replace("\t", "")
    i = 0
    while i < len(input_str):
        char = input_str[i]
        if char == "{":
            tokens.append(Token("LBRACE", char))
        elif char == "}":
            tokens.append(Token("RBRACE", char))
        elif char == ":":
            tokens.append(Token("COLON", char))
        elif char == ";":
            tokens.append(Token("SEMICOLON", char))
        elif char.isalpha():
            value = ""
            while i < len(input_str) and input_str[i].isalpha():
                value += input_str[i]
                i += 1
            tokens.append(Token("WORD", value))
            continue
        i += 1
    return tokens

def parse_config(tokens):
    config = {}
    current_key = None
    for token in tokens:
        if token.type == "WORD":
            current_key = token.value
            config[current_key] = {}
        elif token.type == "LBRACE":
            pass
        elif token.type == "RBRACE":
            current_key = None
        elif token.type == "COLON":
            pass
        elif token.type == "SEMICOLON":
            pass
    return config

def main():
    input_str = '''
    Inicio:{
        Encabezado:{
            TituloPagina:"Ejemplo titulo";
        },
        Cuerpo:[
            Titulo:{
                texto:"Este es un titulo";
                posicion:"izquierda";
                tamaño:"t1";
                color:"rojo";
            },
            Fondo:{
                color:"cyan";
            },
            Parrafo:{
                texto:"Este es un parrafo de ejemplo.";
                posicion:"izquierda";
            }
        ]
    }
    '''

    tokens = tokenize_input(input_str)
    config = parse_config(tokens)
    print(json.dumps(config, indent=4))

if __name__ == "__main__":
    main()
