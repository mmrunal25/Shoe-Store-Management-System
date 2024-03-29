
'''['hello', 'morning']
print([bool('')])
''' '''
t = (1,2,4,3)
print(t[3])
t[3] = 45
'''
'''
d = {0: 'a', 1: 'b', 2: 'c'}
for x in d.keys():
    print(d[x])

for i in range(int(2.0)):
    print(i)
'''
'''
a,b=1,0
a=aˆb
b=aˆb
a=aˆb
print(a)'''
'''
print(2**2**3**1)

val = 154
while(not(val)):
    val **= 2
else:
    val //= 2
    print(val)

print(not(val))

print(range(5))'''
'''
l = list()
l.append([1,2,[3,4]])
l.extend([5,6,7])
print(l)'''
'''
try:
    # Do something
    except:
    # Do something
finally:
    # Do something
'''
'''
print(9//2)'''
'''
while True:
    print(" it's a infinite loop (do not run) ")
'''
'''
s1= {1, 2, 3}
s1.issubset(s1)'''
'''
a=float('inf')
print(a)

for i in range(float('inf')):
    print(i)'''
'''
True = False
while True:
    print(True)
    break'''
'''
string = "my name is x"
for i in ' '.join(string.split()):
    print (i, end=", ")'''
'''
a=["Apple","Ball","Cobra"]
a.sort(key=len)
print(a)'''

'''
a = [1, 5, 7, 9, 9, 1]
b=a[0]
x= 0
for x in range(1, len(a)):
    if a[x] > b:
        b = a[x]
        b= x
print(b)
'''
'''
print('+99'.zfill(5))

a={'B':5,'A':9,'C':7}
print(sorted(a))

a={}
a[2]=1
a[1]=[2,3,4]
print(a[1][1])'''
'''
A = "1234567"
print(A[1::2])'''
'''
x = 4+5/5*2
print(x)'''
'''
c=0
for i in 'abc xyz':
    c = c+1
    print(c)'''

'''print(set(range(1,-3,-5)))
print(range(1,-3,-5))
print(set(range(3,3)))'''

dict = {'a':{3:4, 6:2}, 't':5, 7: {1:3, 9:1}}
print(dict[7][1])