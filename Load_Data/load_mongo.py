import json 
from pymongo import MongoClient 


def load_mongoDB(client_mongo, nom_database, nom_collection, jsonFilename):

    # Making Connection 
    myclient = MongoClient(client_mongo) 
    # database 
    db = myclient[nom_database] 
    # Created or Switched to collection 
    Collection = db[nom_collection] 

    # Loading or Opening the json file 
    with open(jsonFilename) as file: 
        file_regions = json.load(file) 
        
    # Inserting the loaded data in the Collection 
    # if JSON contains data more than one entry 
    # insert_many is used else inser_one is used 
    if isinstance(file_regions, list): 
        Collection.insert_many(file_regions) 
    else: 
        Collection.insert_one(file_regions) 

def load_tables_technique_mongo():

    client_mongo = "mongodb://localhost:27017/"
    nom_database = "meteofrancedb"

    nom_collection = "regions"
    lien_fichier = "/home/fitec/projet_fil_rouge/source_des_données/data/regions.json"

    print("Table de correspondance : départements - régions")
    load_mongoDB(client_mongo, nom_database, nom_collection, lien_fichier)

    nom_collection = "position_stations"
    lien_fichier = "/home/fitec/projet_fil_rouge/source_des_données/data/postesSynop.json"

    print("Table des positions gps des stations meteo")
    load_mongoDB(client_mongo, nom_database, nom_collection, lien_fichier)

    print("Chargement des données OK")