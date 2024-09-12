a, b, c = map(int, input("정수 입력 : ").split())
ls = str(a * b * c)
for i in range(10): # 0 ~ 9
    print(ls.count(str(i)), end=" ")
