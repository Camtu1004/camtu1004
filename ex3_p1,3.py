x = float(input("Nhap so thu nhat: "))
y = float(input("Nhap so thu hai: "))
ch = input("Nhap phep toan (+, -, *, /): ")

if ch == '+':
    ket_qua = x + y
elif ch == '-':
    ket_qua = x - y
elif ch == '*':
    ket_qua = x * y
elif ch == '/':
    if y == 0:
        print("Khong hop le!!!")
    else:
        ket_qua = x / y
else:
    print("Khong hop le!!!")

if ch in ['+', '-', '*', '/'] and y != 0:
    print(f"{x} {ch} {y} = {ket_qua}")
