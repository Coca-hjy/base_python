'''
    类的定义
'''
'''
class Car:
    pass
class Car(object):
    def getCarInfo(self):
        print("这是一辆红色的smart")
    def move(self):
        print("车子在移动中..")
    def toot(self):
        print("车在鸣笛...嘟嘟嘟...")
BMW=Car()
BMW.color="红色"
BMW.wheelNum = 4
BMW.move()
BMW.toot()
print(BMW.color)
print(BMW.wheelNum)
'''

# 定义汽车类
# class Car:

#     def __init__(self):
#         self.wheelNum = 4
#         self.color = '蓝色'

#     def move(self):
#         print('车在跑，目标:夏威夷')

# # 创建对象
# BMW = Car()
# BMW.move()

# print('车的颜色为:%s'%BMW.color)
# print('车轮胎数量为:%d'%BMW.wheelNum)

class Animal:

    # 方法
    def __init__(self, name):
        self.name = name

    def printName(self):
        print('名字为:%s'%self.name)

# 定义一个函数
def myPrint(animal):
    animal.printName()


dog1 = Animal('西西')
myPrint(dog1)

dog2 = Animal('北北')
myPrint(dog2)
