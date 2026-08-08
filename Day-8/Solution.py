# ==========================================
# PATTERN PROGRAMS – SOLUTIONS
# ==========================================

# ==========================================
# 1️⃣ Star Pattern
# ==========================================

# *
# **
# ***
# ****
# *****

for row in range(1, 6):
    print("*" * row)


# ------------------------------------------

# ==========================================
# 2️⃣ Star Pattern
# ==========================================

# *****
# ****
# ***
# **
# *

for row in range(5, 0, -1):
    print("*" * row)


# ------------------------------------------

# ==========================================
# 3️⃣ Pattern
# ==========================================

# 1
# 2 3
# 4 5 6
# 7 8 9 10
# 11 12 13 14 15
# 16 17 18 19 20 21

num = 1

for row in range(1, 7):
    for col in range(row):
        print(num, end=" ")
        num += 1
    print()

# ------------------------------------------

# ==========================================
# 4️⃣ Pattern
# ==========================================

# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

for row in range(1, 6):
    for col in range(1, row + 1):
        print(col, end=" ")
    print()


# ------------------------------------------

# ==========================================
# 5️⃣ Pattern
# ==========================================

# 12345
# 1234
# 123
# 12
# 1

for row in range(5, 0, -1):
    for col in range(1, row + 1):
        print(col, end="")
    print()

# ------------------------------------------

# ==========================================
# 6️⃣ Pattern
# ==========================================

# 1
# 2 2
# 3 3 3
# 4 4 4 4

for row in range(1, 5):
    for col in range(row):
        print(row, end=" ")
    print()

# ------------------------------------------

# ==========================================
# 7️⃣ Pattern
# ==========================================

# 1
# 2 2
# 3 3 3
# 4 4 4 4

for row in range(1, 5):
    print(" " * (5 - row), end="")
    for col in range(row):
        print(row, end=" ")
    print()

# ------------------------------------------

# ==========================================
# 8️⃣ Pattern
# ==========================================

# 1
# 2 3
# 4 5 6
# 7 8 9 10

num = 1

for row in range(1, 5):
    print(" " * (7 - row), end="")
    for col in range(row):
        print(num, end=" ")
        num += 1
    print()

# ------------------------------------------

# ==========================================
# 9️⃣ Pattern
# ==========================================

# 1
# 1 2 1
# 1 2 3 2 1
# 1 2 3 4 3 2 1

for row in range(1, 5):
    print(" " * (7 - row), end="")
    for col in range(1, row + 1):
        print(col, end=" ")
    for col in range(row - 1, 0, -1):
        print(col, end=" ")
    print()

# ------------------------------------------

# ==========================================
# 🔟 Star Pyramid
# ==========================================

# *
# * *
# * * *
# * * * *
# * * * * *

for row in range(1, 6):
    print("  " * (5 - row), end="")
    for col in range(row):
        print("*", end=" ")
    print()

# ------------------------------------------

# ==========================================
# FINAL LEARNING
# ==========================================

# Pattern programming improves:

# = loop understanding
# = nested loop concepts
# = logic building
# = spacing concepts
# = row-column thinking
# = increment/decrement
# = forward and reverse loops
# = combining loops for symmetrical patterns

# Most important concepts:

# = outer loop → rows
# = inner loop → columns
# = print(end=" ")
# = spacing logic
# = number sequence logic
# = row-based repetition

# ==========================================
