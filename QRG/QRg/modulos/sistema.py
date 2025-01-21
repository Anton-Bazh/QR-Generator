import os
import datetime

def ruta_fin_qr():
    descargas_path = os.path.join(os.path.expanduser('~'), 'Downloads') 
    carpeta_qr = os.path.join(descargas_path, 'Qr')
    if not os.path.exists(carpeta_qr):
        os.makedirs(carpeta_qr)
    return carpeta_qr

def obtener_nombre():
    fecha_hora_actual = datetime.datetime.now()
    nombre = str(fecha_hora_actual.strftime("%d%m%y-%H%M%S"))
    return nombre + ".png"

def msg_listo():
    print(" Listo ")
