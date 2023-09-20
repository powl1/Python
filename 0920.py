a = [1,2,3]
a[2] = 4
print(a) #[1, 2, 4]

a=[1,2,3,4,5]
del a[2:]
print(a) #[1, 2]


#append() : 리스트의 맨 마지막에 요소 추가
# 어떤 자료형도 추가 가능
a=[1,2,3]
a.append(4) #리스트 맨 마지막에 4를 추가
print(a) #[1, 2, 3, 4]

a.append([5,6])
print(a) #[1, 2, 3, 4, [5, 6]]


#sort() : 리스트의 요소를 순서대로 정렬
# 문자의 경우 알파벳 순서로 정렬 가능
a=[1,4,3,2]
a.sort()
print(a) #[1, 2, 3, 4]


#reverse() : 리스트를 역순으로 뒤집어 줌
# 요소를 역순으로 정렬하는 것이 아닌, 현재의 리스트 그대로 뒤집음
a = ['a', 'b', 'c']
a.reverse()
print(a) #[]'c', 'b', 'a']


#index() : 욧를 검색하여 위치 값 변환
# 값이 존재하지 않으면, 값 오류 발생
a=[1,2,3]
print(a.index(3))

print(a.index(0)) # Traceback (most recent call last): File "<stdin>", line 1, in <module> ValueError: 0 is not in list


#insert() : 리스트에 요소 삽입
#inset(a,b) : a번째 위치에 b를 삽입하는 함수
a=[1,2,3]
print(a.insert(0,4)) #[4,1,2,3]

#remove() : 리스트에서 첫번째로 오는 x 삭제

#튜플


#인덱싱하기
t1=(1,2,'a', 'b')
print(t1[0]) #1
print(t1[3]) #b

#슬라이싱하기
t1=(1,2,'a','b')
print(t1[1:]) #(2, 'a', 'b')

#튜플 더하기와 곱하기
t2=(3,4)
print(t1+t2) #(1, 2, 'a', 'b', 3, 4)

print(t2*3) #(3, 4, 3, 4, 3, 4)

#튜플 길이 구하기
print(len(t1)) #4


# 딕셔너리
# 대응 관계를 나타내는 자료형
# 연관배열(Associative aray) 또는 해시(hash)
# key와 value를 한쌍으로 갖는 자료형
# 순차적으로 해당 요솟값을 구하지 않고, key 를 통해 value를 바로 얻는 특징 [= 집합들의 모임 느낌]

#딕셔너리는 {} 중괄호의 형태로 각 요소는 쉼표로 구분된다.
dic={'name':'pey','phone':'01199993333','birth':'1118'}
type(dic) #<class 'dict'>

print(dic) #{'name': 'pey', 'phone': '01199993333', 'birth': '1118'}

# 리스트나 튜플, 문자열은 요솟값 접근 시 인덱싱이나 슬라이싱 기법을 사용
# 딕셔너리는 key를 사용해 value 접근

# 딕셔너리 쌍 추가
a={1:'a'}
a[2] = 'b' 
print(a) #{1: 'a', 2: 'b'}

# 딕셔너리 요소 삭제
del a[1]
print(a) #{2: 'b'}

#딕셔너리에서 key 사용해 value 얻기
grade = {'pey': 10, 'julliet': 99}
grade['pey'] #10 : key가 'pey'인 딕셔너리의 value를 반환
grade['julliet'] #99 : 줄리엣 값 반환




