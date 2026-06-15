# def print_numbers_1_10():
#     for i in range (1,11):
#         print(i)
#
# print_numbers_1_10()

# def even_numbers():
#     for i in range(2, 11, 2):
#         print(i, end=" ")
#
# even_numbers()

# def squares_of_num():
#     for i in range(1, 8):
#         print(f"Square of {i} = {i**2}")
#
# # Function call
# squares_of_num()

# def print_string(word):
#     for letter in word:
#         print(letter)
#
# print_string("HELLO")

# def print_elements():
#
#     ls= [10, 20, 30, 40, 50]
#
#     for element in ls:
#         print(element)
# print_elements()

# def multiplication_table(num):
#     for i in range (1,11,1):
#
#         print(f"{num} * {i} = {num * i}")
#
# multiplication_table(4)


# def reverse_order():
#
#     for i in range(10,0,-1):
#         print(i)
#
# reverse_order()

#
# def sum_of_numbers():
#     numbers = [3, 5, 7, 9]
#     sum = 0
#
#     for num in numbers:
#         sum += num
#
#     print(f"Sum of given numbers = {sum}")
#
# sum_of_numbers()

# def Vowels():
#     Word = "education"
#
#     for char in Word:
#         if char in "aeiou":
#             print(char)
#
# Vowels()


# def character_in_string_check():
#     Word = "scala"
#
#     if Word.__contains__("s"):
#         print(f"{Word} -> s")
#
# character_in_string_check()

# def print_even_indexed_characters():
#     Word = "Students"
#
#     for i in range(0, len(Word), 2):
#         print(Word[i])
#
# print_even_indexed_characters()

# def print_numbers_5_to_1():
#     num = 5
#
#     while num >= 1:
#         print(num)
#         num -= 1
#
# print_numbers_5_to_1()

# def odd_numbers():
#     num = 1
#     count = 0
#
#     while count < 6:
#         print(num)
#         num += 2
#         count += 1
#
#
# odd_numbers()

# def Characters():
#     text = "Education"
#     i = 0
#
#     while i < len(text):
#         print(text[i],end=" ")
#
#         i += 1
#
# Characters()

# def sum_of_numbers():
#     num = 1
#     sum = 0
#
#     while num <= 20:
#         sum += num
#         num += 1
#
#     print("Sum =", sum)
#
#
# sum_of_numbers()


# def factorial_of_6():
#     num = 6
#     factorial = 1
#
#     while num > 0:
#         factorial *= num
#         num -= 1
#
#     print(f"Factorial of 6 is {factorial} ")
#
# factorial_of_6()


# def reverse_string():
#     sample_data = "code"
#     reverse = ""
#     i = len(sample_data) - 1
#
#     while i >= 0:
#         reverse += sample_data[i]
#         i -= 1
#
#     print(reverse)
#
# reverse_string()

# def count_of_digits():
#     num = 12345
#     count = 0
#
#     while num > 0:
#         count += 1
#         num //= 10
#
#     print("Number of digits =", count)
#
#
# count_of_digits()

# def Elements_of_lists():
#     ls = ["Mumbai","Pune","Chennai","MP"]
#     i = 0
#
#     while i < len(ls):
#         print(ls[i])
#         i += 1
#
#
# Elements_of_lists()


# def print_numbers_1_to_20():
#     num = 1
#
#     while num <= 20:
#         if num % 3 == 0:
#             num += 1
#             continue
#
#         print(num,end=" ")
#         num += 1
#
#
#
# print_numbers_1_to_20()


# def print_numbers():
#     num = 1
#
#     while num <= 20:
#         if num % 3 != 0:
#             print(num,end=" ")
#
#         num += 1
#
# print_numbers()


# def print_even_squares():
#     num = 2
#
#     while num <= 10:
#         print(num * num)
#         num += 2
#
# print_even_squares()

# def print_pattern():
#     for i in range(1, 5):
#         print("#" * i)
#
#
# print_pattern()


# def print_pattern():
#     i = 1
#
#     while i <= 4:
#         j = 1
#
#         while j <= i:
#             print(j, end="")
#             j += 1
#
#         print()
#         i += 1
#
#
# print_pattern()

# def print_numbers():
#     for i in range(10, 101, 10):
#         print(i)
#
#
# print_numbers()

# def print_numbers():
#     for i in range(1, 31):
#         if i == 17:
#             break
#         print(i, end=" ")
#
#
# print_numbers()

def print_numbers():
    for i in range(1, 11):
        if i == 5 or i == 6:
            continue
        print(i)


print_numbers()