lst = [96, 39, 11, None, 82, 47, 20, 58, 2, 50]
lst[lst.index(None)] = sum([i for i in lst if i != None]) / len(lst)
print(lst)