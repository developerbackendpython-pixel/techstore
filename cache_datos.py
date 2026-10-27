from datos import pedidos,almacen_principal,ciudad_principal,historial_clientes_compras
import time
# Vamos a crear una memoizacion donde el usuario puede ver todo lo que esta dentro del cache
def cache():
    cache = {}
    while True:
        opciones = {
            1: "DATOS",
            2: "Salir"
            }
        print("1. Ver todos los datos\n2.Salir")
        try: 
            opcion = int(input("Opcion: "))
        except ValueError:
            print("Opcion Invalida")
        accion = opciones.get(opcion)
        if accion == None:
            print("Porfavor ingrese una opcion valida")
            continue


        if opcion == 1 and "datos" in cache:
            for id_pedidos, contenido  in pedidos.items():
                print(f"ID PEDIDO: {id_pedidos} CONTENIDO: {contenido}")
            for id_almacen, contenido_alamcen in almacen_principal.items():
                print(f"ID ALMACEN: {id_almacen} CONTENIDO: {contenido_alamcen}")
            for numero_ciudad, ciudades in enumerate(ciudad_principal):
                print(f"{numero_ciudad}. {ciudades}")
            for id_compras, historial in historial_clientes_compras.items():
                print(F"ID_HISTORIAL: {id_compras} CONTENIDO: {historial}")
        elif opcion == 2:
            return "Hasta luego"
        else:
            for cargar in range(0,101,1):
                time.sleep(0.05)
                if cargar == 25:
                    print("pedidos cargados")
                if cargar ==  50:
                    print("almacen_principal cargado...")
                if cargar == 75:
                    print("ciudades_principales cargadas...")
                if cargar ==  100:
                    print("historial compras cargadas...")

            print("Datos cargados con exito")
            cache["datos"] = True
