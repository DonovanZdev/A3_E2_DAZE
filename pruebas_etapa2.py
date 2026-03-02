'''
Proyecto Integrador - Etapa 2
Script de Pruebas para el Sistema de Gestión de Inventarios

Este script prueba las funciones básicas del módulo `inventario_etapa2`.
'''

# Se importa el módulo con las funciones del inventario
from inventario_etapa2 import (
    registrar_producto,
    modificar_producto,
    eliminar_producto,
    consultar_inventario,
    consultar_producto,
    inventario
)

def ejecutar_pruebas():
    print("--- INICIANDO PRUEBAS DE FUNCIONALIDADES BÁSICAS ---")

    # 1. Prueba de consulta en inventario vacío
    print("\n--- Prueba 1: Consultar inventario inicial (vacío) ---")
    consultar_inventario()

    # 2. Prueba de registro de nuevos productos
    print("\n--- Prueba 2: Registrar tres productos nuevos ---")
    registrar_producto("LAP-001", "Laptop Gamer", 10, 25000.50)
    registrar_producto("MOU-002", "Mouse Inalámbrico", 50, 350.00)
    registrar_producto("TEC-003", "Teclado Mecánico", 30, 1200.75)
    consultar_inventario()

    # 3. Prueba de registro de un producto con SKU duplicado
    print("\n--- Prueba 3: Intentar registrar un producto con SKU duplicado ---")
    registrar_producto("LAP-001", "Laptop de Oficina", 5, 18000.00)
    consultar_inventario()

    # 4. Prueba de consulta de un producto específico existente
    print("\n--- Prueba 4: Consultar un producto específico (MOU-002) ---")
    consultar_producto("MOU-002")

    # 5. Prueba de consulta de un producto específico no existente
    print("\n--- Prueba 5: Consultar un producto que no existe (XYZ-999) ---")
    consultar_producto("XYZ-999")

    # 6. Prueba de modificación de un producto existente
    print("\n--- Prueba 6: Modificar la cantidad y el precio de un producto (TEC-003) ---")
    modificar_producto("TEC-003", nueva_cantidad=25, nuevo_precio=1150.00)
    consultar_producto("TEC-003")

    # 7. Prueba de modificación de un producto no existente
    print("\n--- Prueba 7: Intentar modificar un producto que no existe (XYZ-999) ---")
    modificar_producto("XYZ-999", nuevo_nombre="Producto Fantasma")

    # 8. Prueba de eliminación de un producto existente
    print("\n--- Prueba 8: Eliminar un producto (LAP-001) ---")
    eliminar_producto("LAP-001")
    consultar_inventario()

    # 9. Prueba de eliminación de un producto no existente
    print("\n--- Prueba 9: Intentar eliminar un producto que no existe (XYZ-999) ---")
    eliminar_producto("XYZ-999")

    print("\n--- FIN DE LAS PRUEBAS ---")

# Se ejecuta la función principal de pruebas
if __name__ == "__main__":
    ejecutar_pruebas()
