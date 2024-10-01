from mysql.connector import Error
import mysql.connector

Constants = {
    "DB_HOST": "localhost",
    "DB_PORT": 3306,
    "DB_USER": "root",
    "DB_USER_PASSWORD": "root",
    "DB_NAME": "app_activitats",
    "TABLA_USUARI": "usuaris",
    "DNI_USUARI": "dni_usuari",
    "NOM_USUARI": "nom_usuari",
    "COGNOMS_USUARI": "cognoms_usuari",
    "EDAT_USUARI": "edad_usuari",
    "CONTRASENYA_USUARI": "contrasenya_usuari",
    "TABLA_ACTIVITATS": "activitats",
    "NOM_ACTIVITAT": "nom_activitat",
    "DESCRIPCIO_ACTIVITAT": "descripcio",
    "CAPACITAT_MAXIMA_ACTIVITAT": "capacitat_maxima",
    "TABLA_USUARI_ACTIVITAT": "usuari_activitat"
}

def connectar_afectar_db_usuaris(query):
    try:
        connection = mysql.connector.connect(
            host=Constants['DB_HOST'],
            port=Constants['DB_PORT'],
            user=Constants['DB_USER'],
            password=Constants['DB_USER_PASSWORD'],
            db=Constants['DB_NAME']
        )
        
        cursor = connection.cursor()
        cursor.execute(query)
        
        if cursor.rowcount == 1:
            connection.commit()
            return 0
        else:
            connection.rollback()
            return 1, "No se afectó ninguna fila."

    except Error as er:
        return 1, f"Error al ejecutar la consulta: {er}"

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("Conexio tancada.")

def connectar_consultar_db_usuaris(query):
    try:
        connection = mysql.connector.connect(
            host=Constants['DB_HOST'],
            port=Constants['DB_PORT'],
            user=Constants['DB_USER'],
            password=Constants['DB_USER_PASSWORD'],
            db=Constants['DB_NAME']
        )
        
        cursor = connection.cursor()
        cursor.execute(query)

        resultados = cursor.fetchall()
        if resultados:
            connection.commit()
            return resultados
        else:
            return [], "No se encontraron filas."

    except Error as er:
        return 1, f"Error al ejecutar la consulta: {er}"

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("Conexio tancada.")

def registrar_usuari(dni, nom, cognoms, edat, contrasenya):
    query = f"INSERT INTO {Constants['TABLA_USUARI']} ({Constants['DNI_USUARI']}, {Constants['NOM_USUARI']}, {Constants['COGNOMS_USUARI']}, {Constants['EDAT_USUARI']}, {Constants['CONTRASENYA_USUARI']}) VALUES ('{dni}', '{nom}', '{cognoms}', {edat}, '{contrasenya}');"
    return connectar_afectar_db_usuaris(query)

def actualitzar_usuari(dni, nom, cognoms, edat, contrasenya):
    query = f"UPDATE {Constants['TABLA_USUARI']} SET {Constants['NOM_USUARI']} = '{nom}', {Constants['COGNOMS_USUARI']} = '{cognoms}', {Constants['EDAT_USUARI']} = {edat}, {Constants['CONTRASENYA_USUARI']} = '{contrasenya}' WHERE {Constants['DNI_USUARI']} = '{dni}';"
    return connectar_afectar_db_usuaris(query)

def consultar_usuari(dni):
    if dni == "all":
        query = f"SELECT * FROM {Constants['TABLA_USUARI']};"
    else:
        query = f"SELECT * FROM {Constants['TABLA_USUARI']} WHERE {Constants['DNI_USUARI']} = '{dni}';"
    return connectar_consultar_db_usuaris(query)

def eliminar_usuari(dni):
    query = f"DELETE FROM {Constants['TABLA_USUARI']} WHERE {Constants['DNI_USUARI']} = '{dni}';"
    return connectar_afectar_db_usuaris(query)

def crear_activitat(nom, descripcio, data_activitat):
    query = f"INSERT INTO {Constants['TABLA_ACTIVITATS']} ({Constants['NOM_ACTIVITAT']}, {Constants['DESCRIPCIO_ACTIVITAT']}, {Constants['da']}, {Constants['EDAT_USUARI']}, {Constants['CONTRASENYA_USUARI']}) VALUES ('{dni}', '{nom}', '{cognoms}', {edat}, '{contrasenya}');"
    return connectar_afectar_db_usuaris(query)

def apuntar_usuari_a_activitat(dni, nom):
    query = f"INSERT INTO {Constants['TABLA_USUARI_ACTIVITAT']} ({Constants['DNI_USUARI']}, {Constants['NOM_ACTIVITAT']}) VALUES ('{dni}', '{nom}');"
    return connectar_afectar_db_usuaris(query)

def consultar_activitats():
    query = f"SELECT * FROM {Constants['TABLA_ACTIVITATS']};"
    return connectar_consultar_db_usuaris(query)

def eliminar_activitat(nom):
    query = f"DELETE FROM {Constants['TABLA_ACTIVITATS']} WHERE {Constants['NOM_ACTIVITAT']} = '{nom}';"
    return connectar_afectar_db_usuaris(query)
