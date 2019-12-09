B = bytearray(b'spam')  # To combine two strings
print(B)
# bytearray(b'spam')
B.extend(b'eggs')
print(B)
# bytearray(b'spameggs')
B.decode()
# 'spameggs'
print(B)
# bytearray(b'spameggs')
B = B.decode()
print(B)
'spameggs'

# Text string #Byte string
#    'x'    +    b'y'  cannot be mixed

# Convert text into byte strings:
'x'.encode()  # or u'x'.encode

# Convert byte into text strings:
b'y'.decode()

# Byte strings or bytearray mainly used to transfer data to and from files (Ex. binary file)
# Text strings or Unicode are used majority of time directly (or from text file)
