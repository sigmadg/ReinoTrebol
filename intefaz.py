import tkinter as tk
from tkinter import messagebox
import requests

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Escuela Mágica")

        self.create_widgets()


    def create_widgets(self):
        root.configure(bg="pink")
        root.geometry("270x340")
        self.title = tk.Label(self.root, text="Solicitud de Ingreso", font=("Arial", 16, "bold"), fg="black", bg="pink")
        self.title.grid(row=0, column=0, columnspan=2, pady=(20, 0))

        self.name_label = tk.Label(self.root, text="Nombre:", font=("Arial", 11), fg="black", bg="pink")
        self.name_label.grid(row=1, column=0, padx=(20, 10), pady=(10, 0))
        self.name_entry = tk.Entry(self.root)
        self.name_entry.grid(row=1, column=1, padx=(10, 20), pady=(10, 0))

        self.surname_label = tk.Label(self.root, text="Apellido:", font=("Arial", 11), fg="black", bg="pink")
        self.surname_label.grid(row=2, column=0, padx=(20, 10), pady=(10, 0))
        self.surname_entry = tk.Entry(self.root)
        self.surname_entry.grid(row=2, column=1, padx=(10, 20), pady=(10, 0))

        self.id_label = tk.Label(self.root, text="Identificación:", font=("Arial", 11), fg="black", bg="pink")
        self.id_label.grid(row=3, column=0, padx=(20, 10), pady=(10, 0))
        self.id_entry = tk.Entry(self.root)
        self.id_entry.grid(row=3, column=1, padx=(10, 20), pady=(10, 0))

        self.age_label = tk.Label(self.root, text="Edad:", font=("Arial", 11), fg="black", bg="pink")
        self.age_label.grid(row=4, column=0, padx=(20, 10), pady=(10, 0))
        self.age_entry = tk.Entry(self.root)
        self.age_entry.grid(row=4, column=1, padx=(10, 20), pady=(10, 0))

        self.submit_button = tk.Button(self.root, text="Enviar Solicitud", font=("Arial", 12), fg="black", bg="lightpink", command=self.submit_form)
        self.submit_button.grid(row=6, column=0, columnspan=2, pady=(10, 10))

        self.btn_actualizar = tk.Button(self.root, text="Actualizar", font=("Arial", 12), fg="black", bg="lightpink", command=self.actualizar_alumno)
        self.btn_actualizar.grid(row=7, column=0, pady=(10, 10))

        self.btn_borrar = tk.Button(self.root, text="Borrar", font=("Arial", 12), fg="black", bg="lightpink", command=self.borrar_alumno)
        self.btn_borrar.grid(row=7, column=1,  pady=(10, 10))

        self.btn_ver_registro = tk.Button(self.root, text="Ver Registro", font=("Arial", 12), fg="black", bg="lightpink", command=self.ver_registro)
        self.btn_ver_registro.grid(row=8, column=0,  pady=(10, 10))

        self.btn_ver_grimorios = tk.Button(self.root, text="Ver Grimorios", font=("Arial", 12), fg="black", bg="lightpink", command=self.ver_grimorios)
        self.btn_ver_grimorios.grid(row=8, column=1,  pady=(10, 10))

        # Colocar botones en la ventana
        # self.btn_actualizar.grid(row=6, column=0, pady=(20, 0))
        # self.btn_borrar.grid(row=6, column=1, pady=(20, 0))
        # self.btn_ver_registro.grid(row=7, column=0, pady=(20, 0))
        # self.btn_ver_grimorios.grid(row=7, column=1, pady=(20, 0))

    def submit_form(self):
        name = self.name_entry.get()
        surname = self.surname_entry.get()
        id_number = self.id_entry.get()
        age = self.age_entry.get()

        data = {
            "nombre": name,
            "apellido": surname,
            "identificacion": id_number,
            "edad": age
        }

        response = requests.post("http://127.0.0.1:5000/solicitudes_ingreso", json=data)
        result = response.json()

        if response.status_code == 201:
            messagebox.showinfo("Éxito", result["message"])
            self.clear_entries()
        else:
            messagebox.showerror("Error", result["message"])

    def clear_entries(self):
        self.name_entry.delete(0, tk.END)
        self.surname_entry.delete(0, tk.END)
        self.id_entry.delete(0, tk.END)
        self.age_entry.delete(0, tk.END)

    def actualizar_alumno(self):
        alumno_id = 4  # Reemplazar con el ID real del alumno
        data = {"nombre": "NuevoNombre"}  # Reemplazar con los datos reales
        response = requests.put(f"http://localhost:5000/actualizacion_ingreso/{alumno_id}", json=data)
        print(response.json())

    def borrar_alumno(self):
        alumno_id = 4  # Reemplazar con el ID real del alumno
        response = requests.delete(f"http://localhost:5000/borrado_ingreso/{alumno_id}")
        print(response.json())

    def ver_registro(self):
        response = requests.get("http://localhost:5000/solicitudes_registro")
        alumnos = response.json()["alumnos"]
        for alumno in alumnos:
            print(alumno)

    def ver_grimorios(self):
        response = requests.get("http://localhost:5000/asignaciones_grimorios")
        asignaciones = response.json()["asignaciones"]
        for asignacion in asignaciones:
            print(asignacion)

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()

