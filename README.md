# Projet_fil_rouge
#Consommation electrique

Avant de lancer le main.py il faut démarrer les bases de données Cassandra et mongoDB avec le shell.py

La partie machine learning utilisera spark. 
spark-submit devra être lancé à partir du répertoire suivant :
"/home/fitec/spark/spark-3.0.0-bin-hadoop2.7/bin/spark-submit"


Liste des liens à utiliser

# -----------------------------------------------------------
#          enedis
# -----------------------------------------------------------

# dataset=conso-sup36-region pour 2019 - all

"https://data.enedis.fr/api/records/1.0/download/?dataset=conso-inf36-region
&q=horodate%3A%5B2018-12-30T23%3A00%3A00Z+TO+2019-12-31T22%3A59%3A59Z%5D
&rows=150000
&facet=horodate
&facet=region&facet=profil
&facet=plage_de_puissance_souscrite
&facet=indice_representativite_courbe_ndeg1
&facet=indice_representativite_courbe_ndeg2
&facet=indice_representativite_courbe_ndeg1_ndeg2
&facet=jour_max_du_mois_0_1
&facet=semaine_max_du_mois_0_1
&format=json"


# -----------------------------------------------------------
#          meteo france
# -----------------------------------------------------------

# meteo france pour 2019
csvUrl="https://public.opendatasoft.com/explore/dataset/donnees-synop-essentielles-omm/download/?format=csv
&q=date:%5B2018-12-30T23:00:00Z+TO+2019-12-31T22:59:59Z%5D
&timezone=Europe/Berlin
&lang=fr&use_labels_for_header=true
&csv_separator=%3B"
       

