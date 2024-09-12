a = int(input("A값 입력 : "))
b = int(input("B값 입력 : "))
c = int(input("C값 입력 : "))

num = a*b*c
count_0, count_1, count_2, count_3, count_4, count_5, count_6, count_7, count_8, count_9  = 0,0,0,0,0,0,0,0,0,0
num_str = str(num)
num_len = len(str(num))

print(num, num_str, num_len)

for i in range(0, int(num_len)):
    if num_str[i] == "0":
        count_0 += 1
    if num_str[i] == "1":
        count_1 += 1
    if num_str[i] == "2":
        count_2 += 1
    if num_str[i] == "3":
        count_3 += 1
    if num_str[i] == "4":
        count_4 += 1
    if num_str[i] == "5":
        count_5 += 1
    if num_str[i] == "6":
        count_6 += 1
    if num_str[i] == "7":
        count_7 += 1
    if num_str[i] == "8":
        count_8 += 1
    if num_str[i] == "9":
        count_9 += 1

print(f"숫자 0의 개수는 {count_0}개")
print(f"숫자 1의 개수는 {count_1}개")
print(f"숫자 2의 개수는 {count_2}개")
print(f"숫자 3의 개수는 {count_3}개")
print(f"숫자 4의 개수는 {count_4}개")
print(f"숫자 5의 개수는 {count_5}개")
print(f"숫자 6의 개수는 {count_6}개")
print(f"숫자 7의 개수는 {count_7}개")
print(f"숫자 8의 개수는 {count_8}개")
print(f"숫자 9의 개수는 {count_9}개")

