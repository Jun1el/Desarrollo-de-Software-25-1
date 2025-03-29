# Actividad 2 : Del codigo a la produccion: Infraestructura, contenedores, despliegue y observabilidad

## Tarea teórica P1:

- Investigar una herramienta de IaC (p. ej. Terraform) y describir cómo organiza sus módulos.

**HashiCorp Terraform**

Terraform es una herramienta de infraestructura como código (IaC) que permite definir, configurar y gestionar la infraestructura en la nube. Utiliza archivos de configuración en formato HCL (HashiCorp Configuration Language), donde se describen los recursos a gestionar, como redes, bases de datos y servidores.

**Estructura basica de un modulo**

main.tf: Define los recursos y configuraciones principales del módulo.

variables.tf: Contiene las variables que el módulo acepta como parámetros de entrada.

outputs.tf: Define las salidas que el módulo genera para ser utilizadas en otros módulos o configuraciones.

README.md: Documentación del módulo (opcional, pero recomendado).

- Proponer la estructura de archivos y directorios para un proyecto hipotético que incluya tres módulos: network, database y application. Justificar la jerarquía elegida.

```plaintext
terraform-project/
│── modules/                   # Módulos reutilizables
│   ├── network/               
│   │   ├── main.tf            
│   │   ├── variables.tf       
│   │   ├── outputs.tf         
│   │   └── README.md          
│   ├── database/              
│   │   ├── main.tf            
│   │   ├── variables.tf       
│   │   ├── outputs.tf         
│   │   └── README.md          
│   ├── application/           
│   │   ├── main.tf            
│   │   ├── variables.tf       
│   │   ├── outputs.tf         
│   │   └── README.md          
│── main.tf                    # Infraestructura principal
│── variables.tf                # Variables globales
│── outputs.tf                  # Salidas globales
│── backend.tf                  # Configuración del backend remoto (opcional)
│── .gitignore                   # Ignorar archivos innecesarios
│── README.md                    # Descripción del proyecto
```
Cada componente principal de la infraestructura (network, database y application) se organiza en módulos dentro de modules/. Esto ofrece varios beneficios:

**1. Separación en Módulos (modules/)**

Cada módulo contiene:

- main.tf → Define los recursos principales del módulo.

- variables.tf → Contiene las variables necesarias para el módulo.

- outputs.tf → Define las salidas (outputs) del módulo, útiles para conectar módulos entre sí.

- README.md → Explica qué hace el módulo y cómo usarlo.

**2. Archivos Globales en la Raíz**

Los archivos en la raíz (main.tf, variables.tf, outputs.tf, etc.) manejan la infraestructura general del proyecto.

- main.tf → Importa y organiza los módulos (network, database, application).

- variables.tf → Define variables globales como nombres de recursos, regiones, etc.

- outputs.tf → Contiene valores de salida que pueden ser utilizados por otros módulos o herramientas externas.

- backend.tf (opcional) → Permite definir un backend remoto (ej. S3 en AWS) para almacenar el estado de Terraform.

- .gitignore → Evita subir archivos innecesarios o sensibles al repositorio.

- README.md → Explica el propósito del proyecto y cómo usarlo.

## Tarea teórica P2:

- Describir un flujo simple de despliegue donde un desarrollador hace un cambio en el código, se construye una nueva imagen Docker y se actualiza un Deployment de Kubernetes.

**1️⃣ Hacer un cambio en el código y subirlo a Git**

`git add . `

`git commit -m "Actualización de la aplicación"`

`git push origin main`

**2️⃣ Construir y subir la nueva imagen Docker**

`docker build -t Juniel/mi-app:v2 .`

`docker push Juniel/mi-app:v2`

**3️⃣ Actualizar el Deployment en Kubernetes**

```
apiVersion: apps/v1
kind: Deployment
metadata:
  name: mi-app
spec:
  replicas: 3
  selector:
    matchLabels:
      app: mi-app
  template:
    metadata:
      labels:
        app: mi-app
    spec:
      containers:
        - name: mi-app
          image: miusuario/mi-app:v2  #Nueva versión de la imagen
          ports:
            - containerPort: 80
```
**Aplicar los cambios en Kubernetes:**

`kubectl apply -f deployment.yaml`

**Verificar el despliegue**

`kubectl get pods`

`kubectl rollout status deployment/mi-app`

- Explicar las ventajas de usar Kubernetes para escalar una aplicación en un evento de alto tráfico.

**Ventajas de Kubernetes para escalar en eventos de alto tráfico**

1. Escalado automático (Auto-scaling)

Kubernetes escala automáticamente la cantidad de pods según la carga del sistema usando el Horizontal Pod Autoscaler (HPA).

Si el tráfico aumenta Kubernetes puede crear más instancias de la aplicación para soportar la demanda.

2. Balanceo de carga

Kubernetes usa Services para distribuir el tráfico entre múltiples pods, evitando que un solo nodo o pod se sobrecargue.

3. Alta disponibilidad y tolerancia a fallos

Si un pod falla Kubernetes lo reemplaza automáticamente.

Si un nodo se cae los pods pueden ser reasignados a otros nodos disponibles.

4. Despliegues sin interrupciones

Con estrategias como Rolling Updates o Canary Deployment permite actualizar la aplicación sin afectar a los usuarios.

## Tarea teórica P3: ##

- Investigar y describir cómo Prometheus y Grafana se integran con Kubernetes para monitorear los contenedores y el cluster.


**Prometheus** es una herramienta de monitoreo que usa series temporales que recopila métricas de aplicaciones y componentes del clúster. 

Ejemplo de configuración en `prometheus.yml`:

```yaml
global:
  scrape_interval: 15s

scrape_configs:
  - job_name: 'mi-app'
    static_configs:
      - targets: ['app-service:8080']
```

Prometheus se integra con Kubernetes mediante **Service Discovery**, detectando automáticamente pods y servicios para recopilar métricas sin configuraciones manuales.

**Grafana**, por su parte, proporciona visualización avanzada mediante dashboards personalizables. A través de consultas en **PromQL**, se pueden graficar indicadores clave como latencia de peticiones, uso de recursos y tasas de error, facilitando la supervisión en tiempo real.


- Proponer un set de métricas y alertas mínimas para una aplicación web (por ejemplo, latencia de peticiones, uso de CPU/memoria, tasa de errores).

Métricas y alertas mínimas recomendadas

Para garantizar un monitoreo eficiente de una aplicación web en Kubernetes, se recomienda establecer métricas clave y configurar alertas asociadas:

| **Métrica** | **Descripción** | **Umbral de alerta** |
|------------|---------------|----------------------|
| **Latencia de peticiones** (`http_request_duration_seconds`) | Tiempo de respuesta de la API. | P95 > 500ms |
| **Tasa de errores HTTP** (`http_requests_total{status="5xx"}`) | Cantidad de respuestas con código 5xx. | Más del 5% de errores en 5 min |
| **Uso de CPU** (`container_cpu_usage_seconds_total`) | Consumo de CPU por contenedor. | Más del 80% del límite asignado |
| **Uso de memoria** (`container_memory_usage_bytes`) | Consumo de RAM por contenedor. | Más del 80% del límite asignado |
| **Estado de réplicas** (`kube_deployment_status_replicas_available`) | Número de réplicas activas. | Menos réplicas de las esperadas |
| **Errores en logs** (`log_errors_total`) | Cantidad de errores en registros. | Más de 10 errores en 5 min |

## Tarea Teorica P4 ##


- Diferencia entre Entrega Continua (Continuous Delivery) y Despliegue Continuo (Continuous Deployment)

**Entrega Continua (CD - Continuous Delivery)**
Es la práctica de asegurarse de que el código esté siempre en un estado **listo para producción**. Cada cambio en el código pasa por una serie de pruebas y revisiones, y una vez aprobado, se deja preparado para ser desplegado manualmente cuando el equipo lo decida.

**Despliegue Continuo (CD - Continuous Deployment)**
Es la evolución del proceso de entrega continua, donde cada cambio aprobado se **despliega automáticamente en producción** sin intervención manual. Solo se detendría en caso de que alguna prueba falle.


**Comparación**

| **Concepto**              | **Entrega Continua (Continuous Delivery)** | **Despliegue Continuo (Continuous Deployment)** |
|---------------------------|--------------------------------|-----------------------------------|
| **¿Se automatiza el proceso hasta producción?** | No, requiere aprobación manual.  | Sí, todo el proceso es automático. |
| **¿Cuándo se libera el software?** | Cuando el equipo lo decide.       | Inmediatamente después de pasar las pruebas. |
| **Nivel de riesgo**       | Bajo (control manual).         | Medio (totalmente automatizado). |
| **Ejemplo de uso**        | Aplicaciones críticas (banca, salud). | Aplicaciones web con despliegue frecuente. |

---

- Relevancia de las Pruebas Automáticas en el Pipeline

🔹 **Pruebas Unitarias**
- Verifican el **funcionamiento de unidades individuales** de código (como funciones o métodos).
- Se ejecutan rápidamente y detectan errores en una etapa temprana.
- **Ejemplo:** Probar que una función matemática devuelve el resultado esperado.

🔹 **Pruebas de Integración**
- Verifican la **interacción entre diferentes módulos** del sistema.
- Aseguran que los componentes se comuniquen correctamente.
- **Ejemplo:** Comprobar que un servicio backend responde correctamente a una solicitud de la API.

🔹 **Pruebas de Seguridad**
- Detectan vulnerabilidades y posibles riesgos de seguridad.
- Evitan que código con fallos de seguridad llegue a producción.
- **Ejemplo:** Escaneo de inyecciones SQL o autenticaciones inseguras.

