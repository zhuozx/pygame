# 定义一个手机类
class Phone:
    # 构造方法，初始化手机的系统和颜色
    def __init__(self, system, color):
        self.system = system
        self.color = color

    # 手机拍照方法
    def photo(self):
        print(f"我在使用{self.system}系统的{self.color}手机在拍照")


# 创建一个iOS的手机对象
iphone = Phone('iOS', '白色')
# 调用拍照功能
iphone.photo()
# 创建一个Android的手机对象
android = Phone('Android', '黑色')
# 调用拍照功能
android.photo()
