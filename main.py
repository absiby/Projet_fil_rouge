import os

print("3 - Get Data")
os.system("python3 /home/fitec/FITEC/Projet_fil_rouge/Get_Data/get_data_enedis.py")
os.system("python3 /home/fitec/FITEC/Projet_fil_rouge/Get_Data/get_data_meteofrance.py")

print("4 - Load Data")
os.system("python3 /home/fitec/FITEC/Projet_fil_rouge/Load_Data/load_cassandra.py")
os.system("python3 /home/fitec/FITEC/Projet_fil_rouge/Load_Data/load_hdfs.py")

