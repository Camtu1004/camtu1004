a=int(input(''))
b=int(input(""))
c=int(input(""))
a,b,c>0
if a+b>c and a+c>b and b+c>a:
     if a*a==b*b+c*c or b*b==a*a+c*c or c*c==a*a+b*b:
                print('Tam giac vuong')
     elif a==b==c:
                print('Tam giac deu')
     else:
                print('Tam giac loai khac')
else:
    print("Khong hop le")