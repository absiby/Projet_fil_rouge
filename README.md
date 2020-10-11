# Projet_fil_rouge
#Consommation electrique

Avant de lancer le main.py il faut démarrer les bases de données Cassandra et HDFS avec le shell.py


Liste des liens à utiliser

# -----------------------------------------------------------
#          enedis
# -----------------------------------------------------------

# dataset=conso-sup36-region pour 2019 - all

https://data.enedis.fr/api/records/1.0/search/?dataset=conso-sup36-region
&q=horodate%3A%5B2018-12-30T23%3A00%3A00Z+TO+2019-12-31T22%3A59%3A59Z%5D
&facet=horodate
&facet=region
&facet=profil
&facet=plage_de_puissance_souscrite
&facet=secteur_activite&facet=indice_representativite_courbe_ndeg1
&facet=indice_representativite_courbe_ndeg2
&facet=indice_representativite_courbe_ndeg1_ndeg2
&facet=jour_max_du_mois_0_1
&facet=semaine_max_du_mois_0_1

https://data.enedis.fr/api/records/1.0/search/?dataset=conso-sup36region&q=horodate%3A%5B2018-12-30T23%3A00%3A00Z+TO+2019-12-31T22%3A59%3A59Z%5D&facet=horodate&facet=region&facet=profil&facet=plage_de_puissance_souscrite&facet=secteur_activite&facet=indice_representativite_courbe_ndeg1&facet=indice_representativite_courbe_ndeg2&facet=indice_representativite_courbe_ndeg1_ndeg2&facet=jour_max_du_mois_0_1&facet=semaine_max_du_mois_0_1


# dataset=conso-sup36-region pour 2019 - 10 lignes

https://data.enedis.fr/api/records/1.0/search/?dataset=conso-sup36-region
&q=horodate%3A%5B2018-12-30T23%3A00%3A00Z+TO+2019-12-31T22%3A59%3A59Z%5D
&rows=10
&facet=horodate
&facet=region
&facet=profil
&facet=plage_de_puissance_souscrite
&facet=secteur_activite&facet=indice_representativite_courbe_ndeg1
&facet=indice_representativite_courbe_ndeg2
&facet=indice_representativite_courbe_ndeg1_ndeg2
&facet=jour_max_du_mois_0_1
&facet=semaine_max_du_mois_0_1

https://data.enedis.fr/api/records/1.0/search/?dataset=conso-sup36-region&q=horodate%3A%5B2018-12-30T23%3A00%3A00Z+TO+2019-12-31T22%3A59%3A59Z%5D&rows=10&facet=horodate&facet=region&facet=profil&facet=plage_de_puissance_souscrite&facet=secteur_activite&facet=indice_representativite_courbe_ndeg1&facet=indice_representativite_courbe_ndeg2&facet=indice_representativite_courbe_ndeg1_ndeg2&facet=jour_max_du_mois_0_1&facet=semaine_max_du_mois_0_1

# -----------------------------------------------------------
#          meteo france
# -----------------------------------------------------------

# meteo france pour 2019
https://public.opendatasoft.com/api/records/1.0/search/?dataset=donnees-synop-essentielles-omm
&q=date%3A%5B2018-12-30T23%3A00%3A00Z+TO+2019-12-31T22%3A59%3A59Z%5D
&sort=date
&facet=date
&facet=nom
&facet=temps_present
&facet=libgeo
&facet=nom_epci
&facet=nom_dept
&facet=nom_reg


# meteo france pour 2019 - 10 lignes
https://public.opendatasoft.com/api/records/1.0/search/?dataset=donnees-synop-essentielles-omm
&q=date%3A%5B2018-12-30T23%3A00%3A00Z+TO+2019-12-31T22%3A59%3A59Z%5D
&rows=10
&sort=date
&facet=date
&facet=nom
&facet=temps_present
&facet=libgeo
&facet=nom_epci
&facet=nom_dept
&facet=nom_reg


