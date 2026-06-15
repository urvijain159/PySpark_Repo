# def convert_kg_to_grams(kg):
#     grams = kg * 1000
#     print(f"{kg} kg = {grams} gms")
#
# convert_kg_to_grams(82)

# def convert_celsius_to_fahrenheit(c):
#     f = (c * 9/5) + 32
#     print(f"{c}°C = {f}°F")
#
# convert_celsius_to_fahrenheit(35)


def largest_number():
    a = 25
    b = 48
    c = 36

#     if a >= b and a >= c:
#         print("Largest number is:", a)
#     elif b >= a and b >= c:
#         print("Largest number is:", b)
#     else:
#         print("Largest number is:", c)
#
# def largest_of_three_numbers(num1,num2,num3):
#     if num1 >= num2 and num1 >=num3:
#         print("Largest number is:", num1)
#     elif num2 >= num1 and num2 >=num3:
#         print("Largest number is:", num2)
#     else:
#         print("Largest number is:", num3)
# largest_of_three_numbers(45,68,33)

#
# def Number_evaluation(number):
#
#     if number < 150 or number > 950:
#         print("Invalid number")
#     else:
#         if number % 2 == 0:
#             print("Even number")
#             print(f"Remainder when divided by 4: {number % 4}")
#         else:
#             print("Odd number")
#             print(f"Remainder when divided by 3: {number % 3}")
#
# Number_evaluation(721)


# def Range_Labelling_Evaluation(num):
#
#     if 0 <= num <= 100:
#         if 90 <= num <= 100:
#             print("Genius")
#         elif 80 <= num <= 89:
#             print("Excellent")
#         elif 70 <= num <= 79:
#             print("Very Good")
#         elif 60 <= num <= 69:
#             print("Good")
#         elif 40 <= num <= 59:
#             print("Average")
#         else:
#             print("Fail")
#     else:
#         print("Invalid input")
#
# Range_Labelling_Evaluation(75)


# def simple_calculator(a,b,op):
#
#
#     if op == "+":
#         print(f"Addition = {a+b}")
#     elif op == "-":
#         print(f"Subtraction = {a+b}")
#     elif op == "*":
#         print(f"Multiplication = {a*b}")
#     elif op == "/":
#         print(f"Division = {a/b}")
#     elif op == "%":
#         print(f"Modulus = {a%b}")
#     else:
#         print("Invalid operator")
#
# simple_calculator(25,6,"%")


# def repeat_phrase_with_loop():
#
#     for i in range(75):
#         print("LEARN SCALA PYTHON")
#
#
#     print("Total lines printed:", 75)
#
# repeat_phrase_with_loop()

#
# count = 0
#
# for i in range(75):
#     print("LEARN SCALA PYTHON")
#     count += 1
#
# print("Total lines printed:", count)




# def divisible_by_14():
#     for i in range(120, 361):
#         if i % 14 == 0:
#             print(i,end =" ")
#
# divisible_by_14()


# def sum_of_numbers():
#     sum = 0
#
#     for i in range(60, 171):
#         sum += i
#
#     print(f"Sum of numbers from 60 to 170 is : {sum}")
#
# sum_of_numbers()



# def print_even_numbers():
#     for i in range(350, 501):
#         if i % 2 == 0:
#             print(i, end=" ")
#
# print_even_numbers()


# def print_odd_reverse():
#     for i in range(401, 200, -1):
#         if i % 2 != 0:
#             print(i, end=" ")
#
# print_odd_reverse()


# def count_even_numbers():
#     count = 0
#
#     for i in range(45, 146):
#         if i % 2 == 0:
#             count += 1
#
#     print("Total even numbers:", count)
#
# count_even_numbers()


# def print_alternate_even():
#     for i in range(38, 141, 4):
#         print(i, end=" ")
#
# print_alternate_even()

#
# def print_pattern_product():
#     for i in range(3, 16):
#         print(f"{i} * {i+1} = {i*(i+1)}")
#
# print_pattern_product()

# def sum_even_numbers():
#     sum = 0
#
#     for i in range(280, 481):
#         if i % 2 == 0:
#             sum += i
#
#     print(f"Sum of even numbers = {sum}")
#
# sum_even_numbers()

#
# def print_alphabets():
#     for i in range(ord('a'), ord('z') + 1):               #ord gives ASCII Value
#         print(chr(i), end=" ")                            #chr to convert ASCII value to corresponding characters
#
# print_alphabets()

# def average_series():
# #     total = sum(range(28, 97, 2))
# #     count = len(range(28, 97, 2))
# #
# #     print(f"Average = {total / count}")
# #
# # average_series()

# def sum_of_squares():
#     sum = 0
#
#     for i in range(55, 96, 2):
#         sum += i ** 2
#
#     print(f"Sum of squares = {sum}")
#
# sum_of_squares()

# def print_alternate():
#     for i in range(100):
#         if i % 2 == 0:
#             print("A", end=" ")
#         else:
#             print("B", end=" ")
#
# print_alternate()


# def print_pattern():
#     for i in range(18, 0, -1):
#         print(f"{i}@{i-1}",end=" ")
#
# print_pattern()


# def progressive_250s_series():
#     for i in range(250, 10001, 250):
#         print(i, end=" ")
#
# progressive_250s_series()

# def odd_squares():
#     for i in range(13, 30, 2):
#         print(f"{i}² = {i**2}")
#
# odd_squares()

# def alternating_values_series():
#     for i in range(7):
#         print(6, end=" ")
#         print(12, end=" ")
#
# alternating_values_series()

# def decreasing_multiplication():
#     for i in range(4, -11, -1):
#         print(f"6 * {i} = {6 * i}")
#
# decreasing_multiplication()


# def even_odd_label():
#     for i in range(1, 34, 2):
#         print(f"{i}, even", end=", ")
#
# even_odd_label()

# def factor_of_five_label():
#     for i in range(1, 31):
#         if i % 3 == 0:
#             print("factor of five", end=", ")
#         else:
#             print(i, end=", ")
#
# factor_of_five_label()

# def divisible_by_4_label():
#     for i in range(1, 26):
#         if i % 4 == 0:
#             print("divisible by 4", end=", ")
#         else:
#             print(i, end=", ")
#
# divisible_by_4_label()

# def floating_point_square_series():
#     for i in range(6, 47, 2):
#         num = i / 10
#         print(f"{num:.1f}² = {num**2:.2f}")
#
# floating_point_square_series()


# def infinite_loop():
#     while True:
#         print("Running infinite loop...")
#
# infinite_loop()

def nested_loop_flow():
    for outer in range(1, 4):
        print(f"Outer Loop: {outer}")

        for inner in range(1, 3):
            print(f"Inner Loop: {inner}")

nested_loop_flow()