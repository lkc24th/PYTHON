## tổng 100 số đầu tiên
i = 1 
s = 0
while i <= 100:
   s = s+i
   i = i+1
print("Tổng là:",s)


## in ra tổng các số chia hết cho 3
n = int(input("Nhập số tự nhiên n"))
j = 1
p = 0
while j<=n and j%3==0:
   p  = p + j
   j = j + 1
print ("Tổng các số chia hết cho 3:",p)


## in ra 100 số fibonaci
def fibonacci(k=100):
    if k <= 0:
        return []
    elif k == 1:
        return [0]
    fi = [0, 1]
    i = 2
    while i < k:
        fi.append(fi[i - 1] + fi[i - 2])
        i += 1
    return fi[:k]
print(f"Dãy 100 số Fibonacci đầu tiên:{ fibonacci(100)}")


j = 100
while j<= 999 and j%3==0:
   j = j+1
print("Các số chia hết cho 3 từ 100 đến 999:",j)



