# asin_take_home_challenge

## Version française
Ce programme est sensé remplir une base de données à partir d'un fichier excel.
La base de données utilisée dans ce programme est postgresql. Pour exécuter le programme,
il faut:
- Installer et configurer postgresql sur machine.
- Renseigner les informations dans un fichier `.env` a créer dans le même répertoire que le
fichier main. (Vous pouvez vous servir du fichier env_sample fourni dans ce répertoire)
- Installer les dépendances contenues dans le fichier `requirements.txt`:
    - `pip -r install requirements.txt`
Pour exécuter le programme, lancer la commande suivante:
- `python3 main.py chemin_vers_le_fichier_excel`

## English version
This program is designed to populate a database from an Excel file.  
The database used in this program is PostgreSQL. To run the program, follow these steps:  

- Install and configure PostgreSQL on your machine.  
- Provide the connection details in a `.env` file, which should be created in the same directory as the `main` file. (You can use the `env_sample` file provided in this directory as a reference.)  
- Install the dependencies listed in the `requirements.txt` file:  
  - `pip install -r requirements.txt`  

To execute the program, run the following command:  
- `python3 main.py path_to_excel_file`
