########################################### Récupération du fichier de données des consommation d'electricité à partir de l'api ###############################

import requests

def data_enedis():
        apiUrl='''https://data.enedis.fr/api/records/1.0/search/?dataset=consommation-electrique-par-secteur-dactivite-commune&q=&facet=annee
        &facet=code_commune&facet=nom_commune&facet=code_epci&facet=nom_epci&facet=code_departement&facet=nom_departement
        &facet=code_region&facet=nom_region&facet=code_categorie_consommation&facet=code_grand_secteur&facet=code_secteur_naf2&refine.annee=2019'''

        jsonResponse = requests.get(apiUrl)

        #Enregistrement des données dans un fichier au format json
        jsonFilename = "/home/fitec/projet_fil_rouge/source_des_données/data/consommation_elec.json"

        #écriture en binaire
        with open(jsonFilename,"wb") as file:
                file.write(jsonResponse.content)
        




