from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from database import db_operator

app = Flask(__name__)
app.secret_key = 'clave_secreta_para_flash'

usuarios = {}
actividades = {}

@app.route('/')
def index():
    return render_template('index.html')

@app.errorhandler(404)
def not_found_error(error):
    return jsonify({'message': 'Recurso no encontrado'}), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({'message': 'Error interno del servidor'}), 500

@app.route('/appActivitats/user', methods=["POST"])
def registrar_usuari():
    try:
        data = request.get_json()
        dni = data.get('dni')
        nom = data.get('nom')
        cognoms = data.get('cognoms')
        edat = data.get('edat')
        contrasenya = data.get('contrasenya')

        operacio = db_operator.registrar_usuari(dni, nom, cognoms, edat, contrasenya)
        if operacio == 0:
            return jsonify({'message': 'Usuari registrat amb éxit'}), 201
        else:
            raise ValueError(f"Error: {operacio}")
    except Exception as e:
        return jsonify({'message': 'Error al registrar usuari', 'error': str(e)}), 500

@app.route('/appActivitats/user/<string:dni>', methods=["PUT"])
def actualitzar_usuari(dni):
    try:
        data = request.get_json()
        nom = data.get('nom')
        cognoms = data.get('cognoms')
        edat = data.get('edat')
        contrasenya = data.get('contrasenya')

        operacio = db_operator.actualitzar_usuari(dni, nom, cognoms, edat, contrasenya)
        if operacio == 0:
            return jsonify({'message': 'Usuari actualitzat amb éxit'}), 201
        else:
            raise ValueError(f"Error: {operacio}")
    except Exception as e:
        return jsonify({'message': 'Error al actualizar usuari', 'error': str(e)}), 500

@app.route('/appActivitats/user/<string:dni>', methods=["GET"])
def consultar_usuari(dni):
    try:
        operacio = db_operator.consultar_usuari(dni)
        print(operacio)
        retorn = ""
        if len(operacio) == 1:
            for user in operacio:
                for apartat in user:
                    retorn += str(apartat)+','
                retorn = retorn[:-1]
                retorn += '|'
            return jsonify({'message': 'Consultat amb exit', 'resultat': retorn[:-1]}), 201
        
        elif operacio[1] != 'No se encontraron filas.' and len(operacio) > 0:
            for user in operacio:
                for apartat in user:
                    retorn += str(apartat)+','
                retorn = retorn[:-1]
                retorn += '|'
            return jsonify({'message': 'Consultat amb exit', 'resultat': retorn[:-1]}), 201
        else:
            raise ValueError(f"Error: No s'han trobat usuaris")

    except Exception as e:
        return jsonify({'message': str(e), 'error': str(e)}), 500

@app.route('/appActivitats/user/<string:dni>', methods=["DELETE"])
def eliminar_usuari(dni):
    try:
        operacio = db_operator.eliminar_usuari(dni)
        if operacio == 0:
            return jsonify({'message': 'Usuari eliminat amb éxit'}), 201
        else:
            raise ValueError(f"Error: {operacio}")
    except Exception as e:
        return jsonify({'message': 'Error al eliminar usuari', 'error': str(e)}), 500

@app.route('/appActivitats/activitat', methods=["POST"])
def crear_activitat():
    try:
        data = request.get_json()
        nom = data.get('nomActivitat')
        descripcio = data.get('descripcioActivitat')
        data_activitat = data.get('dataActivitat')


        return jsonify({'message': 'Actividad creada con éxito'}), 201
    except Exception as e:
        return jsonify({'message': 'Error al crear actividad', 'error': str(e)}), 500

@app.route('/appActivitats/activitat/apuntar_usuari', methods=["POST"])
def apuntar_usuari_activitat():
    try:
        data = request.get_json()
        dni = data.get('dni')
        nom = data.get('nomActivitat')

        if not all([nom, dni]):
            return jsonify({'message': 'Faltan datos requeridos'}), 400

        return jsonify({'message': f'Usuari {dni} apuntat a {nom}'}), 201
    except Exception as e:
        return jsonify({'message': 'Error al crear actividad', 'error': str(e)}), 500

@app.route('/appActivitats/activitat', methods=["GET"])
def consultar_activitats():
    try:
        return jsonify({'message': 'Exito al consultar actividades'}), 200
    except Exception as e:
        return jsonify({'message': 'Error al consultar actividades', 'error': str(e)}), 500

@app.route('/appActivitats/activitat/<string:nombre>', methods=["DELETE"])
def eliminar_actividad(nombre):
    try:
        if nombre not in actividades:
            return jsonify({'message': 'Actividad no encontrada'}), 404

        del actividades[nombre]

        return jsonify({'message': 'Actividad eliminada con éxito'}), 200
    except Exception as e:
        return jsonify({'message': 'Error al eliminar actividad', 'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)