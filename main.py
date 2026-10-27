from inventario_principal import inventario_principal
from  ordenes_compra import ordenes_compra
from clientes_vip import clasificar
from colorama import Fore
from inventario_critico import productos_criticos
from Estadisticas_ventas import ventas_ciudades
from cache_datos import cache
print(f"{Fore.GREEN}¡¡¡Bienvenido a la tienda TechStore Colombia!!!{Fore.RESET}".center(60))
# MENU MAESTRO
def menu_maestro(inventario, compras, categoria_clientes, criticos, estadisticas,datos):
    control_opciones = {
                1: inventario,
                2: compras,
                3: categoria_clientes,
                4: criticos,
                5: estadisticas,
                6: datos,
            }
    while True:
        print("__________TechStore__________\n"
              "1. Inventario\n"
              "2. Registrar Compras\n"
              "3. Clasificacion de Clientes\n"
              "4. Productos mas caros y criticos\n"
              "5. Frecuencia de las tiendas con mas ventas\n"
              "6. datos\n"
              "7. Salir de la tienda")
        try:
            opcion = int(input("Opcion: "))
        except ValueError:
            print("Solo se puede ingresar numeros enteros")
            continue
        if opcion == 7:
            return control_opciones.get(opcion)
        elif opcion in control_opciones:
            print(control_opciones[opcion]())
        else:
            print("Esa clave no existe porfavor intentelo de nuevo")
            continue

print((menu_maestro(inventario_principal, ordenes_compra, clasificar, productos_criticos, ventas_ciudades,cache)))


