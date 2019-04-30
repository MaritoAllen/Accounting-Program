'''
Created on Apr 30, 2019

@author: Mario
'''
import Tkinter as tk

class Logueo:
    def __init__(self,master):
        frame = tk.Frame(master)
        frame.pack()
        
        self.L1 = tk.Label(frame, text='Usuario: ')
        self.L1.grid(row=0,column=0, sticky='W')
        
        self.L2 = tk.Label(frame, text='Contrasena: ')
        self.L2.grid(row=1,column=0, sticky='W')
        
        self.E1 = tk.Entry(frame)
        self.E1.grid(row=0,column=1, sticky='W')
        
        self.E2 = tk.Entry(frame)
        self.E2.grid(row=1,column=1, sticky='W')
        
        self.B1 = tk.Button(frame, text='Iniciar Sesion', command=self.vmenu)
        self.B1.grid(row=0, column=2, columnspan=2, rowspan=2)
        
    def vmenu(self):
        self.v2 = tk.Toplevel(v1)
        self.v2.title('Menu')
        
        self.L3 = tk.Label(self.v2, text='Que transa mama')
        self.L3.pack()
        
        self.B2 = tk.Button(self.v2, text='Salir', command=self.v2.quit)
        self.B2.pack()
        
v1 = tk.Tk()
v1.title('Inicio')
logueo=Logueo(v1)

v1.mainloop()