# def odd_numbers(ls):
#     for i in ls:
#         if i % 2 != 0:
#             print(i)
#
# odd_numbers([12, 7, 25, 30, 50, 61, 82, 91])

# def sum_of_numbers(ls):
#     sum = 0
#     for num in ls:
#         sum=num+sum
#     print(sum)
#
#
# sum_of_numbers([5, 15, 25, 35, 45, 55, 65, 75])

# def min_max_value(ls):
#     min_value = ls[0]
#     max_value = ls[0]
#     for num in ls:
#
#         if num < min_value:
#             min_value = num
#
#
#         if num > max_value:
#             max_value = num
#
#
#     print(f" Minimum value is {min_value}")
#     print(f" Maximum value is {max_value}")
#
# min_max_value([98, 34, 76, 21, 89, 45, 67, 102])

# def min_max_value(ls):
#
#     ls.sort()
#     print("List in ascending order :",ls)
#     min_value=ls[0]
#     print("Minimum value is :",min_value)
#
#     ls.reverse()
#     print("List in reverse order :",ls)
#     max_value=ls[0]
#     print("Maximum value is :",max_value)
#
# min_max_value([98, 34, 76, 21, 89, 45, 67, 102])


# def count_positive_negative_numbers(ls):
#
#     negative_numbers_count=0
#     positive_numbers_count=0
#
#     for i in ls:
#         if i < 0:
#             negative_numbers_count+=1
#
#         elif i > 0:
#             positive_numbers_count+=1
#
#     print("count of positive numbers is :",positive_numbers_count)
#     print("count of negative numbers is :",negative_numbers_count)
#
# count_positive_negative_numbers([-12, 20, -35, 40, -55, 60, -71, 80])

# def check_divisibility(ls):
#
#     for i in ls:
#         if i % 5 == 0:
#             Multiplication=i*2
#             print(f"Number is divisble by 5 so multiplying it with 2 : {i} * 2 = {Multiplication}")
#         else:
#             addition=i+3
#             print(f"Number is not divisble by 5 so adding it with 3 : {i} + 3 = {addition}")
#
# check_divisibility([10, 15, 18, 22, 35, 40, 50, 55])

# check_number([25, 60, 45, 80, 33, 90, 10, 55])
#
# ls = [25, 60, 45, 80, 33, 90, 10, 55]
#
# for num in ls:
#
#     if num > 50:
#         updated_value = num - (num * 10 / 100)
#
#     else:
#         updated_value = num + (num * 20 / 100)
#
#     print(updated_value)


# def check_number(ls):
#     for i in ls:
#         if i > 50:
#             reduced_value= i - (i * 10 / 100)
#             print(f" Number is greater than 50 so reduced_value is {reduced_value}")
#         if i < 50:
#             increased_value= i + (i * 20 / 100)
#             print(f" Number is less than 50 so increased_value is {increased_value}")
#
# check_number([25, 60, 45, 80, 33, 90, 10, 55])


# def replace_prime_numbers(ls):
#
#     for num in ls:
#
#         count = 0
#
#         for i in range(1, num + 1):
#
#             if num % i == 0:
#                 count += 1
#
#         if count == 2:
#             print(-1)
#
#         else:
#             print(num)
#
#
# replace_prime_numbers([11, 22, 37, 44, 53, 61, 72, 88])


# def prime_numbers(ls):
#
#     new_list = []
#
#     for num in ls:
#         count = 0
#
#         for i in range(1, num + 1):
#
#             if num % i == 0:
#                 count += 1
#
#         if count == 2:
#             new_list.append(-1)
#
#         else:
#             new_list.append(num)
#
#     print(new_list)
#
# prime_numbers([11, 22, 37, 44, 53, 61, 72, 88])



# def check_palindrome(ls):
#
#     if ls == ls[::-1]:
#         print("List is palindrome")
#
#     else:
#         print("List is not palindrome")
#
#
# check_palindrome([1, 2, 3, 4, 3, 2, 1])

# def odd_even_numbers(ls):
#
#     new_list=[]
#
#     for num in ls:
#         if num % 2 != 0:
#             new_list.append(0)
#         if num % 2 == 0:
#             new_list.append(1)
#
#     print(new_list)
#
# odd_even_numbers([3, 14, 27, 40, 55, 68, 71, 89])


# def discount(ls):
#
#     for i in range(len(ls)):
#
#         if ls[i] > 100:
#             ls[i] = ls[i] - (ls[i] * 10 / 100)
#
#     print(ls)
#
# discount([150, 200, 50, 80, 120, 95, 300, 400])



# def apply_discount(prices):
#
#     discounted_prices = [price - (price * 15 / 100) if len(prices) > 5 else price for price in prices]
#
#     print(discounted_prices)
#
#
# apply_discount([120, 40, 60, 80, 100, 30, 50])

# def free_item(prices):
#
#    discounted_prices = [0 if price > 500 else price for price in prices]
#
#    print(discounted_prices)
#
#
# free_item([250, 500, 750, 300, 100, 800, 900])



# items = [("Laptop", 1000), ("Milk", 50), ("Mobile", 500), ("Eggs", 30)]
#
# updated_price = []
#
# for item, price in items:
#
#     if item in ["Laptop", "Mobile"]:
#         updated_price.append((item, price * 1.05))
#
#     if item in ["Milk", "Eggs"]:
#         updated_price.append((item, price * 1.03))
#
# print(updated_priceQ)


# def discount(prices):
#
#     total_bill = sum(prices)
#
#     if total_bill > 1000:
#         final_price = total_bill - 100
#     else:
#         final_price = total_bill
#
#     print("Total Bill:", total_bill)
#     print("Final Bill:", final_price)
#
# discount([150, 200, 250, 300, 400, 50, 100])

# def find_index(ls):
#
#     num=50
#
#     if num in (ls):
#         result=ls.index(num)
#     else:
#         result=-1
#
#     print(result)
#
# find_index([10, 20, 30, 40, 50, 60, 70, 80])

# def count_numbers(ls):
#
#     threshold = 40
#
#     count = 0
#
#     for i in ls:
#         if i > threshold:
#             count += 1
#
#     print(f"count of numbers greater than a threshold {threshold} is {count}")
#
# count_numbers([15, 25, 35, 45, 55, 65, 75, 85])

# def check_number(ls,num):
#
#      if num in ls:
#          print("The given number is exist in the list")
#      else:
#          print("The given number does not exist in the list")
#
# ls = list((9, 18, 27, 36, 45, 54, 63, 72))
#
# check_number(ls,63)

# def sum_of_odd_numbers(ls):
#
#     sum=0
#
#     for i in range(1,len(ls),2):
#         sum+=ls[i]
#
#     print(sum)
#
# ls = list((4, 8, 12, 16, 20, 24, 28, 32))
#
# sum_of_odd_numbers(ls)


# def count_of_number(ls):
#
#     count = 0
#
#     for num in ls:
#         if num % 3 == 0 and num % 5 == 0:
#             count+=1
#
#     print("Count of numbers divisible by 3 and 5 is :",count)
#
#
# count_of_number((15, 30, 45, 60, 75, 90, 105, 120))

# def replace_numbers(ls):
#
#     replaced_numbers=[]
#     for num in ls:
#         if num % 10 == 0:
#             replaced_numbers.append(str(num).replace(str(num),"-1"))
#         else:
#             replaced_numbers.append(num)
#
#     print(replaced_numbers)
#
# replace_numbers((10, 25, 30, 45, 50, 65, 70, 85))


# def product_of_odd_numbers(ls):
#
#     product = 1
#
#     for num in ls:
#         if num % 2 !=0:
#             product = product * num
#
#     print("Product of odd numbers is :",product)
#
# product_of_odd_numbers((3, 5, 7, 9, 11, 13, 15, 17))


# def replace_numbers(ls):
#
#     new_ls = []
#
#     for i in range(1, len(ls)-1):
#         difference = ls[i - 1] - ls[i + 1]
#         new_ls.append(difference)
#
#     print(new_ls)
#
# replace_numbers((10, 20, 30, 40, 50, 60, 70, 80))

# def find_numbers(ls):
#
#     count = 0
#
#     for num in ls:
#         if num >= 10:
#             count+=1
#
#     print("Total numbers in the array which have at least two digits are :",count )
#
# find_numbers((1, 5, 10, 25, 30, 45, 50, 8, 99, 100))

# def change_in_price(prices):
#
#     increased_price=0
#     decreased_price=0
#
#     for price in prices:
#         if price < 200:
#             increased_price=price + (price * 20/100)
#
#             print("Price is increased to :", increased_price)
#         else:
#              decreased_price = price - (price * 10/100)
#
#              print("Price is decreased to :", decreased_price)
#
#
# change_in_price((150, 220, 180, 90, 300, 50, 400))

# def discount(ls):
#
#         if len(ls) == 3:
#             item=item - (item * 10/100)
#
#         print(item)
#         else:
#         print(item)
#
# discount((120, 80, 40, 200, 300))

# def discount(prices):
#
#     total_price = sum(prices)
#
#     if len(prices) == 3:
#         total_price = total_price-(total_price * 0.10)
#
#     print("Total_Final Bill is =", total_price)
#
# discount((120, 80, 40, 200, 300))

# def offer(prices):
#
#         total = 0
#
#         for i in range(len(prices)):
#
#             if (i + 1) % 3 != 0:
#                 total += prices[i]
#
#         print("Total price after offer:", total)
#
# offer((100, 150, 200, 250, 300, 350))


# def tiered_discount(prices):
#
#     discounted_prices = []
#
#     for price in prices:
#
#         if price < 100:
#             discounted_price=price-(price * 5 / 100)
#
#
#         elif 100 <= price <= 300:
#              discounted_price = price - (price * 10 / 100)
#
#         elif price > 300:
#              discounted_price=price-(price * 15 / 100)
#
#         discounted_prices.append(discounted_price)
#
#     print(discounted_prices)
#
# tiered_discount((80, 150, 220, 90, 350, 500, 100))


# def shipping(prices):
#
#     total = sum(prices)
#
#     if total > 500:
#         shipping_charges = 0
#     else:
#         shipping_charges = 20
#
#     final_amount = total + shipping_charges
#
#     print("Final Amount:", final_amount)
#
# shipping((120, 130, 100, 200, 50, 60))


# def missing_number(ls):
#
#     num = max(ls)                 # here max number in ls is 10
#
#     expected_sum = num * (num + 1) // 2
#     actual_sum = sum(ls)
#
#     missing_num = expected_sum - actual_sum
#
#     print("Missing number is :", missing_num)
#
# missing_number((1, 2, 3, 5, 6, 7, 8, 9, 10))

# def count(ls):
#
#     max_count = 0
#     most_frequent = ls[0]
#
#     for i in ls:
#         if ls.count(i) > max_count:
#             max_count = ls.count(i)
#             most_frequent = i
#
#     print("Most frequently occurring number in the array is :",most_frequent)
#
# count((4, 4, 5, 6, 7, 5, 6, 6, 6, 7, 8))

#
# def find_pairs(ls,target):
#
#       for i in range(len(ls)):
#
#           for j in range(i+1,len(ls)):
#
#               if ls[i] + ls[j] == target:
#                   print(f"Pair found : {ls[i]} + {ls[j]} == {target}")
#
# find_pairs((1, 2, 3, 4, 5, 6, 7, 8, 9, 10),10)

# def changing_order(ls):
#
#     result = [x for x in ls if x != 0] + [0] * ls.count(0)
#
#     print(result)
#
# changing_order((1, 0, 2, 3, 0, 4, 0, 5, 6, 0))

def check_order(ls):

       if sorted(ls) == ls:
           print("The list is sorted")
       else:
           print("The list is not sorted")

check_order([10, 20, 30, 40, 50, 60, 70, 80])