from tkinter import *
from controller.controlador import Controlador
class Vistas:
    @staticmethod
    def borrarPantalla(ventana):
        for w in ventana.winfo_children(): w.destroy()
    
    @staticmethod
    def interfaz(ventana):
        Vistas.borrarPantalla(ventana)
        Label(ventana ,text="Menu Principal").pack(pady=5)
        Button(ventana,text="Autos",command=lambda:Vistas.menu_autos(ventana)).pack(pady=5)
        Button(ventana,text="Camionetas",command=lambda:Vistas.menu_camionetas(ventana)).pack(pady=5)
        Button(ventana,text="Camiones",command=lambda:Vistas.menu_camiones(ventana)).pack(pady=5)
        Button(ventana,text="Salir",command=ventana.quit).pack(pady=5)
    
    @staticmethod
    def menu_autos(ventana):
        Vistas.borrarPantalla(ventana)
        Label(ventana,text="Menú Autos").pack(pady=5)
        Button(ventana,text="Insertar",command=lambda:Vistas.insertar_autos(ventana)).pack(pady=5)
        Button(ventana,text="Consultar",command=lambda:Vistas.consultar_autos(ventana)).pack(pady=5)
        Button(ventana,text="Modificar",command=lambda:Vistas.modificar_autos(ventana)).pack(pady=5)
        Button(ventana,text="Eliminar",command=lambda:Vistas.eliminar_autos(ventana)).pack(pady=5)
        Button(ventana,text="Regresar",command=lambda:Vistas.interfaz(ventana)).pack(pady=5)
   
    @staticmethod
    def insertar_autos(ventana):
        Vistas.borrarPantalla(ventana)
        Label(ventana,text="Insertar Auto").pack(pady=5)
        lbl=["Marca","Color","Modelo","Velocidad","Caballaje","Plazas"]; ents=[]
        for t in lbl:
            Label(ventana,text=t).pack(); e=Entry(ventana); e.pack(); ents.append(e)
        Button(ventana,text="Guardar",width=20,command=lambda:Controlador.insertar_auto(*[e.get() for e in ents])).pack(pady=5)
        Button(ventana,text="Regresar",width=20,command=lambda:Vistas.menu_autos(ventana)).pack(pady=5)
    
    @staticmethod
    def consultar_autos(ventana):
        Vistas.borrarPantalla(ventana)
        Label(ventana,text="Autos Registrados").pack(pady=5)
        datos=Controlador.consultar_auto("all")
        if not datos:
            Label(ventana,text="No hay autos registrados").pack(pady=5)
        else:
            for a in datos:
                Label(ventana,text=f"id {a[0]} {a[1]}  {a[2]} {a[3]} {a[4]} {a[5]} {a[6]}").pack()
        Button(ventana,text="Regresar",width=20,command=lambda:Vistas.menu_autos(ventana)).pack(pady=5)
    
    @staticmethod
    def modificar_autos(ventana):
        Vistas.borrarPantalla(ventana)
        Label(ventana,text="Modificar Auto").pack(pady=5)
        Label(ventana,text="ID").pack(); e=Entry(ventana); e.pack()
        Button(ventana,text="Buscar",command=lambda:Vistas.modificar_form(ventana,e.get())).pack(pady=5)
        Button(ventana,text="Regresar",command=lambda:Vistas.menu_autos(ventana)).pack(pady=5)
    
    @staticmethod
    def modificar_form(ventana,id):
        auto=Controlador.consultar_auto(id)
        if not auto:
            Vistas.borrarPantalla(ventana)
            Label(ventana,text="No existe ese ID").pack(pady=5)
            Button(ventana,text="Regresar",width=20,command=lambda: Vistas.modificar_autos(ventana)).pack(pady=5)
            return
        if isinstance(auto,list) and len(auto)>0: auto=auto[0]
        Vistas.borrarPantalla(ventana)
        Label(ventana,text=f"Modificar Auto id {id}").pack(pady=5)
        lbl=["Marca","Color","Modelo","Velocidad","Caballaje","Plazas"]; ents=[]
        for i,t in enumerate(lbl):
            Label(ventana,text=t).pack(); e=Entry(ventana); e.insert(0,str(auto[i+1])); e.pack(); ents.append(e)
        Button(ventana,text="Guardar Cambios",width=20,command=lambda: Controlador.modificar_auto(*[e.get() for e in ents],id)).pack(pady=5)
        Button(ventana,text="Regresar",width=20,command=lambda: Vistas.menu_autos(ventana)).pack(pady=5)

    @staticmethod
    def eliminar_autos(ventana):
        Vistas.borrarPantalla(ventana)
        Label(ventana,text="Eliminar Auto").pack(pady=5)
        Label(ventana,text="ID").pack(); e=Entry(ventana); e.pack()
        Button(ventana,text="Buscar",width=20,command=lambda:Vistas.eliminar_confirmar(ventana,e.get())).pack(pady=5)
        Button(ventana,text="Regresar",width=20,command=lambda:Vistas.menu_autos(ventana)).pack(pady=5)

    @staticmethod
    def eliminar_confirmar(ventana,id):
        auto=Controlador.consultar_auto(id)
        if not auto:
            Vistas.borrarPantalla(ventana); Label(ventana,text="No existe ese ID").pack(pady=5)
            Button(ventana,text="Regresar",width=20,command=lambda:Vistas.eliminar_autos(ventana)).pack(pady=5); return
        auto=auto[0]
        Vistas.borrarPantalla(ventana)
        Label(ventana,text=f"¿Eliminar auto? id {auto[0]} {auto[1]} {auto[2]} {auto[3]}").pack(pady=10)
        Button(ventana,text="Sí",width=20,command=lambda:Controlador.eliminar_auto(id)).pack(pady=5)
        Button(ventana,text="Regresar",width=20,command=lambda:Vistas.menu_autos(ventana)).pack(pady=5)




  #camionetas
    @staticmethod
    def menu_camionetas(ventana):
        Vistas.borrarPantalla(ventana)
        Label(ventana,text="Menú Camionetas").pack(pady=5)
        Button(ventana,text="Insertar",command=lambda:Vistas.insertar_camionetas(ventana)).pack(pady=5)
        Button(ventana,text="Consultar",width=20,command=lambda:Vistas.consultar_camionetas(ventana)).pack(pady=5)
        Button(ventana,text="Modificar",width=20,command=lambda:Vistas.modificar_camionetas(ventana)).pack(pady=5)
        Button(ventana,text="Eliminar",width=20,command=lambda:Vistas.eliminar_camionetas(ventana)).pack(pady=5)
        Button(ventana,text="Regresar",width=20,command=lambda:Vistas.interfaz(ventana)).pack(pady=5)


    @staticmethod
    def insertar_camionetas(ventana):
        Vistas.borrarPantalla(ventana)
        Label(ventana,text="Insertar Camioneta").pack(pady=5)
        lbls=["Marca","Color","Modelo","Velocidad","Caballaje","Plazas","Tracción"]
        ents=[]
        for t in lbls:
            Label(ventana,text=t).pack()
            e=Entry(ventana)
            e.pack()
            ents.append(e)

        Button(ventana,text="Guardar",width=20,command=lambda:
               Controlador.insertar_camioneta(*[e.get() for e in ents])).pack(pady=5)

        Button(ventana,text="Regresar",width=20,command=lambda:Vistas.menu_camionetas(ventana)).pack(pady=5)


    @staticmethod
    def consultar_camionetas(ventana):
        Vistas.borrarPantalla(ventana)
        Label(ventana,text="Camionetas Registradas").pack(pady=5)

        datos = Controlador.consultar_camioneta("all")

        if not datos:
            Label(ventana,text="No hay camionetas registradas").pack(pady=5)
        else:
            for c in datos:
                Label(
                    ventana,
                    text=f"id {c[0]}  {c[1]}  {c[2]}  {c[3]}  {c[4]}  {c[5]}  {c[6]}  {c[7]}"
                ).pack()

        Button(ventana,text="Regresar",width=20,command=lambda:Vistas.menu_camionetas(ventana)).pack(pady=5)


    @staticmethod
    def modificar_camionetas(ventana):
        Vistas.borrarPantalla(ventana)
        Label(ventana,text="Modificar Camioneta").pack(pady=5)
        Label(ventana,text="ID").pack()

        e = Entry(ventana)
        e.pack()

        Button(ventana,text="Buscar",width=20,command=lambda:
               Vistas.modificar_form_camioneta(ventana, e.get())).pack(pady=5)

        Button(ventana,text="Regresar",width=20,command=lambda:Vistas.menu_camionetas(ventana)).pack(pady=5)


    @staticmethod
    def modificar_form_camioneta(ventana,id):
        c = Controlador.consultar_camioneta(id)

        if not c:
            Vistas.borrarPantalla(ventana)
            Label(ventana,text="No existe ese ID").pack(pady=5)
            Button(ventana,text="Regresar",width=20,command=lambda:
                   Vistas.modificar_camionetas(ventana)).pack(pady=5)
            return

        if isinstance(c,list) and len(c)>0:
            c = c[0]

        Vistas.borrarPantalla(ventana)
        Label(ventana,text=f"Modificar Camioneta id {id}").pack(pady=5)

        lbls=["Marca","Color","Modelo","Velocidad","Caballaje","Plazas","Tracción"]
        ents=[]

        for i,t in enumerate(lbls):
            Label(ventana,text=t).pack()
            e = Entry(ventana)
            e.insert(0,str(c[i+1]))
            e.pack()
            ents.append(e)

        Button(
            ventana,
            text="Guardar Cambios",
            width=20,
            command=lambda: Controlador.modificar_camioneta(*[e.get() for e in ents], id)
        ).pack(pady=5)

        Button(ventana,text="Regresar",width=20,command=lambda:
               Vistas.menu_camionetas(ventana)).pack(pady=5)


    @staticmethod
    def eliminar_camionetas(ventana):
        Vistas.borrarPantalla(ventana)
        Label(ventana,text="Eliminar Camioneta").pack(pady=5)
        Label(ventana,text="ID").pack()

        e = Entry(ventana)
        e.pack()

        Button(ventana,text="Eliminar",command=lambda:
               Controlador.eliminar_camioneta(e.get())).pack(pady=5)

        Button(ventana,text="Volver",command=lambda:
               Vistas.menu_camionetas(ventana)).pack(pady=5)


    #camiones
    @staticmethod
    def menu_camiones(ventana):
        Vistas.borrarPantalla(ventana)
        Label(ventana,text="Menú Camiones").pack(pady=5)
        Button(ventana,text="Insertar",width=20,command=lambda:Vistas.insertar_camiones(ventana)).pack(pady=5)
        Button(ventana,text="Consultar",width=20,command=lambda:Vistas.consultar_camiones(ventana)).pack(pady=5)
        Button(ventana,text="Modificar",width=20,command=lambda:Vistas.modificar_camiones(ventana)).pack(pady=5)
        Button(ventana,text="Eliminar",width=20,command=lambda:Vistas.eliminar_camiones(ventana)).pack(pady=5)
        Button(ventana,text="Volver",width=20,command=lambda:Vistas.interfaz(ventana)).pack(pady=5)

    @staticmethod
    def insertar_camiones(ventana):
        Vistas.borrarPantalla(ventana)
        Label(ventana,text="Insertar Camión").pack(pady=5)
        lbl=["Marca","Color","Modelo","Velocidad","Caballaje","Plazas","Eje","CapacidadCarga"]; ents=[]
        for t in lbl:
            Label(ventana,text=t).pack()
            e=Entry(ventana); e.pack(); ents.append(e)
        Button(ventana,text="Guardar",width=20,command=lambda:Controlador.insertar_camion(*[e.get() for e in ents])).pack(pady=5)
        Button(ventana,text="Volver",width=20,command=lambda:Vistas.menu_camiones(ventana)).pack(pady=5)

    @staticmethod
    def consultar_camiones(ventana):
        Vistas.borrarPantalla(ventana)
        Label(ventana,text="Camiones Registrados").pack(pady=5)
        datos=Controlador.consultar_camion("all")
        if not datos:
            Label(ventana,text="No hay camiones registrados").pack(pady=5)
        else:
            for c in datos:
                Label(ventana,text=f"id {c[0]} {c[1]} {c[2]} {c[3]} {c[4]} {c[5]} {c[6]} {c[7]} {c[8]}").pack()
        Button(ventana,text="Volver",width=20,command=lambda:Vistas.menu_camiones(ventana)).pack(pady=5)

    @staticmethod
    def modificar_camiones(ventana):
        Vistas.borrarPantalla(ventana)
        Label(ventana,text="Modificar Camión").pack(pady=5)
        Label(ventana,text="ID").pack()
        e=Entry(ventana); e.pack()
        Button(ventana,text="Buscar",width=20,command=lambda:Vistas.modificar_form_camion(ventana,e.get())).pack(pady=5)
        Button(ventana,text="Volver",width=20,command=lambda:Vistas.menu_camiones(ventana)).pack(pady=5)

    @staticmethod
    def modificar_form_camion(ventana,id):
        c=Controlador.consultar_camion(id)
        if not c:
            Vistas.borrarPantalla(ventana)
            Label(ventana,text="No existe ese ID").pack(pady=5)
            Button(ventana,text="Volver",width=20,command=lambda:Vistas.modificar_camiones(ventana)).pack(pady=5)
            return
        if isinstance(c,list) and len(c)>0: c=c[0]
        Vistas.borrarPantalla(ventana)
        Label(ventana,text=f"Modificar Camión id {id}").pack(pady=5)
        lbl=["Marca","Color","Modelo","Velocidad","Caballaje","Plazas","Eje","CapacidadCarga"]; ents=[]
        for i,t in enumerate(lbl):
            Label(ventana,text=t).pack()
            e=Entry(ventana)
            e.insert(0,str(c[i+1]))
            e.pack(); ents.append(e)
        Button(ventana,text="Guardar Cambios",width=20,command=lambda:Controlador.modificar_camion(*[e.get() for e in ents],id)).pack(pady=5)
        Button(ventana,text="Volver",width=20,command=lambda:Vistas.menu_camiones(ventana)).pack(pady=5)

    @staticmethod
    def eliminar_camiones(ventana):
        Vistas.borrarPantalla(ventana)
        Label(ventana,text="Eliminar Camión").pack(pady=5)
        Label(ventana,text="ID").pack()
        e=Entry(ventana); e.pack()
        Button(ventana,text="Eliminar",width=20,command=lambda:Controlador.eliminar_camion(e.get())).pack(pady=5)
        Button(ventana,text="Volver",width=20,command=lambda:Vistas.menu_camiones(ventana)).pack(pady=5)
