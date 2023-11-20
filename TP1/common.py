from pyspark.sql import SparkSession

def createSession():
    spark = SparkSession.builder \
        .appName("tp1") \
        .config("spark.executor.instances", "2") \
        .config("spark.executor.cores", "2") \
        .config("spark.executor.memory", "1024M") \
        .getOrCreate()
    return spark

