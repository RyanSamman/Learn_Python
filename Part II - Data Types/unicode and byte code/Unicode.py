S = 'sp\xc4m'
print(S, '\n')

file = open('unidata.txt','w',encoding='utf-8')  #utf-8 encoding for unicode
file.write(S)
file.close()

text = open('unidata.txt', encoding ='utf-8').read() #utf-8 into text again
print(text, len(text), '\n')  #4 chars

#To read encoded bytes:
raw = open('unidata.txt', 'rb').read() #'rb' as its in byte code and not exchanged
print(raw, len(raw), '\n') #in reality, its 5 bytes in utf-8

#you can also manually convert between them using:
print(text.encode('utf-8'), raw.decode('utf-8'), '\n')

print(
'\nlatin-1:', text.encode('latin-1'), len(text.encode('latin-1')),
'\nutf-16:', text.encode('utf-16'), len(text.encode('utf-16')))
#all the same string 'spÄm' but encoded differently.



