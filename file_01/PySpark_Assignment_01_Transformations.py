# def map_function():
#
#     data = list(('hello', 'world', 'scala', 'spark'))
#
#     sc=spark.sparkContext
#     rdd=sc.parallelize(data)
#
#     upper_case=rdd.map(lambda x : x.upper())
#
#     print(upper_case.collect())
#
# map_function()





# def flat_map():
#
#     data = list(('Big Data is powerful', 'Spark makes processing faster'))
#
#     sc=spark.sparkContext
#     rdd=sc.parallelize(data)
#     rdd1=rdd.flatMap(lambda x : x.split())
#     print(rdd1.collect())
#
# flat_map()


# def is_prime(num):
#     if num < 2:
#         return False
#
#     for i in range(2, num):
#         if num % i == 0:
#             return False
#
#     return True
#
# def filter_prime_numbers():
#
#     data = list((2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13))
#
#     rdd = spark.sparkContext.parallelize(data)
#
#     prime_rdd = rdd.filter(is_prime)
#
#     print(prime_rdd.collect())
#
# filter_prime_numbers()




# def product_of_numbers():
#
#     data = list((1, 2, 3, 4, 5, 6))
#
#     sc=spark.sparkContext
#     rdd=sc.parallelize(data)
#     product=rdd.reduce(lambda x,y : x*y)
#     print(f"The product of all numbers is : {product}")
#
# product_of_numbers()


# def map_partitions():
#
#     data = list((10, 20, 30, 40, 50, 60, 70, 80, 90))
#
#     sc=spark.sparkContext
#     rdd=sc.parallelize(data,3)
#     print(f"Data divided into 3 partitions : {rdd.glom().collect()}")
#     add=rdd.mapPartitions(lambda num:[i+10 for i in num])
#     print(f"Added 10 on each number : {add.collect()}")
#     print(f"Added 10 on each number : {add.glom().collect()}")
#
#
# map_partitions()


# def implement_sample():
#
#     data = list((100, 200, 300, 400, 500, 600, 700))
#
#     sc=spark.sparkContext
#     rdd = sc.parallelize(data)
#     print(rdd.sample(True,0.5).collect())
#
# implement_sample()

from pyspark import SparkConf
conf1 = SparkConf().setAppName("First Application").setMaster("local[2]")
from pyspark.sql import SparkSession
spark = SparkSession.builder.config(conf=conf1).getOrCreate()