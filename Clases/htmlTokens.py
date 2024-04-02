
class htmlTokens:
    def __init__(self):
        self.html = ""

    def createHtml(self, tokens):
        self.html = "<html><head><title>Tokens</title><style>body{font-family:Arial,sans-serif;background-color:#f7f7f7;padding:20px}h1{color:#333}table{border-collapse:collapse;width:100%;margin-top:20px}th,td{border:1px solid #ddd;padding:8px;text-align:left}th{background-color:#f2f2f2;color:#333}tr:nth-child(even){background-color:#f9f9f9}tr:hover{background-color:#f1f1f1}</style></head><body><h1>Reporte de Tokens</h1><table border='1'><tr><th>Token</th><th>Lexema</th><th>Linea</th><th>Columna</th></tr>"
        for token in tokens:
            self.html += "<tr><td>" + token.identificador + "</td><td>" + token.value +"</td><td>" + str(token.line) + "</td><td>"+ str(token.col) + "</td></tr>"
        self.html += "</table></body></html>"
    
    def generateHtml(self):
        open("tokens.html", "w").write(self.html)