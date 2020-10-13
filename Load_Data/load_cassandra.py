######################################## Chargement des données du fichier csv dans cassandra #########################################

from cassandra.cluster import Cluster

def load_meteofrance():

    cluster = Cluster()
    session = cluster.connect()

    session.execute("CREATE KEYSPACE IF NOT EXISTS meteofrancedb WITH REPLICATION = { 'class' : 'SimpleStrategy', 'replication_factor': 1}")
    session.execute('use meteofrancedb')
    session.execute('CREATE TABLE IF NOT EXISTS meteofrance(numer_sta INT ,date VARCHAR,pmer VARCHAR,tend VARCHAR,cod_tend VARCHAR,dd VARCHAR,ff VARCHAR,t VARCHAR,td VARCHAR,u VARCHAR,vv VARCHAR,ww VARCHAR,w1 VARCHAR,w2 VARCHAR,n VARCHAR,nbas VARCHAR,hbas VARCHAR,cl VARCHAR,cm VARCHAR,ch VARCHAR,pres VARCHAR,niv_bar VARCHAR,geop VARCHAR,tend24 VARCHAR,tnN VARCHAR,txN VARCHAR,tminsol VARCHAR,sw VARCHAR,tw VARCHAR,raf10 VARCHAR,rafper VARCHAR,per VARCHAR,etat_sol VARCHAR,ht_neige VARCHAR,ssfrai VARCHAR,perssfrai VARCHAR,rrN VARCHAR,phenspeN VARCHAR,nnuageN VARCHAR,ctypeN VARCHAR,hnuageN VARCHAR,nom_dept VARCHAR,code_dep VARCHAR,nom_reg VARCHAR,code_reg VARCHAR, primary key(numer_sta, date) )')

    prepared = session.prepare("""
            INSERT INTO meteofrance(numer_sta,date,pmer,tend,cod_tend,dd,ff,t,td,u,vv,ww,w1,w2,n,nbas,hbas,cl,cm,ch,pres,niv_bar,geop,tend24,tnN,txN,tminsol,sw,tw,raf10,rafper,per,etat_sol,ht_neige,ssfrai,perssfrai,rrN,phenspeN,nnuageN,ctypeN,hnuageN,nom_dept,code_dep,nom_reg,code_reg)
            VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
            """)

    # load 10 lignes
    #lien_fichier = "/home/fitec/projet_fil_rouge/source_des_données/data/donnees-meteofrance_l10.csv"
    # load total
    lien_fichier = "/home/fitec/projet_fil_rouge/source_des_données/data/donnees-meteofrance.csv"

    with open(lien_fichier, "r") as rows:
        i = 0    
        for row in rows:
            if i == 1:
                columns = row.split(";")
                numer_sta = int(columns[0])
                date = columns[1]
                pmer = columns[2]
                tend = columns[3]
                cod_tend = columns[4]
                dd = columns[5]
                ff = columns[6]
                t = columns[7]
                td = columns[8]
                u = columns[9]
                vv = columns[10]
                ww = columns[11]
                w1 = columns[12]
                w2 = columns[13]
                n = columns[14]
                nbas = columns[15]
                hbas = columns[16]
                cl = columns[17]
                cm = columns[18]
                ch = columns[19]
                pres = columns[20]
                niv_bar = columns[21]
                geop = columns[22]
                tend24 = columns[23]
                tnN = columns[24]
                txN = columns[25]
                tminsol = columns[26]
                sw = columns[27]
                tw = columns[28]
                raf10 = columns[29]
                rafper = columns[30]
                per = columns[31]
                etat_sol = columns[32]
                ht_neige = columns[33]
                ssfrai = columns[34]
                perssfrai = columns[35]
                rrN = columns[36]
                phenspeN = columns[37]
                nnuageN = columns[38]
                ctypeN = columns[39]
                hnuageN = columns[40]
                nom_dept = columns[77]
                code_dep = columns[78]
                nom_reg = columns[79]
                code_reg = columns[80]


                session.execute(prepared, [numer_sta,date,pmer,tend,cod_tend,dd,ff,t,td,u,vv,ww,w1,w2,n,nbas,hbas,cl,cm,ch,pres,niv_bar,geop,tend24,tnN,txN,tminsol,sw,tw,raf10,rafper,per,etat_sol,ht_neige,ssfrai,perssfrai,rrN,phenspeN,nnuageN,ctypeN,hnuageN,nom_dept,code_dep,nom_reg,code_reg]
)
            i = 1    



    #closing Cassandra connection
    session.shutdown()