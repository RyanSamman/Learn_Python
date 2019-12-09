
import sys                  # Loads library module sys from which the function platform is used in (ch.3 p55)
print(sys.platform)

print(2 ** 100)
x = 'Spam! '
print(x * 10)


y = 'Spam2!'
z = 0
while z < 10:
    z = z+1
    print(y + ' ')

#input()                     # inputs into GUI (cmd) to show output instead of closing automatically

#run in working directory, cd c:\code (p47)
# then, c:\code> python script1.py



#to reload to obtain updated input, first:
# import script1
# from imp import reload
# reload (script1)

# >>> script1.py > saveit.txt # to save to txt