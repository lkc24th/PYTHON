

l = int(input("Nhập số nguyên l khác 0 bất kì:"))
if (l>0):
    print("l là số nguyên dương")
else :
    print("l là số nguyên âm")

n = int(input("Nhập số nguyên n:"))
if(n%5==0):
    print("n là số chia hết cho 5")
else:
    print("n chia hết cho 3")
    


thang =int(input("Nhập tháng mấy(số nguyên từ 1-12):"))
if(thang==1 or thang==3 or thang==5 or thang==7 or thang==8 or thang==10 or thang==12):
    print("Tháng có 31 ngày")
else:
    print("Tháng có 30 hoặc 28 hoặc 29 ngày")





import math
a = float(input("Nhập số a:"))
b = float(input("Nhập số b:"))
c = float(input("Nhập số c:"))
delta = (b**2)-4*a*c
if(delta>=0):
    print(f"x1={(-b+math.sqrt(delta))/2*a} x2={(-b-math.sqrt(delta))/2*a}")
else:
    print("Phương trình vô nghiệm")



m=int(input("Nhập cạnh m của tam giác:"))
n=int(input("Nhập cạnh n của tam giác:"))
p=int(input("Nhập cạnh p của tam giác:"))
if(m+n>p or m+p>n or p+n>m):
    print("Đây là tam giác")
else:
    print("Đây không phải là tam giác")