######################################## Chargement des données du fichier csv dans cassandra #########################################

from cassandra.cluster import Cluster


def meteofrance_in_cassandra():

    cluster = Cluster()
    #cluster = Cluster(['127.0.0.1'], port=9042)
    session = cluster.connect()


    session.execute("CREATE KEYSPACE IF NOT EXISTS meteofrancedb WITH REPLICATION = { 'class' : 'SimpleStrategy', 'replication_factor': 1}")
    session.execute('use meteofrancedb')
    session.execute('CREATE TABLE IF NOT EXISTS meteofrance(numer_sta INT primary key, date VARCHAR, pmer VARCHAR, tend VARCHAR, cod_tend VARCHAR)')

    prepared = session.prepare("""
            INSERT INTO meteofrance (numer_sta, date, pmer, tend, cod_tend)
            VALUES (?, ?, ?, ?, ?)
            """)

    with open("/home/fitec/projet_fil_rouge/source_des_données/data/meteofrance.csv", "r") as rows:
        i = 0    
        for row in rows:
            if i == 1:
                columns = row.split(";")
                numer_sta = int(columns[0])
                date = columns[1]
                pmer = columns[2]
                tend = columns[3]
                cod_tend = columns[4]

                session.execute(prepared, [numer_sta, date, pmer, tend, cod_tend])
            i = 1    



    #closing Cassandra connection
    session.shutdown()

