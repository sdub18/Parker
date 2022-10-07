import csv
from functools import reduce


# Our epic employee object
class employee:
    name = ""
    status = ""
    boss = ""

    def __init__(self, name, status, boss):
        self.name = name
        self.status = status
        self.boss = boss


employees = []
dict = {}
status_dict = {}

# Load All the data from the csv into an array
with open('file.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        employees.append(employee(row[0], row[1], row[2]))



# Load employees into the dictionary
#
#   This function loads all the employees into a dictionary of { Employee Name (String) :  Array of employees under them [String] }
#   It would look something like this:
# 
#   Bob : [Parker, James]
#   Parker: [Sam, Donald]
#   ...
#
for employee in employees:
    if employee.boss not in dict:
        dict[employee.boss] = []
    
    dict[employee.boss].append(employee.name)



# Load employees status into the status dictionary
#
#   This function creates another dictionary to quickly check the status of an employee as a value.
#   It would look something like this:
#
#   Ethan : 1
#   Bob: 1
#   Sam: 0
#   Donald: 0
#
#
#
for employee in employees:
    if employee.status == "terminated":
        status_dict[employee.name] = 0
    else:
        status_dict[employee.name] = 1



# Function to recursively check termination policy
def recursiveStatusCheck(employee_name):

    #   This is the base case for all the people without anyone under them (like Sam and Donald)
    if employee_name not in dict:
        return status_dict[employee_name]
    
    # This case gets run by all the people who have people under them like Parker
    else:
        total_status = status_dict[employee_name]

        for name in dict[employee_name]:
            total_status += recursiveStatusCheck(name)  # This is the recursive part of the function where we call the name under the current person
        
        return (total_status / (len(dict[employee_name]) + 1))


print("Boss Name: Ethan")
print("Turnover Rate: " + str(recursiveStatusCheck("Ethan")))