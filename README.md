# Proyecto: Gestión de Inventarios

## Fase 1 del Proyecto
Analisis, algoritmo y diagrama de flujo.

### Análisis del Proyecto

En la Fase 1 del proyecto, vamos a analizar las operaciones clave del sistema de inventario, detallando cada operación y explicando la justificación técnica para utilizar matrices como única estructura de almacenamiento. Este sistema interactivo permite las siguientes operaciones:

### 1. Registro de productos

**Operación**  
El sistema debe permitir registrar nuevos productos con las características: nombre, código, precio, cantidad disponible y umbral mínimo. Cada vez que se ingresa un producto, la información debe almacenarse eficientemente.

**Análisis**
- **Datos a almacenar:** Para cada producto, se deben almacenar cinco propiedades: nombre, código, precio, cantidad y umbral mínimo.
- **Estructura de almacenamiento:** Usaremos una matriz en la que cada fila representa un producto y cada columna almacena una de sus propiedades (nombre, código, precio, cantidad y umbral mínimo). De este modo, cada producto ocupa una fila, y sus atributos están organizados por columnas.

**Justificación del uso de matrices**  
Las matrices permiten almacenar datos estructurados de forma bidimensional. En este caso, cada fila representa un producto y cada columna una de sus propiedades. Esto facilita la búsqueda, registro y actualización de los productos al poder utilizar índices específicos para acceder y modificar cada propiedad.

---

### 2. Actualización de la cantidad de un producto (Compra y Venta)

**Operación**  
Cuando se recibe nueva mercancía o se realiza una venta, el sistema debe actualizar la cantidad de un producto específico en el inventario.

**Análisis**
- **Proceso:** El sistema permite al usuario ingresar el código del producto. Luego, se busca el código en la matriz y, al encontrarlo, se accede a la columna de cantidad para modificar su valor, sumando o restando unidades según corresponda (dependiendo si es una compra o venta).
- **Flujo lógico:**
  1. Buscar el código del producto en la columna correspondiente.
  2. Si existe, actualizar la cantidad según la transacción.

**Justificación del uso de matrices**  
Usar una matriz permite almacenar los datos de cada producto en una fila, lo que simplifica la actualización de la cantidad al poder acceder directamente a la columna de cantidad en la fila correspondiente al producto. Este enfoque facilita también la verificación y modificación de los datos en tiempo real.

---

### 3. Generación de reportes de productos con bajo stock

**Operación**  
El sistema debe generar un reporte de los productos cuyo stock esté por debajo de un umbral mínimo definido.

**Análisis**
- **Datos a evaluar:** La cantidad disponible (`productos[fila,4]`) de cada producto debe compararse con el umbral mínimo (`productos[fila,5]`).
- **Proceso:** Recorremos cada fila de la matriz, verificando si la cantidad del producto es menor que el umbral mínimo. Si es así, el producto se incluye en el reporte.

**Justificación del uso de matrices**  
Las matrices permiten un acceso estructurado a los datos de cada producto. Este acceso permite verificar en cada fila (producto) si su cantidad está por debajo del umbral. Además, facilita el acceso secuencial, lo cual es eficiente para generar informes de inventario.

---

## Conclusión sobre el uso de matrices

El uso exclusivo de matrices en este sistema de inventarios aporta las siguientes ventajas:
- **Organización y estructura:** Cada fila representa un producto, y cada columna almacena una propiedad del producto, lo que simplifica la visualización de los datos.
- **Acceso y manipulación rápidos:** Las matrices permiten un acceso rápido a los datos de cada producto mediante índices, facilitando operaciones como actualización y generación de reportes.
- **Escalabilidad:** A medida que se añadan más productos, el sistema puede simplemente expandir la matriz con nuevas filas sin necesidad de cambiar la estructura subyacente.

Esta estructura también soporta un análisis y manipulación detallada de los datos, como en las operaciones de compra y venta o en los reportes de bajo stock, al aprovechar la capacidad de las matrices para almacenar y gestionar datos en dos dimensiones.

---

## Algoritmo Principal del Programa de Inventario

Este es el algoritmo principal que controla el flujo general del programa y permite al usuario seleccionar entre las distintas operaciones.

### Pasos del Algoritmo
1. **Mostrar Menú de Opciones:**
   - Presenta un menú interactivo al usuario con las opciones: registrar producto, actualizar cantidad, generar reporte de bajo stock o salir del programa.
2. **Leer Opción:**
   - El programa lee la opción seleccionada por el usuario para decidir cuál de las funciones ejecutar.
3. **Ejecución de Operaciones:**
   - Según la opción seleccionada:
     - **Opción 1:** Llama al algoritmo `operacion1`.
     - **Opción 2:** Llama al algoritmo `operacion2`.
     - **Opción 3:** Llama al algoritmo `operacion3`.
     - **Opción 4:** Finaliza el programa mostrando un mensaje de salida.
   - Si el usuario ingresa una opción inválida, muestra un mensaje indicando que la opción no es válida.
4. **Bucle de Continuidad:**
   - El programa permanece en un bucle, volviendo al menú principal tras ejecutar cada opción, hasta que el usuario seleccione la opción de salir.

---

## Algoritmo para Registrar un Producto

Este algoritmo permite registrar nuevos productos en la matriz de inventario, donde cada fila representa un producto con sus respectivas propiedades: nombre, código, precio, cantidad y umbral mínimo.

### Pasos del Algoritmo
1. **Entrada de Datos:**
   - Solicita al usuario que ingrese los datos básicos del producto: nombre, código, precio, cantidad y umbral mínimo. Estos datos se almacenan temporalmente hasta que se determine si el producto ya existe en el inventario.
2. **Búsqueda del Código del Producto:**
   - Revisa cada fila de la columna de códigos (`productos[fila,2]`) para verificar si el producto ya existe en la matriz. Si el código coincide con uno existente, significa que el producto ya está registrado.
3. **Condición de Existencia:**
   - Si el producto no existe en el inventario (es decir, no se encuentra su código en la matriz), procede a almacenarlo en la siguiente fila vacía.
   - Si el producto ya existe, muestra un mensaje de error indicando que el producto está registrado.
4. **Registro de Datos:**
   - Si el producto no existe, asigna cada propiedad del producto (nombre, código, precio, cantidad y umbral mínimo) en la fila correspondiente de la matriz `productos`, usando un índice `n` que representa el número actual de productos registrados.
   - Incrementa `n` en 1 para la próxima vez que se registre un producto nuevo.
5. **Salida:**
   - Muestra un mensaje de éxito confirmando que el producto ha sido registrado.

---

## Algoritmo para Actualizar la Cantidad de un Producto (Compra y Venta)

Este algoritmo permite modificar la cantidad de un producto específico en el inventario, permitiendo tanto el incremento (al recibir mercancía) como la disminución (al realizar una venta).

### Pasos del Algoritmo
1. **Entrada de Datos:**
   - Solicita al usuario el código del producto y la cantidad a modificar (esta cantidad será positiva para compras y negativa para ventas).
2. **Búsqueda del Producto:**
   - Verifica si el producto existe buscando el código en la matriz `productos` (en la columna de códigos). Si se encuentra el código, su posición (`posición`) indicará la fila donde se localiza el producto.
3. **Condición de Existencia:**
   - Si el producto no existe en la matriz, muestra un mensaje de error informando al usuario.
4. **Actualización de Cantidad:**
   - Si el producto existe, se suma la cantidad ingresada a la cantidad actual (`productos[posición,4]`).
   - Si la cantidad resultante es negativa, el sistema revierte el cambio y muestra un mensaje de error, ya que las cantidades de inventario no pueden ser negativas.
5. **Salida:**
   - Si la cantidad se actualiza correctamente (es decir, no es negativa), el sistema muestra la nueva cantidad del producto.

---

## Algoritmo para Generar Reporte de Productos con Bajo Stock

Este algoritmo genera un reporte de los productos que tienen un stock inferior al umbral mínimo establecido en el inventario.

### Pasos del Algoritmo
1. **Recorrido de la Matriz:**
   - Recorre cada fila en la matriz de `productos`, accediendo a la cantidad y el umbral mínimo de cada producto.
2. **Condición de Stock Bajo:**
   - Para cada producto, compara la cantidad disponible (`productos[fila,4]`) con el umbral mínimo (`productos[fila,5]`). Si la cantidad es menor que el umbral, significa que el producto tiene bajo stock y necesita reposición.
3. **Generación del Reporte:**
   - Si el producto tiene bajo stock, el sistema muestra el nombre, código y cantidad de ese producto, agregándolo al reporte de productos con bajo inventario.
4. **Salida:**
   - Al finalizar el recorrido de la matriz, el sistema ha mostrado todos los productos que necesitan reposición, completando el reporte.
