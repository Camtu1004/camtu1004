Toan=int(input(''))
Ly=int(input(""))
Hoa=int(input(''))
c=(Toan*2+Ly*3+Hoa)/6
if c<3:
    print('Kem')
elif 3<=c<5:
    print('Yeu')
elif 5<=c<6:
    print('Trung binh')
elif 6<=c<7:
    print('Trung binh kha')
elif 7<=c<8:
    print('Kha')
elif 8<=c<9:
    print('Gioi')
elif 9<=c<10:
    print('Xuat sac')