a=[]
tong=0
print("nhập 10 phần tử của mảng/n")
for i in range(10):
    num = int(input(f"Nhập số thứ {i+1}:"))
    a.append(num)
    tong = tong +num
    if tong % 2 == 0:
       print(f"tổng là:chẵn")
    if tong % 2== 1:
        print(f"tổng là:lẻ")
        