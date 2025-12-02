from tkinter import *
from tkinter import messagebox
from controler import controlador
from tkinter import ttk
#interfaz o view
#ACTUALIZAR 
"""
1er Diciembre
1)
"""
class Vistas:
    def __init__(self,ventana):
        ventana.title("Gestion de notas")
        ventana.geometry("700x500")
        #ventana.resizable(False,False) #para que la pantalla este fija
        self.interfaz(ventana)

    def borrarPantalla(self,ventana):
        for widget in ventana.winfo_children():
            widget.destroy()

    def menu_principal(self,ventana):
        self.borrarPantalla(ventana)
        ventana.geometry("700x500")
        txt_mp=Label(ventana,text="Menu Principal")
        txt_mp.pack(pady=7)
        btn1=Button(ventana,text="1.-Coches",command=lambda:self.menu_acciones("Coche",ventana))
        btn1.pack(pady=7)
        btn2=Button(ventana,text="2.-Camiones", command=lambda:self.menu_acciones("Camion",ventana))
        btn2.pack(pady=7)
        btn3=Button(ventana,text="3.-Camionetas",command=lambda:self.menu_acciones("Camioneta",ventana))
        btn3.pack(pady=7)
        btn4=Button(ventana,text="4.-Salir",command=ventana.quit)
        btn4.pack(pady=7)

    def menu_acciones(self,tipo,ventana):
        self.borrarPantalla(ventana)
        ventana.geometry("700x500")
        txt_mp=Label(ventana,text=f"Menu de {tipo}")
        txt_mp.pack(pady=7)
        btn_add=Button(ventana,text="1.-Agregar",command=self.asignacion_de_funcion(tipo,"insertar",ventana))
        btn_add.pack(pady=7)
        btn_show=Button(ventana,text="2.-Consultar", command=self.asignacion_de_funcion(tipo,"consultar",ventana))
        btn_show.pack(pady=7)
        btn_update=Button(ventana,text="3.-Modificar",command=self.asignacion_de_funcion(tipo,"cambiar",ventana))
        btn_update.pack(pady=7)
        btn_delete=Button(ventana,text="4.-Eliminar",command=self.asignacion_de_funcion(tipo,"eliminar",ventana))
        btn_delete.pack(pady=7)
        btn_back=Button(ventana,text="5.-Volver",command=lambda:self.menu_principal(ventana))
        btn_back.pack(pady=7)
    
    def asignacion_de_funcion(self,tipo,accion):
        if tipo=="Coche":
            if accion=="insertar":
                self.insertar_autos()
            elif accion=="consultar":
                self.consultar_autos()
            elif accion=="cambiar":
                self.cambiar_autos()
            elif accion=="eliminar":
                self.eliminar_autos()



    def insertar_autos(self,tipo,ventana):
        ventana.geometry("1000x1000")
        self.borrarPantalla(ventana)
        lbl_titulo=Label(ventana,text=f"Agregar {tipo}")
        lbl_titulo.pack(pady=7)
        lbl_marca=Label(ventana,text="Ingrese la marca: ")
        lbl_marca.pack(pady=7)
        txt_marca=Entry(ventana,width=25,justify="left")
        txt_marca.pack(pady=7) 
        lbl_color=Label(ventana,text="Ingrese el color: ")
        lbl_color.pack(pady=7)
        txt_color=Entry(ventana,width=25,justify="left")
        txt_color.pack(pady=7)
        lbl_modelo=Label(ventana,text="Ingrese el modelo: ")
        lbl_modelo.pack(pady=7)
        txt_modelo=Entry(ventana,width=25,justify="left")
        txt_modelo.pack(pady=7)
        lbl_velocidad=Label(ventana,text="Ingrese la velocidad: ")
        lbl_velocidad.pack(pady=7)
        txt_velocidad=Entry(ventana,width=25,justify="left")
        txt_velocidad.pack(pady=7)
        lbl_caballaje=Label(ventana,text="Ingrese el caballaje: ")
        lbl_caballaje.pack(pady=7)
        txt_caballaje=Entry(ventana,width=25,justify="left")
        txt_caballaje.pack(pady=7)
        lbl_plazas=Label(ventana,text="Ingrese las plazas: ")
        lbl_plazas.pack(pady=7)
        txt_plazas=Entry(ventana,width=25,justify="left")
        txt_plazas.pack(pady=7)
        btnen=Button(ventana,text="Agregar",command=lambda:controlador.Controlador_coches.crear(txt_marca.get(),txt_color.get(),txt_modelo.get(),int(txt_velocidad.get()),int(txt_caballaje.get()),int(txt_plazas.get())))
        btnen.pack(pady=7)
        btnregr = Button(ventana, text="Regresar", command=lambda:self.menu_crud(ventana))
        btnregr.pack()
        

    def cambiar_autos(self,tipo,ventana):
        ventana.geometry("1000x1000")
        self.borrarPantalla(ventana)
        lbl_titulo=Label(ventana,text=f"Actualizar {tipo}")
        lbl_titulo.pack(pady=7)
        lbl_id=Label(ventana,text=f"Ingrese el id de {tipo}: ")
        lbl_id.pack(pady=7)
        txt_id=Entry(ventana,width=25,justify="left")
        txt_id.pack(pady=7) 
        lbl_marca=Label(ventana,text="Ingrese la nueva marca: ")
        lbl_marca.pack(pady=7)
        txt_marca=Entry(ventana,width=25,justify="left")
        txt_marca.pack(pady=7) 
        lbl_color=Label(ventana,text="Ingrese el nuevo color: ")
        lbl_color.pack(pady=7)
        txt_color=Entry(ventana,width=25,justify="left")
        txt_color.pack(pady=7)
        lbl_modelo=Label(ventana,text="Ingrese el nuevo modelo: ")
        lbl_modelo.pack(pady=7)
        txt_modelo=Entry(ventana,width=25,justify="left")
        txt_modelo.pack(pady=7)
        lbl_velocidad=Label(ventana,text="Ingrese la nueva velocidad: ")
        lbl_velocidad.pack(pady=7)
        txt_velocidad=Entry(ventana,width=25,justify="left")
        txt_velocidad.pack(pady=7)
        lbl_caballaje=Label(ventana,text="Ingrese el nuevo caballaje: ")
        lbl_caballaje.pack(pady=7)
        txt_caballaje=Entry(ventana,width=25,justify="left")
        txt_caballaje.pack(pady=7)
        lbl_plazas=Label(ventana,text="Ingrese la nueva cantidad de plazas: ")
        lbl_plazas.pack(pady=7)
        txt_plazas=Entry(ventana,width=25,justify="left")
        txt_plazas.pack(pady=7)
        btnen=Button(ventana,text="Actualizar",command=lambda:controlador.Controlador_coches.actualizar(txt_marca.get(),txt_color.get(),txt_modelo.get(),int(txt_velocidad.get()),int(txt_caballaje.get()),int(txt_plazas.get()),txt_id.get()))
        btnen.pack(pady=7)
        btnregr = Button(ventana, text="Regresar", command=lambda:self.menu_crud(ventana))
        btnregr.pack()

    def consultar_autos(self,ventana):
        self.borrarPantalla(ventana)
        ventana.geometry("1000x700")
        titulos=("id","marca","color","modelo","velocidad","caballaje","plazas")
        registros=controlador.Controlador_coches.mostrar()
        self.tabla = ttk.Treeview(ventana, columns=titulos, show='headings')
        for item in self.tabla.get_children():
            self.tabla.delete(item)

        for fila in registros:
            self.tabla.insert("", "end", values=fila)
        
        for col in titulos:
            self.tabla.heading(col, text=col)
            self.tabla.column(col, width=150,anchor="center")
        self.tabla.pack(fill="both", expand=True, padx=10, pady=10)
        btnregr = Button(ventana, text="Regresar", command=lambda:self.menu_crud(ventana))
        btnregr.pack()

    def eliminar_autos(self,ventana):
        ventana.geometry("1000x1000")
        self.borrarPantalla(ventana)
        lbl_titulo=Label(ventana,text="Eliminar autos")
        lbl_titulo.pack(pady=7)
        lbl_id=Label(ventana,text="Ingrese el ID del Auto a eliminar: ")
        lbl_id.pack(pady=7)
        txt_id=Entry(ventana,width=25,justify="left")
        txt_id.pack(pady=7) 
        btnen=Button(ventana,text="Agregar",command=lambda:controlador.Controlador_coches.crear(txt_id.get()))
        btnen.pack(pady=7)
        btnregr = Button(ventana, text="Regresar", command=lambda:self.menu_acciones(ventana))
        btnregr.pack()

