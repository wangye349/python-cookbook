# though _ is meaningless, the string's length needs to be larger than the variables

a, b, c, d, e, _ = 'hello '
pass


def drop_first_last(grades):
    first, *middle, last = grades
    return sum(middle) / len(middle)


def search_tail(items):
    head, *tail = items
    return len(tail) if head else tail


items_test_first = [1, 2, 3, 4, 5]
items_test_second = [0, 1, 2, 3, 4]

search_a = search_tail(items_test_first)
search_b = search_tail(items_test_second)
pass

from collections import deque

a = deque(maxlen=2)
a.append(1)
a.append(2)
a.append(3)
del a[1]
pass

# find the largest or the smallest numbers of a set/array/list/dict
# usually the number of searching N is way smaller than the length of set
import heapq

a = [2, 5, 1, 7, 8, -2, 45, 6, 23, 77, 28]
b = heapq.nlargest(1, a)[0]
b = max(a)  # this is easier
c = heapq.nsmallest(2, a)
d = heapq.heapify(a)

# noinspection SpellCheckingInspection
portfolio = [
    {'name': 'IBM', 'price': 91.1},
    {'name': 'AAPL', 'price': 32.09},
    {'name': 'FB', 'price': 45.2}
]
c = heapq.nlargest(1, portfolio, key=lambda x: x['price'])[0]
pass

import heapq


class PriorityQueue:

    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue[-1])


pass

from collections import OrderedDict

d = OrderedDict()

d['foo'] = 1
d['bar'] = 3
d['spam'] = 2
d['grok'] = 0

for key in d:
    print(key, d[key])
pass

from collections import defaultdict

d = defaultdict(list)
d['a'].append(1)
d['b'].append(2)
d['a'].append(3)

d = defaultdict(set)
d['a'].add(2)
d['b'].add(3)
d['a'].add(1)
pass

# noinspection SpellCheckingInspection
prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55
}

# zip create a iterator, and this can't be used for 2 times
min_price = min(zip(prices.values(), prices.keys()))
max_price = max(zip(prices.values(), prices.keys()))

# name a slice
from random import randint, shuffle
a = [randint(1,100) for _ in range(10)]
shuffle(a)
a_slice = slice(3, 8)
b = a[a_slice]
pass
