# This is a quick example of how a dictionary can be inverted (swap keys with values) using Python.

# Initialize a dictionary with some existing key-value pairs
student = {
    'name': 'Kristin',
    'age': 34,
    'course': 'Math' 
}

# Initialize an empty dictionary to contain the inverted verison of the above dictionary
inv_student = {}

# Print existing dictionary
print('BEFORE: ', str(student))

# Invert the dictionary using a for loop
for key, value in student.items():
    inv_student.setdefault(value, []).append(key)

# Print the inverted dictionary
print('AFTER: ', str(inv_student))
