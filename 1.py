def nod (a,b):
 while a!=0 and b!=0 :
     if a>b:
         a=a%b
     else:
         b=b%a
 return a+b

a=int(input('Введите A: '))
b=int(input('Введите B: '))

while a<0:
    a=int(input('Введите A: '))
while b<0:
    b=int(input('Введите B: '))

print('Наибольший общий делитель = ', nod(a,b))

