from datos import almacen_principal

# Esta funcion no guarda informacion solo muestra lo que esta en critico
def productos_criticos():
        if not almacen_principal:
                return "Almacen sin productos"

        # Muestra los productos criticos
        inventario_critico = {id_producto: producto for id_producto, producto in almacen_principal.items() if producto['Stock'] < 5}
        if not inventario_critico:
                print("Sin productos criticos".center(100, " "))
        else: 
                print(f"-<[PRODUCTOS CRITICOS]>-".center(100, " "))
                for ID_producto, Producto in inventario_critico.items():
                        print("".center(100, "-"))
                        print(f"ID: {ID_producto} PRODUCTO: {Producto}".center(100, " "))

        # Muestra los productos que estan por encima del precio estandar $500
        precios_altos ={dato["Nombre"]: dato["Precio"] for dato in  almacen_principal.values() if dato["Precio"] > 500}
        if not precios_altos:
                print("Productos con precios razonables".center(100, " "))
        else:
                print()        
                print(f"-<[PRODUCTOS CON MAYOR PRECIO]>-".center(100, " "))
                for nombre, precio in precios_altos.items():
                         print(f"PRODUCTO: [{nombre}] PRECIO: [{precio}]".center(100, " "))

        return "" # Como solo vamos a imprimir los datos criticos entonces no es necesario retornar nada, entonces retonamos un espacio en blanco
