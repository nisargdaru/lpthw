from sys import argv #it imports  `argv` from sys

script, filename = argv #provide a variable for input from cli

txt = open(filename)    #open the filename input by user

print(f"Here's your file {filename}: ")
print(txt.read())       #reads the file opened

print("Type the filename again: ")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())

txt.close()                    #close txt variable
txt_again.close()              #close txt_again variable
