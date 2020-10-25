from tianlongbabu.tonglao import TongLao
import random



"""
规则：
1 虚竹和童姥依次遇到'无崖子', '李秋水', '丁春秋'
2 童姥在遇到丁春秋时，会用天山折梅手与之对打
3 虚竹只有在童姥一回合制失败时，才会用天山折梅手与丁春秋对打
"""

# 定义虚竹类，继承于童姥
class XuZhu(TongLao):
    # 传入虚竹的血量和攻击力给实例变量，同时初始化童姥的血量和武力值
    def __init__(self, xz_hp, xz_power):
        self.xz_hp = xz_hp
        self.xz_power = xz_power
        # 调用父类的构造方法初始化童姥的的血量和武力值
        super().__init__(random.randint(1000, 1500), random.randint(100, 150))

    # 定义虚竹念经方法
    def read(self):
        print('虚竹：罪过罪过~~~')

    # 虚竹和童姥看到不同人的不同表现
    def see_people(self, name):
        # 童姥遇到不同的人，则调用童姥类的see_people方法进行不同的处理
        # 判断返回值如果为True，则表示遇到丁春秋，要开打
        if super().see_people(name):
            # 童姥使用天山折梅手攻击丁春秋，随机初始化丁春秋的血量和攻击力
            dcq_hp = random.randint(1500, 2001)
            dcq_power = random.randint(100, 201)
            # 调用童姥的天山折梅手方法
            super().fight_zms(dcq_hp, dcq_power)
            # 如果童姥失败了，虚竹则使用天山折梅手进行攻击
            if self.tl_result is False:
                print('虚竹：童姥居然败了，丁春秋，那就让我来会一会你，为了公平，等你休息好后再打')
                print(f'丁春秋休息好了，当前血量{dcq_hp}')
                # 调用虚竹类的天山折梅手进行对打
                self.fight_zms(dcq_hp, dcq_power)
        # 虚竹遇到所有人都念经
        self.read()

    def fight_zms(self, dcq_hp, dcq_power):
        # 使用天山折梅手，虚竹的武力值增强10倍，血量减少一半
        self.xz_power *= 10
        self.xz_hp /= 2
        print(f'虚竹使用天山折梅手，武力值提升10倍，当前武力值:{self.xz_power},血量缩减2倍，当前血量为：{self.xz_hp}')
        # 丁春秋被打中，血量减少
        dcq_hp -= self.xz_power
        print(f"虚竹出招，攻击中丁春秋，丁春秋剩余血量：{dcq_hp}")
        print(f"丁春秋反击，一招打向虚竹,攻击力为{dcq_power}")
        # 虚竹被丁春秋打中，血量减少
        self.xz_hp -= dcq_power
        print("虚竹和天山童姥的这一回合结束，结果为：")
        # 判断此回合的结果：
        # 血量相等，则平局
        # xz_np大于dcq_hp，则虚竹获胜
        # 否则，丁春秋获胜
        if self.xz_hp == dcq_hp:
            print("平局，双方剩余血量一样多")
        elif self.xz_hp > dcq_hp:
            print(f"虚竹获胜，剩余血量：{self.xz_hp},丁春秋剩余血量：{dcq_hp}")
        else:
            print(f"丁春秋获胜，剩余血量：{dcq_hp},虚竹剩余血量：{self.xz_hp}")


if __name__ == '__main__':
    # 初始化虚竹会遇到的人
    people = ['无崖子', '李秋水', '丁春秋']
    # 初始化虚竹血量和攻击力
    xztl = XuZhu(random.randint(1500, 2000), random.randint(130, 180))

    # 依次循环虚竹和虚竹会看到的人
    for i in people:
        print(f"虚竹和童姥看到了{i}")
        # 调用虚竹类的see_people方法
        xztl.see_people(i)
