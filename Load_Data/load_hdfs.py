######################### Exporter le fichier de données json de enedis sur hdfs. #################################""
from hdfs import InsecureClient

def load_enedis():

    client = InsecureClient('http://localhost:50070', user='cloudera')
    client.makedirs('data')
    print(client.list('/user/cloudera'))

    #client.write('/user/cloudera/data','/home/fitec/projet_fil_rouge/source_des_données/data/consommation_elec_2019.json', overwrite=True)
    client.upload('/user/cloudera/data', '/home/fitec/projet_fil_rouge/source_des_données/data/consommation_elec_2019.json',overwrite=True)

