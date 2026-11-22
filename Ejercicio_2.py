import tkinter as tk
from tkinter import messagebox
class Vendedor:

    def __init__(self, nombre: str, apellidos: str, edad: int):
        self.verifica_años(edad)
        self.nombre = nombre
        self.apellidos = apellidos
        self.edad = edad

    def verifica_años(self, edad: int):
        if edad < 0 or edad > 120:
            raise ValueError("La edad no puede ser negativa ni mayor a 120")
        if edad < 18:
            raise ValueError("El vendedor debe ser mayor de 18 años")
    def imprimir(self) -> str:
        datos = (
            f"Nombre: {self.nombre}\n"
            f"Apellidos: {self.apellidos}\n"
            f"Edad: {self.edad} años"
        )
        print("Datos del Vendedor")
        print(datos)
        return datos

class InterfazVendedor:

    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("Registro de Vendedor")
        self.root.geometry("360x280")
        self.root.resizable(False, False)
        tk.Label(
            root, text="Datos del Vendedor", font=("Arial", 13, "bold")
        ).pack(pady=10)
        frame_form = tk.Frame(root)
        frame_form.pack(pady=5, padx=20, fill="x")
        tk.Label(frame_form, text="Nombre:", font=("Arial", 10)).grid(
            row=0, column=0, sticky="w", pady=5
        )
        self.entry_nombre = tk.Entry(frame_form, width=25)
        self.entry_nombre.grid(row=0, column=1, pady=5)
        tk.Label(frame_form, text="Apellidos:", font=("Arial", 10)).grid(
            row=1, column=0, sticky="w", pady=5
        )
        self.entry_apellidos = tk.Entry(frame_form, width=25)
        self.entry_apellidos.grid(row=1, column=1, pady=5)
        tk.Label(frame_form, text="Edad:", font=("Arial", 10)).grid(
            row=2, column=0, sticky="w", pady=5
        )
        self.entry_edad = tk.Entry(frame_form, width=25)
        self.entry_edad.grid(row=2, column=1, pady=5)
        frame_botones = tk.Frame(root)
        frame_botones.pack(pady=15)

        tk.Button(
            frame_botones,
            text="Registrar Vendedor",
            command=self.registrar_vendedor,
            bg="#4CAF50",
            fg="white",
            font=("Arial", 10, "bold"),
            padx=10,
        ).grid(row=0, column=0, padx=5)

        tk.Button(
            frame_botones,
            text="Limpiar",
            command=self.limpiar_campos,
            font=("Arial", 10),
            padx=10,
        ).grid(row=0, column=1, padx=5)

    def registrar_vendedor(self):
        nombre = self.entry_nombre.get().strip()
        apellidos = self.entry_apellidos.get().strip()
        edad_texto = self.entry_edad.get().strip()

        if not nombre or not apellidos or not edad_texto:
            messagebox.showwarning(
                "Campos vacíos", "Por favor, completa todos los campos."
            )
            return

        try:
            edad = int(edad_texto)
            vendedor = Vendedor(nombre, apellidos, edad)

            info_vendedor = vendedor.imprimir()
            messagebox.showinfo(
                "Vendedor Registrado",
                f"Objeto instanciado correctamente:\n\n{info_vendedor}",
            )

        except ValueError as e:
            if "invalid literal for int()" in str(e):
                messagebox.showerror(
                    "Error de Tipo",
                    "La edad debe ser un número entero válido.",
                )
            else:
                messagebox.showerror("Error de Validación", str(e))
    def limpiar_campos(self):
        self.entry_nombre.delete(0, tk.END)
        self.entry_apellidos.delete(0, tk.END)
        self.entry_edad.delete(0, tk.END)
        self.entry_nombre.focus()

if __name__ == "__main__":
    ventana = tk.Tk()
    app = InterfazVendedor(ventana)
    ventana.mainloop()