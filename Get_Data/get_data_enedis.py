########################################### Récupération du fichier de données des consommation d'electricité à partir de l'api ###############################

import requests

def get_enedis():

        # France entiere
        apiUrl="https://data.enedis.fr/explore/dataset/conso-inf36/download/?format=json&disjunctive.profil=true&disjunctive.plage_de_puissance_souscrite=true&refine.horodate=2019&timezone=Europe/Berlin&lang=fr"

        # par régions
        apiUrl="https://data.enedis.fr/explore/dataset/conso-inf36-region/download/?format=csv&refine.horodate=2019&timezone=Europe/Berlin&lang=fr&use_labels_for_header=true&csv_separator=%3B"

        #apiUrl="https://data.enedis.fr/api/records/1.0/search/?dataset=conso-inf36&q=&sort=horodate&facet=horodate&facet=profil&facet=plage_de_puissance_souscrite&facet=jour_max_du_mois_0_1&facet=semaine_max_du_mois_0_1&refine.horodate=2019"

        #apiUrl='''https://data.enedis.fr/api/records/1.0/search/?dataset=consommation-electrique-par-secteur-dactivite-commune&q=&facet=annee
        #&facet=code_commune&facet=nom_commune&facet=code_epci&facet=nom_epci&facet=code_departement&facet=nom_departement
        #&facet=code_region&facet=nom_region&facet=code_categorie_consommation&facet=code_grand_secteur&facet=code_secteur_naf2&refine.annee=2019'''

        jsonResponse = requests.get(apiUrl)

        #Enregistrement des données dans un fichier au format json
        #jsonFilename = "/home/fitec/projet_fil_rouge/source_des_données/data/consommation_elec_2019.json"
        jsonFilename = "/home/fitec/projet_fil_rouge/source_des_données/data/consommation_elec_regions_2019.json"

        #écriture en binaire
        with open(jsonFilename,"wb") as file:
                file.write(jsonResponse.content)





