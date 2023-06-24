li = [1, 2, 2, 4, 5]
print(list(dict.fromkeys(li)))
print(list(set(li)))
print(list(filter(lambda x: x != 2, li)))

while 2 in li:
    li.remove(2)
print(li)


