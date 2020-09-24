######################### Exporter le fichier de données json de enedis sur hdfs. #################################""
from hdfs import InsecureClient

client = InsecureClient('http://localhost:50070', user='cloudera')
client.makedirs('data')
print(client.list('/user/cloudera'))

client.write('/home/fitec/projet_fil_rouge/source_des_données/data/consommation_elec.json', '/user/cloudera/data')
#client.upload('/user/cloudera/data', '/home/fitec/projet_fil_rouge/source_des_données/data/consommation_elec.json')

