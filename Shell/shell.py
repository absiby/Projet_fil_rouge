import os

# créer les répertoires nécessaire 
os.system("mkdir -p /home/fitec/projet_fil_rouge/source_des_données/data")
os.system("chmod 777 /home/fitec/projet_fil_rouge/source_des_données/data")

os.system("mkdir -p /home/fitec/projet_fil_rouge/ML_resultats")
os.system("chmod 777 /home/fitec/projet_fil_rouge/ML_resultats")


print("1 - Démarrage de Cassendra")
os.system("sudo docker run --name fitec-cassandra -v /home/fitec/FITEC/Cassandra:/var/lib/cassandra -p 9042:9042 -d --rm cassandra")
print("2 - Fin Démarrage de Cassendra")

print("1 - Démarrage de MongoDB")
os.system("systemctl start mongodb")
print("2 - Fin Démarrage de MongoDB")



