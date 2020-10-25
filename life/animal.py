#定义动物类
class Animal:
    # 构造方法，初始化实例变量，指定什么类型的歌曲
    def __init__(self, name, way):
        self.name = name
        self.way = way

    # 定义动物行走方式方法
    def way_to_walk(self):
        print(f'这只动物是{self.name}，它是通过{self.way}的方式行动的')


# 创建狗的对象
dog = Animal('狗', '四肢奔跑')
# 显示狗的行动方式
dog.way_to_walk()

# 创建鸟的对象
bird = Animal('鸟', '翅膀飞翔')
# 显示鸟的行动方式
bird.way_to_walk()
