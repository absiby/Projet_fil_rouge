######################### Demarrer hdfs. #################################""

#docker run --hostname=quickstart.cloudera --privileged=true -t -i -v /home/fitec/FITEC/hadoop/cloudera:/src --publish-all=true -p 8888:8888 -p 90:90 -p 7180:7180 -p 50070:50070 -p 10002:10002 cloudera/quickstart /usr/bin/docker-quickstart



#########################Exporter le fichier de données json de enedis sur hdfs.#################################""
from hdfs import InsecureClient

client = InsecureClient('http://localhost:50070', user='cloudera')
client.makedirs('data')
print(client.list('/user/cloudera'))

#client.write('/home/fitec/projet_fil_rouge/source_des_données/data/consommation_elec.json', '/user/cloudera/data')
client.upload('/user/cloudera/data', '/home/fitec/projet_fil_rouge/source_des_données/data/consommation_elec.json')

