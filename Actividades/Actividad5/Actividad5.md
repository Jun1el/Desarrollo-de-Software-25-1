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

## Ejercicio: Comparar los historiales con git log después de diferentes fusiones

![Imagen 14](Act5imagenes/Act5_14.png)

![Imagen 15](Act5imagenes/Act5_15.png)

![Imagen 16](Act5imagenes/Act5_16.png)

![Imagen 17](Act5imagenes/Act5_17.png)

![Imagen 18](Act5imagenes/Act5_18.png)

![Imagen 19](Act5imagenes/Act5_19.png)

![Imagen 20](Act5imagenes/Act5_20.png)

![Imagen 21](Act5imagenes/Act5_21.png)

![Imagen 22](Act5imagenes/Act5_22.png)

![Imagen 23](Act5imagenes/Act5_23.png)

![Imagen 25](Act5imagenes/Act5_25.png)

![Imagen 24](Act5imagenes/Act5_24.png)

![Imagen 26](Act5imagenes/Act5_26.png)

![Imagen 27](Act5imagenes/Act5_27.png)

![Imagen 28](Act5imagenes/Act5_28.png)