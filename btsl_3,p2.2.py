n=int(input("Nhap so nguyen n (1<=n<=50): "))
while n<1 or n>50:
    n=int(input("Nhap lai so nguyen n (1<=n<=50): "))
a=1
i=0
while i<=n//10:
    j=0
    while j<10:
        if a<=n:
            print(a,end=" ")
            a=a+1
        else:
            break
        j=j+1
    print()  
    i=i+1
