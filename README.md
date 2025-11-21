# Laboratorio 7 - Aplicaciones Flask con AWS

Este repositorio contiene dos aplicaciones Flask desarrolladas para el Laboratorio 7 de Introducción a la Computación Cognitiva.

## 📁 Estructura del Proyecto

```
Laboratorio_7/
├── pregunta1/          # Aplicación de Conversión de Divisas
├── pregunta2/          # Aplicación de Catálogo de Vehículos con RDS MySQL
├── venv/              # Entorno virtual de Python (excluido en git)
└── README.md          # Este archivo
```

## 🎯 Pregunta 1 - Conversión de Divisas

Aplicación Flask que consume la API ExchangeRate-API para mostrar tasas de cambio actualizadas.

### Características:
- Conversión de USD a EUR y PEN
- Interfaz responsive con Bootstrap 5
- Despliegue en AWS Lambda con Zappa

### Archivos:
- `app.py` - Aplicación Flask principal
- `templates/index.html` - Interfaz de usuario
- `requirements.txt` - Dependencias del proyecto
- `zappa_settings.json` - Configuración para AWS Lambda

## 🚗 Pregunta 2 - Catálogo de Vehículos

Aplicación Flask con conexión a AWS RDS MySQL para gestionar un catálogo de vehículos.

### Características:
- CRUD completo de vehículos (marca, modelo, precio)
- Conexión a AWS RDS MySQL
- Interfaz web con Bootstrap 5
- Auto-creación de base de datos y tablas
- Despliegue en AWS Lambda con Zappa

### Configuración de Base de Datos:
```python
DB_HOST = "vehiculos-db.cfs4boqm1wbl.us-east-1.rds.amazonaws.com"
DB_USER = "root"
DB_PASSWORD = "Ut3c$201810610"
DB_NAME = "vehiculos_db"
DB_PORT = 3306
```

### Archivos:
- `app.py` - Aplicación Flask con conexión MySQL
- `templates/` - Templates HTML (base.html, index.html, agregar.html)
- `requirements.txt` - Dependencias (Flask, PyMySQL, Zappa)
- `zappa_settings.json` - Configuración para AWS Lambda

## 🚀 Instalación Local

1. Clonar el repositorio:
```bash
git clone https://github.com/keneth-urbizagastegui/Laboratorio_7.git
cd Laboratorio_7
```

2. Crear entorno virtual:
```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

3. Instalar dependencias:
```bash
# Para pregunta1
cd pregunta1
pip install -r requirements.txt

# Para pregunta2
cd ../pregunta2
pip install -r requirements.txt
```

4. Ejecutar aplicaciones:
```bash
python app.py
```

## ☁️ Despliegue en AWS

Ambas aplicaciones están configuradas para despliegue en AWS Lambda usando Zappa:

```bash
# En cada carpeta de aplicación
zappa deploy dev
```

## 🛠️ Tecnologías Utilizadas

- **Python 3.9**
- **Flask 2.3.3**
- **Bootstrap 5**
- **PyMySQL**
- **Zappa** (para AWS Lambda)
- **AWS RDS MySQL**
- **ExchangeRate-API**

## 📬 Contacto

Keneth Urbizagastegui - [Tu email]

Proyecto desarrollado para el curso de Introducción a la Computación Cognitiva.