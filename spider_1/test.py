import re


class Test:
    a = 1

    def s(self):
        a = 2
        print(a)

    def ss(self):
        self.a = 22
        print(self.a)

c = Test()
print(c.a)
c.s()
print(c.a)
c.ss()
print(c.a)

print('-------------------')

class Test1:
    a = 1
    b = 2
    def __init__(self):
        self.c = 3

d = Test1()
print(d.a)
print(d.b)
print(d.c)

a = {'a': 1}
for key, value in a.items():
    print(key)
    print(value)

print('+++++++++++++++')

a = '''<p><img src="http://res.ycw.com/app/images/book/breed/cat/M19/M1906.jpg" alt=""/></p><p>国内血统纯正的俄罗斯蓝猫相当稀少，要想获得一只纯正俄罗斯蓝猫相当不易。所以，一定要确保纯种繁殖，避免杂交，这样才能保证纯正的俄罗斯蓝猫数量在国内不断增加。有多年从业经验的医生指出，纯种的俄罗斯蓝猫已经非常罕见，市面上见到的号称俄罗斯蓝猫的猫多由英国短毛猫配种而来。
    购买仅仅是根据毛色来鉴别是不正确的，不要忘记问宠物店或者原主人出示出生证和血统证。&nbsp;</p><p><br/></p>'''
pat = re.compile('<p>\s*([\u4a00-\u9fa5]+.*)\s*</p>', re.S)

b = re.findall(pat, a)
print(b)

