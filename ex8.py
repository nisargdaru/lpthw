formatter = "{} {} {} {}" #a variable named formatter

print(formatter.format("one", "two", "three", "four"))
#one string for each bracket in the formatter variable, `format` function is used here
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(#each comma below seperates the string that goes into the four individual braces
         "Here goes",
         "My text, thought by me",
         "Nothing specific, just random lines;",
         "that came to my mind at this very instant."
))
#if one bracket is less, the last string won't be printed
