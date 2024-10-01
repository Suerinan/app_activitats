from decouple import config

class UserActivity:
    
    def __init__(self, dni, name):
        self.user_dni = dni
        self.activity_name = name

    def to_json(self):
        return {
            'dni': self.user_dni,
            'nom_activitat': self.activity_name,
        }
    
    def get_user_activity_register_insert(self):
        return f"INSERT INTO {config('TABLE_USER_ACTIVITY')} ({config('USER_DNI')},{config('ACTIVITY_NAME')}) VALUES('{self.user_dni}','{self.activity_name}');"