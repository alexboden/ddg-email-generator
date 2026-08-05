

# Generador de Correo Electrónico Temporal

Un script simple de Python que genera direcciones de correo electrónico temporales utilizando la API de Protección de Correo de DuckDuckGo y copiándolas en tu portapapeles. Vincula el script a un atajo de teclado para tener acceso instantáneo al registrarte en nuevas cuentas o servicios.

## Requisitos Previos

Crea un archivo `.env` en el mismo directorio que el script y agrega tu token de acceso de la API de DuckDuckGo:

   ```
   DUCKDUCKGO_ACCESS_TOKEN=your_access_token_here
   ```

Puedes encontrarlo visitando https://duckduckgo.com/email/settings/autofill e inspeccionando las solicitudes POST de la red al generar una nueva dirección de correo electrónico.

## Instalación de Dependencias

Para ejecutar el script, necesitas instalar los paquetes de Python requeridos. Usa el siguiente comando para instalarlos:

   ```
   pip install -r requirements.txt
   ```

## Configuración de un Atajo de Teclado

### macOS

1. Usa Automator para crear una Acción Rápida que ejecute el script de Python.
```
python /path/to/this/repo/main.py
```
3. En Preferencias del Sistema > Teclado > Atajos > Servicios, asigna un atajo de teclado a esta Acción Rápida.
