########################################### Récupération du fichier de données des consommation d'electricité à partir de l'api ###############################

import requests

def get_enedis():

        # par régions 10 lignes
        apiUrl="https://data.enedis.fr/api/records/1.0/search/?dataset=conso-inf36&q=horodate%3A%5B2018-12-31T23%3A00%3A00Z+TO+2019-12-31T22%3A59%3A59Z%5D&rows=10&facet=horodate&facet=profil&facet=plage_de_puissance_souscrite&facet=jour_max_du_mois_0_1&facet=semaine_max_du_mois_0_1"

        
        # par régions
        #apiUrl="https://data.enedis.fr/api/records/1.0/search/?dataset=conso-inf36&q=horodate%3A%5B2018-12-31T23%3A00%3A00Z+TO+2019-12-31T22%3A59%3A59Z%5D&facet=horodate&facet=profil&facet=plage_de_puissance_souscrite&facet=jour_max_du_mois_0_1&facet=semaine_max_du_mois_0_1"

   
        jsonResponse = requests.get(apiUrl)

        #Enregistrement des données dans un fichier au format json
        jsonFilename = "/home/fitec/projet_fil_rouge/source_des_données/data/consommation_elec_regions_2019_l10.json"
        #jsonFilename = "/home/fitec/projet_fil_rouge/source_des_données/data/consommation_elec_regions_2019.json"

        #écriture en binaire
        with open(jsonFilename,"wb") as file:
                file.write(jsonResponse.content)





