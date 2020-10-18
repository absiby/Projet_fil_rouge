#######################################Récupération du fichier de données de meteo France à partir d'un fichier csv en remote##############################
import requests

def get_meteofrance():
        
        # par régions - CSV
        csvUrl="https://public.opendatasoft.com/explore/dataset/donnees-synop-essentielles-omm/download/?format=csv&q=date:%5B2018-12-30T23:00:00Z+TO+2019-12-31T22:59:59Z%5D&timezone=Europe/Berlin&lang=fr&use_labels_for_header=true&csv_separator=%3B"
        csvResponse=requests.get(csvUrl)

        #Enregistrement des données dans un fichier au format csv
         csvFilename = "/home/fitec/projet_fil_rouge/source_des_données/data/donnees-meteofrance.csv"

        #écriture en binaire
        with open(csvFilename,"wb") as file:
                file.write(csvResponse.content)

