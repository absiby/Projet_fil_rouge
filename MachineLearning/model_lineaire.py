# -*- coding: utf-8 -*-

from pyspark.sql import SparkSession
from pyspark import SparkConf, SparkContext
from pyspark.sql import SQLContext

from pyspark.ml.feature import VectorAssembler
from pyspark.ml.feature import StandardScaler
from pyspark.ml.regression import LinearRegression
from pyspark.ml import Pipeline
from pyspark.sql.types import *

from pyspark.ml.evaluation import RegressionEvaluator



def modelsummary(model, colnames):
    import numpy as np
    print ("Note: the last rows are the information for Intercept")
    print ("##","-------------------------------------------------")
    print ("Name","  Estimate   |   Std.Error | t Values  |  P-value")
    coef = np.append(list(model.coefficients),model.intercept)
    colnames = np.append( colnames, "Intercept")

    Summary=model.summary

    for i in range(len(Summary.pValues)):
        print (colnames[i],'{:10.6f}'.format(coef[i]),\
        '{:10.6f}'.format(Summary.coefficientStandardErrors[i]),\
        '{:8.3f}'.format(Summary.tValues[i]),\
        '{:10.6f}'.format(Summary.pValues[i]))

    print ("##",'---')
    print ("##","Mean squared error: % .6f" \
           % Summary.meanSquaredError, ", RMSE: % .6f" \
           % Summary.rootMeanSquaredError )
    print ("##","Multiple R-squared: %f" % Summary.r2, ", \
            Total iterations: %i"% Summary.totalIterations)

 
print("SparkSession: ##################################################################################")
my_spark = SparkSession \
 .builder \
 .appName("myApp") \
 .config("spark.mongodb.input.uri", "mongodb://127.0.0.1/DB_projet.meteo_enedis") \
 .config("spark.mongodb.output.uri", "mongodb://127.0.0.1/DB_projet.meteo_enedis") \
 .getOrCreate()
 
print("table mean_meteo de mongoDB: ##################################################################################") 
# table mean_meteo de mongoDB
df = my_spark.read.format("mongo").load()
df.printSchema()
df.registerTempTable("meteo_enedis")
 
print("Requete SQL all_data: ##################################################################################") 
all_data = my_spark.sql(\
	"SELECT * FROM meteo_enedis \
	where total_energie_soutiree_wh is not null \
	and code_reg = '24' \
	and profil like '%RES%' ")

print("all_data:")
all_data.show()

#all_data.printSchema()

conso_df = all_data.select("total_energie_soutiree_wh","t","td","tend","tend24","tminsol","tnn","per","pres","pmer","dd", "ff", "u", "vv", "txn", "n")

conso_df.printSchema()



(training, test) = conso_df.randomSplit([.8, .2])

numericCols = ["t","td","tend","tend24","tminsol","tnn","per","pres","pmer","dd", "ff", "u", "vv", "txn", "n"]


vectorAssembler = VectorAssembler(inputCols=numericCols, outputCol="unscaled_features")
standardScaler = StandardScaler(inputCol="unscaled_features", outputCol="features")

lr = LinearRegression(labelCol="total_energie_soutiree_wh", maxIter=100, regParam=.01)

# stages = [vectorAssembler,standardScaler, lr]
# pipeline = Pipeline(stages=stages)

pipeline = Pipeline(stages=[vectorAssembler,standardScaler, lr])

model = pipeline.fit(training)

prediction = model.transform(test)

print("prediction: ##################################################################################")
prediction.show()

print("Resultat: ##################################################################################")

#summary = model.stages.summary
table_res = modelsummary(model.stages[-1],numericCols)



print("Resultat: ##################################################################################")


eval = RegressionEvaluator(labelCol="total_energie_soutiree_wh", predictionCol="prediction", metricName="rmse")

print("Resultat: ##################################################################################")
# Root Mean Square Error
rmse = eval.evaluate(prediction)
print("RMSE: %.3f" % rmse)

print("Resultat: ##################################################################################")
# Mean Square Error
mse = eval.evaluate(prediction, {eval.metricName: "mse"})
print("MSE: %.3f" % mse)

print("Resultat: ##################################################################################")
# Mean Absolute Error
mae = eval.evaluate(prediction, {eval.metricName: "mae"})
print("MAE: %.3f" % mae)

print("Resultat: ##################################################################################")
# r2 - coefficient of determination
r2 = eval.evaluate(prediction, {eval.metricName: "r2"})
print("r2: %.3f" %r2)



les_resultats = {"RMSE": rmse, "MSE": mse, "MAE": mae, "r2": r2}

les_resultats.toPandas("/home/fitec/projet_fil_rouge/ML_resultats/resultats")
table_res.toPandas().to_csv("/home/fitec/projet_fil_rouge/ML_resultats/table_res.csv")

 
'''/home/fitec/spark/spark-3.0.0-bin-hadoop2.7/bin/spark-submit --packages org.mongodb.spark:mongo-spark-connector_2.12:3.0.0 MachineLearning/model_lineaire.py '''