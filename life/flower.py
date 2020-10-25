# 定义一个花的类
class Flower:
    # 构造方法，初始化花的名字和颜色
    def __init__(self, name, color):
        self.name = name
        self.color = color

    # 定义一个开花的方法
    def flowering(self, season):
        print(f"这是{self.name},颜色是{self.color},这是在{season}开花的")


# 实例化一个牡丹对象
peony = Flower('牡丹', '大红色')
# 调用牡丹的开花方法
peony.flowering('春季')
# 实例化一个梅花对象
plum = Flower('梅花', '白色')
# 调用梅花的开花方法
plum.flowering('冬春季节')
