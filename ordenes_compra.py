from datos import almacen_principal,pedidos,ciudad_principal
def ordenes_compra():
    
    # Sistema
    while True:
        print("----------Productos disponibles----------")
        for llave, itemss in almacen_principal.items():
            print(f"PRODUCTO: {itemss["Nombre"]} Precio: {itemss["Precio"]} Stock: {itemss["Stock"]} ID: {llave}")
        print("----------REGISTROS DE USUARIOS----------")
        for tickets, usuario_pedido in pedidos.items():
            print(f"TICKET: [{tickets}] PEDIDO: {usuario_pedido}")
        maximos_pedidos = len(pedidos)
        if maximos_pedidos == 5:
            print("En estos momentos estamos teniendo muchos pedidos intentelo mas tarde..")
            print("El administrador pronto procesara todos los pedidos")
            break
     

        print("---MENU---")
        print("1. PEDIR TU PRODUCTO")
        print("2. Salir")

       
        try:
            opcion = int(input(">>: "))
        except ValueError:
            print("¡¡Ingrese una opcion valida!!")
            continue

     
        if opcion == 1:
            
           
            nombre = input("Nombre: ")
            producto = input("Producto: ")
            ciudad_destino = input("Ciudad: ").strip().title()

            buscar_producto = {clave: contenido for clave, contenido in almacen_principal.items() if producto == contenido["Nombre"]}
            if not buscar_producto:
                print("No se encontro ninguno producto {0}".format(producto))
            #______________________________________________________________________________________________________________________________
            else:
                while True:
                    
                    try:
                        cantidad = int(input("Cantidad: "))
                        break
                    except ValueError:
                        print("Porfavor ingrese una cantidad valida")
                        
                clave, contenido = list(buscar_producto.items())[0]
                
                if ciudad_destino not in ciudad_principal:
                    print(f"Lo sentimos solo estamos haciendo envios a Bogota y Medellin")
                    continue
                if cantidad <= 0:
                    print("La cantidad no puede ser menor a 1")
                elif contenido["Stock"] == 0:
                    print("¡¡Lo sentimos mucho, producto agotado!!")
                elif cantidad <= contenido["Stock"]:
                    if not pedidos:
                        generar_ticket = 100
                    else:
                       generar_ticket = max(pedidos.keys()) + 1

                    pedidos[generar_ticket]
                    pedidos[generar_ticket]["Nombre"] = nombre
                    pedidos[generar_ticket]["Ciudad"] = ciudad_destino
                    pedidos[generar_ticket]["Producto"] = producto
                    pedidos[generar_ticket]["Cantidad"] =  cantidad
                    total_apagar = cantidad * contenido["Precio"]
                    pedidos[generar_ticket]["Total a Pagar"] = total_apagar
                else:
                    print(f"Lo sentimos no tenemos esa cantidad de producto solo {contenido['Stock']}")
                #_______________________________________________________________________________________      
        
        if opcion == 2:
            return "Saliendo de registro de clientes..."
