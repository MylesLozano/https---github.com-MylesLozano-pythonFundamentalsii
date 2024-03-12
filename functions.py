# Functions
# - consists of function name, parameters
# - starts with "def" keyword.
# - Optimizes and make a block of code reusable.

# void function
def averageOfThreeNumbers(num1, num2, num3):
    # codes ...
    average = (num1 + num2 + num3) / 3
    print("Average: ", average)

# SHORTCUT FOR COPYING HIGHLIGHTED/SINGLE LINE : Alt + Shift + ArrowDown/ArrowUp
# SHORTCUT FOR REPOSITIONING HIGHLIGHTED/SINGLE LINE : Alt + ArrowDown/ArrowUp

averageOfThreeNumbers(89, 76, 81)
averageOfThreeNumbers(89, 76, 81)
averageOfThreeNumbers(89, 76, 81)

# return function
title = "ang alamat ni loudie"
title2 = ": Bagsakan Era"

def stringToTitle(title):
    return title.title()

def stringToUppercase(message):
    return message.upper()

def stringToLowercase(message):
    return message.lower()

def joinString(message, message2):
    return message.join(message2)

def countLetters(message):
    return len(message)

def countWords(message):
    return message.count(message)

print(stringToTitle(title))
print(stringToUppercase(title))
print(stringToLowercase(title))
# print(joinString(title, title2))
print(countLetters(title))
print(countWords(title))