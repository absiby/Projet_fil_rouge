import os

# Démarrer les bases de données
os.system("python3 Shell/shell.py")

# Télécharger les données sur le web
os.system("python3 Get_Data/get_data_enedis.py")
os.system("python3 Get_Data/get_data_meteofrance.py")

# Charger les données dans HDFS et Cassandra
os.system("python3 Load_Data/load_cassandra.py")
os.system("python3 Load_Data/load_hdfs.py")


