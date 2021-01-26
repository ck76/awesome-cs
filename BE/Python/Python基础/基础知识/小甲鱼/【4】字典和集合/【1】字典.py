# TODO 当索引不好用的时候 key calue登场
empty = {}
empty = {"key1": 'value1', "key2": 'value2', "key3": 'value3'}
print(type(empty))
dict1 = dict((("key1", "value1"), ("key2", "value2"), ("key3", "value3")))
print(dict1.get("key1"))
# 因为dict方法参数只能是一个序列，不能是多个
dict1 = dict(key1='value1', key2='value2', key3='value3')
print(dict1)

# TODO 内置的各种方法
print(dict1.fromkeys((1, 2, 3), ('x', 'y', 'z')))
print(dict1.fromkeys((1, 2, 3)))

print(dict1.keys())
print(dict1.values())
print(dict1.items())
dict1.update(key1="new Value1---------", key2="121212121212")
print(dict1)


def test(**params):
    print(params)


test(**{"key1": 'value1', "key2": 'value2', "key3": 'value3'})
