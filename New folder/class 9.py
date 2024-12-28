#Dictionary
"""
key:value
unordered
unique key
"""
from xml.dom.minidom import ProcessingInstruction

myDict = {1:"python",
          2:"java",
          3:"c++",
          "name": ("Hasan Mahmud")

        }
print(myDict)

#2_value access dictionary

myDict = {"favourite_programing": ("python", "java", "c++",),
"name": 'Omar Zayan'}

print(myDict.keys())
print(myDict.values())
print(myDict.items())

print("name" in myDict.keys())
print('num' in myDict.keys())

mydict = {"nameFamily": ['omar', 'ayan','sidratul', 'Zayan', 'navana', 'Golsan'],
"mobileNumber": "0154856466342"}
print(mydict)

#update.value

myDict = {"favourite_programing": ("python", "java", "c++",),
"name": 'Omar Zayan '}
print(myDict)
myDict.update({'name':'omar zayan ayaan'})
print(myDict)
myDict['name']="Omar Zayaan"
print(myDict)
myDict["favourite"]="C+","php"
print(myDict)
myDict['email']="smlukman91@gmail.com"
print(myDict)
myDict['email']= "navanagolsnagmal"
print(myDict)


#dictionary value remove
"""
myDict.pop('name')
print(myDict)
del myDict["email"]
print(myDict)

myDict.clear()
print(myDict)
"""

#Dictionary method
myDict_copy = myDict.copy()
print(myDict)


'''
name: {pythom :1,
java  : 2}
'''

programming_language = {"python", "java", "C++"}
priority_of_programming_language=(1,0,1)
programming_dict = dict.fromkeys(programming_language, priority_of_programming_language)
print (programming_dict)

'''
"python":(1),
"java"  :(0),
'''
programming_zip = zip(programming_dict, priority_of_programming_language)
print(dict(programming_zip))


