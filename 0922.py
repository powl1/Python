#for 문
# while문과 비슷한 반복문
# 리스트나 튜플, 믄자열의 첫번째  요소부터 마지막 요소까지 차례로 변수에 대입 되어 '수행할 문장1', '수행할 문장2' 등이 수행됨


#리스트 내포 사용법
#리스트 내포
a=[1,2,3,4]

for num in a:
    result.append(num * 3) # 자바에서는 add 지만, 파이썬에서는 append 이다.
    
print(result) #[3, 6, 9, 12]

## 리스트 안에 for 문 포함하기
result=[num*3 forn  num in a]
print(result) #[3, 6, 9, 12]
## 리스트 내포 안에 if조건 사용가능
## [1,2,3,4] 중에서 짝수에만 3을 곱하여 담도록 수정
result=[num * 3 for  num in a if num % 2 == 0]
print(result) #[6, 12]

result=[x*y for x in range(1,10) for y in range(1,10)]
print(result)


# 함수
# def : 함수를 만들 때 사용하는 예약어
# 함수 이름은 임의로 생성 가능
# 매개변수는 함수에 입력으로 전달되는 값을 받는 변수
def sum(a,b):
    return a+b
a,b = 3, 4
c = sum(a,b)

print(c) #7

########################################################
def sum_print(a,b) :
    print(a+b)

sum_print(5, 7) #12
sum_print(a, b) #7

def say():
    print('Hi')

say() # Hi


# 입력값과 결과값에 따른 함수 형태
sum_print(a = 7, b = 9) #16

# 초기값 설정하기 : 매개 변수에 초기값을 미리 설정
# 
def say_myself(name, old, man = True) :
    print('나의 이름은 %s입니다.' % name)
    print('나이는 %d살 입니다.' % old)
    if man :
        print('남자입니다.')
    else:
        print('여자입니다.')

say_myself('박응용', 27)
say_myself('박응용', 27, True)
# 나의 이름은 박응용입니다.
# 나이는 27살 입니다.
# 남자입니다.
say_myself('박응용', 27, False)
# 나의 이름은 박응용입니다.
# 나이는 27살 입니다.
# 여자입니다.

