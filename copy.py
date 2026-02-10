import copy
a=[[3,5],[8,16]]
b=copy.deepcopy(a)
b[0].append(10)
print(a)
print(b)
