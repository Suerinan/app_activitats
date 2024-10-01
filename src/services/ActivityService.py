from src.models.ActivityModel import Activity
from src.database.db_mysql import get_connection
import pymysql

class ActivityService:
    @classmethod
    def create_activity(self, activity: Activity):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute(activity.get_activity_insert())
                connection.commit()
                return 0
        except pymysql.err.IntegrityError as e:
            if e.args[0] == 1062:
                return {"status": "error", "message": "Error: Nom duplicat, l'activitat ja existeix."}
            else:
                return {"status": "error", "message": f"Error d'integritat: {str(e)}"}
        except Exception as ex:
            print(f"Error: {ex}")
            return {"status": "error", "message": "S'ha produït un error en crear l'activitat."}

        finally:
            if connection:
                connection.close()

    @classmethod
    def select_activity(self, activity: Activity):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute(activity.get_activity_select())
                result = cursor.fetchone()
                
                if result:
                    activity_info = {
                        'nom': result[0],
                        'descripció': result[1],
                        'capacitat_màxima': result[2]
                    }
                    return {"status": "success", "data": activity_info}

                else:
                    return {"status": "error", "message": "Error: L'activitat no existeix"}

        except pymysql.err.IntegrityError as e:
            if e.args[0] == 1062:
                return {"status": "error", "message": "Error: L'activitat no existeix"}
            else:
                return {"status": "error", "message": f"Error d'integritat: {str(e)}"}

        except Exception as ex:
            print(f"Error: {ex}")
            return {"status": "error", "message": "S'ha produït un error en consultar l'activitat."}

        finally:
            if connection:
                connection.close()