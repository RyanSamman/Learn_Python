# you can't edit a string directly using a list like:
# S = 'Spam!'
# S[0] ='z'
# due to them being immutable, however lists, dictionaries, and sets are so:

S='Omar'
print(S)
L= list(S) #to make into a list
print(L)
print(L[0:3])
# now >>>L is
#['S','p', 'a', 'm', '!'] so:

L[0:2]="B"    #second number [#1:#2] is until but not included
print(L)
S=''.join(L)
print(S)
