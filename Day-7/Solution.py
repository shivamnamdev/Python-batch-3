# ==========================================
# Python Assignment: For Loop Practice
# SOLUTIONS
# ==========================================
# ------------------------------------------

# ==========================================
# SECTION 1: Basic For Loop Programs
# ==========================================

# 1. Print numbers from 1 to 10

for number in range(1, 11):

    print(number)

# ------------------------------------------


# 2. Print numbers from 10 to 1

for number in range(10, 0, -1):

    print(number)

# ==========================================

# ------------------------------------------
# 3. Print your name 5 times

for count in range(5):

    print("Shivam")

# ==========================================

# ------------------------------------------
# 4. Print even numbers from 1 to 20

for number in range(1, 21):

    if number % 2 == 0:

        print(number)

# ==========================================

# ------------------------------------------
# 5. Print odd numbers from 1 to 20

for number in range(1, 21):

    if number % 2 != 0:

        print(number)
# ------------------------------------------

# ==========================================
# SECTION 2: Number-Based Logic Programs
# ==========================================

# ------------------------------------------
# 6. Print square of numbers from 1 to 10

for number in range(1, 11):

    print(number, "→", number ** 2)

# ==========================================

# ------------------------------------------
# 7. Print cube of numbers from 1 to 5

for number in range(1, 6):

    print(number, "→", number ** 3)

# ==========================================

# ------------------------------------------
# 8. Print multiplication table of 5

for number in range(1, 11):

    print(
        "5 ×",
        number,
        "=",
        5 * number
    )

# ==========================================

# ------------------------------------------
# 9. Print numbers divisible by 3
# between 1 and 30

for number in range(1, 31):

    if number % 3 == 0:

        print(number)

# ==========================================

# ------------------------------------------
# 10. Print sum of numbers from 1 to 10

total = 0

for number in range(1, 11):

    total += number

print("Total Sum:", total)
# ------------------------------------------

# ==========================================
# SECTION 3: String-Based Programs
# ==========================================

# ------------------------------------------
# 11. Print each character of a word

word = "Python"

for character in word:

    print(character)

# ==========================================

# ------------------------------------------
# 12. Count total characters in a word

word = "Programming"

count = 0

for character in word:

    count += 1

print("Total Characters:", count)

# ==========================================

# ------------------------------------------
# 13. Count vowels in a word

word = "Education"

vowel_count = 0

for character in word.lower():

    if character in "aeiou":

        vowel_count += 1

print("Total Vowels:", vowel_count)
# ------------------------------------------

# ==========================================
# SECTION 4: Basic Pattern Programs
# ==========================================

# ------------------------------------------
# 14. Print stars vertically

for star in range(5):

    print("*")

# ==========================================

# ------------------------------------------
# 15. Print 5 stars in one line

for star in range(5):

    print("*", end=" ")

# ------------------------------------------

# ==========================================
# 16. Count Even and Odd Numbers
# ==========================================

even_count = 0

odd_count = 0

for count in range(10):

    number = int(input("Enter number: "))

    if number % 2 == 0:

        even_count += 1

    else:

        odd_count += 1

print("Total even numbers:", even_count)

print("Total odd numbers:", odd_count)

# ------------------------------------------

# ==========================================
# 17. Sum of Only Positive Numbers
# ==========================================

total = 0

for count in range(7):

    number = int(input("Enter number: "))

    if number > 0:

        total += number

print("Sum of positive numbers:", total)
# ------------------------------------------

# ==========================================
# 18. Find Largest Number (Without max())
# ==========================================

largest = None

for count in range(5):

    number = int(input("Enter number: "))

    if largest is None or number > largest:

        largest = number

print("Largest number:", largest)
# ------------------------------------------

# ==========================================
# 19. Count Vowels and Consonants
# ==========================================

word = input("Enter a word: ")

vowels = 0

consonants = 0

for character in word.lower():

    if character.isalpha():

        if character in "aeiou":

            vowels += 1

        else:

            consonants += 1

print("Total vowels:", vowels)

print("Total consonants:", consonants)
# ------------------------------------------

# ==========================================
# 20. Print Prime Numbers from 1 to N
# ==========================================

n = int(input("Enter value of N: "))

for number in range(2, n + 1):

    is_prime = True

    for value in range(2, number):

        if number % value == 0:

            is_prime = False

            break

    if is_prime:

        print(number)


# ==========================================
# FINAL LEARNING
# ==========================================

# Important concepts learned:
# = for loop
# = range()
# = conditions
# = even/odd checking
# = arithmetic operations
# = string traversal
# = counting logic
# = pattern printing
# = nested conditions
# = prime numbers
# = Armstrong numbers
# = reversing numbers
# = boolean flags
# = input validation

# ==========================================
