
# CONVERTING JSON TO DATAFRAME

from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, ArrayType

# Initialize SparkSession
spark = SparkSession.builder \
    .appName("JSON to DataFrame") \
    .getOrCreate()

# Define a simplified schema
schema = StructType([
    StructField("quiz", StringType(), True)
])

# Path to your JSON file
json_file = r"C:\Users\ASUS\Desktop\dummyjson.json"

try:
    # Read JSON file into DataFrame with explicit schema
    df = spark.read.schema(schema).json(json_file)
    
    # Show the DataFrame
    df.show(truncate=False)

except Exception as e:
    print(f"Error reading JSON file: {e}")

finally:
    spark.stop()
