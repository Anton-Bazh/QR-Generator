import os
import qrcode
from modulos.sistema import ruta_fin_qr, msg_listo
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers import (
    CircleModuleDrawer,
    GappedSquareModuleDrawer,
    HorizontalBarsDrawer,
    RoundedModuleDrawer,
    SquareModuleDrawer,
    VerticalBarsDrawer,
)

def crear_qr(valorQR, opc_usuario, imagenQR):
    carpeta_qr = ruta_fin_qr()
    imagenQR = os.path.join(carpeta_qr, imagenQR)

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(valorQR)

    # Seleccionar el estilo del código QR
    if opc_usuario == 1:
        tipoQRC = CircleModuleDrawer()
    elif opc_usuario == 2:
        tipoQRC = GappedSquareModuleDrawer()
    elif opc_usuario == 3:
        tipoQRC = VerticalBarsDrawer()
    elif opc_usuario == 4:
        tipoQRC = HorizontalBarsDrawer()
    elif opc_usuario == 5:
        tipoQRC = RoundedModuleDrawer()
    elif opc_usuario == 6:
        tipoQRC = SquareModuleDrawer()
    else:
        tipoQRC = SquareModuleDrawer()

    img = qr.make_image(image_factory=StyledPilImage, module_drawer=tipoQRC)

    with open(imagenQR, "wb") as f:
        img.save(f)

def codigo_predeterminado(valorQR):
    opc_usuario = 6  # Estilo predeterminado (cuadrado grande)
    imagenQR = "qr_predeterminado.png"
    crear_qr(valorQR, opc_usuario, imagenQR)
    msg_listo()

def codigo_personalizado(valorQR, opc_usuario, nombreQR):
    imagenQR = nombreQR + ".png"
    crear_qr(valorQR, opc_usuario, imagenQR)
    msg_listo()
