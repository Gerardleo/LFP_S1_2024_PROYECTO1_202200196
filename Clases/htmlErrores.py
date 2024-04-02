class htmlErrores:
    def __init__(self):
        self.html = ""

    def createHtml(self, errores):
        self.html = "<html><head><title>Errores</title><style>body{font-family:Arial,sans-serif;background-color:#f7f7f7;padding:20px}h1{color:#333}table{border-collapse:collapse;width:100%;margin-top:20px}th,td{border:1px solid #ddd;padding:8px;text-align:left}th{background-color:#f2f2f2;color:#333}tr:nth-child(even){background-color:#f9f9f9}tr:hover{background-color:#f1f1f1}</style></head><body><h1>Reporte de Errores</h1><table border='1'><tr><th>N.</th><th>Mensaje</th><th>Caracter</th><th>Linea</th><th>Columna</th></tr>"
        for error in errores:
            self.html += "<tr><td>" + str(error["N."]) + "</td><td>" + error["mensaje"] +"</td><td>" + error["caracter"] + "</td><td>"+ str(error["linea"]) + "</td><td>" + str(error["columna"]) + "</td></tr>"
        self.html += "</table></body></html>"

    def generateHtml(self):
        open("errores.html", "w").write(self.html)