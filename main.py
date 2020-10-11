
import Get_Data.get_data_meteofrance as gm
import Get_Data.get_data_enedis as ge
import Load_Data.load_cassandra as lc
import Load_Data.load_hdfs as lh
import Load_Data.load_mongo as lm



def main():
    print("3 - Get Data")
    #gm.get_meteofrance()
    #ge.get_enedis()

    print("4 - Load Data")
    #lc.load_meteofrance()
    #lh.load_enedis()
    lm.load_tables_technique_mongo()

if __name__ == "__main__":
    main()