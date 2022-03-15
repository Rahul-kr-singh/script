a = int(input('number'))
b = 0
c = a
while(a > 0):
    dig = a % 10
    b = b * 10 + dig
    a = a // 10

if b == c:
    print('number is palindrome')
else:
    print('number is not palindrome')