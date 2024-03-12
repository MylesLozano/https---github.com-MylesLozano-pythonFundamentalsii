# Python Repetition Statements
# Data types allowed to be iterated: Lists, Ranges, Sets, Tuple, Dictionaries, Strings

x = range(5,11)
petName = ["snowy","blacky","bruno"]

# For loop
for i in x:
    print(i)

# Slicing a list
for name in petName[0:2]:
    print(name)

# Looping Dictionaries

# pc = {
#     "CPU": "AMD Ryzen 5 5600",
#     "GPU": "XFX Speedster Qick319 Radeon RX6700 XT 12GB",
#     "MOBO": "ASRock B550M Pro4",
#     "RAM": "Teamgroup T-Force Delta RGB 32GB (2x16GB)",
#     "SSD": "XPG SX8200 PRO 1TB",
#     "PSU": "Corsair CX750",
#     "Case": "Tecware Forge M Omni w/4 fans"
# }

user = {
    "first_name": "Johnny",
    "last_name": "Tadea",
    "age": 25,
    "average": 81.76,
    "list_subjects": ["Programming", "Mathematics", "English"]
}

# ctrl + / - shortcut for comment

for key in user:
    print(key, ":", user[key])

# Looping List of Dictionaries
list_of_users = [
    {
        "first_name": "Johnny",
        "last_name": "Tadea",
        "age": 25,
        "average": 81.76,
        "list_subjects": ["Programming", "Mathematics", "English"]
    },
    {
        "first_name": "Rose",
        "last_name": "Tadea",
        "age": 22,
        "average": 82.54,
        "list_subjects": ["Programming", "Mathematics", "English"]
    },
    {
        "first_name": "Angel",
        "last_name": "Tadea",
        "age": 27,
        "average": 86,
        "list_subjects": ["Programming", "Mathematics", "English"]
    }
]

for key in list_of_users:
    for x in key:
        print(x, ":", key[x])

# Looping in reverse
x = range(1,10)
for i in x[::-1]:
    print(i)