#######################################Récupération du fichier de données de meteo France à partir d'un fichier csv en remote##############################
import requests

def get_meteofrance():

        csvUrl="https://donneespubliques.meteofrance.fr/donnees_libres/Txt/Synop/synop.2020091112.csv"

        csvResponse=requests.get(csvUrl)

        #Enregistrement des données dans un fichier au format csv
        csvFilename = "/home/fitec/projet_fil_rouge/source_des_données/data/meteofrance.csv"

        #écriture en binaire
        with open(csvFilename,"wb") as file:
                file.write(csvResponse.content)

