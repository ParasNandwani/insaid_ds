import keyword
print("hello")
print(keyword.kwlist)
print(len(keyword.kwlist))
# not allowd in pyrhon  variable name like thid
# 99variable="hello"#invalid syntax
# print(99variable)
listOfStrings=['One','Two','Three','Four']
print(listOfStrings)
print(type(listOfStrings))
print(len(listOfStrings))
listOfStrings.append("Five")#insert at last
listOfStrings.insert(2,"Six")
print(listOfStrings)
print(type(listOfStrings))
print(len(listOfStrings))

listOfInt=[1,2,3,4,5,6]
listOfStrings.append(listOfInt)#append as another list
listOfStrings.extend(listOfInt)#extend as members of list
print(listOfStrings)
print(type(listOfStrings))
print(len(listOfStrings))

del listOfInt[3]
print(listOfInt)
print(listOfStrings)
print(type(listOfStrings))
print(len(listOfStrings))
print(listOfStrings.pop(1))
print(listOfStrings)
print(type(listOfStrings))
print(len(listOfStrings))
# reverse list
print(listOfStrings.reverse())
print(listOfStrings)

print(sorted(listOfStrings,reverse=True))# soriginal list wont be changed ad returns a new sorted list
print(listOfStrings)
print(listOfInt.sort())# changes the original list