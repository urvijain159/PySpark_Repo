

# def check_num(Num):
#
#     if  Num > 0 and Num % 2== 0:
#         print(f"{Num} is even and Positive")
#     elif Num > 0 and Num % 2 != 0:
#         print(f"{Num} is positive number and it is odd number")
#     else:
#         print(f"{Num} is either not even or not positive")
#
# check_num(28)

# def num_gt_lt_check():
#     num=int(input("Please enter a value : "))
#     if num <-10 or num > 10:
#         print(f"{num} is either less than -10 or greater than 10")
#     else:
#         print(f"{num} is not either less than -10 or not greater than 10")
#
# num_gt_lt_check()

# def odd_num_check():
#      num=int(input("Please enter a value : "))
#
#      if num % 2 != 0 and num % 3 !=0:
#          print(f"{num} is odd and not divisible by 3")
#      else:
#          print("False")
# odd_num_check()


# def check_divisible():
#     num=int(input("Please enter a value : "))
#
#     if num % 4 == 0 or num % 6 ==0:
#         print(f"{num} is divisible by either 4 or 6")
#     else:
#         print(f"{num} is not divisible by either 4 or not by 6")
# check_divisible()

# def check_eligibility():
#
#     age = int(input("Please enter age: "))
#     if age >= 18:
#         print("Person is eligible to drive and vote'")
#     elif age >= 16 and age < 18:
#         print("Person is eligible to drive but not eligible to vote")
#     else:
#         print("Person is not eligible to vote or drive")
# check_eligibility()


# def multiple_range_check(num):
#     if (num >=1 and num <= 10) or (num >=20 and num <= 30):
#         print(f"{num} is in between 1 and 10 or between 20 and 30")
#     # elif num >=20 and num <= 30:
#     #     print(f"{num} is between 20 and 30")
#     else:
#         print(f"{num} is not in between 1 and 10 and not in between 20 and 30 ")
# multiple_range_check(7)

# def num_check(num):
#     if num < 0 and num % 2 != 0:
#         print(f"{num} is negative and odd")
#     else:
#         print(f"{num} is either not odd or negative")
# num_check(89)


# def senior_student_eligibility(age):
#     if age > 60:
#         print("Person is eligible for senior discount")
#     elif age < 25:
#         print("Person is eligible for student discount")
#     else:
#         print("Person is not eligible for student discount and senior discount")
# senior_student_eligibility(55)

# def even_or_positive_check(num):
#     if num >= 0 or num % 2 == 0:
#         print(f"{num} is either non-negative or even")
#     else:
#         print(f"{num} is negative and odd")
# even_or_positive_check(-11)

# def prime_odd_check(num):
#     if num <= 1:
#         print(f"{num} is not both prime and odd")
#     else:
#         for i in range(2, num):
#             if num % i == 0:
#                 print(f"{num} is not both prime and odd")
#                 break
#         else:
#             if num % 2 != 0:
#                 print(f"{num} is both prime and odd")
#             else:
#                 print(f"{num} is not both prime and odd")
#
# prime_odd_check(2)

# def check_offer(purchase_amount):
#     if purchase_amount > 150 or purchase_amount > 100:
#         print(f" purchase amount is {purchase_amount} so person is eligible for discount or free shipping")
#     else:
#         print(f"purchase amount is <=100 so person is not eligible for any offer")
# check_offer(50)

# def check_divisible():
#     num=int(input("Please enter a value : "))
#
#     if num % 3 == 0 or num % 8 ==0:
#         print(f"{num} is divisible by either 3 or 8")
#     else:
#         print(f"{num} is not divisible by either 3 or not by 8")
# check_divisible()


# def check_num(Num):
#
#     if  Num < 0 and Num % 2== 0:
#         print(f"{Num} is even and non_positive")
#     else:
#         print(f"{Num} is not both even and positive")
#
# check_num(0)

# def age_group(age):
#     if age < 13:
#         print("Child")
#     elif age >= 13 and age <= 19:
#         print("Teen")
#     else:
#         print("Adult")
# age_group(39)

# def check_divisible():
#     num=int(input("Please enter a value : "))
#
#     if num % 2 == 0 or num % 5 ==0:
#         print(f"{num} is divisible by either 2 or 5")
#     else:
#         print(f"{num} is not divisible by either 2 or not by 5")
# check_divisible()


# def check_discounts(age):
#     if age > 60 and age < 25:
#         print("Eligible for Senior Discount AND Student Discount ")
#     else:
#         print("Impossible case")
#
# age = int(input("Enter age: "))
# check_discounts(age)


# def check_divisible(num):
#     if num % 5 == 0 or num % 9 ==0:
#         print(f"{num} is divisible by either 5 or 9")
#     else:
#         print(f"{num} is not divisible by either 5 or 9")
# check_divisible(50)


# def Eligible_for_discount(purchase_amount, loyalty_card):
#     if purchase_amount > 200 or loyalty_card:
#         print("Eligible for Discount or Membership Benefits")
#     else:
#         print("Not Eligible")
#
# Eligible_for_discount(140,True)


# def check_divisible(num):
#     if num % 2 == 0 or num % 3 == 0:
#         print("Number is divisible by either 2 or 3")
#     else:
#         print("Number is not divisible by 2 or 3")
#
# check_divisible(4)


# def check_number(num):
#     if num > 0 and num % 3 != 0:
#         print("Number is positive and not divisible by 3")
#     else:
#         print("Condition not satisfied")
#
# check_number(10)


# def check_customer(age, is_new_customer):
#     if age > 65 and not is_new_customer:
#         print("Eligible")
#     else:
#         print("Not Eligible")
#
# check_customer(68, False)



# def check_number_prime_or_odd(num):
#     is_prime = True
#
#     if num <= 1:
#         is_prime = False
#     else:
#         for i in range(2, num):
#             if num % i == 0:
#                 is_prime = False
#                 break
#
#     if num % 2 != 0 or is_prime:
#         print("Number is odd or prime")
#     else:
#         print("Condition not satisfied")
#
# check_number_prime_or_odd(9)


# def check_eligibility(purchase_amount):
#     if purchase_amount > 150 and purchase_amount > 100:
#         print("Eligible for Discount and Free Shipping")
#     else:
#         print("Not Eligible")
#
# check_eligibility(700)



# def check_number(num):
#     if num >= 0 and num % 7 != 0:
#         print("Number is non-negative and not divisible by 7")
#     else:
#         print("Condition not satisfied")
#
# check_number(9)

# def check_eligibility(age, free_trial):
#     if age < 25 or free_trial:
#         print("Eligible for Student Discount or Free Trial")
#     else:
#         print("Not Eligible")
#
# check_eligibility(27, True)

def check_number(num):
    if num % 4 == 0 or num % 6 == 0:
        print("Number is divisible by 4 or 6")
    else:
        print("Number is not divisible by 4 or 6")

check_number(60)
