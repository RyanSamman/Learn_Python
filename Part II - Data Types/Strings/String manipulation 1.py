L = 'aqa,bbb,ccc'   #characters in a string are stored as 0,1,2,3,4....
L.find('q')         #So location 2nd character gives 1
print(L.find('q'))

print(L.replace('q','a'),)
L=L.replace('q','a')

L.split(',')          # X.split('...') makes one string into many substrings,
print(L.split(','))   # breaking it depending on what is in between ('...')

L.upper()
print(L.upper())      #makes everything uppercase


Z='abc'                      #Returns true/false if *ALL* is letters
Y = '5'                      #also isdigit for numbers only present in *STRING*
print(L.isalpha(),Z.isalpha(),Y.isdigit())

Q= 'aaa,bbb,ccc\n'
print(Q)
Q.rstrip()
print(Q.rstrip())             #Removes \n ???

#Can use more than one time in one line:
Q.rstrip().split(',')
print(Q.rstrip().split(','))

#To add to a string, you can also:

print('{0},{1},Potato,{2}'.format('henlo','u2','tomato'))  #Called formatting, best way p103, more features later

X='qwerty'
#print(dir(X)) to find everything you can do with X.onwards
#there is a built in help function too,
#help(X.onwards) #To know the rest

#Furthermore, you can preserve a text's new line and tab formatting by:

msg= """
    Hello it's Ryan
    @Qwerty."
    """
print(msg)      #Bad for variables in string, idk how to introduce them into it

