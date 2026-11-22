import tkinter as tk

class Excepcion():
    def try1(self):
        res = []
        try:
            res.append("Entrando al primer try")
            divcero = 1000/0
        except:
            res.append("Division por cero")
        finally:
            res.append("Entrando al primer finally")
        return res
    def try2(self):
        res = []
        try:
            res.append("Entrando al segundo try")
            objeto = None
            objeto = round(objeto)
        except:
            res.append("Ocurrio una excepcion")
        finally:
            res.append("Entrando al segundo finally")
        return res   
class Ventana(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Pruebas de excepciones")
        self.resizable(False, False)
        self.boton()
        self.resultados()
    def boton(self):
        btnejecutar = tk.Button(self, text="ejecutar", command=self.ejecutar)
        btnejecutar.grid(row = 0, column = 0, pady = "5", padx = "5")
        btnborrar = tk.Button(self, text="Borrar", command=self.borrar)
        btnborrar.grid(row = 0, column = 1)
    def resultados(self):
        self.restry1 = tk.Label(self, text="Primer try: ")
        self.restry1.grid(row = 2, column = 0, pady = "10", padx = "10")
        self.restry2 = tk.Label(self, text="Segundo try: ")
        self.restry2.grid(row = 3, column = 0, pady = "10", padx = "10")
    def ejecutar(self):
        exc = Excepcion()
        res1 = exc.try1()
        res2 = exc.try2()
        self.restry1.config(text="Primer try:\n" + "\n".join(res1))
        self.restry2.config(text="Segundo try:\n" + "\n".join(res2))
    def borrar(self):
        self.restry1.config(text="Primer try: ") 
        self.restry2.config(text="Segundo try: ")

ven = Ventana()
ven.mainloop()



            
