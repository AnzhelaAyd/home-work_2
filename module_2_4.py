a = int(input('введи число'))

k=0
for i in range(2,16):
    if list(a) % i ==0:
        k=k+1
if (k<=0):
    print('Число простое')
else:
    print('Число составное')



