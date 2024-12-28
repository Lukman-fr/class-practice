#string manupulation
'''
i love 'python'
i love "python"
'''


statement = 'I love "python"'
print(statement)
statement = "I love 'python'"
print(statement)

statement = "I love \"python\""
print(statement)
statement = ' we love \'python\''
print(statement)
#string operator
homeland ="I live in france but my homeland Bangladesh"
print(homeland.upper())
print(homeland.lower())
print(homeland.capitalize())
print(homeland.title())
print(homeland.count('i'))
print(homeland.count("l", 2,5))
print(homeland.replace("my", "your"))
print(homeland.isspace())
print(homeland.isdigit())
print(homeland.islower())
print(homeland.istitle())


