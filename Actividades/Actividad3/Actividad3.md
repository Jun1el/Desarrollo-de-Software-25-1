# Actividad 3: Computación en la nube

## A. Cuestionario

1. **Motivaciones para la nube**

- (a) ¿Qué problemas o limitaciones existían antes del surgimiento de la computación en la nube y cómo los solucionó la centralización de servidores en data centers?

Antes las empresas tenian que tener todo el hardware en instalaciones fisicas y esto implicaba gastos iniciales mas altos, limitaciones para escalar o uso ineficiente de recursos.

La centralizacion de servidores ayudo en estos problemas al tener acceso remoto y baja demanda a recursos compartidos, ademas gracias a la virtualizacion y el pago por uso las organizaciones pueden escalar facilmente, reducir gastos y enfocarse mas en su producto.

- (b) ¿Por qué se habla de “The Power Wall” y cómo influyó la aparición de procesadores multi-core en la evolución hacia la nube?

"The power wall" hace alusion a la limitacion fisica en la velocidad de los procesadores debido al alto consumo energetico y generacion de calor, esto hacia que se dificultase aumentar la frecuencia del CPU para mejorar el rendimiento.

La solucion a esto fue los procesadores multicore que pueden realizar tareas simultaneamente sin aumentar demasiado el consumo energetico. Esta evolucion en la tecnologia hizo mas viable y eficiente la virtualizacion y ejecucion de procesos en paralelo lo que tambien a su vez impulso la computacion en la nube.

**Fuente:** https://link.springer.com/referenceworkentry/10.1007/978-0-387-09766-4_499#:~:text=Definition,rules%20%5B5%2C%2015%5D.

2. **Clusters y load balancing**

- (a) Explica cómo la necesidad de atender grandes volúmenes de tráfico en sitios web condujo a la adopción de clústeres y balanceadores de carga.

Es cuando demasiados usuarios intentan acceder a un sitio web y este colapsa ya que un solo servidor no puede procesar todas las peticiones lo que genera la lentitud o caida del servicio, debido a esto surgieron los cluesteres de servidores que son varios servidores que trabajan como uno solo pero para poder distribuir bien las peticiones se hace uso de load balancers(balanceadores de carga) que actuan como intermediarios y redireccionan el trafico de manera equitativa. Esto mejora el rendimiento, la disponibilidad y la experiencia del usuario.

- (b) Describe un ejemplo práctico de cómo un desarrollador de software puede beneficiarse del uso de load balancers para una aplicación web.

Un desarrollador que lanza una aplicación web de ventas puede beneficiarse usando load balancers para asegurar que la app se mantenga disponible durante campañas con alto tráfico como el Black Friday.

Por ejemplo, si la app está desplegada en tres servidores diferentes (dentro de un clúster), el load balancer distribuirá las peticiones de los usuarios entre los tres evitando que uno solo colapse. Además si uno de los servidores falla el balanceador puede redirigir el tráfico automáticamente a los otros dos asegurando continuidad del servicio sin necesidad de intervención manual.

3. **Elastic computing**

- (a) Define con tus propias palabras el concepto de Elastic Computing.

Es la capacidad de ajustar de manera rapida los recursos como CPU, RAM y almacenamiemto ya que la demanda en las organizaciones son cambiantes y esto tambien se puede aplicar en la nube o clusteres independientes.

- (b) ¿Por qué la virtualización es una pieza clave para la elasticidad en la nube?

Porque nos permite crear entornos virtuales escalables, configurables y con un costo acorde a la demanda necesitada 

- (c) Menciona un escenario donde, desde la perspectiva de desarrollo, sería muy difícil escalar la infraestructura sin un entorno elástico.

En una app web viral con miles de usuarios nuevos cada minuto, sin elasticidad sería lento y costoso escalar servidores manualmente un ejemplo puede ser la pagina de teleticket cuando lanzan ventas de conciertos de artistas famosos muchos fans se suelen registrar por ese motivo y llegan a ser mas de 25 mil personas en cola como el caso del 2022 con bad bunny las entradas se agotaron en 45 minutos y eran alrededor de 30 mil entradas.


**Fuente:** 

https://lab.wallarm.com/what/elasticidad-de-la-nube/?lang=es

https://www.oracle.com/pe/cloud/what-is-cloud-computing/virtualization-vs-cloud-computing/

4. **Modelos de servicio (IaaS, PaaS, SaaS, DaaS)**

- (a) Diferencia cada uno de estos modelos. ¿En qué casos un desarrollador optaría por PaaS en lugar de IaaS?

  * IaaS (Infrastructure as a Service): Proporciona máquinas virtuales, redes y almacenamiento. El desarrollador gestiona todo lo que está sobre la infraestructura.

  * PaaS (Platform as a Service): Ofrece un entorno ya configurado para desarrollar y desplegar aplicaciones sin preocuparse por la infraestructura.

  * SaaS (Software as a Service): Aplicaciones completas listas para usar. El usuario solo las consume (como Gmail).

  * DaaS (Desktop as a Service): Escritorios virtuales accesibles desde cualquier lugar.

- (b) Enumera tres ejemplos concretos de proveedores o herramientas que correspondan a cada tipo de servicio.

    * IaaS: AWS EC2, Google Compute Engine, Microsoft Azure VMs.

    * PaaS: Heroku, Google App Engine, Azure App Service.

    * SaaS: Google Docs, Dropbox, Salesforce.

    * DaaS: Amazon WorkSpaces, Citrix DaaS, Azure Virtual Desktop.

1. **Tipos de nubes (Pública, Privada, Híbrida, Multi-Cloud)**

- (a) ¿Cuáles son las ventajas de implementar una nube privada para una organización grande?

Una nube privada brinda mayor control, seguridad y personalización. Para una empresa grande esto es ideal si maneja información sensible (como bancos o gobiernos) o tiene requisitos específicos de cumplimiento. Además puede optimizar recursos según sus propias reglas.

- (b) ¿Por qué una empresa podría verse afectada por el “provider lock-in”?

El provider lock-in ocurre cuando una empresa se vuelve muy dependiente de un solo proveedor de nube usando servicios propietarios difíciles de migrar. Esto puede limitar su flexibilidad, aumentar costos a largo plazo y complicar una salida si el proveedor cambia precios o políticas.

**Fuente:** https://www.cloudflare.com/learning/cloud/what-is-vendor-lock-in/

- (c) ¿Qué rol juegan los “hyperscalers” en el ecosistema de la nube?

Los hyperscalers (como AWS, Azure o Google Cloud) ofrecen infraestructura masiva y escalable a nivel global. Permiten a empresas de cualquier tamaño acceder a tecnología avanzada (IA, big data, cómputo elástico) sin necesidad de construir centros de datos propios. Son clave en la expansión del uso de la nube.

**Fuente:** https://www.redhat.com/es/topics/cloud-computing/what-is-a-hyperscaler