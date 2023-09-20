print("hello world")

num = 1+1
words = "hello world"

print(words[0]) #h
print(words[1]) #e
print(words[2]) #l

print(words[-1]) #d
print(words[-2]) #l
print(words[0:5]) #
print(words[:5]) #워드 index 0 ~ 5까지 # hello
print(words[3:]) #워드 (3:) 에서 부터 #lo world

add=[1,3,5,7,9]
print(add)
print(type(add))

strs=['life', 'is','short']
print(strs) #['life', 'is', 'short']
print(strs[0]) #life
print(strs[1]) #is

strs=[1,2.1,'life','is','short']
print(strs[0]) #1
print(type(strs[0])) #<class 'int'>
print(type(strs[1])) #<class 'float'>

strs=[1,2.1,['life','is']]

# 리스트 끼리의 덧셈은 리스트의 나열을 합쳐서 나열한다.
a = [1,2,3]
b = [4,5,6]
print(a+b) # [1, 2, 3, 4, 5, 6]

# 리스트 타입을 X3 해서 나열하여 출력해라
a = [1,2,3]
print(a*3) # [1, 2, 3, 1, 2, 3, 1, 2, 3]