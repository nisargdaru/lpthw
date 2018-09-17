from sys import argv
script, input_file = argv

def print_all(f):   # define function print_all with argument 'variable f'
    print(f.read())


def rewind(f):      #define function rewind with argument as 'variable f'
    f.seek(0)       #move the read head to the start of the file "f"


def print_a_line(line_count, f): #define function print_a_line with arguments as variables 'line_count' and file 'f'
    print(line_count, f.readline())


current_file = open(input_file)

print("First let's print the whole file:\n")

print_all(current_file)

print("Now let's rewind, kind of like a tape.")
rewind(current_file)

print("Let's print three lines: ")

current_line = 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line,current_file)

current_line += 1
print_a_line(current_line, current_file)
