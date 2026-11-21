# ==========================================
# OOP Assignment Solutions
# (Constructor + Polymorphism + Overriding)
# ==========================================

# NOTE: The assignment refers to "given" classes (student_database, Student,
# Teacher, Math, Math2) that were not included in the sheet. Standard
# classroom versions of them are written below so every program runs.


# ------------------------------------------

# Program 1: Constructor Behavior & Default Values

class student_database:
    # Class variables (shared by all objects)
    name = "Unknown"
    course = "Python"

    # Constructor with default parameters
    def __init__(self, name=None, course=None):
        # Create instance variables only when values are passed
        if name is not None:
            self.name = name
        if course is not None:
            self.course = course


student1 = student_database("Aman", "Java")
student2 = student_database("Riya", "AI/ML")
student3 = student_database("Karan", "DevOps")
student4 = student_database()          # no values

students = [student1, student2, student3, student4]

for s in students:
    print(s.name, "-", s.course)

# Output:
# Aman - Java
# Riya - AI/ML
# Karan - DevOps
# Unknown - Python

# Q1. What values does the 4th object get?
# Ans: name = "Unknown" and course = "Python".
#      No values were passed, so name and course stay None and no
#      instance variables are created. Python then looks up the class
#      and finds the class variables "Unknown" and "Python".
#
# Q2. Why does it not fail?
# Ans: The constructor has default parameters (name=None, course=None),
#      so calling student_database() with no arguments is allowed.
#      When an attribute is missing on the object, Python falls back to
#      the class variable instead of raising an error.

# ------------------------------------------

# Program 2: Instance vs Class Variable Deep Understanding

print(student1.name)             # Aman    -> instance variable
print(student_database.name)     # Unknown -> class variable

# Update the class variable
student_database.course = "Data Science"

for s in students:
    print(s.name, "-", s.course)

# Output:
# Aman - Java
# Riya - AI/ML
# Karan - DevOps
# Unknown - Data Science

# Q1. Which objects got updated?
# Ans: Only student4.
#
# Q2. Which did NOT change?
# Ans: student1, student2 and student3.
#
# Q3. Why?
# Ans: student1 to student3 have their own instance variable "course"
#      (created in __init__). An instance variable hides the class variable,
#      so changing the class variable does not affect them.
#      student4 has no instance variable, so it reads the class variable
#      and sees the new value "Data Science".
#      Lookup order: object first -> then class.

# ------------------------------------------

# Program 3: Polymorphism Using Loop

class Student:
    def show(self):
        print("I study in the class")


class Teacher:
    def show(self):
        print("I teach the class")


class Admin:
    def show(self):
        print("I manage the system")


people = [Student(), Teacher(), Admin()]

for person in people:
    person.show()

# Output:
# I study in the class
# I teach the class
# I manage the system

# Q1. How does the same method behave differently?
# Ans: Every class has its own show() method. The loop calls the same
#      name, person.show(), but Python runs the version that belongs to
#      that object's class. This is polymorphism: one interface,
#      many behaviours. (This style is also called "duck typing".)
#
# Q2. What would happen if one class doesn't have show()?
# Ans: Python raises AttributeError when the loop reaches that object, e.g.
#      AttributeError: 'Guest' object has no attribute 'show'
#      The objects before it still print, then the program stops.

class Guest:
    pass

try:
    for person in [Student(), Guest()]:
        person.show()
except AttributeError as e:
    print("Error:", e)

# ------------------------------------------

# Program 4: Method Overriding Behavior (same method name in the same class)

class Math:
    def add(self, a, b, c):
        return a + b + c

    def add(self, a, b):          # same name -> replaces the first add()
        return a + b


m = Math()
print(m.add(2, 3))                # 5

# Q1. Will this work or give an error?
# Ans: It works and prints 5.
#      (But m.add(2, 3, 4) would raise TypeError, because the 3-argument
#      version no longer exists.)
#
# Q2. Which method is actually executed?
# Ans: The LAST one defined: add(self, a, b).
#
# Q3. Why did the first method not run?
# Ans: A class body is executed top to bottom, like normal code.
#      "def add" creates the name add. The second "def add" assigns a new
#      function to the same name, so the first one is overwritten and lost.
#      Python keeps one entry per name, so the last definition wins.

# ------------------------------------------

# Program 5: Method Overloading (Python Way)

class Math2:
    # Default parameter -> works with 2 or 3 values
    def add(self, a, b, c=0):
        return a + b + c

    # *numbers -> works with any number of values
    def multiply(self, *numbers):
        result = 1
        for n in numbers:
            result = result * n
        return result


a = Math2()
print(a.add(2, 3))                # 5
print(a.add(2, 3, 4))             # 9

m = Math2()
print(m.multiply(2, 3))           # 6
print(m.multiply(2, 3, 4, 5))     # 120

# Q1. How is add() working with different inputs?
# Ans: There is only ONE add() method. The third parameter c has a
#      default value of 0. With 2 arguments, c becomes 0. With 3 arguments,
#      c takes the value passed. One method handles both cases.
#
# Q2. What is the role of the default parameter?
# Ans: It makes a parameter optional. If the caller skips it, the default
#      value is used. This lets one method act like several overloaded
#      methods.
#
# Q3. How does *numbers help in flexibility?
# Ans: *numbers collects any number of positional arguments into a tuple,
#      e.g. multiply(2, 3, 4, 5) -> numbers = (2, 3, 4, 5).
#      The method can handle 1, 2 or 100 values without changing the code.


# ==========================================
# MINI PROJECT ASSIGNMENT
# Banking System Using OOP + Inheritance
# ==========================================

# ------------------------------------------

# STEP 1: Base Class

class BankAccount:
    def __init__(self, customer_name, balance=0):
        self.customer_name = customer_name
        self.balance = balance

    def deposit(self, amount):
        self.balance = self.balance + amount
        print(f"{amount} deposited")

    def withdraw(self, amount):
        # Normal rule: you cannot withdraw more than you have
        if amount > self.balance:
            print("Insufficient balance!")
        else:
            self.balance = self.balance - amount
            print(f"{amount} withdrawn")

    def show_balance(self):
        print(f"Customer: {self.customer_name} | Balance: {self.balance}")

# ------------------------------------------

# STEP 2: Single Inheritance

class SavingsAccount(BankAccount):
    def add_interest(self):
        interest = self.balance * 5 / 100
        self.balance = self.balance + interest
        print(f"Interest added: {interest}")

# ------------------------------------------

# STEP 3: Method Overriding

class CurrentAccount(BankAccount):
    OVERDRAFT_LIMIT = -500

    # Overrides BankAccount.withdraw()
    def withdraw(self, amount):
        if self.balance - amount < self.OVERDRAFT_LIMIT:
            print("Overdraft limit exceeded!")
        else:
            self.balance = self.balance - amount
            print(f"{amount} withdrawn")

# ------------------------------------------

# STEP 4: Multilevel Inheritance
# BankAccount -> SavingsAccount -> PremiumSavings

class PremiumSavings(SavingsAccount):
    def add_bonus(self):
        bonus = 100
        self.balance = self.balance + bonus
        print(f"Bonus added: {bonus}")

# ------------------------------------------

# STEP 5: Hierarchical Inheritance
# BankAccount is the parent of SavingsAccount, CurrentAccount and SalaryAccount

class SalaryAccount(BankAccount):
    def credit_salary(self, amount):
        self.deposit(amount)          # reuse the parent method
        print("Salary credited")

# ------------------------------------------

# STEP 6: Multiple Inheritance

class Loan:
    # Used together with an account class, which provides self.balance
    def take_loan(self, amount):
        self.balance = self.balance + amount
        print(f"Loan approved: {amount}")


class SmartAccount(SavingsAccount, Loan):
    def features(self):
        print("Smart Account: Savings + Loan")

# ------------------------------------------

# STEP 7: Testing

print("\n--- Savings Account ---")
sa = SavingsAccount("Aman", 1000)
sa.deposit(500)
sa.withdraw(200)
sa.add_interest()
sa.show_balance()                 # 1365.0

print("\n--- Current Account ---")
ca = CurrentAccount("Riya", 300)
ca.withdraw(700)                  # balance becomes -400 (allowed)
ca.withdraw(200)                  # -600 would cross -500 -> blocked
ca.show_balance()                 # -400

print("\n--- Premium Savings ---")
ps = PremiumSavings("Karan", 2000)
ps.add_interest()
ps.add_bonus()
ps.show_balance()                 # 2200.0

print("\n--- Salary Account ---")
sal = SalaryAccount("Neha")
sal.credit_salary(50000)
sal.withdraw(10000)
sal.show_balance()                # 40000

print("\n--- Smart Account ---")
sm = SmartAccount("Vikram", 5000)
sm.features()
sm.take_loan(20000)
sm.add_interest()
sm.show_balance()                 # 26250.0

# ------------------------------------------

# CONCEPT QUESTIONS

# 1. Which class is the parent class for all accounts?
# Ans: BankAccount.
#
# 2. Which inheritance type is used in SavingsAccount?
# Ans: Single inheritance (one child, one parent: BankAccount).
#
# 3. Which class demonstrates Method Overriding?
# Ans: CurrentAccount. It redefines withdraw() with an overdraft rule.
#
# 4. Why is PremiumSavings called Multilevel Inheritance?
# Ans: It inherits in a chain: BankAccount -> SavingsAccount -> PremiumSavings.
#      PremiumSavings gets deposit() from its grandparent, add_interest()
#      from its parent, and adds its own add_bonus().
#
# 5. Which class demonstrates Multiple Inheritance?
# Ans: SmartAccount, which inherits from both SavingsAccount and Loan.
#
# 6. What is the benefit of inheritance in this project?
# Ans: deposit(), withdraw(), show_balance() and the constructor are
#      written once in BankAccount and reused by every account type.
#      Each child only adds what is special about it. Less code,
#      fewer bugs, and a fix in the parent reaches every child.
#
# 7. Why do banks reuse the base structure instead of rewriting everything?
# Ans: Every account shares the same core (owner, balance, deposit,
#      balance check). Reusing it keeps rules consistent across products,
#      makes new account types fast to launch, and means one tested
#      core instead of many copies that can drift apart.
#
# 8. What is the role of the constructor in BankAccount?
# Ans: __init__ runs automatically when an account is created. It sets
#      the starting state: customer_name and balance (default 0).
#      Every child class inherits it, so all accounts start correctly.
#
# 9. What happens if SmartAccount inherits from two classes?
# Ans: It gets the methods of both: deposit/add_interest from
#      SavingsAccount and take_loan from Loan. If both parents had a method
#      with the same name, Python picks one using the MRO
#      (Method Resolution Order): left to right, here SavingsAccount first.

print("\nMRO of SmartAccount:", [c.__name__ for c in SmartAccount.__mro__])
# ['SmartAccount', 'SavingsAccount', 'BankAccount', 'Loan', 'object']

# 10. Explain the real-world use of:
# Ans: Inheritance  -> all account types (savings, current, salary) share
#                      a common "account" base with balance and deposit.
#      Overriding   -> a current account changes the withdraw rule to
#                      allow overdraft, while keeping the same method name.
#      Polymorphism -> the bank can loop over all accounts and call
#                      withdraw() or show_balance(); each account
#                      responds according to its own rules.

# ------------------------------------------

# BONUS CHALLENGE
# Transaction History + PIN Verification + Transfer Money
# + Minimum Balance Rule + Account Number Generator

class SecureAccount:
    next_account_number = 1001        # class variable -> shared counter
    MIN_BALANCE = 500

    def __init__(self, customer_name, pin, balance=0):
        self.customer_name = customer_name
        self.__pin = pin              # private (name-mangled) attribute
        self.balance = balance
        self.transactions = []

        # Account number generator
        self.account_number = SecureAccount.next_account_number
        SecureAccount.next_account_number += 1

        self.transactions.append(f"Account opened with {balance}")

    def verify_pin(self, pin):
        if pin == self.__pin:
            return True
        print("Wrong PIN!")
        return False

    def deposit(self, amount):
        self.balance += amount
        self.transactions.append(f"Deposited {amount}")
        print(f"{amount} deposited")

    def withdraw(self, amount, pin):
        if not self.verify_pin(pin):
            return False
        if self.balance - amount < self.MIN_BALANCE:
            print(f"Cannot withdraw. Minimum balance of {self.MIN_BALANCE} required.")
            return False
        self.balance -= amount
        self.transactions.append(f"Withdrew {amount}")
        print(f"{amount} withdrawn")
        return True

    def transfer(self, other_account, amount, pin):
        if not self.verify_pin(pin):
            return
        if self.balance - amount < self.MIN_BALANCE:
            print("Transfer failed: minimum balance rule.")
            return
        self.balance -= amount
        other_account.balance += amount
        self.transactions.append(f"Transferred {amount} to A/C {other_account.account_number}")
        other_account.transactions.append(f"Received {amount} from A/C {self.account_number}")
        print(f"{amount} transferred to A/C {other_account.account_number}")

    def show_history(self):
        print(f"\nTransaction history of A/C {self.account_number} ({self.customer_name}):")
        for t in self.transactions:
            print(" -", t)

    def show_balance(self):
        print(f"A/C {self.account_number} | {self.customer_name} | Balance: {self.balance}")


print("\n--- Bonus Challenge ---")
acc1 = SecureAccount("Aman", pin=1234, balance=5000)
acc2 = SecureAccount("Riya", pin=4321, balance=1000)

acc1.deposit(1000)
acc1.withdraw(500, pin=1111)          # wrong PIN
acc1.withdraw(5800, pin=1234)         # would break minimum balance
acc1.transfer(acc2, 2000, pin=1234)   # success

acc1.show_balance()                   # A/C 1001 | Aman | Balance: 4000
acc2.show_balance()                   # A/C 1002 | Riya | Balance: 3000
acc1.show_history()
acc2.show_history()

# ------------------------------------------

# FINAL CONCEPT QUESTIONS (Must Answer)

# 1. Why is __init__ preferred over a manual method call?
# Ans: __init__ runs automatically when the object is created, so the
#      object is never in a half-ready state. With a manual method like
#      obj.set_data(...), you might forget to call it and get an
#      AttributeError later. __init__ also forces the required values
#      at creation time: BankAccount() without a name fails immediately.
#
# 2. Difference between a class variable and an instance variable:
# Ans: Class variable    -> defined inside the class, outside methods.
#                           One copy shared by ALL objects.
#                           e.g. student_database.course, SecureAccount.MIN_BALANCE
#      Instance variable -> defined with self.xxx (usually in __init__).
#                           Each object has its OWN copy.
#                           e.g. self.name, self.balance
#      Changing a class variable affects every object that has not set its
#      own instance variable of the same name (see Program 2).
#
# 3. Why does Python NOT support traditional overloading?
# Ans: In Python a method name is a variable pointing to a function, and a
#      class keeps one entry per name. Defining a second method with the same
#      name rebinds that name, so the old one is replaced (see Program 4).
#      Python is also dynamically typed, so it can't choose a method by
#      parameter types. Instead, Python uses default parameters and
#      *args / **kwargs to get the same flexibility (see Program 5).
#
# 4. What is the key idea behind polymorphism?
# Ans: The same method name has different behaviour depending on the
#      object. The calling code stays the same (obj.show()), and each class
#      decides what show() does. Code written for the general case works
#      with any new class that follows the same interface.
#
# 5. What happens when two methods have the same name in the same class?
# Ans: The last definition overwrites the earlier one. Only the last method
#      exists; calling the earlier signature gives a TypeError.

# ------------------------------------------
# "You are not just creating objects —
#  you are controlling how they behave."
# ------------------------------------------