from decouple import config

class User:
    
    def __init__(self, dni, name=None, surname=None, age=None, password=None):
        self.user_dni = dni
        self.user_name = name
        self.user_surname = surname
        self.user_age = age
        self.user_password = password

    def to_json(self):
        return {
            'dni': self.user_dni,
            'nom': self.user_name,
            'cognoms': self.user_surname,
            'edat': self.user_age,
            'contrasenya': self.user_password
        }
    
    def get_user_insert(self):
        return f"INSERT INTO {config('TABLE_USERS')} ({config('USER_DNI')},{config('USER_NAME')},{config('USER_SURNAME')},{config('USER_AGE')},{config('USER_PASSWORD')})  VALUES('{self.user_dni}','{self.user_name}','{self.user_surname}',{self.user_age},'{self.user_password}');"
    
    def get_user_update(self):
        return f"UPDATE {config('TABLE_USERS')} SET {config('USER_NAME')}='{self.user_name}', {config('USER_SURNAME')}='{self.user_surname}', {config('USER_AGE')}={self.user_age}, {config('USER_PASSWORD')}='{self.user_password}' WHERE {config('USER_DNI')}='{self.user_dni}';"
    
    def get_user_select(self):
        return f"SELECT * FROM {config('TABLE_USERS')} WHERE {config('USER_DNI')}='{self.user_dni}';"
    
    def get_user_delete(self):
        return f"DELETE FROM {config('TABLE_USERS')} WHERE {config('USER_DNI')}='{self.user_dni}';"
