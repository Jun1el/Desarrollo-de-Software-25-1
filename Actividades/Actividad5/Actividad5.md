# Actividad 5: Explorando diferentes formas de fusionar en Git

## Ejemplos
## 1. Fusión Fast-forward (git merge --ff)

La fusión fast-forward es la forma más simple de combinar ramas en Git. Solo es posible cuando la rama base no ha recibido nuevos commits desde que se creó la rama feature.

Seguimos la ruta mostrada: 

![Imagen 1](Act5imagenes/Act5_1.png)

**Mostramos la estructura de los commits resultante.**

```bash
$ git checkout main
$ git merge add-description

$ git log --graph --oneline
```
![Imagen 4](Act5imagenes/Act5_4.png)

## 2. **Fusión No-fast-forward (git merge --no-ff)**

La fusión no-fast-forward crea un nuevo commit de fusión. Es útil para preservar el contexto de la fusión, especialmente en equipos donde se requiere más claridad en el historial de cambios.

![Imagen 2](Act5imagenes/Act5_2.png)

**Mostramos la estructura de los commits resultante.**
```bash
$ git checkout main
$ git merge --no-ff add-feature

$ git log --graph --oneline
```
![Imagen 5](Act5imagenes/Act5_5.png)

## 3. **Fusión squash (git merge --squash)**

La fusión squash combina todos los cambios de una rama en un solo commit en la rama principal. Este método es útil cuando se quiere mantener un historial de commits limpio.

![Imagen 3](Act5imagenes/Act5_3.png)

**¿Cuál es tu estructura de commits?**

```bash
$ git checkout main
$ git merge --squash add-basic-files

$ git add .
$ git commit -m "Agregar documentación estándar del repositorio"
$ git log --graph --oneline
```

![Imagen 6](Act5imagenes/Act5_6.png)

![Imagen 7](Act5imagenes/Act5_7.png)

# Ejercicios

1. Clona un repositorio Git con múltiples ramas.
Identifica dos ramas que puedas fusionar utilizando git merge --ff.
Haz el proceso de fusión utilizando git merge --ff.
Verifica el historial con git log --graph --oneline.

- Pregunta: ¿En qué situaciones recomendarías evitar el uso de git merge --ff? Reflexiona sobre las desventajas de este método.

    - Pierdes el contexto de la rama:

        No queda rastro de que alguna vez hubo otra rama. Todo se ve como si hubieras trabajado directamente en main lo que hace dificil rastrear cambios si estamos en equipos colaborativos.

        Ademas dificulta rollbacks cuando queremos deshacer una funcion entera es mas facil cuando hay un commit en especifico.

2. Simula un flujo de trabajo de equipo.
Trabaja en dos ramas independientes, creando diferentes cambios en cada una.
Fusiona ambas ramas con git merge --no-ff para ver cómo se crean los commits de fusión.
Observa el historial utilizando git log --graph --oneline.

- Pregunta: ¿Cuáles son las principales ventajas de utilizar git merge --no-ff en un proyecto en equipo? ¿Qué problemas podrían surgir al depender excesivamente de commits de fusión?

    - Tener un historial claro y estructurado para un mejor control de versiones, tambien ayuda a las revisiones de codigo ya que cada commit esta documentado ademas en que el codigo en los commits.
    - Si haces merges muy seguido y sin necesidad el git log se llena de commits de fusión dificultando la lectura.Ademas al hacer varias fusiones complicaria si queremos hacer un rebase futuro.

3. Crea múltiples commits en una rama.
Haz varios cambios y commits en una rama feature.
Fusiona la rama con git merge --squash para aplanar todos los commits en uno solo.
Verifica el historial de commits antes y después de la fusión para ver la diferencia.

- Pregunta: ¿Cuándo es recomendable utilizar una fusión squash? ¿Qué ventajas ofrece para proyectos grandes en comparación con fusiones estándar?

    - Se recomiendo cuando tenemos muchos commits pequeños o sin mucha importancia individual y queremos mantener el historial limpio y legible al trabajar en una rama aislada que no requiere mantener cada paso.
## Resolver conflictos en una fusión non-fast-forward

En algunos casos, las fusiones no son tan sencillas y pueden surgir conflictos que necesitas resolver manualmente. Este ejercicio te guiará a través del proceso de manejo de conflictos.

![Imagen 8](Act5imagenes/Act5_8.png)

![Imagen 9](Act5imagenes/Act5_9.png)

Regresamos a la rama main y preseguimos

![Imagen 10](Act5imagenes/Act5_10.png)

![Imagen 11](Act5imagenes/Act5_11.png)

Solucionamos conflicto en el programa en esat ocasion yo use VSC.

![Imagen 12](Act5imagenes/Act5_12.png)

![Imagen 13](Act5imagenes/Act5_13.png)

### Preguntas:

- ¿Qué pasos adicionales tuviste que tomar para resolver el conflicto?

    - Cuando me lanzo el conflicto tuve que entrar al codigo y borrar las lineas y simbolos que genera git para resaltar lo que se ha combinado

- ¿Qué estrategias podrías emplear para evitar conflictos en futuros desarrollos colaborativos?
    - Considero que primeramente tener buena comunicacion con tu equipo para evitar que uno escriba sobre el codigo de otro asi como designar partes distintas del proyecto a cada desarrollador.

## Ejercicio: Comparar los historiales con git log después de diferentes fusiones

![Imagen 14](Act5imagenes/Act5_14.png)

### **Fusionamos feature-1 usando fast-forward:**

![Imagen 15](Act5imagenes/Act5_15.png)

### **Fusionamos feature-2 usando non-fast-forward:**

![Imagen 16](Act5imagenes/Act5_16.png)

### **Realizamos una nueva rama feature-3 con múltiples commits y fusionamos con squash:**

![Imagen 17](Act5imagenes/Act5_17.png)

### **Compara el historial de Git:**

#### Historial Fast-forward:

![Imagen 18](Act5imagenes/Act5_18.png)

#### Historial Non-fast-forward

![Imagen 19](Act5imagenes/Act5_19.png)

#### Historial con Squash:

![Imagen 20](Act5imagenes/Act5_20.png)

Adicional mirando las branches agrupadas en la rama maestra

![Imagen 21](Act5imagenes/Act5_21.png)

#### Preguntas:

- ¿Cómo se ve el historial en cada tipo de fusión?

    En este caso el ff y no ff se ven iguales ya que solo se hizo un commit en cada rama antes de fusionar. La diferencia se nota más cuando hay varios commits en la rama antes de fusionar.

    Sin embargo con squash si se notó claramente la diferencia ya que se redujo toda una rama con múltiples commits a un solo commit en main y podemos ver en la imagen todo el proceso que se hizo en las ramas para llegar a ese punto.

- ¿Qué método prefieres en diferentes escenarios y por qué?

    - Fast-forward (--ff):
        - Ideal para pequeños cambios o fixes rápidos.
        - Hace el historial mas limpio pero con menos informacion.
    - Non-fast-forward (--no-ff): 
        - En util para funcionalidades mas grandes en ramas que tuvimos bastantes commits de desarrollo
        - Te permite ver claramente cuándo se integró esa característica al proyecto.
    - Squash (--squash):
        - Dejamos solo un commit limpio que representa toda la funcionalidad.
        - Si el proceso de desarrollo interno no es importante de registrar.



## Ejercicio: Usando fusiones automáticas y revertir fusiones

Inicializamos un nuevo repositorio y realizamos dos commits en main:

![Imagen 22](Act5imagenes/Act5_22.png)

Creamos una nueva rama auto-merge y realiza otro commit en file.txt:

![Imagen 23](Act5imagenes/Act5_23.png)

Volvemos a main y realizamos cambios no conflictivos en otra parte del archivo:

![Imagen 25](Act5imagenes/Act5_25.png)

![Imagen 24](Act5imagenes/Act5_24.png)

Fusionamos la rama auto-merge con main:

![Imagen 26](Act5imagenes/Act5_26.png)

Revertir la fusión: Si decidimos que la fusión fue un error, podemos revertirla

![Imagen 27](Act5imagenes/Act5_27.png)

Verificamos el historial:

![Imagen 28](Act5imagenes/Act5_28.png)

### Preguntas:

- ¿Cuándo usarías un comando como git revert para deshacer una fusión?

    - Usaría **git revert** cuando ya hice una fusión (merge) que se completo, pero me doy cuenta después de que fue un error o que no debería haberse hecho en ese momento ya que este comando no borra el historial ni revierte commits individuales sino que revierte todo el efecto del merge, dejando el historial limpio y manteniendo el control de los cambios.

- ¿Qué tan útil es la función de fusión automática en Git?
    - Ahorra tiempo: Git detecta automáticamente que los cambios en ambas ramas no entran en conflicto.
    - Permite trabajar en paralelo con otros desarrolladores sin bloquear el flujo.
    - Evita errores humanos al hacer merges manuales.





