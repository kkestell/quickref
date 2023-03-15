import collections

# Counter
c = collections.Counter(['a', 'b', 'c', 'a', 'b', 'b'])
print(c)  # Counter({'b': 3, 'a': 2, 'c': 1})
print(c['b'])  # 3

# defaultdict
d = collections.defaultdict(int)
d['a'] += 1
print(d['a'])  # 1

# OrderedDict
od = collections.OrderedDict([('a', 1), ('b', 2), ('c', 3)])
print(od)  # OrderedDict([('a', 1), ('b', 2), ('c', 3)])

# deque
d = collections.deque([1, 2, 3])
d.append(4)
d.appendleft(0)
print(d)  # deque([0, 1, 2, 3, 4])
print(d.pop())  # 4
print(d.popleft())  # 0

# namedtuple
Point = collections.namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print(p)  # Point(x=1, y=2)
print(p.x)  # 1

