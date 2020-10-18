
import Get_Data.get_data_meteofrance as gm
import Get_Data.get_data_enedis as ge
import Load_Data.load_cassandra as lc
import Load_Data.load_mongo as lm
import os



def main():
    print("3 - Get Data")
    #gm.get_meteofrance()
    #ge.get_enedis()

    print("4 - Load Data")
    #lc.load_meteofrance()

    print("5 - Talend")
    os.system("chmod 777 /home/fitec/FITEC/Projet_fil_rouge/Talend/Job_merge_enedis_v2_0.1/Job_merge_enedis_v2/*")
    os.system("/home/fitec/FITEC/Projet_fil_rouge/Talend/Job_merge_enedis_v2_0.1/Job_merge_enedis_v2/Job_merge_enedis_v2_run.sh")


    print("6 - Machine learning")
    #os.system("/home/fitec/spark/spark-3.0.0-bin-hadoop2.7/bin/spark-submit --packages org.mongodb.spark:mongo-spark-connector_2.12:3.0.0 MachineLearning/model_lineaire.py")


if __name__ == "__main__":
    main()