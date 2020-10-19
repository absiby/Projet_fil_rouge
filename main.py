
import Get_Data.get_data_meteofrance as gm
import Get_Data.get_data_enedis as ge
import Load_Data.load_cassandra as lc
import Load_Data.load_mongo as lm
import os



def main():
    print("1 - Get Data meteo")
    #gm.get_meteofrance()
    print("2 - Get Data enedis")
    #ge.get_enedis()

    print("3 - Load Data meteo")
    #lc.load_meteofrance()

    print("4 - Talend: chargement dans mongoDB")
    #os.system("chmod -R 777 /home/fitec/FITEC/Projet_fil_rouge/Talend/*")
    #os.system("/home/fitec/FITEC/Projet_fil_rouge/Talend/Cassandra_to_Mongodb_v1_0.1/Cassandra_to_Mongodb_v1/Cassandra_to_Mongodb_v1_run.sh")


    print("5 - Machine learning: régression lineaire")
    os.system("/home/fitec/spark/spark-3.0.0-bin-hadoop2.7/bin/spark-submit --packages org.mongodb.spark:mongo-spark-connector_2.12:3.0.0 MachineLearning/model_lineaire.py")


if __name__ == "__main__":
    main()