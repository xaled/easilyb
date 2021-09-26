from easilyb.serialization.map import Map
import json


class Test(Map):
    def __init__(self, a, b, c=0):
        super(Test, self).__init__()
        self.a = a
        self.b = b
        self.c = c


t = Test(1, 2, 3)
print(t)
s = json.dumps(t)
print(s)
t2 = json.loads(s)
print(t2)
print(t == t2)
t3 = Test.from_dict(t2)
print(t3)
print(t == t3)
