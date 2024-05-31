import tkinter as tk 

def si():
    ventana.destroy()
    ventanaSI = tk.Tk()
    ventanaSI.title("INICIO")
    ventanaSI.geometry("400x200")
    ventanaSI.configure(bg="black")
    label = tk.Label(ventanaSI, text="Muchas gracias por confiar\n empesemos con la prueba de git\n cual es tu nommbre?")
    entrynombre=tk.Entry(ventanaSI)
    boton=tk.Button(ventanaSI, text="continuar")
    
    label.pack()
    entrynombre.pack()
    boton.pack()
    ventanaSI.mainloop()
    
def no():
    ventana.destroy()
    ventanaNO = tk.Tk()
    ventanaNO.title("INICIO")
    ventanaNO.geometry("400x200")
    ventanaNO.configure(bg="black")
    label = tk.Label(ventanaNO, text="Muchas gracias por confiar\n espero que te animes a probar git\n hasta luego")
    boton=tk.Button(ventanaNO, text="salir", command=ventanaNO.destroy)
    
    label.pack()
    boton.pack()
    ventanaNO.mainloop()


ventana = tk.Tk()
ventana.title("primera ventana")
ventana.geometry("400x200")
ventana.configure(bg="black")
label = tk.Label(ventana, text="Bienvenido a la prueba de git")    
label2 = tk.Label(ventana, text="Listo para inciciar?")

botonSI=tk.Button(ventana, text="SI", command=si)
botonNO=tk.Button(ventana, text="NO", command=no)

label.pack()
label2.pack()
botonSI.pack()
botonNO.pack() 



ventana.mainloop()
