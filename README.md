# ERPNext Renamer

**ERPNext Renamer** is a graphical tool built with Python and `customtkinter`, designed to simplify the process of renaming custom fields (`Custom Field`) in a local ERPNext instance running inside Docker.

## 🎯 Features

This program allows you to:

- Specify multiple pairs of old and new `fieldnames`.
- Automatically execute the `frappe.rename_doc` command inside the Docker container.
- Apply changes without opening a terminal or typing manual commands.

## 🖼️ Interface

The interface is built with `customtkinter`, modern and simple:

- Input fields for the current and new names of the `Custom Field`.
- A button to dynamically add more rows.
- A button to batch rename fields.

## ⚙️ Requirements

- Python 3.8 or higher
- Docker
- Access to the container where ERPNext is running (usually named `frappe_app` or similar)
- Python dependencies:
  - `customtkinter`

## 🛠️ Technology Used

- Python  
- customtkinter  
- Docker  
- Frappe Framework

## 📂 Project Structure

```
erpnext-renamer/
├── app.py # Main UI
├── renamer.py # Logic for renaming fields using Docker
├── main.py # App initializer
├── config.json # Container configuration
├── requirements.txt # Python dependencies
├── .gitignore
└── README.md
```

 ## ✅ Status: 
 In progress...

 ## 🧑‍💻 Developed by:
 Ixgramdev


-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# ERPNext Renamer

**ERPNext Renamer** es una herramienta con interfaz gráfica construida en Python y `customtkinter`. 
Diseñada para simplificar el proceso de renombrar campos personalizados (`Custom Field`) en una instancia local de ERPNext ejecutada dentro de Docker.

## 🎯 Funcionalidad

Este programa permite:

- Especificar múltiples pares de `fieldnames` antiguos y nuevos.
- Ejecutar automáticamente el comando `frappe.rename_doc` dentro del contenedor de Docker.
- Aplicar los cambios sin necesidad de abrir una consola o escribir comandos manuales.

## 🖼️ Interfaz

La interfaz está diseñada con `customtkinter`, moderna y simple:

- Campos para ingresar los nombres actuales y nuevos de los `Custom Field`.
- Botón para agregar más filas dinámicamente.
- Botón para ejecutar el renombrado en lote.

## ⚙️ Requisitos

- Python 3.8 o superior
- Docker
- Acceso al contenedor donde está corriendo ERPNext (usualmente llamado `frappe_app` o similar)
- Dependencias Python:
  - `customtkinter`

🛠️ Tecnología usada

- Python  
- customtkinter  
- Docker  
- Frappe Framework

📂 Estructura del proyecto

```
erpnext-renamer/
├── app.py             # Interfaz principal
├── renamer.py         # Lógica para renombrar campos usando Docker
├── main.py            # Inicializador de la app
├── config.json        # Configuración del contenedor
├── requirements.txt   # Dependencias
├── .gitignore
└── README.md
```

## ✅ Estado: 
In progress...

## 🧑‍💻 Desarrollado por:
Ixgramdev
