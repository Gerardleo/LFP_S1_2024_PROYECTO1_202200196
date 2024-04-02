

class Html:
    def __init__(self):
        self.html = "<!DOCTYPE html>"
        self.content = "<body>"
        self.head = "<head>"
        self.styles = "<style>"
        
    def encabezado(self, titulo):
        self.head += f"<title>{titulo}</title>"
        return self.head
    
    def agregar_estilo(self, estilo):
        self.styles += estilo
        return self.styles
    
    def cuerpo(self, contenido):
        self.content += contenido
        return self.content
    
    def generarArchivo(self):
        self.styles += "</style>"
        self.head += self.styles
        self.head += "</head>"
        self.content += "</body>"
        self.content += "</html>"
        contenido = self.html + self.head + self.content
        with open("index.html", "w+") as file:
            file.truncate(0)  # Limpiar el contenido del archivo

            file.write(contenido)
        self.limpiar() 
        return contenido
    
    def limpiar(self):
        self.html = "<!DOCTYPE html>"
        self.content = "<body>"
        self.head = "<head>"
        self.styles = "<style>"
