from PySide6.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QLineEdit, QLabel, QFileDialog, QMessageBox, QInputDialog
)
from PySide6.QtGui import QFont, QPalette, QColor
from PySide6.QtCore import Qt
import sys
from modulos.crear_qr import codigo_personalizado, codigo_predeterminado
from modulos.leer_qr import opc_leer_qr

class QRCodeApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Generador de Códigos QR - Moderno")
        self.setGeometry(100, 100, 600, 400)
        self.setStyleSheet(self.window_style())

        # Widget central
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Layout principal
        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        # Etiqueta principal
        label = QLabel("Bienvenido al Generador de Códigos QR")
        label.setFont(QFont("Arial", 20))
        label.setAlignment(Qt.AlignCenter)
        label.setStyleSheet("color: white; margin-bottom: 20px;")
        layout.addWidget(label)

        # Botón para crear QR clásico
        btn_qr_clasico = QPushButton("Crear QR Clásico")
        btn_qr_clasico.setFont(QFont("Arial", 14))
        btn_qr_clasico.setStyleSheet(self.button_style())
        btn_qr_clasico.clicked.connect(self.crear_qr_clasico)
        layout.addWidget(btn_qr_clasico)

        # Botón para crear QR personalizado
        btn_qr_personalizado = QPushButton("Crear QR Personalizado")
        btn_qr_personalizado.setFont(QFont("Arial", 14))
        btn_qr_personalizado.setStyleSheet(self.button_style())
        btn_qr_personalizado.clicked.connect(self.crear_qr_personalizado)
        layout.addWidget(btn_qr_personalizado)

        # Botón para leer QR
        btn_leer_qr = QPushButton("Leer QR")
        btn_leer_qr.setFont(QFont("Arial", 14))
        btn_leer_qr.setStyleSheet(self.button_style())
        btn_leer_qr.clicked.connect(self.leer_qr)
        layout.addWidget(btn_leer_qr)

        # Botón para salir
        btn_salir = QPushButton("Salir")
        btn_salir.setFont(QFont("Arial", 14))
        btn_salir.setStyleSheet(self.button_style())
        btn_salir.clicked.connect(self.close)
        layout.addWidget(btn_salir)

    def window_style(self):
        return """
        QMainWindow {
            background-color: rgba(30, 30, 30, 0.95);
            border-radius: 15px;
        }
        """

    def button_style(self):
        return """
        QPushButton {
            background-color: rgba(70, 130, 180, 0.8);
            color: white;
            border: none;
            border-radius: 10px;
            padding: 10px 20px;
        }
        QPushButton:hover {
            background-color: rgba(70, 130, 180, 1.0);
        }
        QPushButton:pressed {
            background-color: rgba(50, 90, 140, 1.0);
        }
        """

    def crear_qr_clasico(self):
        texto, ok = self.get_text_input("Crear QR Clásico", "Introduce el texto para el QR clásico:")
        if ok and texto:
            codigo_predeterminado(texto)
            QMessageBox.information(self, "Éxito", "El código QR clásico se ha creado correctamente.")

    def crear_qr_personalizado(self):
        texto, ok = self.get_text_input("Crear QR Personalizado", "Introduce el texto para el QR personalizado:")
        if ok and texto:
            # Obtener el formato del QR
            opciones = ["Círculo", "Cuadrado", "Barra vertical", "Barra Horizontal", "Redondeado", "Cuadrado Grande (clásico)"]
            tipo, ok = QInputDialog.getItem(self, "Seleccionar Formato QR", "Selecciona el formato del QR:", opciones, 0, False)
            if ok and tipo:
                # Obtener el nombre del archivo
                nombre, ok = self.get_text_input("Nombre del Archivo", "Introduce el nombre del archivo QR (sin extensión):")
                if ok and nombre:
                    # Llamar a la función `codigo_personalizado` con los datos obtenidos
                    codigo_personalizado(texto, opciones.index(tipo) + 1, nombre + ".png")
                    QMessageBox.information(self, "Éxito", "El código QR personalizado se ha creado correctamente.")

    def leer_qr(self):
        archivo, _ = QFileDialog.getOpenFileName(self, "Seleccionar Código QR", "", "Imágenes (*.png *.jpg *.jpeg)")
        if archivo:
            resultado = opc_leer_qr(archivo)
            QMessageBox.information(self, "Resultado del QR", f"Contenido del QR: {resultado}")

    def get_text_input(self, titulo, etiqueta):
        input_dialog = QInputDialog(self)
        input_dialog.setWindowTitle(titulo)
        input_dialog.setLabelText(etiqueta)
        input_dialog.setInputMode(QInputDialog.TextInput)
        input_dialog.setOkButtonText("Aceptar")
        input_dialog.setCancelButtonText("Cancelar")
        if input_dialog.exec() == QInputDialog.Accepted:
            return input_dialog.textValue(), True
        return "", False

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("Fusion")

    # Configuración de la paleta para tema oscuro
    palette = QPalette()
    palette.setColor(QPalette.Window, QColor(30, 30, 30))
    palette.setColor(QPalette.WindowText, QColor(255, 255, 255))
    palette.setColor(QPalette.Base, QColor(50, 50, 50))
    palette.setColor(QPalette.AlternateBase, QColor(30, 30, 30))
    palette.setColor(QPalette.ToolTipBase, QColor(255, 255, 255))
    palette.setColor(QPalette.ToolTipText, QColor(255, 255, 255))
    palette.setColor(QPalette.Text, QColor(255, 255, 255))
    palette.setColor(QPalette.Button, QColor(70, 130, 180))
    palette.setColor(QPalette.ButtonText, QColor(255, 255, 255))
    palette.setColor(QPalette.BrightText, QColor(255, 0, 0))
    palette.setColor(QPalette.Highlight, QColor(70, 130, 180))
    palette.setColor(QPalette.HighlightedText, QColor(0, 0, 0))
    app.setPalette(palette)

    window = QRCodeApp()
    window.show()
    sys.exit(app.exec())
