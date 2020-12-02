import os
import sys

print("start!")
if os.path.exists('src.zip'):
    print(sys.path)
    sys.path.insert(0, 'src.zip')
    print(sys.path)
else:
    sys.path.insert(0, './src')

from myModule import TestFuntions

if __name__ == '__main__':

    from pyspark.sql import SparkSession

    spark = SparkSession.builder \
        .master("local") \
        .appName("myCluster") \
        .getOrCreate()

    TestFuntions.hello_world('Peiran')
     
    print(spark.range(100000).where("id > 1000").selectExpr("sum(id)").collect())
