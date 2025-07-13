import random

answer = random.randint(1, 100)
COUNT = 0

for i in range(10):
    choose = int(input('숫자를 입력하세요: '))
    if answer > choose:
        print("오버")
    elif answer < choose:
        print("언더")
    else:
        print("클리어!")
        COUNT += 1
        break

if COUNT == 0:
    print("정답은 {}였습니다".format(answer))