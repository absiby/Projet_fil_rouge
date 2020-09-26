import os

print("1 - Démarrage de Cassendra")
os.system("sudo docker run --name fitec-cassandra -v /home/fitec/FITEC/Cassandra:/var/lib/cassandra -p 9042:9042 -d --rm cassandra")
os.system("echo Fin Démarrage de Cassendra")

print("2 - Démarrage de HDFS")

#os.system("sudo docker run --hostname=quickstart.cloudera --privileged=true -t -i -v /home/fitec/FITEC/hadoop/cloudera:/src --publish-all=true -p 8888:8888 -p 90:90 -p 7180:7180 -p 50070:50070 -p 10002:10002 cloudera/quickstart /usr/bin/docker-quickstart")
os.system("sudo docker run --hostname=quickstart.cloudera --privileged=true -t -d --rm -v /home/fitec/FITEC/hadoop/cloudera:/src --publish-all=true -p 8888:8888 -p 90:90 -p 7180:7180 -p 50070:50070 -p 10002:10002 cloudera/quickstart /usr/bin/docker-quickstart")
os.system("echo Fin Démarrage de HDFS")


