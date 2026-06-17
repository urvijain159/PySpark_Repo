# def find_union():
#
#     data1 = list((1, 2, 3, 4))
#     data2 = list((3, 4, 5, 6))
#
#     sc=spark.sparkContext
#     rdd1 = sc.parallelize(data1)
#     rdd2 = sc.parallelize(data2)
#
#     union_rdd=rdd1.union(rdd2)
#     print(union_rdd.collect())
#
# find_union()



# def find_intersection():
#
#     data1 = list((1, 2, 3, 4, 5))
#     data2 = list((3, 4, 5, 6, 7))
#
#     sc=spark.sparkContext
#     rdd1 = sc.parallelize(data1)
#     rdd2 = sc.parallelize(data2)
#
#     intersection_rdd=rdd1.intersection(rdd2)
#     print(intersection_rdd.collect())
#
# find_intersection()

# def find_subtraction():
#
#     data1 = list((10, 20, 30, 40, 50))
#     data2 = list((30, 40, 50))
#
#     sc=spark.sparkContext
#     rdd1 = sc.parallelize(data1)
#     rdd2 = sc.parallelize(data2)
#
#     subtract_rdd=rdd1.subtract(rdd2)
#     print(subtract_rdd.collect())
#
# find_subtraction()

from pyspark import SparkConf
conf1 = SparkConf().setAppName("First Application").setMaster("local[2]")
from pyspark.sql import SparkSession
spark = SparkSession.builder.config(conf=conf1).getOrCreate()

def find_cartesian():

    data1 = list((1, 2, 3))
    data2 = list(("A", "B"))

    sc=spark.sparkContext
    rdd1 = sc.parallelize(data1)
    rdd2 = sc.parallelize(data2)

    cartesian_rdd=rdd1.cartesian(rdd2)
    print(cartesian_rdd.collect())

find_cartesian()