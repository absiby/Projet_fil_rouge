########################################### Récupération du fichier de données des consommation d'electricité à partir de l'api ###############################

import requests
import Configure.link as cf

def get_enedis(var_env):

        if var_env == 'PROD':
                config = cf.ProductionConfig
        elif var_env == 'TEST':
                config = cf.TestingConfig
        else:
                config = cf.DevelopmentConfig

       
        jsonResponse = requests.get(config.URL)

        #Enregistrement des données dans un fichier au format json
        jsonFilename = config.Filename

        #écriture en binaire
        with open(jsonFilename,"wb") as file:
                file.write(jsonResponse.content)





