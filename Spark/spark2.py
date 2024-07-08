# CONVERTING CSV TO DATAFRAME

from pyspark.sql import SparkSession

# Initialize SparkSession
spark = SparkSession.builder \
    .appName("CSV to DataFrame") \
    .getOrCreate()

# Read CSV into DataFrame
df = spark.read.csv(r"C:\Users\ASUS\Desktop\dummycust.csv", header=True)

# Show the DataFrame
df.show()