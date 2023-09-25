# 객체
class Calculator:
    def __init__(self, first, second): # __init__ : 매직 메소드, 스페셜 메소드
        self.first = first # 자바~변수선언 = this.first (초기화)
        self.second = second
        #self.result = 0
    
    def add(self):
        result = self.first + self.second
        return result
    
    """ def sub(self, num):
        self.result -= num
        return self.result """
    
    
cal = Calculator(4,3)
print(cal.add()) #7

#Calculator.add(cal.1) # 다이렉트로 self에 직접적으로 넣어 사용하는. #문법적으로 가능하지만 사용X

#print(cal.add(3)) #3
#print(cal.add(5)) #8
#print(cal.add(3)) #11

#print(cal.sub(1)) #10

class FourCal:
  def __init__(self, first, second):
    self.first = first # 인스턴스 변수
    self.second = second
    
  def add(self):
    result = self.first + self.second
    return result
  
  def mul(self):
    result = self.first * self.second
    return result
  
  def sub(self):
    result = self.first - self.second
    return result
  
  def div(self):
    result = self.first / self.second
    return result


# a = FourCal()  # 객체 생성할 때 초기값 설정

# a.setdata(4, 2)

# print(a.add())
# print(a.sub())


class MoreFourCal(FourCal): # 상속 자식(부모)
    def pow(self):
        result = self.first ** self.second
        return result

    def div(self): # 파이썬도 함수오버라이딩이 가능하다.
        if self.second == 0:
            return 0
        else:
            return self.first/self.second
    #


more = MoreFourCal(10, 5) # MoreFourCal 클래스의 인스턴스 생성

print(id(more))

print(more.add())

print(more.sub())

print(more.pow())

more = MoreFourCal(10, 0)
print(more.div()) # 0으로 나눠서 오류가 발생한다.

# 클래스 변수
# 자바클래스 변수 = static = 공용변수 = 정적 변수 = 먼저 한번 올리는 변수
# class A { static int a = 0; }
# A.a = 0 # 접근방법은 클래스명.변수 = 초기화;

class Famliy:
    lastname = 'kim' # 클래스 변수 
    
print(Famliy.lastname)
a=Famliy()
a.lastname

b=Famliy()
b.lastname #kim #먼저 올려 공유하기 때문에 kim이 출력된다.
