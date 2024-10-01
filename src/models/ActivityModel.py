from decouple import config

class Activity:
    
    def __init__(self, name, description=None, capacity=None):
        self.activity_name = name
        self.activity_description = description
        self.activity_maximum_capacity = capacity

    def to_json(self):
        return {
            'nom': self.activity_name,
            'descripció': self.activity_description,
            'capacitat_màxima': self.activity_maximum_capacity
        }
    
    def get_activity_insert(self):
        return f"INSERT INTO {config('TABLE_ACTIVITIES')} ({config('ACTIVITY_NAME')},{config('ACTIVITY_DESCRIPTION')}, \
        {config('ACTIVITY_MAXIMUM_CAPACITY')})  VALUES('{self.activity_name}','{self.activity_description}',{self.activity_maximum_capacity});"
    
    def get_activity_select(self):
        return f"SELECT * FROM {config('TABLE_ACTIVITIES')} WHERE {config('ACTIVITY_NAME')}='{self.activity_name}';"