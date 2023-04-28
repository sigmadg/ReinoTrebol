from flask import Flask, request
from flask_restful import Resource, Api
import mysql.connector
import random

app = Flask(__name__)
api = Api(app)

def conexion_bd():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="1234",
        database="EscuelaMagica"
    )

class SolicitudesIngreso(Resource):
    def post(self):
        data = request.get_json()

        nombre = data.get('nombre')
        apellido = data.get('apellido')
        identificacion = data.get('identificacion')
        edad = data.get('edad')

        if not (nombre and apellido and identificacion and edad):
            return {"message": "Todos los campos son obligatorios."}, 400

        if not (nombre.isalpha() and len(nombre) <= 20):
            return {"message": "El nombre debe tener solo letras y máximo 20 caracteres."}, 400

        if not (apellido.isalpha() and len(apellido) <= 20):
            return {"message": "El apellido debe tener solo letras y máximo 20 caracteres."}, 400

        if not (identificacion.isalnum() and len(identificacion) <= 10):
            return {"message": "La identificación debe tener números y letras, y máximo 10 caracteres."}, 400

        if not (str(edad).isdigit() and len(str(edad)) <= 2):
            return {"message": "La edad debe tener solo números y máximo 2 dígitos."}, 400

        afinidades = ['Magia de Acero', 'Magia de Agua', 'Magia de Aire', 'Magia de Alas', 'Magia de Algodón']
        grimorios = ['Sinceridad', 'Esperanza', 'Amor', 'Buena Fortuna', 'Desesperación']

        afinidad_magica = random.choice(afinidades)
        grimorio = random.choice(grimorios)

        try:
            conexion = conexion_bd()
            cursor = conexion.cursor()

            query = "INSERT INTO Alumnos (nombre, apellido, identificacion, edad, afinidad_magica, grimorio) VALUES (%s, %s, %s, %s, %s, %s)"
            cursor.execute(query, (nombre, apellido, identificacion, edad, afinidad_magica, grimorio))
            conexion.commit()

            return {"message": "Solicitud de ingreso creada exitosamente."}, 201

        except mysql.connector.Error as error:
            return {"message": f"Error al crear la solicitud de ingreso: {error}"}, 500

        finally:
            cursor.close()
            conexion.close()

class ActualizacionIngreso(Resource):
    def put(self, alumno_id):
        data = request.get_json()

        nombre = data.get('nombre')
        apellido = data.get('apellido')
        identificacion = data.get('identificacion')
        edad = data.get('edad')

        if not (nombre or apellido or identificacion or edad):
            return {"message": "Debe proporcionar al menos un campo para actualizar."}, 400

        campos = []
        valores = []

        if nombre:
            if nombre.isalpha() and len(nombre) <= 20:
                campos.append("nombre = %s")
                valores.append(nombre)
            else:
                return {"message": "El nombre debe tener solo letras y máximo 20 caracteres."}, 400

        if apellido:
            if apellido.isalpha() and len(apellido) <= 20:
                campos.append("apellido = %s")
                valores.append(apellido)
            else:
                return {"message": "El apellido debe tener solo letras y máximo 20 caracteres."}, 400

        if identificacion:
            if identificacion.isalnum() and len(identificacion) <= 10:
                campos.append("identificacion = %s")
                valores.append(identificacion)
            else:
                return {"message": "La identificación debe tener números y letras, y máximo 10 caracteres."}, 400

        if edad:
            if str(edad).isdigit() and len(str(edad)) <= 2:
                campos.append("edad = %s")
                valores.append(edad)
            else:
                return {"message": "La edad debe tener solo números y máximo 2 dígitos."}, 400

        try:
            conexion = conexion_bd()
            cursor = conexion.cursor()

            query = f"UPDATE Alumnos SET {', '.join(campos)} WHERE id = %s"
            valores.append(alumno_id)
            cursor.execute(query, tuple(valores))
            conexion.commit()

            if cursor.rowcount:
                return {"message": "Solicitud de ingreso actualizada exitosamente."}, 200
            else:
                return {"message": "No se encontró la solicitud de ingreso."}, 404

        except mysql.connector.Error as error:
            return {"message": f"Error al actualizar la solicitud de ingreso: {error}"}, 500

        finally:
            cursor.close()
            conexion.close()

class BorradoIngreso(Resource):
    def delete(self, alumno_id):
        try:
            conexion = conexion_bd()
            cursor = conexion.cursor()

            query = "DELETE FROM Alumnos WHERE id = %s"
            cursor.execute(query, (alumno_id,))
            conexion.commit()

            if cursor.rowcount:
                return {"message": "Solicitud de ingreso eliminada exitosamente."}, 200
            else:
                return {"message": "No se encontró la solicitud de ingreso."}, 404

        except mysql.connector.Error as error:
            return {"message": f"Error al eliminar la solicitud de ingreso: {error}"}, 500

        finally:
            cursor.close()
            conexion.close()


class SolicitudesRegistro(Resource):
    def get(self):
        try:
            conexion = conexion_bd()
            cursor = conexion.cursor()

            query = "SELECT * FROM Alumnos"
            cursor.execute(query)
            resultados = cursor.fetchall()

            alumnos = []
            for alumno in resultados:
                alumnos.append({
                    "id": alumno[0],
                    "nombre": alumno[1],
                    "apellido": alumno[2],
                    "identificacion": alumno[3],
                    "edad": alumno[4],
                    "afinidad_magica": alumno[5],
                    "grimorio": alumno[6]
                })

            return {"alumnos": alumnos}, 200

        except mysql.connector.Error as error:
            return {"message": f"Error al consultar las solicitudes de ingreso: {error}"}, 500

        finally:
            cursor.close()
            conexion.close()

class AsignacionesGrimorios(Resource):
    def get(self):
        try:
            conexion = conexion_bd()
            cursor = conexion.cursor()

            query = "SELECT id, afinidad_magica, grimorio FROM Alumnos"
            cursor.execute(query)
            resultados = cursor.fetchall()

            asignaciones = []
            for asignacion in resultados:
                asignaciones.append({
                    "id": asignacion[0],
                    "afinidad_magica": asignacion[1],
                    "grimorio": asignacion[2]
                })

            return {"asignaciones": asignaciones}, 200

        except mysql.connector.Error as error:
            return {"message": f"Error al consultar las asignaciones de grimorios: {error}"}, 500

        finally:
            cursor.close()
            conexion.close()

api.add_resource(ActualizacionIngreso, '/actualizacion_ingreso/<int:alumno_id>')
api.add_resource(BorradoIngreso, '/borrado_ingreso/<int:alumno_id>')
api.add_resource(SolicitudesIngreso, '/solicitudes_ingreso')
api.add_resource(SolicitudesRegistro, '/solicitudes_registro')
api.add_resource(AsignacionesGrimorios, '/asignaciones_grimorios')

if __name__ == '__main__':
    app.run(debug=True)




