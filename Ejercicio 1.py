import tkinter as tk
from tkinter import messagebox
import math


class Notas:
    def __init__(self):
        self.listaNotas = [0.0] * 5

    def calcularPromedio(self):
        suma = sum(self.listaNotas)
        return suma / len(self.listaNotas)

    def calcularDesviacion(self):
        prom = self.calcularPromedio()
        suma = 0.0
        for nota in self.listaNotas:
            suma += math.pow(nota - prom, 2)
        return math.sqrt(suma / len(self.listaNotas))

    def calcularMenor(self):
        menor = self.listaNotas[0]
        for nota in self.listaNotas:
            if nota < menor:
                menor = nota
        return menor

    def calcularMayor(self):
        mayor = self.listaNotas[0]
        for nota in self.listaNotas:
            if nota > mayor:
                mayor = nota
        return mayor


class VentanaPrincipal(tk.Tk):
    def __init__(self):
        super().__init__()
        self.inicio()

    def inicio(self):
        self.title("Notas")
        self.geometry("280x380")
        self.resizable(False, False)
        self.eval('tk::PlaceWindow . center')

        
        tk.Label(self, text="Nota 1:").place(x=20, y=20, width=135, height=23)
        self.campoNota1 = tk.Entry(self)
        self.campoNota1.place(x=105, y=20, width=135, height=23)

        tk.Label(self, text="Nota 2:").place(x=20, y=50, width=135, height=23)
        self.campoNota2 = tk.Entry(self)
        self.campoNota2.place(x=105, y=50, width=135, height=23)

        tk.Label(self, text="Nota 3:").place(x=20, y=80, width=135, height=23)
        self.campoNota3 = tk.Entry(self)
        self.campoNota3.place(x=105, y=80, width=135, height=23)

        tk.Label(self, text="Nota 4:").place(x=20, y=110, width=135, height=23)
        self.campoNota4 = tk.Entry(self)
        self.campoNota4.place(x=105, y=110, width=135, height=23)

        tk.Label(self, text="Nota 5:").place(x=20, y=140, width=135, height=23)
        self.campoNota5 = tk.Entry(self)
        self.campoNota5.place(x=105, y=140, width=135, height=23)

      
        self.btnCalcular = tk.Button(self, text="Calcular", command=self.actionPerformed_Calcular)
        self.btnCalcular.place(x=20, y=170, width=100, height=23)

        self.btnLimpiar = tk.Button(self, text="Limpiar", command=self.actionPerformed_Limpiar)
        self.btnLimpiar.place(x=125, y=170, width=80, height=23)

      
        self.lblPromedio = tk.Label(self, text="Promedio = ", anchor="w")
        self.lblPromedio.place(x=20, y=210, width=200, height=23)

        self.lblDesviacion = tk.Label(self, text="Desviación = ", anchor="w")
        self.lblDesviacion.place(x=20, y=240, width=200, height=23)

        self.lblMayor = tk.Label(self, text="Nota mayor = ", anchor="w")
        self.lblMayor.place(x=20, y=270, width=200, height=23)

        self.lblMenor = tk.Label(self, text="Nota menor = ", anchor="w")
        self.lblMenor.place(x=20, y=300, width=200, height=23)

 
    def validarDatos(self):
        campos = [self.campoNota1, self.campoNota2, self.campoNota3, self.campoNota4, self.campoNota5]
        
        
        for i, campo in enumerate(campos):
            if not campo.get().strip():
                messagebox.showwarning("Faltan datos", f"Es obligatorio ingresar la Nota {i+1}.")
                return False 
        
       
        try:
            for campo in campos:
                float(campo.get().replace(',', '.'))
        except ValueError:
            messagebox.showerror("Error de formato", "Se han ingresado datos que no son numéricos.\nPor favor verifica las notas.")
            return False 
            
        return True 

   
    def actionPerformed_Calcular(self):
      
        if not self.validarDatos():
            return 
            
        campos = [self.campoNota1, self.campoNota2, self.campoNota3, self.campoNota4, self.campoNota5]
        notas_obj = Notas()

       
        for i in range(5):
            notas_obj.listaNotas[i] = float(campos[i].get().replace(',', '.'))

       
        self.lblPromedio.config(text=f"Promedio = {notas_obj.calcularPromedio():.2f}")
        self.lblDesviacion.config(text=f"Desviación estándar = {notas_obj.calcularDesviacion():.2f}")
        self.lblMayor.config(text=f"Valor mayor = {notas_obj.calcularMayor():.1f}")
        self.lblMenor.config(text=f"Valor menor = {notas_obj.calcularMenor():.1f}")

    def actionPerformed_Limpiar(self):
        self.campoNota1.delete(0, tk.END)
        self.campoNota2.delete(0, tk.END)
        self.campoNota3.delete(0, tk.END)
        self.campoNota4.delete(0, tk.END)
        self.campoNota5.delete(0, tk.END)
        
        self.lblPromedio.config(text="Promedio = ")
        self.lblDesviacion.config(text="Desviación = ")
        self.lblMayor.config(text="Nota mayor = ")
        self.lblMenor.config(text="Nota menor = ")


class Principal:
    @staticmethod
    def main():
        miVentanaPrincipal = VentanaPrincipal()
        miVentanaPrincipal.mainloop()

if __name__ == "__main__":
    Principal.main()
