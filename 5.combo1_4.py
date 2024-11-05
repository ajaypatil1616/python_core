#Q How to make tuple mutable 
"""
tuples = (1,2,3,4,5,6,7)
ls = list(tuples)
ls.append(8)
ls.append(9)
ls.append(10)
tuples = tuple(ls)
print(tuples)
"""
#Q type casting into all
ls = ["list",1,2,3,4,5,6]
t = ("tuple",1,2,3,45,6)
s = {"Set",1,2,3,45,6,5}
d ={"type":"dict","a":1,"b":2}

# print(list(t))
# print(list(s))
# print(list(d.items()))

# print(tuple(ls))
# print(tuple(s))
# print(tuple(d.items()))

# print(set(ls))
# print(set(t))
# print(set(d))
# print(set(d.values()))
# print(set(d.items()))

# print(dict(ls)) #gives error
# print(dict(t)) #gives error
# print(dict(s))

# print(d.keys())
# print(d.values())
# print(d.items())

# #finding from values
# if 1 in d.values():
#     print(d.keys())


#storing dictionary in a list 
# lsd = [{"name":"ajay"},{"name":"vijay"},{"name":"sourabh"}]
# lsd[1]["name"] = "shubham"
# print(lsd)
# print(dict(lsd))


#tuple unpacking
dictionary = {"name":"ajay","value":"akshay","salary":"supriya"}
list_dict = list(dictionary.items())
print(list_dict) #creates tuple of dictionary inside the list

for a,b in list_dict:#this is called tuple unpacking
    print(a,b)
 