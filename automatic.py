import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import schedule
import os
import time

# Configuración del correo
EMAIL_REMITE = os.getenv("EMAIL_REMITE")  # Todos usan una variable de entorno
EMAIL_PASS = os.getenv("EMAIL_PASS")  
EMAIL_DESTINO = os.getenv("EMAIL_DESTINO")  


def enviar_correo():
    asunto = "Saludo Diario"
    mensaje = "¡Buenos días! Espero que tengas un gran día."

    msg = MIMEMultipart()
    msg["From"] = EMAIL_REMITE
    msg["To"] = EMAIL_DESTINO
    msg["Subject"] = asunto
    msg.attach(MIMEText(mensaje, "plain"))

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(EMAIL_REMITE, EMAIL_PASS)
        server.sendmail(EMAIL_REMITE, EMAIL_DESTINO, msg.as_string())
        server.quit()
        print(f"Correo enviado a {EMAIL_DESTINO}")
    except smtplib.SMTPException as e:
        print(f"Error al enviar el correo: {e}")


# Programar las tareas diarias
schedule.every().day.at("08:05").do(enviar_correo)  # Enviar correo 5 minutos después

# Bucle para ejecutar el programador
while True:
    schedule.run_pending()
    time.sleep(1)
