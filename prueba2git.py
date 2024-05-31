import tkinter as tk 

def si():
    ventana.destroy()
    ventanaSI = tk.Tk()
    ventanaSI.title("INICIO")
    ventanaSI.geometry("400x200")
    ventanaSI.configure(bg="black")
    label = tk.Label(ventanaSI, text="Muchas gracias por confiar\n empesemos con la prueba de git\n cual es tu nommbre?")
    entrynombre=tk.Entry(ventanaSI)
    label2 = tk.Label(ventanaSI, text="Listo para inciciar?", bg="turquoise2", fg="white", font=("Arial", 15))
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
label = tk.Label(ventana, text="Bienvenido a la prueba de git",bg="black", fg="white" ,font=("Arial", 20))    
label2 = tk.Label(ventana, text="Listo para inciciar?", bg="turquoise2", fg="white", font=("Arial", 15))

botonSI=tk.Button(ventana, text="SI",width=6, height=3,bg="lightblue",command=si)
botonNO=tk.Button(ventana, text="NO",width=6, height=3,bg="lightblue",command=no)

label.pack()
label2.pack()
botonSI.pack()
botonNO.pack() 



ventana.mainloop()
