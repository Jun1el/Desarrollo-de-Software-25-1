# Ejercicio 1: Manejo avanzado de ramas y resolución de conflictos

## Procedimiento

### 1. Crear una nueva rama para una característica
Primero creamos una nueva rama llamada `feature/advanced-feature` desde la rama `main`:

**Nota:** Hay ramas ya creadas asi como los archivos readme.md, main.py y contributing.md que fueron creados en la parte teorica de la actividad pero no coloque el procedimiento de esa parte por temas de espacio, Continuamos con la actividad.

```bash
$ git branch feature/advanced-feature
$ git checkout feature/advanced-feature
```
![Imagen 1](Actividad4imagenes/Act4Prob1P1.png)

### 2.Modificar archivos en la nueva rama:

Editamos el archivo main.py para incluir una función adicional, la carpeta main ya fue creada anteriormente en la parte teorica de la actividad por lo cual solo lo editamos directamente 

```python
def greet():
    print('Hello from advanced feature')

greet()
```
Añadimos y confirmamos estos cambios en la rama feature/advanced-feature

```bash 
$ git add main.py
$ git commit -m "Add greet function in advanced feature"
```
![Imagen 1](Actividad4imagenes/Act4Prob1P2.png)

### 3.Simular un desarrollo paralelo en la rama main:

Cambiamos de nuevo a la rama main
```bash 
$ git checkout main
```
Editamos el archivo main.py de forma diferente :
```python
print('Hello World - updated in main')
```
Añadimos y confirmamos estos cambios en la rama main:
```bash
$ git add main.py
$ git commit -m "Update main.py message in main branch"
```
![Imagen 1](Actividad4imagenes/Act4Prob1P3.png)
### 4.Intentar fusionar la rama feature/advanced-feature en main:

Fusionamos la rama feature/advanced-feature en main 
```bash
$ git merge feature/advanced-feature
```
### 5.Resolver el conflicto de fusión:
Cuando hicimos el merge nos genero un problema ya que son dos codigos complemtamente diferentes por lo cual debemos entrar al codigo y acomodar la estructura del programa

Después de resolver el conflicto, añadimos el archivo resuelto y completa la fusión:

```bash
$ git add main.py
$ git commit -m "Resolve merge conflict between main and feature/advanced-feature"
```
![Imagen 1](Actividad4imagenes/Act4Prob1P4.png)

### 6.Eliminar la rama fusionada:

Como fusionamos con exito los conflictos eliminamos la rama feature/advanced-feature 

```bash
$ git branch -d feature/advanced-feature
```
![Imagen 1](Actividad4imagenes/Act4Prob1P5.png)

como podemos ver se elimino la rama y nos quedamos con las ramas que creamos en la parte teorica.

# Ejercicio 2: Exploración y manipulación del historial de commits
# Ejercicio 3: Creación y gestión de ramas desde commits específicos
# Ejercicio 4: Manipulación y restauración de commits con git reset y git restore
# Ejercicio 5: Trabajo colaborativo y manejo de Pull Requests
# Ejercicio 6: Cherry-Picking y Git Stash