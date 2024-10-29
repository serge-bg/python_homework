# challenge

# If this the list [1 2 3 4 5 ], 
# write a python program that write the elements of a list to the file denoted by the variable file. 
# Each element should be written on a seperate line
'''

list_1 = [1, 2, 3, 4, 5]

def my_list(item, file):

    # Write the list to the file
    with open(file, 'w') as f:
        for element in item:
            f.write(str(element) + '\n')

# Call the function
my_list(list_1, 'output.txt')  '''

# Operation
list_1 = [1, 2, 3, 4, 5]

def my_list(item, file):
    # Write the list to the file
    with open(file, 'w') as f:
        for element in item:
            f.write(str(element) + '\n')

# Call the function with a different file name
my_list(list_1, 'new_output.txt')  # This will write the list to 'new_output.txt'

