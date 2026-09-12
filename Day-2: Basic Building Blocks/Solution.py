# ================================
# Operators and Built-in Functions
# ================================
# --------------------------------
# 1. Take a name as input and print it
name = input("Enter your name: ")
print("Name:", name)

# --------------------------------

# 2. Take age as input and print value and type
age = input("Enter your age: ")
print("Age:", age)
print("Type of age:", type(age))  # always string

# --------------------------------

# 3. Take a number as input, convert it into integer, and print its type
num = input("Enter a number: ")
num = int(num)
print("Number:", num)
print("Type of number:", type(num))

# --------------------------------

# 4. Print the type of each variable
a = 10
b = 5.5
c = "Python"
d = True

print("Type of a:", type(a))  # int
print("Type of b:", type(b))  # float
print("Type of c:", type(c))  # str
print("Type of d:", type(d))  # bool

# --------------------------------

# 5. Membership operator (in)
print("Is 'a' in 'Python'? ->", "a" in "Python")   # False
print("Is 'Py' in 'Python'? ->", "Py" in "Python") # True

# --------------------------------

# 6. Observe 'is' with integers
a = 10
b = 10
print("a is b:", a is b)  # True (same memory for small integers)

# --------------------------------

# 7. Difference between == and is
a = [1, 2]
b = [1, 2]

print("a == b:", a == b)  # True (values same)
print("a is b:", a is b)  # False (different objects)

# --------------------------------

# 8. Difference between is not and !=
a = [1]
b = [1]

print("a != b:", a != b)        # False (values same)
print("a is not b:", a is not b) # True (different objects)

# --------------------------------

# 9. Identity for strings
s1 = "Python"
s2 = "Python"

print("s1 is s2:", s1 is s2)  # Usually True (string interning)

# Check whether two variables point to same object
a = input("Enter value: ")
b = a

print("a is b:", a is b)  # True (same reference)



# Key Concepts:
# - input() always returns string
# - == compares values
# - is compares memory (object identity)
# - in checks membership
# - type() gives data type

# --------------------------------
# 1️⃣ Arithmetic + Precedence

a = 8
b = 3
c = 2

print(a + b * c - a // b)

## ✅ Step-by-step (operator precedence)

# Order:

# 1. `*` and `//`
# 2. `+` and `-`

### Step 1: Multiplication

b * c = 3 * 2 = 6

### Step 2: Floor Division

a // b = 8 // 3 = 2

# 👉 `//` means **floor division** → removes decimal → 2.66 → 2

### Step 3: Final expression


a + 6 - 2 = 8 + 6 - 2 = 12

## ✅ Output:

12
# --------------------------------
# 2️⃣ Arithmetic (Mix Operations)


x = 10
y = 4

print(x % y + x // y * 2)

## ✅ Step-by-step

### Step 1: Modulus


x % y = 10 % 4 = 2


# 👉 `%` gives **remainder**

### Step 2: Floor division


x // y = 10 // 4 = 2


### Step 3: Multiplication

2 * 2 = 4

### Step 4: Addition

2 + 4 = 6

## ✅ Output:

6
# --------------------------------
# 3️⃣ Logical Operator (Truthy/Falsy)

print("" or 0 or False or "Python")
print("Hello" and "World")


## ✅ First line


"" or 0 or False or "Python"


# 👉 Python checks left → right
# Returns **first truthy value**

# * `""` → False
# * `0` → False
# * `False` → False
# * `"Python"` → True ✅

## Output:

"Python"

## ✅ Second line

"Hello" and "World"

# 👉 `and` returns **last value if all are True**

# * `"Hello"` → True
# * `"World"` → True

## Output:

"World"

## 🧠 Why not True/False?

# Python returns **actual value**, not just boolean.

# --------------------------------
# 4️⃣ Comparative + Logical

a = 5
b = 10
c = 5

print(a == c and b > a or b == c)

## ✅ Step-by-step

### Step 1: Comparisons

a == c # → 5 == 5 → True
b > a # → 10 > 5 → True
b == c # → 10 == 5 → False

### Step 2: Logical precedence

# Order:

# 1. `and`
# 2. `or`

### Step 3:

True and True # → True
True or False # → True


## ✅ Output:

True
# --------------------------------
# 5️⃣ Logical + `not`

print(not 0)
print(not "Hello")
print(not "")

## ✅ Evaluate one by one

### 1. `not 0`

# `0` → False
# `not False` → True

# 👉 Output:

True

### 2. `not "Hello"`

#  Non-empty string → True
#  `not True` → False

# 👉 Output:

False

### 3. `not ""`

#  Empty string → False
#  `not False` → True

# 👉 Output:

True

# 🧠 Truthy vs Falsy (Core Concept)

## ❌ Falsy values:

# * `0`
# * `""` (empty string)
# * `False`
# * `None`

## ✅ Truthy:

# * Any non-zero number
# * Any non-empty string


# 🔥 Final Insight (Very Important)

# * `or` → returns **first True value**
# * `and` → returns **last value if all True**
# * `not` → flips True ↔ False
