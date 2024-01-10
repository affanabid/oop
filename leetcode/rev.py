x = -10030
neg = False
if x < 0:
    x = x * -1
    neg = True
x = str(x)
n = []
for i in x:
    n.append(i)
l = len(n) - 1
string = ''

while l >= 0:
    string += n[l]
    l -= 1

a = 0
ns = False
s = ''
if neg:
    s += '-'
for i in string:
    if ns == True:
        s += i
    else:
        if i != '0':
            ns = True
            s+= i
print(s)
