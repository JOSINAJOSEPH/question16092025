a = 78
b = 85
c = 92
d = 74
e = 88
# a,b,c,d,e are subjects
t = a + b + c + d + e
# t is total
print('TOTAL MARKS=', t)
Y = t / 500 
P = Y * 100
# P is percentage
print('percentage=', P)
if P >=90 and P <=100 :
    print('GRADE A+')
elif P >= 80 and P < 89 :
    print('GRADE A')
elif P >=70 and P < 79 :
    print('GRADE B')
elif P >= 60 and P < 69 :
    print('GRADE C')
elif P >= 50 and P < 59 :
    print('GRADE D')
else:
    print('GRADE F')