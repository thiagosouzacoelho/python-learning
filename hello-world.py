# line comment

print('Hello, world!')
print 'Hello'
print "Another hello"

print(1 == 1 and 2 == 3)
print(not True)
print(not False)

if (True and False):
    print('The conditional is True')
else:
    print('The conditional is False')

x = 1;
while (x < 10):
    x += 1
    print(x)

x = [1, 2, 3, 4]
t = ['t', 'h', 'i', 'a', 'g', 'o'];
print(x[3])

print(range(9))
print(range);
# error -> x[4] = 5;
# error -> print(x[4]);
for i in t:
    print(i)

for i in range(5):
    print i

def funcName(x, y):
    return x * y

print 'Function call: '
print funcName(3, 4)
