import tkinter as tk, webbrowser
from tkinter import filedialog, messagebox
from tkinter.scrolledtext import ScrolledText
from interpretador.lectura import *


Ruta = None


class TextEditorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Editor de texto")

        # Configuración del fondo
        root.configure(bg='#303030')  # Color gris oscuro para el fondo de la ventana principal

        self.editor_frame = tk.Frame(root, bg='#404040')  # Color gris un poco más claro para el fondo del marco
        self.editor_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=(10, 8))  # 10px padding en los lados, 10px arriba y 5px abajo

        # Configuración del menú
        self.menu_bar = tk.Menu(root, bg='#505050', fg='white', activebackground='#707070', activeforeground='white')  # Color gris claro para el fondo del menú, texto blanco y colores activos más claros
        root.config(menu=self.menu_bar)

        self.file_menu = tk.Menu(self.menu_bar, tearoff=0, bg='#505050', fg='white', activebackground='#707070', activeforeground='white')  # Configuración similar para el menú desplegable de Archivo
        self.menu_bar.add_cascade(label="Menu", menu=self.file_menu)
        self.file_menu.add_command(label="Abrir", command=self.open_file)
        self.file_menu.add_command(label="Guardar", command=self.save_file)

        # Etiqueta para el primer editor
        self.label_editor1 = tk.Label(self.editor_frame, text="Entrada", bg='#404040', fg='white', padx=10, pady=5)
        self.label_editor1.grid(row=0, column=0, sticky="nsew")

        # Primer editor
        self.text_widget = ScrolledText(self.editor_frame, wrap=tk.WORD, bg='#505050', fg='white')  # Color gris claro para el fondo del editor y texto blanco
        self.text_widget.grid(row=1, column=0, sticky="nsew")

        # Separador entre editores
        separator = tk.Button(self.editor_frame, text="Traducir", command=self.analizar)
        separator.grid(row=1, column=1, padx=10, pady=10)

        # Etiqueta para el segundo editor
        self.label_editor2 = tk.Label(self.editor_frame, text="Salida", bg='#404040', fg='white', padx=10, pady=5)
        self.label_editor2.grid(row=0, column=2, sticky="nsew")

        # Segundo editor
        self.second_text_widget = ScrolledText(self.editor_frame, wrap=tk.WORD, state='disabled', bg='#505050', fg='white')  # Color gris claro para el fondo del editor y texto blanco
        self.second_text_widget.grid(row=1, column=2, sticky="nsew")

        self.editor_frame.grid_columnconfigure(0, weight=1)
        self.editor_frame.grid_columnconfigure(2, weight=1)

    def open_file(self):
        global Ruta
        Ruta = filedialog.askopenfilename(filetypes=[("Archivos de Texto", "*.lfp")])
        if Ruta:
            with open(Ruta, 'r') as file:
                print(Ruta)
                content = file.read()
                self.text_widget.delete(1.0, tk.END)
                self.text_widget.insert(tk.END, content)

    def save_file(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Archivos de Texto", "*.lfp")])
        if file_path:
            content = self.text_widget.get(1.0, tk.END)
            with open(file_path, 'w') as file:
                file.write(content)
            messagebox.showinfo("Guardado", "Archivo guardado exitosamente.")


    def show_text(self):
        text = self.text_widget.get(1.0, tk.END)
        self.second_text_widget.config(state='normal')
        self.second_text_widget.delete(1.0, tk.END)
        self.second_text_widget.insert(tk.END, text)
        self.second_text_widget.config(state='disabled')

    def analizar(self):
        global Ruta
        if Ruta:
            HT = inicializador(Ruta)
            if HT:
                self.second_text_widget.config(state='normal')
                self.second_text_widget.delete(1.0, tk.END)
                for i in HT:
                    self.second_text_widget.insert(tk.END, i)
                self.second_text_widget.config(state='disabled')
                messagebox.showinfo(message="Se ha analizado el archivo correctamente.")
                webbrowser.open_new_tab("index.html")
            else:
                messagebox.showerror(message="Se han encontrado errores en el archivo.")
                webbrowser.open_new_tab("errores.html")
        else:
            messagebox.showwarning(message="No se ha seleccionado ningún archivo.")
if __name__ == "__main__":
    root = tk.Tk()
    app = TextEditorApp(root)
    root.mainloop()
