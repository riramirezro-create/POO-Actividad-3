import tkinter as tk
from tkinter import messagebox
import math
import os


class Cilindro:
    def __init__(self, radio, altura):
        self.radio = radio
        self.altura = altura

    def calcular_volumen(self):
        return math.pi * math.pow(self.radio, 2) * self.altura

    def calcular_superficie(self):
        area_lateral = 2 * math.pi * self.radio * self.altura
        area_base = 2 * math.pi * math.pow(self.radio, 2)
        return area_lateral + area_base

class Esfera:
    def __init__(self, radio):
        self.radio = radio

    def calcular_volumen(self):
        return (4.0 / 3.0) * math.pi * math.pow(self.radio, 3)

    def calcular_superficie(self):
        return 4.0 * math.pi * math.pow(self.radio, 2)

class Piramide:
    def __init__(self, base, altura, apotema):
        self.base = base
        self.altura = altura
        self.apotema = apotema

    def calcular_volumen(self):
        return (math.pow(self.base, 2) * self.altura) / 3.0

    def calcular_superficie(self):
        area_base = math.pow(self.base, 2)
        area_lateral = 2.0 * self.base * self.apotema
        return area_base + area_lateral


class Cubo:
    def __init__(self, lado):
        self.lado = lado

    def calcular_volumen(self):
        return math.pow(self.lado, 3)

    def calcular_superficie(self):
        return 6.0 * math.pow(self.lado, 2)

class Prisma:
    def __init__(self, base, altura, profundidad):
        self.base = base
        self.altura = altura
        self.profundidad = profundidad

    def calcular_volumen(self):
        return self.base * self.altura * self.profundidad

    def calcular_superficie(self):
        return 2.0 * (self.base * self.altura + self.base * self.profundidad + self.altura * self.profundidad)




class VentanaFigura(tk.Toplevel):
    """Clase base para evitar repetir código en cada ventana secundaria"""
    def __init__(self, parent, titulo, img_path):
        super().__init__(parent)
        self.title(titulo)
        self.geometry("280x380")
        self.resizable(False, False)
        
        
        self.lbl_img = tk.Label(self, text="[Imagen no encontrada]", bg="lightgray")
        self.lbl_img.place(x=40, y=10, width=200, height=100)
        
        
        if os.path.exists(img_path):
            try:
                self.img = tk.PhotoImage(file=img_path)
                self.lbl_img.config(image=self.img, text="")
            except tk.TclError:
                self.lbl_img.config(text="[Formato de imagen no válido]")

class VentanaCilindro(VentanaFigura):
    def __init__(self, parent):
        super().__init__(parent, "Cilindro", "cilindro.png")
        
        tk.Label(self, text="Radio (cms):").place(x=20, y=120)
        self.campo_radio = tk.Entry(self)
        self.campo_radio.place(x=120, y=120, width=120)

        tk.Label(self, text="Altura (cms):").place(x=20, y=150)
        self.campo_altura = tk.Entry(self)
        self.campo_altura.place(x=120, y=150, width=120)

        tk.Button(self, text="Calcular", command=self.calcular).place(x=100, y=190, width=80)

        self.lbl_volumen = tk.Label(self, text="Volumen (cm3): ")
        self.lbl_volumen.place(x=20, y=240)
        self.lbl_superficie = tk.Label(self, text="Superficie (cm2): ")
        self.lbl_superficie.place(x=20, y=270)

    def calcular(self):
        try:
            r = float(self.campo_radio.get().replace(',', '.'))
            h = float(self.campo_altura.get().replace(',', '.'))
            cilindro = Cilindro(r, h)
            self.lbl_volumen.config(text=f"Volumen (cm3): {cilindro.calcular_volumen():.2f}")
            self.lbl_superficie.config(text=f"Superficie (cm2): {cilindro.calcular_superficie():.2f}")
        except ValueError:
            messagebox.showerror("Error", "Campo nulo o error en formato de número")

class VentanaEsfera(VentanaFigura):
    def __init__(self, parent):
        super().__init__(parent, "Esfera", "esfera.png")
        tk.Label(self, text="Radio (cms):").place(x=20, y=120)
        self.campo_radio = tk.Entry(self)
        self.campo_radio.place(x=120, y=120, width=120)

        tk.Button(self, text="Calcular", command=self.calcular).place(x=100, y=160, width=80)

        self.lbl_volumen = tk.Label(self, text="Volumen (cm3): ")
        self.lbl_volumen.place(x=20, y=210)
        self.lbl_superficie = tk.Label(self, text="Superficie (cm2): ")
        self.lbl_superficie.place(x=20, y=240)

    def calcular(self):
        try:
            r = float(self.campo_radio.get().replace(',', '.'))
            esfera = Esfera(r)
            self.lbl_volumen.config(text=f"Volumen (cm3): {esfera.calcular_volumen():.2f}")
            self.lbl_superficie.config(text=f"Superficie (cm2): {esfera.calcular_superficie():.2f}")
        except ValueError:
            messagebox.showerror("Error", "Campo nulo o error en formato de número")

class VentanaPiramide(VentanaFigura):
    def __init__(self, parent):
        super().__init__(parent, "Pirámide", "piramide.png")
        tk.Label(self, text="Base (cms):").place(x=20, y=120)
        self.campo_base = tk.Entry(self)
        self.campo_base.place(x=120, y=120, width=120)

        tk.Label(self, text="Altura (cms):").place(x=20, y=150)
        self.campo_altura = tk.Entry(self)
        self.campo_altura.place(x=120, y=150, width=120)

        tk.Label(self, text="Apotema (cms):").place(x=20, y=180)
        self.campo_apotema = tk.Entry(self)
        self.campo_apotema.place(x=120, y=180, width=120)

        tk.Button(self, text="Calcular", command=self.calcular).place(x=100, y=220, width=80)

        self.lbl_volumen = tk.Label(self, text="Volumen (cm3): ")
        self.lbl_volumen.place(x=20, y=270)
        self.lbl_superficie = tk.Label(self, text="Superficie (cm2): ")
        self.lbl_superficie.place(x=20, y=300)

    def calcular(self):
        try:
            b = float(self.campo_base.get().replace(',', '.'))
            h = float(self.campo_altura.get().replace(',', '.'))
            a = float(self.campo_apotema.get().replace(',', '.'))
            piramide = Piramide(b, h, a)
            self.lbl_volumen.config(text=f"Volumen (cm3): {piramide.calcular_volumen():.2f}")
            self.lbl_superficie.config(text=f"Superficie (cm2): {piramide.calcular_superficie():.2f}")
        except ValueError:
            messagebox.showerror("Error", "Campo nulo o error en formato de número")

class VentanaCubo(VentanaFigura):
    def __init__(self, parent):
        super().__init__(parent, "Cubo", "cubo.png")
        tk.Label(self, text="Lado (cms):").place(x=20, y=120)
        self.campo_lado = tk.Entry(self)
        self.campo_lado.place(x=120, y=120, width=120)

        tk.Button(self, text="Calcular", command=self.calcular).place(x=100, y=160, width=80)

        self.lbl_volumen = tk.Label(self, text="Volumen (cm3): ")
        self.lbl_volumen.place(x=20, y=210)
        self.lbl_superficie = tk.Label(self, text="Superficie (cm2): ")
        self.lbl_superficie.place(x=20, y=240)

    def calcular(self):
        try:
            l = float(self.campo_lado.get().replace(',', '.'))
            cubo = Cubo(l)
            self.lbl_volumen.config(text=f"Volumen (cm3): {cubo.calcular_volumen():.2f}")
            self.lbl_superficie.config(text=f"Superficie (cm2): {cubo.calcular_superficie():.2f}")
        except ValueError:
            messagebox.showerror("Error", "Campo nulo o error en formato de número")

class VentanaPrisma(VentanaFigura):
    def __init__(self, parent):
        super().__init__(parent, "Prisma", "prisma.png")
        tk.Label(self, text="Base (cms):").place(x=20, y=120)
        self.campo_base = tk.Entry(self)
        self.campo_base.place(x=120, y=120, width=120)

        tk.Label(self, text="Altura (cms):").place(x=20, y=150)
        self.campo_altura = tk.Entry(self)
        self.campo_altura.place(x=120, y=150, width=120)

        tk.Label(self, text="Profundidad:").place(x=20, y=180)
        self.campo_prof = tk.Entry(self)
        self.campo_prof.place(x=120, y=180, width=120)

        tk.Button(self, text="Calcular", command=self.calcular).place(x=100, y=220, width=80)

        self.lbl_volumen = tk.Label(self, text="Volumen (cm3): ")
        self.lbl_volumen.place(x=20, y=270)
        self.lbl_superficie = tk.Label(self, text="Superficie (cm2): ")
        self.lbl_superficie.place(x=20, y=300)

    def calcular(self):
        try:
            b = float(self.campo_base.get().replace(',', '.'))
            h = float(self.campo_altura.get().replace(',', '.'))
            p = float(self.campo_prof.get().replace(',', '.'))
            prisma = Prisma(b, h, p)
            self.lbl_volumen.config(text=f"Volumen (cm3): {prisma.calcular_volumen():.2f}")
            self.lbl_superficie.config(text=f"Superficie (cm2): {prisma.calcular_superficie():.2f}")
        except ValueError:
            messagebox.showerror("Error", "Campo nulo o error en formato de número")



class VentanaPrincipal(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Figuras Geométricas")
        self.geometry("350x160")
        self.resizable(False, False)
        self.eval('tk::PlaceWindow . center')

        
        tk.Button(self, text="Cilindro", command=lambda: VentanaCilindro(self)).place(x=20, y=50, width=80)
        tk.Button(self, text="Esfera", command=lambda: VentanaEsfera(self)).place(x=125, y=50, width=80)
        tk.Button(self, text="Pirámide", command=lambda: VentanaPiramide(self)).place(x=225, y=50, width=80)
        
       
        tk.Button(self, text="Cubo", command=lambda: VentanaCubo(self)).place(x=70, y=90, width=80)
        tk.Button(self, text="Prisma", command=lambda: VentanaPrisma(self)).place(x=175, y=90, width=80)

if __name__ == "__main__":
    app = VentanaPrincipal()
    app.mainloop()