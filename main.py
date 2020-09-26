import Shell.shell as sh
import Get_Data.get_data_enedis as gde
import Get_Data.get_data_meteofrance as gdm
import Load_Data.load_cassandra as lc
import Load_Data.load_hdfs as lh



def main():
    sh.start_data_lake()
    gde.data_enedis()
    gdm.data_meteofrance()
    #lc.meteofrance_in_cassandra()
    lh.enedis_in_hdfs()

if __name__ == "__main__":
    main()


