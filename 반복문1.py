# 조건이 참인 동안 반복 수행
# 파이썬에서는 들여쓰기를 통해 라인 벗어나는 것을 구분한다
n = int(input("정수 입력 : "))
sum = 0     # 값을 누적하기 위한 변수

# 자바의 경우에만 while 조건식을 만들 때 참거짓 판별을 위해 while n > 0 : 등의 형태로 써주어야 한다.
# while n:    # 0이 아닌 모든 값은 참으로 간주 (자바 제외)
#     sum += n
#     n -= 1  # n = n -1, n--
# print(sum)
for i in range(1, n+1):     # 범위 기반의 for문
    sum += i
print(sum)

# while문은 주로 횟수가 정해지지 않은 반복적인 수행을 할 때 사용
while True:     # 반복문 내에 탈출 조건이 있어야 함
    age = int(input("나이를 입력 하세요 : "))
    if 0 <= age <= 200: break   # 정상적인 입력이므로 반복문 탈출
    print("나이를 잘못 입력 하셨습니다.")

print(f"당신의 나이는 {age}입니다.")




