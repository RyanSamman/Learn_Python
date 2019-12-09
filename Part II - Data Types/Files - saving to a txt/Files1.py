f = open('data.txt', 'w')  # Main method of file processing atm
# Makes a new file 'data.txt' in the same directory as .py
# 'w' is write mode, while if empty or 'r' mode it reads file

f.write('Hello\n')  # write string into text file, also shows how many char is entered
f.write('world\n')

f.close()  # Flushes output buffers to disk

# Chapter 9 ~~~~~~~~~~~~ p. 282 to 289
# Read about:  other file tools:
# pipes, FIFOs, sockets, keyed-access files, persistent object shelves,
# descriptor-based files, relational and object-oriented database interfaces
# saved method to automatically close?
