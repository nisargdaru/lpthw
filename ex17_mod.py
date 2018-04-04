#fileobj = open(filename, mode)
poem = '''
..assfffljjfkfjlsfjljfljlfjlfj
..fsjflfl;lfjlfjljflflsjfjfjfjfj
..flkjlfjlfjlsjflkjflsjfjslfj;sfjlsfj
'''
fout = open('relativity', 'wt')
fout.write(poem)
fout.close()

#print(poem, file=fout) 
#print(poem, file=fout, sep='', end='') sep stands for seperator 