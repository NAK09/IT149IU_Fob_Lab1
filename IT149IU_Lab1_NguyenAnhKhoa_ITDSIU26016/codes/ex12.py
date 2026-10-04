a = float(input('Enter time for runner 1: '))
b = float(input('Enter time for runner 2: '))
c = float(input('Enter time for runner 3: '))

print('Times in ascending order:')
if a <= b and b <= c: print(a, b, c)
if a <= c and c < b:  print(a, c, b)
if b < a  and a <= c: print(b, a, c)
if b <= c and c < a:  print(b, c, a)
if c < a  and a <= b: print(c, a, b)
if c < b  and b < a:  print(c, b, a)

if a <= b and a <= c:
    print('Runner 1 won!')
if b < a and b <= c:
    print('Runner 2 won!')
if c < a and c < b:
    print('Runner 3 won!')