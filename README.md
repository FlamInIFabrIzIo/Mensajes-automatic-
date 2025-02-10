# 📧 Programador de Correos Automáticos

Este script en Python envía un correo electrónico automáticamente todos los días a una hora programada utilizando el protocolo SMTP de Gmail.

## 📌 Requisitos

- Python 3.x instalado
- Una cuenta de Gmail
- Generar una contraseña de aplicación en Gmail para evitar problemas de autenticación
- Instalar la siguiente librería:
  ```sh
  pip install schedule
  ```

## ⚙️ Configuración

Antes de ejecutar el script, debes configurar las variables de entorno para almacenar tus credenciales de Gmail de forma segura:

```sh
export EMAIL_REMITE="tucorreo@gmail.com"
export EMAIL_PASS="tu_contraseña"
export EMAIL_DESTINO="correo_destino@gmail.com"
```

## 📜 Descripción del Código

El script realiza las siguientes acciones:

1. Obtiene las credenciales del remitente desde variables de entorno.
2. Crea un mensaje con un saludo diario.
3. Se conecta al servidor SMTP de Gmail y envía el correo.
4. Utiliza la librería `schedule` para programar el envío todos los días a las 08:05 AM.
5. El script se ejecuta en un bucle infinito, verificando si es hora de enviar el correo.

## 🚀 Ejecución

Para ejecutar el script, simplemente usa:

```sh
python script.py
```

## 🛠 Posibles Errores y Soluciones

- **SMTP Authentication Error:** Verifica que activaste "Acceso de apps menos seguras" en Gmail o usa una contraseña de aplicación.
- **Permiso denegado en variables de entorno:** Asegúrate de exportarlas correctamente antes de ejecutar el script.

## 📩 Contacto

Si tienes dudas o mejoras, ¡no dudes en contribuir! 😃
