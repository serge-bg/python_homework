# Homework 2
# Print out the List name of the second employee. 
# Please search through the dictionary below: "Alexandra 0

# OPERATION
d = {
    "employees": [
        {"firstName": "John", "lastName": "Doe"},      # Index 0
        {"firstName": "Anna", "lastName": "Smith"},    # Index 1
        {"firstName": "Peter", "lastName": "Jones"}     # Index 2
    ],
    "owners": [
        {"firstName": "Jack", "lastName": "Petter"},
        {"firstName": "Jessy", "lastName": "Petter"}
    ]
}


# Printing the last name of the second employee
second_employee_last_name = d["employees"][1]["lastName"]
print(f"Second employee's last name is {second_employee_last_name}")  # Output: Smith

# Searching for 'Alexandra' in employees / OPTION 1
found = False
for employee in d["employees"]:
    if employee["firstName"] == "Alexandra" or employee["lastName"] == "Alexandra":
        print(f"Found Alexandra in employees: {employee}")
        found = True
if not found:
    print("Alexandra not found in employees.")
    

# Searching for 'Alexandra' in employees / OPTION 2

if d["employees"][0]["firstName"] == "Alexandra" or d["employees"][0]["lastName"] == "Alexandra":
    print("Found Alexandra in first employee.")
elif d["employees"][1]["firstName"] == "Alexandra" or d["employees"][1]["lastName"] == "Alexandra":
    print("Found Alexandra in second employee.")
elif d["employees"][2]["firstName"] == "Alexandra" or d["employees"][2]["lastName"] == "Alexandra":
    print("Found Alexandra in third employee.")
else:
    print("Alexandra not found in employees.")