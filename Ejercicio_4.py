import tkinter as tk
from tkinter import messagebox

class Programador:
    def __init__(self, nombre: str, apellidos: str):
        self.nombre = nombre
        self.apellidos = apellidos
    def __str__(self) -> str:
        return f"{self.nombre} {self.apellidos}"
class EquipoMaratonProgramacion:
    def __init__(
        self,
        nombre_equipo: str,
        universidad: str,
        lenguaje_programacion: str,
        tamano_equipo: int,
    ):
        if tamano_equipo < 2 or tamano_equipo > 3:
            raise ValueError(
                "El tamaño del equipo debe ser minimo 2 y maximo 3 programadores."
            )
 
        self.nombre_equipo = nombre_equipo
        self.universidad = universidad
        self.lenguaje_programacion = lenguaje_programacion
        self.tamano_equipo = tamano_equipo
        self.programadores: list[Programador] = []
    def esta_lleno(self) -> bool:
        return len(self.programadores) >= self.tamano_equipo
    def anadir_programador(self, programador: Programador) -> None:
        if self.esta_lleno():
            error_msg = "El equipo esta completo. No se pueden añadir mas programadores."
            print(f"Excepción: {error_msg}")
            raise OverflowError(error_msg)
        self.programadores.append(programador)
    @staticmethod
    def validar_campo(campo: str) -> None:
        if not campo.strip():
            raise ValueError("El campo no puede estar vacio.")
        if any(caracter.isdigit() for caracter in campo):
            raise ValueError(
                "El campo debe contener solo texto (no se permiten numeros)."
            )
        if len(campo) >= 20:
            raise ValueError(
                "El campo no puede tener una longitud igual o superior a 20 caracteres."
            )

class VentanaMaraton(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Maraton de Programacion")
        self.geometry("460x520")
        self.resizable(False, False)
        self.equipo: EquipoMaratonProgramacion | None = None
        frame_equipo = tk.LabelFrame(
            self, text="1. Datos del Equipo", font=("Arial", 10, "bold"), padx=10, pady=10
        )
        frame_equipo.pack(fill="x", padx=15, pady=10)
        tk.Label(frame_equipo, text="Nombre del equipo:").grid(
            row=0, column=0, sticky="w", pady=3
        )
        self.entry_equipo = tk.Entry(frame_equipo, width=28)
        self.entry_equipo.grid(row=0, column=1, pady=3)

        tk.Label(frame_equipo, text="Universidad:").grid(
            row=1, column=0, sticky="w", pady=3
        )
        self.entry_universidad = tk.Entry(frame_equipo, width=28)
        self.entry_universidad.grid(row=1, column=1, pady=3)

        tk.Label(frame_equipo, text="Lenguaje:").grid(
            row=2, column=0, sticky="w", pady=3
        )
        self.entry_lenguaje = tk.Entry(frame_equipo, width=28)
        self.entry_lenguaje.grid(row=2, column=1, pady=3)

        tk.Label(frame_equipo, text="Tamaño (2 o 3):").grid(
            row=3, column=0, sticky="w", pady=3
        )
        self.entry_tamano = tk.Entry(frame_equipo, width=28)
        self.entry_tamano.grid(row=3, column=1, pady=3)

        self.btn_crear_equipo = tk.Button(
            frame_equipo,
            text="Crear Equipo",
            command=self.crear_equipo,
            bg="#2196F3",
            fg="white",
            font=("Arial", 9, "bold"),
        )
        self.btn_crear_equipo.grid(row=4, column=0, columnspan=2, pady=8)
        frame_prog = tk.LabelFrame(
            self, text="2. Añadir Programador", font=("Arial", 10, "bold"), padx=10, pady=10
        )
        frame_prog.pack(fill="x", padx=15, pady=5)
        tk.Label(frame_prog, text="Nombre:").grid(row=0, column=0, sticky="w", pady=3)
        self.entry_nombre_prog = tk.Entry(frame_prog, width=28, state="disabled")
        self.entry_nombre_prog.grid(row=0, column=1, pady=3)

        tk.Label(frame_prog, text="Apellidos:").grid(
            row=1, column=0, sticky="w", pady=3
        )
        self.entry_apellidos_prog = tk.Entry(frame_prog, width=28, state="disabled")
        self.entry_apellidos_prog.grid(row=1, column=1, pady=3)
        self.btn_anadir_prog = tk.Button(
            frame_prog,
            text="Añadir Programador",
            command=self.agregar_programador,
            bg="#4CAF50",
            fg="white",
            font=("Arial", 9, "bold"),
            state="disabled",
        )
        self.btn_anadir_prog.grid(row=2, column=0, columnspan=2, pady=8)
        frame_estado = tk.LabelFrame(
            self, text="Estado del Equipo", font=("Arial", 10, "bold"), padx=10, pady=8
        )
        frame_estado.pack(fill="both", expand=True, padx=15, pady=10)

        self.lbl_info = tk.Label(
            frame_estado,
            text="Aun no se ha creado ningun equipo.",
            justify="left",
            font=("Arial", 9),
        )
        self.lbl_info.pack(anchor="w")

        tk.Button(
            self, text="Reiniciar Todo", command=self.reiniciar, font=("Arial", 9)
        ).pack(pady=5)

    def crear_equipo(self):
        nombre = self.entry_equipo.get().strip()
        universidad = self.entry_universidad.get().strip()
        lenguaje = self.entry_lenguaje.get().strip()
        tamano_texto = self.entry_tamano.get().strip()

        if not nombre or not universidad or not lenguaje or not tamano_texto:
            messagebox.showwarning(
                "Campos incompletos", "Complete todos los datos del equipo."
            )
            return

        try:
            tamano = int(tamano_texto)
            self.equipo = EquipoMaratonProgramacion(
                nombre, universidad, lenguaje, tamaño
            )
            self._estado_form_equipo("disabled")
            self._estado_form_programador("normal")
            self.actualizar_vista()
            messagebox.showinfo(
                "Equipo Creado",
                f"Equipo '{nombre}' creado. Ahora ingrese los {tamano} programadores.",
            )

        except ValueError as e:
            if "invalid literal for int()" in str(e):
                messagebox.showerror(
                    "Error de Tipo", "El tamaño del equipo debe ser un número entero."
                )
            else:
                messagebox.showerror("Error de Validación", str(e))

    def agregar_programador(self):
        if self.equipo is None:
            return

        nombre = self.entry_nombre_prog.get().strip()
        apellidos = self.entry_apellidos_prog.get().strip()

        try:
            EquipoMaratonProgramacion.validar_campo(nombre)
            EquipoMaratonProgramacion.validar_campo(apellidos)
            nuevo_prog = Programador(nombre, apellidos)
            self.equipo.anadir_programador(nuevo_prog)
            self.entry_nombre_prog.delete(0, tk.END)
            self.entry_apellidos_prog.delete(0, tk.END)
            self.entry_nombre_prog.focus()
            self.actualizar_vista()
            if self.equipo.esta_lleno():
                messagebox.showinfo(
                    "Equipo Completo",
                    "Se ha completado el cupo máximo del equipo.",
                )

        except (ValueError, OverflowError) as e:
            messagebox.showerror("Excepción Capturada", str(e))

    def actualizar_vista(self):
        if self.equipo is None:
            return
        integrantes = "\n".join(
            f"   {i + 1}. {prog}" for i, prog in enumerate(self.equipo.programadores)
        )
        if not integrantes:
            integrantes = "   (Sin integrantes registrados)"

        estado_cupo = "COMPLETO" if self.equipo.esta_lleno() else "INCOMPLETO"
        texto = (
            f"Equipo: {self.equipo.nombre_equipo} ({self.equipo.universidad})\n"
            f"Lenguaje: {self.equipo.lenguaje_programacion} | "
            f"Cupo: {len(self.equipo.programadores)}/{self.equipo.tamano_equipo} [{estado_cupo}]\n"
            f"Integrantes:\n{integrantes}"
        )
        self.lbl_info.config(text=texto)
    def reiniciar(self):
        self.equipo = None
        self._estado_form_equipo("normal")
        for entry in (
            self.entry_equipo,
            self.entry_universidad,
            self.entry_lenguaje,
            self.entry_tamano,
            self.entry_nombre_prog,
            self.entry_apellidos_prog,
        ):
            entry.config(state="normal")
            entry.delete(0, tk.END)
        self._estado_form_programador("disabled")
        self.lbl_info.config(text="Aún no se ha creado ningún equipo.")

    def _estado_form_equipo(self, estado: str):
        self.entry_equipo.config(state=estado)
        self.entry_universidad.config(state=estado)
        self.entry_lenguaje.config(state=estado)
        self.entry_tamano.config(state=estado)
        self.btn_crear_equipo.config(state=estado)

    def _estado_form_programador(self, estado: str):
        self.entry_nombre_prog.config(state=estado)
        self.entry_apellidos_prog.config(state=estado)
        self.btn_anadir_prog.config(state=estado)

if __name__ == "__main__":
    app = VentanaMaraton()
    app.mainloop()