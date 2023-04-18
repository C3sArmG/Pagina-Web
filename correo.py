from msilib.schema import File
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
import algoritmo 

def EnviarCorreo(filename, correo):
    Ruta, Clave, Clave_Privada = algoritmo.Encriptar(filename)
    # Define los parametros del correo electronico
    remitente = "proyecto.computacional03@gmail.com"
    destinatario = correo
    asunto = "Archivo Encriptado"
    cuerpo = "En este correo se adjunta su archivo encriptado, y su clave privada \nSu Clave Privada es: ({} , {})".format(Clave, Clave_Privada)
    cuerpo1=str(cuerpo)
    # Crea un objeto MIMEMultipart
    mensaje = MIMEMultipart()
    mensaje["From"] = remitente
    mensaje["To"] = destinatario
    mensaje["Subject"] = asunto

    # Agrega el cuerpo del mensaje como objeto MIMEText
    mensaje.attach(MIMEText(cuerpo1, "plain"))

    # Adjunta el archivo al mensaje como objeto MIMEApplication
    archivo_adjunto = Ruta
    with open(archivo_adjunto, "rb") as adjunto:
        mensaje_adjunto = MIMEApplication(adjunto.read(), _subtype="pdf")
        mensaje_adjunto.add_header("Content-Disposition", "attachment", filename="Archivo Encriptado.enc")
        mensaje.attach(mensaje_adjunto)

    # Env�a el correo electr�nico
    servidor_smtp = smtplib.SMTP("smtp.gmail.com", 587)
    servidor_smtp.starttls()
    servidor_smtp.login("proyecto.computacional03@gmail.com", "wgtlgtnzmvybovad")
    servidor_smtp.sendmail(remitente, destinatario, mensaje.as_string())
    servidor_smtp.quit()
