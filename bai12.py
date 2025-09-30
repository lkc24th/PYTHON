#in từ 1 đến 100
for i in range(1,101,1):
  print (f"in từ 1 đến 100:{i}")


#tổng các số từ 1 đến n chia hết cho 3
print("nhập n từ bàn phím")
n = int(input("nhập n:"))
s = 0
for i in range(1,n+1,1):
 if i %3 == 0:
  s = s + i
print (s)



#100 số Fibonaci đầu tiên bằng vòng lặp for
a, b = 0, 1
for _ in range(100):
    print(a)
    a, b = b, a + b


#in ra các số chia hết cho 3 từ 100 đến 999
for so in range(100,1000,1):
  if so%3==0:
    print(f"in ra các số chia hết cho 3 từ 100 đến 999:{so}")
