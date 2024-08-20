#!/bin/bash

# Actualiza los paquetes e instala pip y otras herramientas necesarias
sudo apt-get update -y
sudo apt-get install -y python3-pip python3-venv

# Crea un entorno virtual (opcional, pero recomendado)
python3 -m venv env
source env/bin/activate

# Instala las dependencias desde el archivo requirements.txt
if [ -f "requirements.txt" ]; then
    pip install -r requirements.txt
else
    echo "No se encontró el archivo requirements.txt"
fi

# Otras configuraciones específicas del proyecto
echo "Instalación completada."
