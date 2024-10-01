from src.models.UserActivityModel import UserActivity
from src.database.db_mysql import get_connection
import pymysql

class UserActivityService:
    @classmethod
    def register_user(self,user: UserActivity):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute(user.get_user_activity_register_insert())
                connection.commit()
                return 0
        except pymysql.err.IntegrityError as e:
            if e.args[0] == 1062:
                return {"status": "error", "message": "Error: L'usuari ja esta apuntat a l'activitat."}
            else:
                return {"status": "error", "message": f"Error d'integritat: {str(e)}"}
        except Exception as ex:
            print(f"Error: {ex}")
            return {"status": "error", "message": "S'ha produït un error en apuntar l'usuaria l'activitat."}

        finally:
            if connection:
                connection.close()