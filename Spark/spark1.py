
# READING A TEXT FILE
from pyspark.sql import SparkSession


spark = SparkSession.builder \
    .appName("PySpark Example") \
    .getOrCreate()

# Read a text file into an RDD
lines = spark.sparkContext.textFile("C:\\Users\\ASUS\\Desktop\\dummy.txt")
print(lines.collect())
spark.stop()
# READING THE DUMMY DATA

# from pyspark.sql import SparkSession

# # Initialize SparkSession
# spark = SparkSession.builder \
#     .appName("PySpark Example") \
#     .getOrCreate()

# data = [
#     ("Alice", 25, "Engineering"),
#     ("Bob", 30, "Sales"),
#     ("Charlie", 28, "Marketing"),
#     ("David", 35, "Engineering"),
#     ("Eve", 27, "HR"),
#     ("Frank", 32, "Finance")
# ]
# # Read a text file into an RDD
# columns=["name","age","degree"]
# df=spark.createDataFrame(data=data,schema=columns)

# print(df.printSchema())
