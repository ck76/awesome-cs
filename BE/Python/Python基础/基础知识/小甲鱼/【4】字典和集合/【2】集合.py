#
empty = {}
print(type(empty))
empty = {1, 2, 3, 4, 5}
print(type(empty))

var = set([1, 2, 3, 4])
print(var)

#  TODO 访问集合
def fun():
    for each in empty:
        print(each)

var =frozenset(var)
print(var)
# var.add(6)