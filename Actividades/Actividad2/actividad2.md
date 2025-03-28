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

- Explicar las ventajas de usar Kubernetes para escalar una aplicación en un evento de alto tráfico.