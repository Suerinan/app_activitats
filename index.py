from config import configs
from src import init__app

configuration = configs['development']
app = init__app(configuration)

if __name__ == '__main__':
    app.run()
