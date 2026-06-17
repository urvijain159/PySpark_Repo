

# def key_count():
#
#     data = list((("Pune", 3), ("Delhi", 2), ("Mumbai", 5), ("Tamil", 1)))
#
#     sc = spark.sparkContext
#     rdd = sc.parallelize(data)
#
#     count_of_keys=rdd.countByKey()
#
#     print(count_of_keys)
#
# key_count()



# def find_top_5():
#
#     data=list((55, 20, 75, 10, 90, 5, 30))
#
#     sc=spark.sparkContext
#     rdd = sc.parallelize(data)
#     print(rdd.takeOrdered(5))
#
# find_top_5()




# def print_all_elements():
#
#     data=list(("Scala","Spark", "Hadoop", "Hive", "Scala", "Spark"))
#
#     sc=spark.sparkContext
#     rdd=sc.parallelize(data)
#
#     rdd.foreach(lambda x: print(x))
#
# print_all_elements()





# def find_min_max_values():
#
#     data=list((500, 1000, 200, 50, 700, 900))
#
#     sc=spark.sparkContext
#     rdd=sc.parallelize(data)
#
#     minimum_value=rdd.min()
#     print(F" Minimum_value is {minimum_value}")
#
#     maximum_value=rdd.max()
#     print(f" Maximum_value is {maximum_value}")
#
# find_min_max_values()




# def calculate_sum():
#
#     data= list((5, 10, 15, 20, 25))
#
#     sc=spark.sparkContext
#     rdd = sc.parallelize(data)
#
#     total=rdd.fold(0,lambda x,y : x+y)
#
#     print(f" Sum of all elements is : {total}")
#
# calculate_sum()





# def number_of_words():
#
#     data=["analytics", "data", "spark", "databricks", "database"]
#
#     sc=spark.sparkContext
#     rdd=sc.parallelize(data)
#
#     word_count=rdd.filter(lambda word : "data" in word).count()
#
#     print(f" Number of words that contain data is : {word_count}")
#
#
# number_of_words()


from pyspark import SparkConf, SparkContext
conf1 = SparkConf().setAppName("First Application").setMaster("local[2]")
from pyspark.sql import SparkSession
spark = SparkSession.builder.config(conf=conf1).getOrCreate()

def find_frequent_words():

    data=list(("Spark is great", "Big Data is powerful", "Spark makes Big Data easy"))

    sc=spark.sparkContext
    rdd=sc.parallelize(data)

    rdd2=rdd.flatMap(lambda x:x.split(" "))
    print(f" Data after split : {rdd2.collect()}")

    rdd3=rdd2.map(lambda x : (x,1))
    print(rdd3.collect())

    rdd4=rdd3.reduceByKey(lambda x,y : x+y)
    print(f" Word count : {rdd4.collect()}")

    rdd5=rdd4.sortBy(lambda x : x[1],False)
    print(f" 5 Most frequent words : {rdd5.take(5)}")

find_frequent_words()