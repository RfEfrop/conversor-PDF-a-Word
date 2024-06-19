import PyPDF2
import tkinter as tk
from tkinter import filedialog, messagebox
from docx import Document

def leer_pdf(ruta_pdf):
    try:
        with open(ruta_pdf, 'rb') as archivo:
            lector = PyPDF2.PdfReader(archivo)
            contenido = ""
            for pagina in range(len(lector.pages)):
                pagina_pdf = lector.pages[pagina]
                contenido += f"Texto de la página {pagina + 1}:\n{pagina_pdf.extract_text()}\n\n"
            return contenido
    except Exception as e:
        return f"Ocurrió un error al leer el archivo PDF: {e}"

def seleccionar_archivo():
    ruta_pdf = filedialog.askopenfilename(filetypes=[("Archivos PDF", "*.pdf")])
    if ruta_pdf:
        contenido = leer_pdf(ruta_pdf)
        guardar_como_word(contenido)
        mostrar_contenido(contenido)

def guardar_como_word(contenido):
    documento = Document()
    documento.add_paragraph(contenido)
    ruta_word = filedialog.asksaveasfilename(defaultextension=".docx", filetypes=[("Documentos Word", "*.docx")])
    if ruta_word:
        documento.save(ruta_word)
        messagebox.showinfo("Guardado", f"El contenido se ha guardado como documento Word en: {ruta_word}")

def mostrar_contenido(contenido):
    ventana_contenido = tk.Toplevel(root)
    ventana_contenido.title("Contenido del PDF")
    
    texto = tk.Text(ventana_contenido, wrap=tk.WORD)
    texto.insert(tk.END, contenido)
    texto.pack(expand=True, fill=tk.BOTH)
    
    boton_cerrar = tk.Button(ventana_contenido, text="Cerrar", command=ventana_contenido.destroy)
    boton_cerrar.pack()

# Configuración de la interfaz gráfica
root = tk.Tk()
root.title("Convertidor de PDF a Word")

frame = tk.Frame(root, padx=10, pady=10)
frame.pack(padx=10, pady=10)

etiqueta = tk.Label(frame, text="Seleccione el archivo PDF que desea convertir a Word:")
etiqueta.pack(pady=5)

boton_seleccionar = tk.Button(frame, text="Seleccionar Archivo", command=seleccionar_archivo)
boton_seleccionar.pack(pady=5)

root.mainloop()
