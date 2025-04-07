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


## B. Actividades de investigación y aplicación

### 1. Estudio de casos

- Busca dos o tres casos de empresas (startups o grandes organizaciones) que hayan migrado parte de su infraestructura a la nube. Describe:
  - Sus motivaciones para la migración.
  - Los beneficios obtenidos (por ejemplo, reducción de costos, escalabilidad, flexibilidad).
  - Los desafíos o dificultades enfrentadas (ej. seguridad, cumplimiento normativo).

### **Airbnb**

Airbnb tuvo un crecimiento exponencial en los ultimos años lo cual ya lo habia hecho migrar en a la nube en sus inicios pero el cual le brindo un servicio ineficiente, especialmente en la administración de servicios. La empresa necesitaba una solución más flexible y escalable para manejar su rápido crecimiento.

**Beneficios obtenidos con su migracion a AWS:**

- Escalabilidad Automática: Uso de Amazon Elastic Compute Cloud (EC2) y Elastic Load Balancing para manejar incrementos en el tráfico de usuarios sin intervención manual.​

- Procesamiento Eficiente de Datos: Implementación de Amazon Elastic MapReduce para analizar aproximadamente 50 GB de datos diariamente.​

- Almacenamiento Confiable: Utilización de Amazon Simple Storage Service (S3) para respaldos y almacenamiento de archivos estáticos, incluyendo 10 TB de imágenes de usuarios.​
Amazon Web Services, Inc.

Desafíos enfrentados: 

La migración de su base de datos principal a Amazon RDS for MySQL requirió una planificación cuidadosa para minimizar el tiempo de inactividad y asegurar la integridad de los datos.​

**Fuente** https://aws.amazon.com/es/solutions/case-studies/airbnb-case-study/

### Atlassian(Trello)

Atlassian, empresa matriz de Trello, buscaba acelerar la transformación digital de sus clientes empresariales mediante la migración de sus productos a la nube. La colaboración con Amazon Web Services tuvo como objetivo facilitar esta transición y ofrecer capacidades avanzadas de inteligencia artificial y seguridad.

**Beneficios obtenidos:**

- Centro de Excelencia en la Nube: Establecimiento de un centro para agilizar migraciones complejas, reduciendo el tiempo de migración hasta en un 50%.​

- Capacidades Avanzadas: Acceso a funciones exclusivas de la nube, como inteligencia artificial, automatización y análisis, mejorando la productividad y toma de decisiones.​

- Innovación Continua: Integración de tecnologías de AWS, incluyendo IA generativa como Amazon Bedrock, para el desarrollo de aplicaciones y soluciones para usuarios finales.​

Desafíos enfrentados: 

Aunque no se detallan específicamente en la fuente, migraciones de esta magnitud suelen enfrentar desafíos relacionados con la gestión del cambio organizacional, formación de personal y aseguramiento de la continuidad operativa durante la transición.

**Fuente** https://www.businesswire.com/news/home/20241204973894/en/Atlassian-and-Amazon-Web-Services-Announce-Strategic-Collaboration-Agreement-to-Drive-Enterprise-Cloud-Migration

### Volkswagen Group

Como parte de su estrategia "NEW AUTO—Movilidad para las generaciones futuras", Volkswagen buscaba transformarse en un proveedor global de movilidad basado en software, reduciendo costos, mejorando la agilidad y aumentando la seguridad.

Beneficios obtenidos:

- Reducción de Costos: Migración de aplicaciones a AWS para disminuir gastos operativos.​

- Mayor Agilidad y Escalabilidad: Capacidad para escalar aplicaciones y servicios según la demanda del mercado.​

- Seguridad Mejorada: Implementación de prácticas de seguridad avanzadas ofrecidas por AWS.​

Desafíos enfrentados:

Hubo 3 puntos desafiantes en este cambio los cuales fueron Gestión del Cambio, Adaptacion de aplicaciones y Planificacion Estrategica. En el primer punto se tenian que asegurar una comunicacion efectiva y la adopcion por parte de los empleados durante la migracion, en el segundo punto modificar aplicaciones y procesos de desarrollo para aprovechar al máximo las capacidades de la nube y en el tercer punto definir una hoja de ruta clara y establecer una gobernanza efectiva para la migración.​


### 2.Comparativa de responsabilidades en modelos de servicio cloud

| **Aspecto / Rol**                  | **IaaS (Infraestructura como Servicio)**                       | **PaaS (Plataforma como Servicio)**                         | **SaaS (Software como Servicio)**                          |
|-----------------------------------|----------------------------------------------------------------|-------------------------------------------------------------|------------------------------------------------------------|
| **Instalación del S.O.**          | Equipo de operaciones                                          | Proveedor                                                   | Proveedor                                                  |
| **Gestión de hardware**           | Proveedor                                                      | Proveedor                                                   | Proveedor                                                  |
| **Configuración de red**          | Equipo de operaciones / Proveedor                              | Proveedor                                                   | Proveedor                                                  |
| **Middleware (runtimes, DB, etc.)** | Equipo de operaciones / Desarrollador                        | Proveedor                                                   | Proveedor                                                  |
| **Parches de seguridad del S.O.** | Equipo de operaciones                                          | Proveedor                                                   | Proveedor                                                  |
| **Escalado automático**           | Equipo de operaciones (configura)                              | Proveedor (configurable)                                   | Proveedor                                                  |
| **Despliegue de aplicaciones**    | Desarrollador / Equipo de operaciones                          | Desarrollador                                               | Proveedor                                                  |
| **Actualización de software**     | Desarrollador / Equipo de operaciones                          | Desarrollador / Proveedor                                  | Proveedor                                                  |
| **Gestión de usuarios y permisos**| Equipo de operaciones / Desarrollador                          | Desarrollador / Equipo de operaciones                      | Usuario administrador (cliente)                           |
| **Monitoreo de rendimiento**      | Equipo de operaciones                                          | Equipo de operaciones / Proveedor                          | Proveedor                                                  |




## 4.Análisis de Costos y Características de Modelos de Nube

| Tipo de Nube   | **Costos (CAPEX / OPEX)** | **Escalabilidad y Flexibilidad** | **Cumplimiento Normativo** | **Complejidad para Cambiar de Proveedor** |
|----------------|----------------------------|----------------------------------|-----------------------------|--------------------------------------------|
| **Pública**    | OPEX bajo, sin inversión inicial; pago por uso. | Alta elasticidad; ideal para crecer rápido o por demanda. | Cumple normativas con servicios certificados (pero debes validar región y servicio). | Alta: riesgo de *vendor lock-in* si usas servicios propietarios. |
| **Privada**    | Alto CAPEX inicial (hardware, licencias, personal). OPEX estable. | Escalabilidad limitada a la capacidad física instalada. | Alta capacidad de control sobre privacidad y cumplimiento (ideal para sectores regulados). | Baja: total control, pero poco flexible para migrar a la nube pública. |
| **Híbrida**    | Mixto: CAPEX por on-premise, OPEX por la nube. | Flexible si se automatiza bien; buena para cargas críticas locales. | Permite ubicar datos sensibles en privado y apps públicas en la nube. | Media: gestión compleja, depende del nivel de integración. |
| **Multi-cloud**| OPEX más alto por duplicidad y gestión. Costos operativos elevados si no se optimiza. | Muy flexible y resiliente; evita dependencia de un solo proveedor. | Buen control con segmentación de datos y servicios. Se pueden usar regiones específicas. | Alta: orquestación compleja y riesgo de incompatibilidad entre nubes. |

