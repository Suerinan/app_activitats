# Instal·lació API App_activitats
## Importar BDD
Descarregar l'arxiu 'app_activitats_creacio.sql' del repositori i importar-ho a MySql

## Importar projecte
Desde el repositori, esxollir el metode d'importació al botó 'Code'
Instal·lar vitualenv, posibles errors:
  - .\env\Scripts\activate : No se puede cargar el archivo  | https://www.alexmedina.net/habilitar-la-ejecucion-de-scripts-para-powershell/#:~:text=Para%20cambiar%20esta%20configuraci%C3%B3n%20basta%20con%20ejecutar%20%C2%ABSet-ExecutionPolicy,ejecutar%20%C2%ABGet-ExecutionPolicy%C2%BB%20ver%C3%A1s%20que%20ya%20aparece%20como%20%C2%ABUnrestricted%C2%BB.
  - virtualenv no se detecta como comando interno | cerca l'arxiu 'virtualenv.exe' en el ccercador de windows, obre la ruta, copiala i afegeix-la al path
Una vegada instal·lat correctament, obre un terminal (NO EL TANQUIS) i executa: 'virtualenv -p python3 env' o python si no tens python3
Una vegada creat l'entorn virtual, actival amb la comanda '.\env\Scripts\activate'
Ara si, una vegada activat, executa 'pip freeze > requirements.txt' per a instal·lar en el entorn totes les dependencies del projecte
Per engegar l'app, executa al terminal que NO HAS TANCAT, 'python .\index.py', si l'has tancat, torna al pas d'activar l'entorn virtual

## Importar comandes postman
A postman, importar l'arxiu 'APP_ACTIVITATS.postman_collection.json', hi tindràs separat per apartat, totes les funcions de l'API
