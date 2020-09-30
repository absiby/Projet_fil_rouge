import os

class Config(object):
	 DEBUG = False
	 TESTING = False

class ProductionConfig(Config):
    URL = "https://data.enedis.fr/api/records/1.0/search/?dataset=conso-inf36&q=horodate%3A%5B2018-12-31T23%3A00%3A00Z+TO+2019-12-31T22%3A59%3A59Z%5D&rows=10&facet=horodate&facet=profil&facet=plage_de_puissance_souscrite&facet=jour_max_du_mois_0_1&facet=semaine_max_du_mois_0_1"
    Filename = "/home/fitec/projet_fil_rouge/source_des_données/data/consommation_elec_regions_2019.json"

class DevelopmentConfig(Config):
	DEBUG = True
	URL = "https://data.enedis.fr/api/records/1.0/search/?dataset=conso-inf36&q=horodate%3A%5B2018-12-31T23%3A00%3A00Z+TO+2019-12-31T22%3A59%3A59Z%5D&rows=10&facet=horodate&facet=profil&facet=plage_de_puissance_souscrite&facet=jour_max_du_mois_0_1&facet=semaine_max_du_mois_0_1"
    Filename = "/home/fitec/projet_fil_rouge/source_des_données/data/consommation_elec_regions_2019.json"

class TestingConfig(Config):
	TESTING = True
	URL = "https://data.enedis.fr/api/records/1.0/search/?dataset=conso-inf36&q=horodate%3A%5B2018-12-31T23%3A00%3A00Z+TO+2019-12-31T22%3A59%3A59Z%5D&rows=10&facet=horodate&facet=profil&facet=plage_de_puissance_souscrite&facet=jour_max_du_mois_0_1&facet=semaine_max_du_mois_0_1"
    Filename = "/home/fitec/projet_fil_rouge/source_des_données/data/consommation_elec_regions_2019.json"




