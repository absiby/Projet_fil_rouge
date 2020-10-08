#######################################Récupération du fichier de données de meteo France à partir d'un fichier csv en remote##############################
import requests

def get_meteofrance():

        # par régions 10 lignes - JSON puis CSV
        # JSON
        #csvUrl="https://public.opendatasoft.com/api/records/1.0/search/?dataset=donnees-synop-essentielles-omm&q=date%3A%5B2017-12-30T23%3A00%3A00Z+TO+2018-12-31T22%3A59%3A59Z%5D&rows=10&sort=date&facet=date&facet=nom&facet=temps_present&facet=libgeo&facet=nom_epci&facet=nom_dept&facet=nom_reg"
        
        # par régions - CSV puis JSON
        # CSV
        csvUrl="https://public.opendatasoft.com/explore/dataset/donnees-synop-essentielles-omm/download/?format=csv&q=date:%5B2017-12-30T23:00:00Z+TO+2018-12-31T22:59:59Z%5D&timezone=Europe/Berlin&lang=fr&use_labels_for_header=true&csv_separator=%3B"
        # JSON
        #csvUrl="https://public.opendatasoft.com/api/records/1.0/search/?dataset=donnees-synop-essentielles-omm&q=date%3A%5B2017-12-30T23%3A00%3A00Z+TO+2018-12-31T22%3A59%3A59Z%5D&sort=date&facet=date&facet=nom&facet=temps_present&facet=libgeo&facet=nom_epci&facet=nom_dept&facet=nom_reg" 

        csvResponse=requests.get(csvUrl)

        #Enregistrement des données dans un fichier au format csv
        csvFilename = "/home/fitec/projet_fil_rouge/source_des_données/data/donnees-meteofrance_l10.csv"
        #csvFilename = "/home/fitec/projet_fil_rouge/source_des_données/data/donnees-meteofrance.csv"

        #écriture en binaire
        with open(csvFilename,"wb") as file:
                file.write(csvResponse.content)

