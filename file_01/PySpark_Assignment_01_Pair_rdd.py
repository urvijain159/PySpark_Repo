
# def pair_rdd():
#
#     data=[(101,"Amit"),(102,"Nilesh"),(103,"Shakti"),(104,"Preeti")]
#
#     sc=spark.sparkContext
#     rdd=sc.parallelize(data)
#     result=rdd.lookup(102)
#     print(result)
#
# pair_rdd()

# def count_of_word():
#
#     data=list(("apple", "banana", "apple", "orange", "banana", "apple"))
#
#     sc=spark.sparkContext
#     rdd=sc.parallelize(data)
#
#     pairing=rdd.map(lambda x : (x,1))
#     print(pairing.collect())
#
#     count=pairing.reduceByKey(lambda x,y : x+y)
#     print(count.collect())
#
# count_of_word()


# def apply_grouping():
#
#     data=list((("IT", 60000), ("HR", 50000), ("IT", 70000), ("HR", 45000), ("Finance", 80000)))
#
#     sc=spark.sparkContext
#     rdd=sc.parallelize(data)
#
#     output=rdd.groupByKey().mapValues(list)
#     print(f" Salaries by department are {output.collect()}")
#
# apply_grouping()





# def sorting():
#
#     data=[(105, "Omkar"), (101, "Vishal"), (103,"Shreya"), (104,"Suraj")]
#
#     sc = spark.sparkContext
#     rdd = sc.parallelize(data)
#
#     output=rdd.sortByKey(True)
#     print(output.collect())
#
# sorting()


# def joining_rdd():
#
#     data1 = [(1, "Laptop"), (2,"Mobile"), (3,"Tablet")]
#     data2 = [(1, 50000), (2, 20000), (4, 15000)]
#
#     sc=spark.sparkContext
#     rdd1=sc.parallelize(data1)
#     rdd2=sc.parallelize(data2)
#
#     inner_join_rdd=rdd1.join(rdd2)
#     print(inner_join_rdd.collect())
#
# joining_rdd()


# def outer_joining_rdd():
#
#     data1 = [(1,"Riya"), (2, "Divya"), (3,"Pallavi")]
#     data2 = [(1,"IT"), (2,"HR")]
#
#     sc=spark.sparkContext
#     rdd1=sc.parallelize(data1)
#     rdd2=sc.parallelize(data2)
#
#     left_join_rdd=rdd1.leftOuterJoin(rdd2)
#     print(left_join_rdd.collect())
#
# outer_joining_rdd()


from pyspark import SparkConf
conf1 = SparkConf().setAppName("First Application").setMaster("local[2]")
from pyspark.sql import SparkSession
spark = SparkSession.builder.config(conf=conf1).getOrCreate()

def find_average_salary():

    data=list((("IT",70000),("IT", 80000), ("HR", 60000), ("HR", 50000), ("Finance", 90000)))

    sc=spark.sparkContext
    rdd=sc.parallelize(data)

    avr_salary=rdd.combineByKey(lambda salary: (salary, 1),
    lambda acc, salary: (acc[0] + salary, acc[1] + 1),
    lambda acc1, acc2: (acc1[0] + acc2[0], acc1[1] + acc2[1])).mapValues(lambda x: x[0] / x[1])

    print(avr_salary.collect())

find_average_salary()

