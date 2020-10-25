# 定义一个汽车类
class Car:
    # 构造方法，初始化汽车的使用能源和颜色
    def __init__(self, energy, color):
        self.energy = energy
        self.color = color

    # 定义汽车行走方法
    def run(self):
        print(f"这是一辆在使用{self.energy}能源行驶的{self.color}汽车")

# 定义一个石油能源的白色汽车
honda = Car('石油','白色')
# 调用汽车的行走方法
honda.run()

# 定义一个电能源的黑色汽车
audi = Car('电','黑色')
# 调用汽车的行走方法
audi.run()