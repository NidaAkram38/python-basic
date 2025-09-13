                                  # Python Logic Building Practice Questions - Set 1

# # 1. Count Even and Odd Numbers in an Array
# # Given an array of integers, count how many numbers are even and how many are odd.

# num = [2, 3, 4, 5, 6, 7, 8, 10, 11, 13, 12, 14]
# even = 0
# odd = 0
# for n in num:
#     if n % 2 == 0:
#         even += 1
#     else:
#         odd += 1
# print("Even numbers:", even)
# print("Odd numbers:", odd)


# # 2. Find Maximum Consecutive Zeros
# # Given a binary array, find the maximum number of consecutive 0s.

# arr = [1, 0, 0, 1, 0, 0, 0, 0, 1, 0]
# def max_consecutive_zeros(arr):
#     count_current = 0
#     count_max = 0
#     for i in arr:
#         if i == 0:
#             count_current += 1
#         elif i != 0 and count_current > count_max:
#             count_max = count_current
#             count_current=0
#         else:
#             count_current = 0
#     return count_max
# result = max_consecutive_zeros(arr)
# print("Max consecutive zeros:", result)


# # 3. Longest Substring Without Repeating Characters
# # Given a string, find the length of the longest substring without repeating characters.

# def unique_char(word):
#     word = word.lower()        ### sab letters ko lowercase mein kar do
#     word = word.replace(" ", "")  ### spaces hata do
#     return len(set(word)) == len(word)
# string = ["Nida", "Usman", "Abdullah", "Abdul Rehaman Khan", "Warisha", "Abiha", "Aniyoe"]
# longest = ""

# for name in string:
#     if unique_char(name) and len(name) > len(longest):
#         longest = name
# for name in string:
#     if name == longest:
#         print(f"longest name with unique char: '{longest}' (length: {len(longest)})")
#     elif not unique_char(name):
#         print(f"no name with unique char in: '{name}'")
        

# # 4. Find the First Non-Repeating Character in a String
# # Return the index of the first character that doesn't repeat in a string.

# def non_repeat_char(s):
#     count = {}
#     for char in s:
#         if char in count:
#             count[char] += 1
#         else:
#             count[char] = 1
#     for index ,char in enumerate(s):
#         if count[char] == 1:
#              return index
#     print("no repeating char")
#     return -1
# s=input("Enter a string:")
# result = non_repeat_char(s)
# print("index of 1st non-repeating char:", result)


# # 5. Check If Array Is Monotonic
# # Return True if the array is monotonic (entirely non-increasing or non-decreasing).

# def monotonic(arr):      ### Monotonic array wo hota hai jo ya to increase karta jaye (non-decreasing) ya decrease karta jaye (non-increasing).
#     inc = dec = True
#     for i in range(1,len(arr)):
#         if arr[i] > arr[i-1]:
#             dec = False
#         elif arr[i] < arr[i-1]:
#             inc = False
#     return inc or dec
# print(monotonic([1,2,4,3]))   ### pehle barh raha hai, phir kam raha hai , not monotonic
# print(monotonic([1,2,4,5]))
# print(monotonic([1,3,4,6]))


# # 6. Count Number of Vowels in a String
# # Write a function that counts how many vowels are in a given string.

# vowels = ['a', 'e', 'i', 'o', 'u']
# string = input("Enter a string: ")
# count = 0
# for ch in string:
#     if ch.lower() in vowels:
#         count += 1
# print("total vowels:", count)


# # 7. Check if Two Arrays Are Equal (after sorting)
# # Given two arrays, return True if both have the same elements after sorting.

# arr1 = [1, 2, 3, 5, 7]
# arr2 = [3, 2, 1, 6, 3]
# arr1.sort()
# arr2.sort()
# if arr1 == arr2:
#     print("arrays are equal")
# else:
#     print("arrays are not equal")


# # 8. Count the Number of Words in a Sentence
# # Write a function that returns the number of words in a string (words separated by space).

# sentence = input("Enter a sentence: ")
# words = sentence.split()      ### spilt() is string method that breks sentence in individual words
# print("total words in sentence:", len(words))


# # 9. Check if a Number is Prime
# # Write a function to check if a given number is prime.

# num = int(input("Enter a number: "))
# if num < 2:
#     print("it is not prime")
# else:
#     for i in range(2, num):
#         if num % i == 0:
#             print("num is not prime")
#             break
#     else:
#         print("num is prime")


# # 10. Find the Majority Element in an Array
# # Return the element that appears more than n/2 times in the array (guaranteed to exist).

# arr = [7, 4, 6, 6, 2, 5, 6]
# n = len(arr)
# d = {}
# for num in arr:
#     if num in d:
#         d[num] += 1
#     else:
#         d[num] = 1
#     if d[num] > n % 2:
#         print("Majority element is:", num)
#         break


                                  # Python Logic Building Practice Questions - Set 2
                                  
# # Question 1: Find the Missing Number in a Sequence
# # You are given a list of numbers from 1 to 100 with one number missing. Find the missing number.

# num = list(range(1, 101))
# num.remove(64) 
# def find_missing(number):
#     expected_sum = 100 * 101 // 2
#     actual_sum = sum(number)
#     return expected_sum - actual_sum 
# print("Missing number:", find_missing(num))


# # Question 2: Check if Two Strings are Anagrams
# # Write a function that checks whether two given strings are anagrams of each other.

# def anagram(a, b):          ### 2 words having same letters but different order
#     a = a.replace(" ", "").lower()   
#     b = b.replace(" ", "").lower()   
#     a_list = list(a)                 ### convert string to list of char
#     b_list = list(b)
#     a_list.sort()                    
#     b_list.sort()
#     if a_list == b_list:             
#         return True
#     else:
#         return False
# print(anagram("listen", "silent"))
# print(anagram("hello", "world"))
# print(anagram("care", "race"))


# # Question 3: Reverse Only Vowels in a String
# # Given a string, reverse only the vowels and return the resulting string.

# def reverse_vowels(s):
#     vowels = "aeiouAEIOU"
#     s = list(s)
#     i, j = 0, len(s) - 1     ### i start se shuru karega aur j end se
#     while i < j:   ### jb tak i aur j ek doosre ko cross nahi karte,loop chalta rahega
#         if s[i] not in vowels:
#             i += 1
#         elif s[j] not in vowels:
#             j -= 1
#         else:
#             s[i], s[j] = s[j], s[i]
#             i += 1
#             j -= 1
#     return "".join(s)
# print(reverse_vowels("hello"))
# print(reverse_vowels("AEIOU"))
# print(reverse_vowels("usman"))


# # Question 4: Check for Palindrome Number
# # Write a function to check if a given integer is a palindrome (reads the same backward).

# def is_palindrome(num):
#     return str(num) == str(num)[::-1]
# print(is_palindrome(121))
# print(is_palindrome(123))
# print(is_palindrome(525))


# # Question 6: Count the Frequency of Each Character
# # Take a string input and count the frequency of each character without using collections module.

# def count_chars(s):
#     freq = {}
#     for ch in s:
#         if ch in freq:
#             freq[ch] += 1
#         else:
#             freq[ch] = 1
#     return freq
# print(count_chars("orange"))
# print(count_chars("banana"))
# print(count_chars("apple"))


# # Question 7: Find All Pairs with Given Sum
# # Write a function to find all pairs in an array that add up to a specific target sum.

# def find_pairs(arr, target):
#     nums = set()
#     pairs = []
#     for num in arr:
#         diff = target - num
#         if diff in nums:
#             pairs.append((diff, num))
#         nums.add(num)
#     return pairs
# print(find_pairs([1, 2, 3, 4, 5, 6, 7], 8))


# # Question 8: Implement a Basic Calculator
# # Create a calculator that can perform +, -, *, / operations. Take expression as a string input (e.g., '3 + 5').

# num1=int(input("Enter the value1:"))
# num2=int(input("Enter the value2:"))
# opr=input("Enter the operation:")
# if opr=="+":
#     print(num1+num2)
# elif opr=="-":
#     print(num1-num2)
# elif opr=="*":
#     print(num1*num2)
# elif opr=="/":
#     print(num1/num2)
# else:
#     print("Invalid operation")
    

# # Question 9: Second Largest Element in List
# # Write code to find the second largest number in a list without using sort().

# def second_largest(arr):
#     if len(arr) < 2:
#         return None      ### atleast 2 elements needed
#     first = second = arr[0]
#     for num in arr[1:]:
#         if num > first:
#             second = first
#             first = num
#         elif num > second and num != first:
#             second = num
#         else:
#             continue     ### num is not greater than first or second, ya same hai
#     if first == second:
#         return None      ### agar sare elements same hain ya second largest mila hi nahi
#     else:
#         return second
# print(second_largest([7, 1, 9, 3, 9, 5]))


# # Question 10: Replace Spaces with Underscores
# # Given a sentence, replace all the spaces with underscores without using built-in replace().

# def replace_spaces(sen):
#     result = ""
#     for ch in sen:
#         if ch == " ":
#             result += "_"
#         else:
#             result += ch
#     return result
# print(replace_spaces("hello from nida"))


                                   # Python Logic Building Practice Questions - Set 3
                                   
# # Question 1: Digit Sum Until One Digit Remains
# # Given a number, repeatedly add its digits until the result is a single digit. Example: 987 -> 9+8+7=24 ->
# # 2+4=6

# def digit_sum(num):
#     while num >= 10:
#         total = 0
#         while num > 0:
#             total += num % 10
#             num = num // 10
#         num = total
#     return num
# print(digit_sum(987))
# print(digit_sum(786))


# # Question 2: Check if a Number is a Power of 2
# # Write a function that returns True if a number is a power of 2, else False.

# def is_power_of_2(n):
#     if n <= 0:
#         return False
#     else:
#         while n % 2 == 0:
#             n = n // 2
#         if n == 1:
#             return True
#         else:
#             return False
# num = int(input("Enter a number: "))
# if is_power_of_2(num):
#     print("yes, it is a power of 2")
# else:
#     print("no, it is not a power of 2")


# # Question 3: Generate Fibonacci Series Up to N Terms
# # Take input n and print first n terms of the Fibonacci series.(Fibonacci series ek number sequence hoti hai jisme:  
# # Pehle 2 numbers hamesha 0 aur 1 hote hain. Uske baad har number previous 2 numbers ka sum hota hai)

# def fibo(n):
#     a = 0
#     b = 1
#     count = 0
#     if n <= 0:
#         print("Please enter a positive integer")
#     elif n == 1:
#         print(a)
#     else:
#         print("Fibonacci sequence:")
#         while count < n:
#             print(a, end=" ")
#             next_num = a + b
#             a = b
#             b = next_num
#             count += 1
# num = int(input("Enter the number of terms: "))
# fibo(num)


# # Question 4: Find Common Elements in Two Lists
# # Without using set, write a function to find common items in two given lists.

# def common_ele(a, b):
#     result = []
#     for i in a:
#         if i in b:
#             result.append(i)
#         else:
#             print(f"{i} not found in second list,skip")
#     return result
# a = [1, 2, 3, 4, 5, 4, 20]
# b = [4, 4, 6, 7, 9, 17, 20]
# print(common_ele(a, b))


# # Question 5: Find the Longest Word in a Sentence
# # Input: A sentence. Output: The longest word and its length.

# def longest_word(sentence):
#     words = sentence.split()
#     longest = ""
#     for word in words:
#         if len(word) > len(longest):
#             longest = word
#         else:
#             print(f"'{word}' its length is: '{len(word)}'")
#     return longest, len(longest)
# sentence = input("Enter a sentence: ")
# word, length = longest_word(sentence)
# print(f"Longest word is: '{word}'")
# print(f"Length of longest word: {length}")


# # Question 6: Print a triangle Pattern of Stars

# def triangle(n):
#     for i in range(1, n + 1):
#         spaces = n - i
#         stars = 2 * i - 1
#         print(" " * spaces + "*" * stars)
# n = int(input("Enter number of rows: "))
# triangle(n)


# # Question 7: Move All Zeros to End of List
# # Input: [0, 1, 0, 3, 12]. Output: [1, 3, 12, 0, 0] (maintain order of non-zero elements).

# def move_zeros(arr):
#     result = []
#     zero_count = 0
#     for i in arr:
#         if i != 0:
#             print(f"{i} is non-zero,added to result")
#             result.append(i)
#         else:
#             print(f"{i} is zero,counting for later")
#             zero_count += 1
#     result += [0] * zero_count
#     return result
# arr=[0, 1, 0, 3, 12]
# print(move_zeros(arr))

# # Question 8: Capitalize First Letter of Each Word (No Built-in)
# # Take a string input and capitalize only the first letter of each word manually.

# def capitalize_words(text):
#     result = ""
#     new_word = True
#     for ch in text:
#         if ch == " ":
#             new_word = True
#             result += ch
#         elif new_word:
#             result += ch.upper()
#             new_word = False
#         else:
#             result += ch.lower()
#     return result
# print(capitalize_words("hello nida how are you"))


# # Question 9: Check for Armstrong Number. Armstrong number wo number hota hai jo apne digits 
# # ke cube (ya power of digits) ka sum ke barabar hota hai
# # An Armstrong number is equal to the sum of its digits raised to the power of number of digits. Example: 153
# # -> 1³ + 5³ + 3³ = 153

# def is_armstrong(n):
#     digits = [int(i) for i in str(n)]
#     power = len(digits)
#     print("Digits:", digits)
#     print("Power:", power)
#     total = 0
#     for i in digits:
#         total += i ** power
#         print(f"{i}^{power} =", i ** power)
#     print("Sum of powers:", total)
#     return total == n
# print(is_armstrong(153))   
# print(is_armstrong(1567)) 
# print(is_armstrong(370))   
# print(is_armstrong(123))   


# # Question 10: Custom Range Generator
# # Write a function my_range(start, end, step) that works like range() and returns a list.

# def my_range(start, end, step):
#     result = []
#     while start < end:
#         result.append(start)
#         start += step
#     return result
# print(my_range(5, 20, 5))


# # Question 11: Sum of Even and Odd Digits Separately
# # Take an integer input and calculate the sum of even and odd digits separately.

# num = input("Enter the numbers: ")
# even_sum = odd_sum = 0
# for i in range(len(num)):
#     digit = int(num[i])
#     if digit % 2 == 0:
#         even_sum = even_sum + digit
#     else:
#         odd_sum = odd_sum + digit
# print("Even digits ka sum:", even_sum)
# print("Odd digits ka sum:", odd_sum)


# # Question 12: Count Vowels and Consonants
# # Write a function to count vowels and consonants in a given string.

# def vow_cons(s):
#     vowels = "aeiouAEIOU"
#     v = c = 0
#     for ch in s:
#         if ch.isalpha():
#             if ch in vowels:
#                 v += 1
#             else:
#                 c += 1
#     return v, c
# s = "nfciet multan"
# v, c = vow_cons(s)
# print("Vowels:", v)
# print("Consonants:", c)


# # Question 13: Find Duplicate Elements
# # Given a list, identify all the duplicate elements without using set or collections.

# def find_dup(lst):
#     dup = []
#     for i in range(len(lst)):
#         for j in range(i+1, len(lst)):
#             if lst[i] == lst[j] and lst[i] not in dup:
#                 dup.append(lst[i])
#             else:
#                 continue
#     return dup
# nums = [1, 2, 3, 2, 4, 5, 1, 6, 5]
# print("Duplicates:", find_dup(nums))


# # Question 16: Find Factorial Without Recursion
# # Write a function to find factorial of a number using loop.

# def factorial(n):
#     result = 1
#     if n == 0 or n == 1:
#         return 1
#     else:
#         for i in range(2, n + 1):
#             result *= i
#         return result
# num = int(input("Enter a number: "))
# fact = factorial(num)
# print("Factorial of", num, "is:", fact)


# # Question 22: Check if Two Lists are Identical
# # Return True if both lists have same elements in same order.

# def are_identical(a, b):
#     return a == b
# a = [1, 2, 3]
# b = [1, 2, 3]
# print(are_identical(a, b))


