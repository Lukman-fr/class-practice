#1_comparison Operator
"""
==
!=
<
<=
>
>=
"""
from struct import pack_into

num1 = 10
num2 = 20
num3 = 10
print(num1==num2) #false
print(num1==num3) #True
print(num1!=num3) #False
print(num1!=num2) #True
print(num1<num2)  #True
print(num1<num3)  #false
print(num1<=num2) #True
print(num1<=num3) #True
print(num1>=num3) #True
print(num1<=num3) #True

#_2_ assignment_operator

num1 = 10
#num1 = num1 + 10

print(num1)
num1+=10
print(num1)


num1 = 10
num1 = num1 - 10

print(num1)
num1-=10
print(num1)

num1 = 10
num1*=10
print(num1)
num1**=10
print(num1)
num1 = 10
num1//10
print(num1)

# Logical_operator
# and, or, not

num1 = 10
num2 = 20

print((num1 == num2) or (num1 <= num2)) #True
print((num1==num2) and (num1<=num2)) #false
print(not(num1==num2)) #True
print(not(num1<=num2)) #false

#membership Opeator
# in, not in
name = "Sidratul Muntaha Ayaan"

print("Sidratul" in name) #True
print("Ayaan" in name)
print("ayaan" not in name)
print("Muntaha" not in name)

#identity Operator
# is, is not

str1 = "hello"
str2 = 'hello'
str3 ='world'
str4 = str1

print(str1 is str2) #True
print(str1 is not str2) #false
print(str4 is  str1)  #true

# string_intro.py
# double or single inverted comma

num1 = "10"
num2 = '100'
print(type(num1))
print(type(num2))


# string value access
statement = "we love python"

print(statement[0])
print(statement[5])
print(statement[:5]) #we lo
print(statement[2])
print(statement[2:-1])
print(statement)

# string value access