# string_concatenation
city_1 = "Sylhet"
city_2 = "Paris"

concate_two_string = city_1 + " and " + city_2
print(concate_two_string)
concate_two_string_v2 = " and ".join((city_1, city_2))
print(concate_two_string_v2)
concate_two_string_v2 = " ".join((city_1, city_2))
print(concate_two_string_v2)
concate_two_string = city_1 + " " + city_2
print(concate_two_string)
satement = "Bangladesh is nice country"
print(satement.replace("nice","beatiful"))

#string formatings
# process _1
print(city_1)
print(city_2)
#proccess_2
print("city_1:"+city_1)
print("city_2:"+city_2)
print("ineger Number:",5)

#proccess-3
print("city_1 one is:{} and city_2 is:{}".format(city_1,city_2))
print("city one is: {} and city two is: {}".format(city_1,city_2))

print("city one is:{}, city two is:{}".format(city_1,city_2))
print("city one is: {a} and city two is: {B}". format(a = city_1, B =city_2))

# PROCESS 4
print(f"City one is: {city_1} and City two is: {city_2}")

# process 5
num = 10.1212345234
print(num)
num = 10.1212345234
print("%.4f" % num)
print("%.2f" % num)
print("%d" % num)  # Output: 10.12

print("%.3f" %num)
print("%s" % city_2)
# list intro
num = [1,2.5,"python", True, 10]
print(type(num))
print(num[-2])
#list identity
print(num[2])
print(len(num))

#add in list

num.append(20)
print(num)

num.insert(0, "java")
print(num)
#names = ['Lukman', 'Navana']
num.extend(('Lukman', 'Navana', 'Omar'))
print(num)
num=['java', 1, 2.5, 'python', True, 10, 20, 'Lukman', 'Navana', 'Omar']
num2 = num.index('python')
num[num2]='c++'
print(num)
#update in list
num[3]="php"
print(num)

#remove in list
del num[]

print(num)
num.remove(2.5)
print(num)
num.pop(2)
print(num)
