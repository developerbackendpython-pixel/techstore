from datos import historial_clientes_compras

Clasificar_clientes = {
    "Clasificacion": {
       
    }
}
def clasificar():
    for clave_cliente, contenido_cliente in historial_clientes_compras.items():
        if historial_clientes_compras[clave_cliente]["Total a Pagar"] >= 7000:
            categoria = "Cliente_VIP"
        else:
            categoria = "Cliente_Normal"
        clientes_categoria = Clasificar_clientes["Clasificacion"].setdefault(categoria, {}) 
        productos_cliente =  clientes_categoria.setdefault(contenido_cliente["Nombre"], set()) 
        productos_cliente.add(contenido_cliente["Producto"])



    while True:
        diccionari_opcion = {
            1: "Comparar",
            2: "Salir"
        }
        print(f"1.{diccionari_opcion[1]}.\n2.{diccionari_opcion[2]}.")

        try: 
            opcion = int(input("Opcion: "))
        except ValueError:
            print("Opcion incorrecta")
            continue
        
        accion = diccionari_opcion.get(opcion)
        if accion == None:
            print("Opcion invalida")
            continue
        
        if accion == "Comparar": 
            nombre1 = (input("Nombre: ")).strip().title(); nombre2 = (input("Nombre: ")).strip().title()
            validacion_1 = None; validacion_2 = None
            for usuario_categoria, usuarios in Clasificar_clientes["Clasificacion"].items():  
                if nombre1 in usuarios.keys() and usuarios in Clasificar_clientes["Clasificacion"].values():
                    cliente_producto_1 = usuarios[nombre1]
                    validacion_1 = True
                    categoria_cliente_1 = usuario_categoria
                if nombre2 in usuarios.keys() and usuarios in Clasificar_clientes["Clasificacion"].values():
                    cliente_producto_2 = usuarios[nombre2]
                    validacion_2 = True
                    categoria_cliente_2 = usuario_categoria
            if validacion_1 == None or validacion_2 == None:
                print(f"Ups comparacion fallida\n".center(30, "-"))
                print(f"El usuario {nombre1} {'Validado' if validacion_1 == True else '!!No hallado!!'}\n"
                      f"El usuario {nombre2} {'Validado' if validacion_2 == True else "!!No hallado!!"}\n")
                continue
            if "Cliente_VIP" in categoria_cliente_1:
                exclusivo = cliente_producto_1
            else:
                exclusivo =  cliente_producto_2
            return (f"Productos en comun: {len(cliente_producto_1.intersection(cliente_producto_2))}|{cliente_producto_1.intersection(cliente_producto_2)}\n"
                    f"Productos diferentes: {cliente_producto_1.symmetric_difference(cliente_producto_2)}\n"
                    f"Exclusivo del cliente VIP: {exclusivo} \n"
                    f"Total categorias: {cliente_producto_1.union(cliente_producto_2)} ")
        if accion == "Salir":
            return "Hasta Luego..."






