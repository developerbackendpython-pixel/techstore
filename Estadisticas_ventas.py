from datos import historial_clientes_compras
from collections import Counter
def ventas_ciudades():
    lista_ciudad = []
    for id_producto, producto in historial_clientes_compras.items():
        lista_ciudad.append(producto["Ciudad"])
    Ciudades_mas_frecuentes = Counter(lista_ciudad)
    dos_ciudades = dict(Ciudades_mas_frecuentes.most_common(2)) # Filtramos solo las 2 ciudades mas frecuentes
    mayor = max(dos_ciudades.items(), key=lambda item: item[1])
    menor = min(dos_ciudades.items(), key=lambda item: item[1])
    

    return (f"La 2 ciudades con mayor frecuencia: \n"
            f"Primera ciudad mas frecuente: {mayor[0]} con {mayor[1]} ventas \n"
            f"Segunda ciudad mas frecuente: {menor[0]} con {menor[1]} ventas ")
