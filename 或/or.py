from urllib.parse import *
file = open('rce_or.txt')
encodes = file.readlines()
file.close()

func = input('function:')

t1 = ''
t2 = ''
for letter in func:
    for encode in encodes:
        if encode[0] == letter:
            t1 += encode[2:5]
            t2 += encode[6:9]
            break

print('("'+t1+'"|"'+t2+'")\n')
result = '("'+unquote(t1)+'"|"'+unquote(t2)+'")'
c = {'c':result}
print(c)