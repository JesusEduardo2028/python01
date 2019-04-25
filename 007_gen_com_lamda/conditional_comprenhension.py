menu = [
    ["egg", "spam", "bacon"],
    ["egg", "sausage", "bacon"],
    ["egg", "spam"],
    ["chicken", "chips"]
]


"""This condition for the list comprehension acts like a filter"""
meals = [meal for meal in menu if "spam" not in meal]

print(meals)