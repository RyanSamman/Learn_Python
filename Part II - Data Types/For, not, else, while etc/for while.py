for c in 'spam':  # c will become 's', then 'p' so on....
    print(c.upper())

D = {'a': 1}
if 'f' not in D:  # if not true (false), prints first one,
    print('\n\'f\' is missing\n')
else:  # else if not false (true), prints second one,
    print('\n\'f\' is present\n')

x = 4
while x > 0:
    print('spam!' * x)
    x -= 1
