import os
import datetime

def ruta_fin_qr():
    descargas_path = os.path.join(os.path.expanduser('~'), 'Downloads') #Obtener ruta raiz de descargas
    carpeta_qr = os.path.join(descargas_path, 'Qr') #Crear carpeta de qr
    if not os.path.exists(carpeta_qr): #Si la carpeta no existe...
        os.makedirs(carpeta_qr)  #...pues lo crea
    return carpeta_qr

def obtener_nombre():
    fecha_hora_actual = datetime.datetime.now()
    nombre = str(fecha_hora_actual.strftime("%d%m%y-%H%M%S"))  # Cambio los ":" a "" en la marca de tiempo.
    return nombre + ".png"