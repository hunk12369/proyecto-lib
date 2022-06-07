#Thaissssssssssss revisaa el codigo!!!!!!!!!!
from tkinter import *
class Aplicacon(Frame):
    def decirHola(self):
        print ("Hola a todos")
    def crearWidgets(self):
        self.SALIR = Button(self)
        self.SALIR["text"] = "SALIR"
        self.SALIR["fg"]   = "blue"
        self.SALIR["command"] =  self.quit

        self.SALIR.pack({"side": "right"})

        self.hola = Button(self)
        self.hola["text"] = "HOLAAA",
        self.hola["command"] = self.decirHola

        self.hola.pack({"side": "left"})
    def __init__(self, master=None):
        Frame.__init__(self,master) #Pasa el frame para iniciarlo
        self.pack()
        self.crearWidgets()
raiz=Tk()#Crea el frame
app=Aplicacon(master=raiz)
app.mainloop()#Inicia la ventana
raiz.destroy()#Destruye el frame?