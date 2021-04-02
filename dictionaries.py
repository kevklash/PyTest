# Dictionaries
# The only way to access a dict item(key and value pair),
# is to use its key, index do not work
# Identifying: {} --> Dictionary and/or Set || [] --> List
# We can have lists and dictionaries within Dictionaries
students = {"Kevin": 31, "Fatima": 30, "Diny": 4}
# Looking for keys
print(students["Diny"])
# Adding a new element
students["Intercambio"] = 25
print(students)
# Modifying values on specific elements
students["Intercambio"] = 26
print(students)
# Delete an item
del(students["Intercambio"])
print(students)
# Showing Dictionary keys(keys are iterable but not indexable)
print(students.keys())
# Showing Dictionary values(values are iterable but not indexable)
print(students.values())
# Converting the dict into a list to make it indexable
students_lits = list(students)
# Accessing through an index
print(students_lits[2])
# Dictionary values can be converted into lists the same way as keys
students_values = list(students.values())
# Accessing through an index
print(students_values[2])
# Showing Dictionary items(items are iterable but not indexable)
print(students.items())
# Dictionary values can be converted into lists the same way as keys
students_items = list(students.values())
# Accessing through an index
print(students_items[2])
# --Practice--
data_base = {
    "User1": {
        "name": "Batman", "symbol": "bat", "city": "Gotham"
    },
    "User2": {
        "name": "Superman", "symbol": "S for hope", "city": "Metropolis"
    },
    "User3": {
        "name": "Wonder Woman", "symbol": "WW", "city": "Themyscira"
    }
}
# Accessing data
print(data_base["User1"])
print(data_base["User2"]["symbol"], data_base["User2"]["name"])
print(data_base["User3"]["name"], data_base["User3"]["city"])