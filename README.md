<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Programador de Correos Automáticos</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            margin: 20px;
            padding: 20px;
            background-color: #f4f4f4;
        }
        h1, h2 {
            color: #333;
        }
        pre {
            background: #222;
            color: #fff;
            padding: 10px;
            border-radius: 5px;
            overflow-x: auto;
        }
        code {
            color: #f4b400;
        }
    </style>
</head>
<body>
    <h1>📧 Correos Automáticos</h1>
    <p>Este script en Python envía un correo electrónico automáticamente todos los días a una hora programada utilizando el protocolo SMTP de Gmail.</p>
    
    <h2>📌 Requisitos</h2>
    <ul>
        <li>Python 3.x instalado</li>
        <li>Una cuenta de Gmail</li>
        <li>Generar una contraseña de aplicación en Gmail para evitar problemas de autenticación</li>
        <li>Las siguientes librerías instaladas:<br>
            <pre><code>pip install schedule</code></pre>
        </li>
    </ul>
    
    <h2>⚙️ Configuración</h2>
    <p>Antes de ejecutar el script, debes configurar las variables de entorno para almacenar tus credenciales de Gmail de forma segura:</p>
    <pre><code>
    export EMAIL_REMITE="tucorreo@gmail.com"
    export EMAIL_PASS="tu_contraseña"
    export EMAIL_DESTINO="correo_destino@gmail.com"
    </code></pre>
    
    <h2>📜 Descripción del Código</h2>
    <p>El script realiza las siguientes acciones:</p>
    <ol>
        <li>Obtiene las credenciales del remitente desde variables de entorno.</li>
        <li>Crea un mensaje con un saludo diario.</li>
        <li>Se conecta al servidor SMTP de Gmail y envía el correo.</li>
        <li>Utiliza la librería <code>schedule</code> para programar el envío todos los días a las 08:05 AM.</li>
        <li>El script se ejecuta en un bucle infinito, verificando si es hora de enviar el correo.</li>
    </ol>
    
    <h2>🚀 Ejecución</h2>
    <p>Para ejecutar el script, simplemente usa:</p>
    <pre><code>python script.py</code></pre>
    
    <h2>🛠 Posibles Errores y Soluciones</h2>
    <ul>
        <li><strong>SMTP Authentication Error:</strong> Verifica que activaste "Acceso de apps menos seguras" en Gmail o usa una contraseña de aplicación.</li>
        <li><strong>Permiso denegado en variables de entorno:</strong> Asegúrate de exportarlas correctamente antes de ejecutar el script.</li>
    </ul>
    
    <h2>📩 Contacto</h2>
    <p>Si tienes dudas o mejoras, ¡no dudes en contribuir!</p>
</body>
</html>
