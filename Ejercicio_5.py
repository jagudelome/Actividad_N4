import io
import tkinter as tk
from tkinter import filedialog, messagebox

class LeerArchivo:
    def __init__(self, nombre_archivo: str = "C:/prueba.txt"):
        self.nombre_archivo = nombre_archivo
    def leer(self) -> str:
        contenido = []
        try:
            with open(self.nombre_archivo, "rb") as archivo_bytes:
                with io.TextIOWrapper(archivo_bytes, encoding="utf-8") as filtro:
                    linea = filtro.readline()
                    while linea != "":
                        print(linea.rstrip("\r\n"))
                        contenido.append(linea)
                        linea = filtro.readline()
            return "".join(contenido)
        except (IOError, OSError) as e:
            print("No se pudo leer el archivo.")
            raise IOError("No se pudo leer el archivo.") from e
        
class VentanaLeerArchivo(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Lector de Archivos (Flujo de Bytes)")
        self.geometry("520x380")
        self.resizable(False, False)
        tk.Label(
            self, text="Lectura de Archivo de Texto (.txt)", font=("Arial", 13, "bold")
        ).pack(pady=10)
        frame_ruta = tk.Frame(self)
        frame_ruta.pack(fill="x", padx=20, pady=5)

        tk.Label(frame_ruta, text="Ruta del archivo:", font=("Arial", 10)).grid(
            row=0, column=0, sticky="w", padx=(0, 5)
        )

        self.entry_ruta = tk.Entry(frame_ruta, width=36, font=("Arial", 10))
        self.entry_ruta.insert(0, "C:/prueba.txt")
        self.entry_ruta.grid(row=0, column=1, padx=5)

        tk.Button(
            frame_ruta,
            text="Examinar...",
            command=self.seleccionar_archivo,
            font=("Arial", 9),
        ).grid(row=0, column=2, padx=(5, 0))
        frame_botones = tk.Frame(self)
        frame_botones.pack(pady=10)
        tk.Button(
            frame_botones,
            text="Leer Archivo",
            command=self.ejecutar_lectura,
            bg="#2196F3",
            fg="white",
            font=("Arial", 10, "bold"),
            padx=12,
        ).grid(row=0, column=0, padx=6)
        tk.Button(
            frame_botones,
            text="Limpiar",
            command=self.limpiar,
            font=("Arial", 10),
            padx=12,
        ).grid(row=0, column=1, padx=6)
        frame_texto = tk.LabelFrame(
            self, text="Contenido del archivo", font=("Arial", 10, "bold"), padx=8, pady=8
        )
        frame_texto.pack(fill="both", expand=True, padx=20, pady=(0, 15))

        scrollbar = tk.Scrollbar(frame_texto)
        scrollbar.pack(side="right", fill="y")

        self.txt_contenido = tk.Text(
            frame_texto,
            wrap="word",
            font=("Consolas", 10),
            yscrollcommand=scrollbar.set,
            state="disabled",
        )
        self.txt_contenido.pack(fill="both", expand=True)
        scrollbar.config(command=self.txt_contenido.yview)

    def seleccionar_archivo(self):
        ruta = filedialog.askopenfilename(
            title="Seleccionar archivo de texto",
            filetypes=[("Archivos de texto", "*.txt"), ("Todos los archivos", "*.*")],
        )
        if ruta:
            self.entry_ruta.delete(0, tk.END)
            self.entry_ruta.insert(0, ruta)

    def ejecutar_lectura(self):
        ruta = self.entry_ruta.get().strip()
        if not ruta:
            messagebox.showwarning(
                "Ruta vacía", "Por favor, ingrese o seleccione la ruta del archivo."
            )
            return
        try:
            lector = LeerArchivo(ruta)
            texto = lector.leer()
            self.txt_contenido.config(state="normal")
            self.txt_contenido.delete("1.0", tk.END)
            self.txt_contenido.insert(tk.END, texto)
            self.txt_contenido.config(state="disabled")
        except IOError as e:
            self.limpiar()
            messagebox.showerror("Error de Entrada/Salida", str(e))
    def limpiar(self):
        self.txt_contenido.config(state="normal")
        self.txt_contenido.delete("1.0", tk.END)
        self.txt_contenido.config(state="disabled")
if __name__ == "__main__":
    app = VentanaLeerArchivo()
    app.mainloop()