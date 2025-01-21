import cv2

def leer_qr(image_path):
    try:
        img = cv2.imread(image_path)
        det = cv2.QRCodeDetector()
        valorQRLeido, pts, st_code = det.detectAndDecode(img)
        return valorQRLeido
    except cv2.error:
        return None

def opc_leer_qr(archivo):
    """Permite al usuario leer el contenido de un código QR."""
    return leer_qr(archivo)
