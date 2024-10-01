from src.models.UserModel import User
from src.database.db_mysql import get_connection
import pymysql

class UserService:
    @classmethod
    def register_user(self, user: User):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute(user.get_user_insert())
                connection.commit()
                return 0
        except pymysql.err.IntegrityError as e:
            if e.args[0] == 1062:
                return {"status": "error", "message": "Error: DNI duplicat, l'usuari ja existeix."}
            else:
                return {"status": "error", "message": f"Error d'integritat: {str(e)}"}
        except Exception as ex:
            print(f"Error: {ex}")
            return {"status": "error", "message": "S'ha produït un error en registrar l'usuari."}

        finally:
            if connection:
                connection.close()
    
    @classmethod
    def update_user(self, user: User):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute(user.get_user_update())
                connection.commit()
                if cursor.rowcount > 0:
                    return 0
                else:
                    return {"status": "error", "message": "Error: L'usuari no existeix o no hi ha hagut modificacions"}

        except pymysql.err.IntegrityError as e:
            if e.args[0] == 1062:
                return {"status": "error", "message": "Error: L'usuari no existeix"}
            else:
                return {"status": "error", "message": f"Error d'integritat: {str(e)}"}

        except Exception as ex:
            print(f"Error: {ex}")
            return {"status": "error", "message": "S'ha produït un error en actualitzar l'usuari."}

        finally:
            if connection:
                connection.close()

    @classmethod
    def select_user(self, user: User):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute(user.get_user_select())
                result = cursor.fetchone()
                
                if result:
                    user_info = {
                        'dni': result[0],
                        'nom': result[1],
                        'cognoms': result[2],
                        'edat': result[3],
                        'contrasenya': result[4]
                    }
                    return {"status": "success", "data": user_info}

                else:
                    return {"status": "error", "message": "Error: L'usuari no existeix"}

        except pymysql.err.IntegrityError as e:
            if e.args[0] == 1062:
                return {"status": "error", "message": "Error: L'usuari no existeix"}
            else:
                return {"status": "error", "message": f"Error d'integritat: {str(e)}"}

        except Exception as ex:
            print(f"Error: {ex}")
            return {"status": "error", "message": "S'ha produït un error en consultar l'usuari."}

        finally:
            if connection:
                connection.close()
    
    @classmethod
    def delete_user(self, user: User):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute(user.get_user_delete())
                connection.commit()

                if cursor.rowcount > 0:
                    return {"status": "success", "message": "Usuari eliminat correctament."}
                else:
                    return {"status": "error", "message": "Error: L'usuari no existeix."}

        except pymysql.err.IntegrityError as e:
            if e.args[0] == 1062:
                return {"status": "error", "message": "Error: L'usuari no existeix."}
            else:
                return {"status": "error", "message": f"Error d'integritat: {str(e)}"}

        except Exception as ex:
            print(f"Error: {ex}")
            return {"status": "error", "message": "S'ha produït un error en eliminar l'usuari."}

        finally:
            if connection:
                connection.close()
