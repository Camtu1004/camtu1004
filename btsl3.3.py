a=float(input('tiêu thụ='))
b=float(input('đơn giá='))
c=10/100
if 1<a<100:
    b=550
elif 101<a<150:
    b=750
elif 151<a<200:
    b=950
elif 201<a:
    b=1350
print('Tiền điện phải trả=', a*b+c)
#sai
