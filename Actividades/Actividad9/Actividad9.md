# Actividad 9: Red-Green-Refactor
### Autor: Andres La Torre Vasquez

## Introducción a Red-Green-Refactor

- Red-Green-Refactor es un ciclo de TDD que constara de 3 etapas :
    - Red (Fallo): Escribir una prueba que falle porque la funcionalidad aún no está implementada.
    - Green (Verde): Implementar la funcionalidad mínima necesaria para que la prueba pase.
    - Refactor (Refactorizar): Mejorar el código existente sin cambiar su comportamiento, manteniendo todas las pruebas pasando.

- Resultado de esta primera parte basica de ejemplos 

Archivo **shopping_cart.py**

![Imagen 1](Act9Imagenes/Act9_1.png) 

Archivo **test_shopping_cart.py**

![Imagen 1](Act9Imagenes/Act9_2.png) 

**Resultados exitosos de las pruebas:** 

![Imagen 1](Act9Imagenes/Act9_3.png)

## RGR, mocks, stubs e inyección de dependencias

**test_shopping_cart.py**

![Imagen 1](Act9Imagenes/Act9_4.png)

**Resultados exitosos de las pruebas**

![Imagen 1](Act9Imagenes/Act9_5.png)

## Ejercicios 

### Iteración 1: Agregar usuario (Básico)

![Imagen 1](Act9Imagenes/Act9_Ejercicio1.png)

### Iteración 2: Autenticación de usuario (Introducción de una dependencia para Hashing)
**tests/test_user_manager.py**

![Imagen 1](Act9Imagenes/Act9_Ejercicio2.png)

**Test exitoso**

![Imagen 1](Act9Imagenes/Act9_Ejercicio2_2.png)

### Iteración 3: Uso de un Mock para verificar llamadas (Spy / Mock)

![Imagen 1](Act9Imagenes/Act9_Ejercicio3.png)

### Iteración 4: Excepción al agregar usuario existente (Stubs/más pruebas negativas)

![Imagen 1](Act9Imagenes/Act9_Ejercicio4.png)

### Iteración 5: Agregar un "Fake" repositorio de datos (Inyección de Dependencias)

![Imagen 1](Act9Imagenes/Act9_Ejercicio5.png)

## Ejercicio integral 
