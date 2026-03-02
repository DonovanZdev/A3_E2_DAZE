# Sistema de Gestión de Inventarios para una Tienda Pequeña

**Proyecto Integrador - Etapa 2**  
Universidad del Valle de México (UVM)  
Asignatura: Lógica y Programación Estructurada  
Alumno: Donovan Adrian Zuñiga Enriquez  
Fecha: 16 de Febrero de 2026

---

## 📋 Descripción

Este proyecto implementa un **Sistema de Gestión de Inventarios** para pequeñas tiendas, desarrollado en Python. El sistema permite realizar operaciones básicas de gestión de productos (CRUD: Crear, Leer, Actualizar, Eliminar) de manera eficiente y segura.

El objetivo es automatizar y organizar procesos que actualmente se realizan de forma manual, reduciendo errores y mejorando la productividad del negocio.

## 🎯 Objetivos

- Implementar funcionalidades básicas de gestión de inventario
- Aplicar estructuras de control (condicionales y ciclos)
- Realizar pruebas exhaustivas de cada función
- Documentar el código de manera clara y profesional

## 🔧 Funcionalidades Implementadas

### 1. **Registrar Producto**
Agrega un nuevo producto al inventario con validación de SKU único.
```python
registrar_producto("LAP-001", "Laptop Gamer", 10, 25000.50)
```

### 2. **Consultar Inventario**
Muestra todos los productos disponibles en el inventario.
```python
consultar_inventario()
```

### 3. **Consultar Producto Específico**
Busca y muestra los detalles de un producto por su SKU.
```python
consultar_producto("LAP-001")
```

### 4. **Modificar Producto**
Actualiza los datos de un producto existente (nombre, cantidad, precio).
```python
modificar_producto("LAP-001", nueva_cantidad=15, nuevo_precio=24500.00)
```

### 5. **Eliminar Producto**
Remueve un producto del inventario.
```python
eliminar_producto("LAP-001")
```

## 📁 Estructura del Proyecto

```
A3_E2_DAZE/
├── inventario_etapa2.py      # Módulo principal con las funciones
├── pruebas_etapa2.py         # Script de pruebas automatizadas
├── README.md                 # Este archivo
└── A2_ADZ.pdf               # Documento oficial del proyecto
```

## 🚀 Cómo Usar

### Requisitos
- Python 3.7 o superior

### Instalación

1. Clona el repositorio:
```bash
git clone https://github.com/DonovanZdev/A3_E2_DAZE.git
cd A3_E2_DAZE
```

2. No hay dependencias externas, el proyecto solo usa la librería estándar de Python.

### Ejecución

Para ejecutar las pruebas:
```bash
python3 pruebas_etapa2.py
```

Para usar el módulo en tu propio código:
```python
from inventario_etapa2 import registrar_producto, consultar_inventario

# Registrar un producto
registrar_producto("MOU-001", "Mouse", 50, 350.00)

# Consultar inventario
consultar_inventario()
```

## ✅ Pruebas Realizadas

Se ejecutaron **8 pruebas** exitosas:

| # | Prueba | Estado |
|---|---|---|
| 1 | Consulta en inventario vacío | ✅ Correcto |
| 2 | Registro de 3 productos | ✅ Correcto |
| 3 | Validación de SKU duplicado | ✅ Correcto |
| 4 | Consulta de producto existente | ✅ Correcto |
| 5 | Consulta de producto no existente | ✅ Correcto |
| 6 | Modificación de producto | ✅ Correcto |
| 7 | Eliminación de producto | ✅ Correcto |
| 8 | Eliminación de producto no existente | ✅ Correcto |

**Resultado:** Todas las funciones operan correctamente sin errores.

## 📊 Estructura de Datos

El inventario se representa como una lista de diccionarios:

```python
inventario = [
    {
        'sku': 'LAP-001',
        'nombre': 'Laptop Gamer',
        'cantidad': 10,
        'precio': 25000.50
    },
    ...
]
```

## 🔍 Características Técnicas

- **Validación de SKU único:** Previene duplicados en el inventario
- **Manejo de errores:** Mensajes claros cuando un producto no existe
- **Código modular:** Cada función tiene una responsabilidad específica
- **Documentación inline:** Comentarios que explican cada sección del código
- **Docstrings completos:** Cada función incluye descripción, argumentos y retorno

## 📚 Fuentes Documentales

1. Python Software Foundation. (2023). *The Python Tutorial*. https://docs.python.org/3/tutorial/
2. W3Schools. (s.f.). *Python Lists*. https://www.w3schools.com/python/python_lists.asp
3. Sweigart, A. (2019). *Automate the Boring Stuff with Python: Practical Programming for Total Beginners* (2nd ed.). No Starch Press.
4. Downey, A. (2015). *Think Python: How to Think Like a Computer Scientist* (2nd ed.). O'Reilly Media.

## 👨‍💻 Autor

**Donovan Adrian Zuñiga Enriquez**  
Universidad del Valle de México (UVM)  
Febrero de 2026
