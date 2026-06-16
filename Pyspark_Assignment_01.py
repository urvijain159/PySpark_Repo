# def rdd_creation():
#
#     data = list((10, 20, 30, 40, 50, 60, 70, 80, 90, 100))
#
#     from pyspark import SparkConf
#     conf1 = SparkConf().setAppName("First Application").setMaster("local[*]")
#
#     from pyspark.sql import SparkSession
#     spark=SparkSession.builder.config(conf=conf1).getOrCreate()
#     sc=spark.sparkContext
#     rdd=sc.parallelize(data)
#     result=rdd.collect()
#     print(result)
#     for num in result:
#         print(num,end=" ")
#
# rdd_creation()



# def rdd_creation():
#
#     data = list((1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
#
#     from pyspark import SparkConf
#     conf1 = SparkConf().setAppName("First Application").setMaster("local[2]")
#
#     from pyspark.sql import SparkSession
#     spark=SparkSession.builder.config(conf=conf1).getOrCreate()
#     sc=spark.sparkContext
#     rdd=sc.parallelize(data)
#     print(rdd.collect())
#     rdd.saveAsTextFile("C:/Users/Urvi/PycharmProjects/PysparkProject1/file_01")
#
# rdd_creation()


# def find_mean():
#
#     data = list((5, 10, 15, 20, 25))
#
#     from pyspark import SparkConf
#     conf1 = SparkConf().setAppName("First Application").setMaster("local[2]")
#
#     from pyspark.sql import SparkSession
#     spark=SparkSession.builder.config(conf=conf1).getOrCreate()
#     sc=spark.sparkContext
#     rdd=sc.parallelize(data)
#
#     # using mean
#     print(f"Result using mean functionality: {rdd.mean()}")
#
#     #without using mean
#     total=rdd.sum()
#     count=rdd.count()
#     mean_value=total/count
#
#     print(f"Result without using mean functionality: {mean_value}")
#
# find_mean()



# def filter_even_numbers():
#
#     data=list((3, 6, 9, 12, 15, 18, 21, 24) )
#
#     sc=spark.sparkContext
#     rdd=sc.parallelize(data)
#     even_numbers=rdd.filter(lambda x : x % 2 == 0)
#     print(even_numbers.collect())
#
# filter_even_numbers()



# def remove_duplicates():
#
#     data=list((1, 2, 3, 3, 4, 5, 5, 6, 7, 7, 8, 9))
#
#     sc=spark.sparkContext
#     rdd=sc.parallelize(data)
#     unique_values=rdd.distinct().collect()
#     print(unique_values)
#
# remove_duplicates()


from pyspark import SparkConf
conf1 = SparkConf().setAppName("First Application").setMaster("local[2]")

from pyspark.sql import SparkSession
spark = SparkSession.builder.config(conf=conf1).getOrCreate()

def count_elements():

    data=list(('Scala', 'Spark', 'Hadoop', 'Hive', 'Scala', 'Spark'))

    sc=spark.sparkContext
    rdd=sc.parallelize(data)
    count_of_elements=rdd.count()

    print(f"Count of elements in the RDD is : {count_of_elements}")

count_elements()
