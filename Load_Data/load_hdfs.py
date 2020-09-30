######################### Exporter le fichier de données json de enedis sur hdfs. #################################""
from hdfs import InsecureClient

def load_enedis():

    client = InsecureClient('http://localhost:50070', user='cloudera')
    client.makedirs('data')
    print(client.list('/user/cloudera'))

    # load 10 lignes
    client.upload('/user/cloudera/data', '/home/fitec/projet_fil_rouge/source_des_données/data/consommation_elec_regions_2019_l10.json',overwrite=True)
    
    # load total
    #client.upload('/user/cloudera/data', '/home/fitec/projet_fil_rouge/source_des_données/data/consommation_elec_regions_2019.json',overwrite=True)


