import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QVBoxLayout, QPushButton, QMessageBox
import requests

class RegistroAlumnos(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Registro de alumnos")
        self.resize(400, 200)

        layout = QVBoxLayout()

        # Nombre
        self.nombre_label = QLabel("Nombre")
        self.nombre_input = QLineEdit()
        layout.addWidget(self.nombre_label)
        layout.addWidget(self.nombre_input)

        # Apellido
        self.apellido_label = QLabel("Apellido")
        self.apellido_input = QLineEdit()
        layout.addWidget(self.apellido_label)
        layout.addWidget(self.apellido_input)

        # Identificación
        self.identificacion_label = QLabel("Identificación")
        self.identificacion_input = QLineEdit()
        layout.addWidget(self.identificacion_label)
        layout.addWidget(self.identificacion_input)

        # Edad
        self.edad_label = QLabel("Edad")
        self.edad_input = QLineEdit()
        layout.addWidget(self.edad_label)
        layout.addWidget(self.edad_input)

        # Botón para enviar solicitud
        self.enviar_button = QPushButton("Enviar solicitud")
        layout.addWidget(self.enviar_button)

        # Conectar el botón a la función para enviar la solicitud
        self.enviar_button.clicked.connect(self.enviar_solicitud)

        self.setLayout(layout)

    def enviar_solicitud(self):
        nombre = self.nombre_input.text()
        apellido = self.apellido_input.text()
        identificacion = self.identificacion_input.text()
        edad = self.edad_input.text()

        data = {
            "nombre": nombre,
            "apellido": apellido,
            "identificacion": identificacion,
            "edad": edad
        }

        response = requests.post("http://127.0.0.1:5000/solicitudes_ingreso", json=data)

        if response.status_code == 200:
            QMessageBox.information(self, "Éxito", "Solicitud enviada exitosamente")
        else:
            QMessageBox.critical(self, "Error", "Error al enviar la solicitud")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = RegistroAlumnos()
    window.show()
    sys.exit(app.exec_())
