import pyspark
from pyspark.sql import SparkSession

spark=SparkSession.builder.appName('Synthegrate').getOrCreate()
print(spark)
print('######################################################################################')

spark.stop()