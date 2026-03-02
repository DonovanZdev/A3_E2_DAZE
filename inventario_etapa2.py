'''
Proyecto Integrador - Etapa 2
Sistema de Gestión de Inventarios para una Tienda Pequeña

Este script contiene las funciones básicas para gestionar un inventario:
- Registrar un nuevo producto.
- Modificar un producto existente.
- Eliminar un producto.
- Consultar el inventario completo.
- Consultar un producto específico.
'''

# El inventario se representa como una lista de diccionarios.
# Cada diccionario representa un producto.
inventario = []

def registrar_producto(sku, nombre, cantidad, precio):
    """
    Registra un nuevo producto en el inventario.

    Args:
        sku (str): El SKU (Stock Keeping Unit) del producto, debe ser único.
        nombre (str): El nombre del producto.
        cantidad (int): La cantidad inicial del producto.
        precio (float): El precio unitario del producto.

    Returns:
        bool: True si el producto se registró con éxito, False si el SKU ya existe.
    """
    # Se utiliza un ciclo para verificar si el SKU ya existe en el inventario
    for producto in inventario:
        if producto['sku'] == sku:
            print(f"Error: El SKU '{sku}' ya existe. No se puede registrar el producto.")
            return False

    # Si el SKU no existe, se crea un nuevo diccionario para el producto
    nuevo_producto = {
        'sku': sku,
        'nombre': nombre,
        'cantidad': cantidad,
        'precio': precio
    }
    # Se agrega el nuevo producto a la lista del inventario
    inventario.append(nuevo_producto)
    print(f"Producto '{nombre}' registrado con éxito.")
    return True

def modificar_producto(sku, nuevo_nombre=None, nueva_cantidad=None, nuevo_precio=None):
    """
    Modifica los datos de un producto existente en el inventario.

    Args:
        sku (str): El SKU del producto a modificar.
        nuevo_nombre (str, optional): El nuevo nombre del producto. Defaults to None.
        nueva_cantidad (int, optional): La nueva cantidad del producto. Defaults to None.
        nuevo_precio (float, optional): El nuevo precio del producto. Defaults to None.

    Returns:
        bool: True si el producto se modificó con éxito, False si el SKU no se encontró.
    """
    # Se busca el producto por su SKU
    for producto in inventario:
        if producto['sku'] == sku:
            # Se utilizan condicionales para actualizar solo los campos proporcionados
            if nuevo_nombre is not None:
                producto['nombre'] = nuevo_nombre
            if nueva_cantidad is not None:
                producto['cantidad'] = nueva_cantidad
            if nuevo_precio is not None:
                producto['precio'] = nuevo_precio
            print(f"Producto con SKU '{sku}' modificado con éxito.")
            return True

    # Si el ciclo termina y no se encontró el producto
    print(f"Error: No se encontró un producto con el SKU '{sku}'.")
    return False

def eliminar_producto(sku):
    """
    Elimina un producto del inventario.

    Args:
        sku (str): El SKU del producto a eliminar.

    Returns:
        bool: True si el producto se eliminó con éxito, False si el SKU no se encontró.
    """
    producto_a_eliminar = None
    # Se busca el producto que se va a eliminar
    for producto in inventario:
        if producto['sku'] == sku:
            producto_a_eliminar = producto
            break

    # Se utiliza una condicional para eliminar el producto si se encontró
    if producto_a_eliminar:
        inventario.remove(producto_a_eliminar)
        print(f"Producto con SKU '{sku}' eliminado con éxito.")
        return True
    else:
        print(f"Error: No se encontró un producto con el SKU '{sku}'.")
        return False

def consultar_inventario():
    """
    Muestra todos los productos en el inventario.
    """
    print("\n--- INVENTARIO COMPLETO ---")
    if not inventario:
        print("El inventario está vacío.")
    else:
        # Se utiliza un ciclo para recorrer e imprimir cada producto
        for producto in inventario:
            print(f"SKU: {producto['sku']}, Nombre: {producto['nombre']}, Cantidad: {producto['cantidad']}, Precio: ${producto['precio']:.2f}")
    print("--------------------------\n")

def consultar_producto(sku):
    """
    Consulta y muestra la información de un producto específico.

    Args:
        sku (str): El SKU del producto a consultar.

    Returns:
        dict: El diccionario del producto si se encuentra, de lo contrario None.
    """
    for producto in inventario:
        if producto['sku'] == sku:
            print(f"\n--- Detalles del Producto ---")
            print(f"SKU: {producto['sku']}")
            print(f"Nombre: {producto['nombre']}")
            print(f"Cantidad: {producto['cantidad']}")
            print(f"Precio: ${producto['precio']:.2f}")
            print("-----------------------------\n")
            return producto

    print(f"Error: No se encontró un producto con el SKU '{sku}'.")
    return None
