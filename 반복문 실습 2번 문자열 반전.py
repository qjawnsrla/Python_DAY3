# 실습 2번 : 문자열 반전, 문자열을 입력 받아서 문자열 반전 출력
# ex) ABCDEF => FEDCBA
in_str = input("문자열 입력 : ")
for i in range(len(in_str)-1, -1, -1):
    print(in_str[i], end="")
print()
reverse_str = in_str[::-1]
print(reverse_str)