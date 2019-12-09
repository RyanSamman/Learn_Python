# Now to read the file:
f = open('data.txt')  # , 'r') is optional, read is default setting
text = f.read()
print(text)

# In loops, .read() is not needed, it has an iterator which reads line by line
for line in open('data.txt'):
    print(line)

# To know more options to do with f, use
# print(dir(f))
