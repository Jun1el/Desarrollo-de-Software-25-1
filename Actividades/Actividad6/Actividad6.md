# Actividad 6
-----
## Parte 1: git rebase para mantener un historial lineal

- Creamos un repositorio Git y dos ramas, main y new-feature donde agregamos 1 commit a cada uno respectivamente
![Imagen 1](ImagenesAct6/1.png)

Historial de ramas hasta el momento

![Imagen 2](ImagenesAct6/2.png)

- Supongamos que alguien agregó un commit a main mientras nosotros trabajamos en new-feature y vemos como el grafico de commits diverge 

![Imagen 3](ImagenesAct6/3.png)

- Ahora cambiamos a rama new-feature y hacemos rebase, mostramos el historial de commits y hacemos el merge en main.

![Imagen 4](ImagenesAct6/4.png)

## Parte 2: git cherry-pick para la integración selectiva de commit

- Creamos un repositorio para nuestra prueba con dos ramas main y add-base-documents con 1 commit y 2 commits respectivamente; Observamos el log de la rama add-base-documents.

![Imagen 5](ImagenesAct6/5.png)

- Hacemos cherry pick a un commit especifico en mi caso escogi el hash de CONTRIBUTING.md y procedemos a ver el historial de commits

![Imagen 6](ImagenesAct6/6.png)

## Preguntas de discusion:
1. ¿Por qué se considera que rebase es más útil para mantener un historial de proyecto lineal en comparación con merge?

Porque rebase reescribe en los commits y los coloca en la parte superior de la rama a diferencia de los commits de merge que quedan mas ramificados o con bifurcaciones 

2. ¿Qué problemas potenciales podrían surgir si haces rebase en una rama compartida con otros miembros del equipo?

Al cambiar el historial de commits puede romper con el orden o sincronizacion del equipo que ha descargado esa rama provacando conflictos con pull o push y nunca debemos hacer rebase en ramas que ya hemos subido a un repositorio remoto.

3. ¿En qué se diferencia cherry-pick de merge, y en qué situaciones preferirías uno sobre el otro?

Que cherry pick solo fusiona el o los commits que le indiquemos en cambio merge fusiona todo lo que tenga en cierta rama.

Preferiria el uso de cherry pick cuando solo quiero aplicar cierta correccion puntual de un bug o archivo especifico. 

4. ¿Por qué es importante evitar hacer rebase en ramas públicas?

Porque esas ramas ya han sido compartidas a otras personas y si les reescribimos el historial va a ser confuso para otros guiarse en el historial y tendrian que usar comandos mas avanzados que tambien seria mas confuso.

## Ejercicios Teoricos

### 1. Diferencias entre git merge y git rebase

**`git merge`:**  
- Combina ramas diferentes creando un nuevo commit de merge.  
- **Mantiene el historial completo** de las ramas incluyendo bifurcaciones.  
- Es ideal cuando necesitamos conservar el contexto completo de como se desarrollaron los cambios.

**`git rebase`:**  
- Reaplica los commits de una rama sobre otra cambiando la base de esos commits.  
- Crea un **historial lineal y más limpio**, sin commits de merge.  
- **Reescribe el historial**, útil antes de subir código a una rama compartida.

> "Rebase para preparar, merge para integrar."

### 2. Relación entre git rebase y DevOps

En DevOps especialmente con **CI/CD** mantener un historial limpio y claro facilita la automatización y reduce errores.

**Beneficios del historial lineal con `rebase`:**
- Los pipelines CI/CD analizan el historial de commits para ejecutar pruebas, validaciones y despliegues. Un historial **ordenado y predecible** evita errores innecesarios.
- En los *pull requests*, es más fácil hacer *code review* si el historial no está lleno de commits irrelevantes o merges innecesarios.
- La depuración de errores es más fácil con un historial lineal, ya que se puede seguir el flujo de cambios sin saltos.


### 3. Impacto del git cherry-pick en un equipo Scrum
**Caso de ejemplo:**

Al cerrar un sprint el equipo descubre que solo algunos commits de una rama deben pasar a producción (por ejemplo una corrección urgente o una funcionalidad estable). El resto aún no está listo o debe testearse más.

**¿Cómo ayudaria `git cherry-pick`?**  
- Nos permitiria seleccionar commits específicos y aplicarlos a `main` sin necesidad de fusionar toda la rama.
- Es útil para hacer hotfixes o lanzamientos parciales sin comprometer el resto del trabajo del sprint.

- Tener encuenta que si el commit seleccionado depende de otros cambios anteriores, podrían surgir **conflictos** o el sistema quedar en un estado **incompleto o inestable**.

