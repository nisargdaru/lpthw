#With Comments
from sys import argv
#import argument variable
script, filename = argv
#filename as a place holder
print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL-C (^C).")
print("If you do not want that, hit Return.")

input("?") #input here

print("Opening the file...")
target = open(filename, 'w') #target is a variable, opening filename with `write` parameter

print("Truncating the file. Goodbye!")
target.truncate() #clear the opened file

print("Now I'm going to ask you for three lines.")

line1 = input("line1: ")
line2 = input("line2: ")
line3 = input("line3: ")

print("I'm going to write these to the file.")

target.write(line1) #write line1 variables in file
target.write("\n")
target.write(line2)
target.write('\n')
target.write(line3)
target.write("\n")

print("And finally, we close it.")
target.close() #close the opened file 
