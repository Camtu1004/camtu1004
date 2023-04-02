a=int(input('S tiêu thụ='))
b=int(input('M1='))
c=int(input('M2='))
d=int(input('M3='))
if a<100:
    tien=b
elif 101<a<150:
    tien=c
elif a>151:
    tien=d
print('Phải trả=',a*tien)
#sai
