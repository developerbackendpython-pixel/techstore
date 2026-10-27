from collections import namedtuple, defaultdict, deque
from colorama import Fore
from itertools import zip_longest
from datos import ciudad_principal, almacen_principal, pedidos, historial_clientes_compras
from collections import deque
import time

def inventario_principal():
    while True:
        # IMPRESION DE OPCIONES DEL MENU
        print("MENU".center(20, "-"))
        print("1. AGREGAR PRODUCTO")
        print("2. EDITAR PRODUCTO")
        print("3. ELIMINAR PRODUCTO")
        print("4. CORDENADAS DE LAS TIENDAS")
        print("5. Procesar todos los pedidos")
        print("6. SALIR")
        # MANEJAMOS LOS ERRORES CON TRY Y EXCEP DONDE EL USUARIO VA A INGRESAR LA OPCION
        try:
            opcion = int(input(">>:  "))
        except ValueError:
            print("!! Opcion Invalida ¡¡")
            continue
        
        # CREAMOS LOS ID AUTOMATICOS PARA AUTO ASIGNAR ID A LOS PRODUCTOS EMEPZANDO DESDE 100 SI EL DICCIONARIO ESTA VACIO
        if not almacen_principal:
            id_automatico = 100
        else:
            id_automatico = max(almacen_principal.keys()) +1


        # ACCION DE LA OPCION 1 SE LE PIDE AL USUARIO LO SIGUIENTE NOMBRE,PRECIO.STOCK DEL RPODUCTO
        if opcion == 1:
            # Manejamos las 2 entradas PRECIO Y STOCK para asegurarnos de que solo se puedan agregar datos de tipo entero
            try:
                Nombre = input("Nombre: ")
                Precio = int(input("Precio: "))
                Stock = int(input("Stock: "))
            except ValueError:
                print("¡ERROR AL CREAR EL PRODUCTO!")
                continue
            # CREAMOS EL DICCIONARIO DENTRO DE LA FUNCION PARA NO CREAR UN DICCIONARIO VACIO SI EL USUARIO FALLA LOS CAMPOS OBLIGATORIOS
            almacen_principal[id_automatico] # ESTE CODIGO ASIGNA EL ID AL DICCIONARIO PRINCIPAL CON UN DICCIONARIO VACIO
            almacen_principal[id_automatico]["Nombre"] = Nombre
            almacen_principal[id_automatico]["Precio"] = Precio
            almacen_principal[id_automatico]["Stock"] = Stock


        # EDITAR  PRODUCTOS CREADOS EL USUARIO PODRA EDITAR LOS SIGUIENTES CAMPOS NOMBRE,PRECIO,STOCK
        if opcion == 2:
            # IMPRIMIMOS Y MOSTRAMOS AL USUARIO TODOS LOS PRODUCTOS DISPONIBLES DEL INVENTARIO PRINCIPAL
            for id_producto, contenido in almacen_principal.items():
                print("ID: {0} CONTENIDO {1}".format(id_producto, contenido))
            # LE PEDIMOS EL ID DEL PRODUCTO AL USUARIO QUE DESEA EDITAR Y MANEJAMOS ERRORES SI EL USUARIO INGRESA LETRAS
            try:
                preguntar_id = int(input("ID: "))
            except ValueError:
                print("INGRESE UN ID VALIDO")
                continue

            # VERIFICAMOS SI EL ID EN REALIDAD EXISTE, SI EXISTE SE PODRA EDITAR SI NO EXISTE REFLEJAREMOS UN MENSAJE 
            if preguntar_id in almacen_principal:
                while True:
                    print("MENU DE EDICCION".center(50))
                    print("1. EDITAR NOMBRE")
                    print("2. EDITAR PRECIO")
                    print("3. EDITAR STOCK")
                    print("4. EDITAR PRODUCTO COMPLETO")
                    print("5. Salir")

                    try:
                        opcion_menu = int(input("Opcion: "))
                    except ValueError:
                        print("Porfavor ingrese una opcion valida.")
                        continue
                    if opcion_menu == 1:
                        almacen_principal[preguntar_id]["Nombre"] = input("Nombre:  ")
                    try:
                        if opcion_menu == 2:
                            almacen_principal[preguntar_id]["Precio"] = int(input("Precio: "))
                        elif opcion_menu == 3:
                            almacen_principal[preguntar_id]["Stock"] = int(input("Stock"))
                    except ValueError:
                        print("Ingrese una opcion valida")
                        continue
                    if opcion_menu == 4:
                        try:
                            almacen_principal[preguntar_id]["Nombre"] = input("Nombre: ")
                            almacen_principal[preguntar_id]["Precio"] = int(input("Precio: "))
                            almacen_principal[preguntar_id]["Stock"] = int(input("Stock: "))
                        except ValueError:
                            print("Ingrese una opcion valida")
                    elif opcion_menu == 5:
                        break
            else:
                print("EL ID {0} NO EXISTE".format(preguntar_id))

        # Preguntamos al usuario que Producto va a eliminar y lo eliminam
        if opcion == 3:
            print("PRODUCTOS DISPONIBLES".center(20, "-"))
            for ID_producto, CT_producto in almacen_principal.items():
                print("ID: {0} Contenido: {1}".format(ID_producto, CT_producto))
                # Ingresar el ID del prducto que se eliminara por completo
            try:
                delete_producto = int(input("ID: "))
            except ValueError:
                print("Porfavor ingrese un ID valido")
                continue
            if delete_producto in almacen_principal:
                print(f"Se elimino el producto {delete_producto}")
                del almacen_principal[delete_producto] # Elimina tanto el id como el contenido del producto de forma permanente
            else:
                print("El id: {0} no existe".format(delete_producto))
        if opcion == 4:
            cordenadas_tienda = namedtuple("Cordenadas", ["X","Y","Z"])
            X = [1637000,835378647]
            Y = [-6103000, 1180816875]
            Z = [512000, 1479]
            cord_guardadas = {
                "Bogota": (1637000, -6103000, 512000),
                "Medellin": (835378647, 1180816875, 1479)
                }
            for cx,cy,cz in zip_longest(X,Y,Z, fillvalue="Sin registros"):
                ubicaciones = cordenadas_tienda(cx,cy,cz)
                for clave, cord in cord_guardadas.items():
                    if ubicaciones == cord_guardadas[clave]:
                        print("Las cordenadas {0} pertenecen a la ciudad {1}".format(ubicaciones, clave))


        if opcion == 5:
            orden_de_llegada = deque(pedidos.keys())
            while orden_de_llegada:
                id_pedido = orden_de_llegada.popleft()
                pedido_actual = pedidos[id_pedido]
                producto_solicitado = pedido_actual["Producto"]
                cantidad_solicitada = pedido_actual["Cantidad"]
                producto_encontrado = False
                for id_producto, datos_producto in almacen_principal.items():
                    if producto_solicitado == datos_producto["Nombre"]:
                        producto_encontrado = True
                        if datos_producto["Stock"] >= cantidad_solicitada:
                            historial_clientes_compras[id_pedido]
                            historial_clientes_compras[id_pedido] = pedido_actual
                            datos_producto["Stock"] -= cantidad_solicitada
                            print(
                                f"En camino el pedido de "
                                f"{pedido_actual['Nombre']} "
                                f"ID: {id_pedido}"
                                )
                            print(
                                f"Stock restante de {producto_solicitado}: "
                                f"{datos_producto['Stock']}"
                                )
                            del pedidos[id_pedido]
                        else:
                            print(
                                f"Stock insuficiente para "
                                f"{pedido_actual['Nombre']}"
                                )
                            break
                if not producto_encontrado:
                    print(
                        f"El producto {producto_solicitado} "
                        f"no existe en el almacén."
                        )
        if opcion == 6: # Salir del sistema
            for salir in range(1,4): # Sale del sistema en 3 segundos
                time.sleep(1) 
                print("Saliendo del sistema en {0}...".format(salir))
            return "TechStore Cerrada."
            
