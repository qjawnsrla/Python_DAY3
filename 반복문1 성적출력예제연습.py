while True:
    score = int(input("성적을 입력하세요 : "))
    if 0<= score <= 100: break
    print("잘못된 값을 입력하셨습니다. 0 ~ 100 사이의 값을 입력해주세요.")

if score >=90: print("A")
elif score >=80: print("B")
elif score >=70: print("C")
elif score >=60: print("D")
else: print("F")
