# Actividad12: Revisión de fixtures en pruebas
## Objetivos de la Actividad

- Comprender el propósito y funcionamiento de los fixtures en Pytest.
- Aplicar fixtures con alcance a nivel de módulo para inicializar y limpiar la base de datos de pruebas.
- Aprender a cargar datos desde archivos `.json` para usarlos como datos de prueba reutilizables.
- Implementar casos de prueba que validen operaciones básicas en modelos ORM (Object Relational Mapping).
- Escribir pruebas limpias, mantenibles y desacopladas del código de producción.


## Resumen de la Actividad

En esta actividad se trabajó con el framework Pytest para implementar pruebas automatizadas orientadas a modelos que interactúan con bases de datos, utilizando SQLAlchemy.  
Se definió un fixture global con alcance de módulo para crear y cerrar la base de datos antes y después de la ejecución del conjunto de pruebas.  
Asimismo, se incorporó la carga de datos desde un archivo externo `.json`, lo cual permitió centralizar y reutilizar la información en distintos métodos de prueba.  
Finalmente, se validó el correcto funcionamiento del método `create()` de un modelo `Account`, comprobando que los registros se almacenan y recuperan de manera esperada.

## Instalación de Dependencias

```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
pip install Flask
pip install Flask-SQLAlchemy
pip install pytest
```

## Estructura del Proyecto

```bash 
./
├── models/
│   ├── __init__.py
│   └── account.py
├── tests/
│   ├── fixtures/
│   │   └── account_data.json
│   ├── test_account.py
└── setup.cfg
```


## Principios SOLID usados en el proyecto 

### 1. **Principio de Responsabilidad Única (SRP)**
Cada componente del sistema tiene una única responsabilidad:
- El archivo de prueba `test_account.py` está enfocado exclusivamente en verificar el comportamiento del modelo `Account`.
- El fixture `setup_database()` se encarga únicamente de inicializar y cerrar la base de datos.
- La función `setup_class()` tiene como única responsabilidad la carga de datos desde el archivo `.json`.


### 2. **Principio de Abierto/Cerrado (OCP)**

- Es posible agregar nuevas pruebas o ampliar el archivo `.json` con más datos sin necesidad de modificar la lógica base del test.


### Paso 1: Inicialización de la base de datos

**Código implementado:**

```python
import pytest
from models import db  # Objeto de base de datos de SQLAlchemy

@pytest.fixture(scope="module", autouse=True)
def setup_database():
    """Configura la base de datos antes y después de todas las pruebas"""
    db.create_all()       # Se ejecuta antes de las pruebas: crea las tablas necesarias
    yield                 # Separador entre lógica de preparación y limpieza
    db.session.close()    # Se ejecuta después de las pruebas: cierra la sesión activa
```

**@pytest.fixture(scope="module", autouse=True)**
  
Define el fixture que se ejecuta automaticamente una vez por modulo.

**yield**

Actúa como un separador: todo lo que va antes se ejecuta antes de las pruebas, y todo lo que va después se ejecuta al finalizar.

### Paso 2: Cargar datos de prueba

**Objetivo:**  
Cargaremos un conjunto de datos de prueba desde un archivo `.json` antes de ejecutar las pruebas unitarias de una clase específica.

### Paso 3: Escribir un caso de prueba para crear una cuenta

**Objetivo:**  
Veremos que el método `create()` del modelo `Account` funciona correctamente insertando un registro en la base de datos y permitiendo su recuperación mediante una consulta.

**Código del caso de prueba:**
```python
def test_create_an_account(self):
    """Probar la creación de una sola cuenta"""
    data = ACCOUNT_DATA[0]  # Obtener la primera cuenta del JSON
    account = Account(**data)  # Crear una instancia del modelo Account
    account.create()  # Insertar en la base de datos
    assert len(Account.all()) == 1  # Verificar que hay exactamente una cuenta
```

- **assert**: Se utiliza para verificar que el número de registros sea exactamente uno confirmando así que la operación de creación fue exitosa.

### Paso 4: Probar la creación de múltiples cuentas

**Objetivo:**  
Verificamos que el sistema es capaz de crear múltiples cuentas de usuario n la base de datos de forma correcta y eficiente.

**Código del caso de prueba:**
```python
def test_create_all_accounts(self):
    """Probar la creación de múltiples cuentas"""
    for data in ACCOUNT_DATA:
        account = Account(**data)
        account.create()
    assert len(Account.all()) == len(ACCOUNT_DATA)
```

### Paso 5: Limpieza de la base de datos entre pruebas

**Código implementado:**
```python
def setup_method(self):
    """Truncar las tablas antes de cada prueba"""
    db.session.query(Account).delete()
    db.session.commit()

def teardown_method(self):
    """Eliminar la sesión después de cada prueba"""
    db.session.remove()
```

- **setup_method(self)**: Este método se ejecuta automáticamente antes de cada prueba. Elimina todos los registros de la tabla Account para garantizar un entorno limpio.

- **teardown_method(self)**: Se ejecuta después de cada prueba. Cierra la sesión actual de SQLAlchemy para liberar recursos y evitar errores por conexiones abiertas.