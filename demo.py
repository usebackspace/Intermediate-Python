a={'b':20, 'c':30,'d':50}
f={'b':20}
print(list(f.keys()))
print(list(a.keys()))


if list(f.keys()) in list(a.keys()):
    print(' lareday extd')
# elif f.keys not in a:
#     a.update(f)
# print(a)