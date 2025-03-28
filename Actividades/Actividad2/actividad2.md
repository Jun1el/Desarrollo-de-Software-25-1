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

- Proponer un set de métricas y alertas mínimas para una aplicación web (por ejemplo, latencia de peticiones, uso de CPU/memoria, tasa de errores).