def gugudan():
    try:
        # 사용자로부터 숫자를 입력받습니다.
        number = int(input("출력할 구구단의 숫자를 입력하세요: "))
        
        # 1부터 9까지 반복하여 구구단을 출력합니다.
        for i in range(1, 10):
            # 각 단계의 곱셈 결과를 출력합니다.
            print(f"{number} x {i} = {number * i}")
    
    except ValueError:
        # 숫자가 아닌 값을 입력했을 때의 예외 처리입니다.
        print("올바른 숫자를 입력하세요.")

# 구구단 함수를 호출합니다.
gugudan()
