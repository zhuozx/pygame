import random


# 天山童姥类，
class TongLao:

    '''
    传入天山童姥的血量和攻击力给实例变量
    tl_hp表示童姥血量
    tl_power表示童姥攻击力
    tl_result表示童姥是否胜利，默认胜利
    '''
    def __init__(self, tl_hp, tl_power):
        self.tl_hp = tl_hp
        self.tl_power = tl_power
        self.tl_result = True

    # 天山童姥看到不同人时有不同的表现
    # 遇到”无崖子”，则打印，“师弟！！！！”
    # 遇到”李秋水”，则打印，“师弟是我的！”
    # 遇到”丁春秋”，则打印，“叛徒！我杀了你”
    # False表示不开打，True表示开打
    def see_people(self, name):
        if name == '无崖子':
            print("师弟！！！！")
            # 返回False，表示不是遇到丁春秋，不开打
            return False
        elif name == '李秋水':
            print('师弟是我的！')
            return False
        elif name == '丁春秋':
            print('叛徒！我杀了你')
            # 返回True，表示遇到丁春秋，开打
            return True

    def fight_zms(self, dcq_hp, dcq_power):
        # 使用天山折梅手，童姥的武力值增强10倍，血量减少一半
        self.tl_power *= 10
        self.tl_hp /= 2
        print(f'天山童姥使用天山折梅手，武力值提升10倍，当前武力值:{self.tl_power},血量缩减2倍，当前血量为：{self.tl_hp}')
        # 丁春秋被打中，血量减少
        dcq_hp -= self.tl_power
        print(f"天山童姥出招，攻击中丁春秋，丁春秋剩余血量：{dcq_hp}")
        print(f"丁春秋反击，一招打向天山童姥,攻击力为{dcq_power}")
        # 天山童姥被丁春秋打中，血量减少
        self.tl_hp -= dcq_power
        print("天山童姥和丁春秋的这一回合结束，结果为：")
        # 判断此回合的结果：
        # 血量相等，则平局
        # tl_np大于dcq_hp，则童姥获胜
        # 否则，丁春秋获胜
        if self.tl_hp == dcq_hp:
            print("平局，双方剩余血量一样多")
        elif self.tl_hp > dcq_hp:
            print(f"天山童姥获胜，剩余血量：{self.tl_hp},丁春秋剩余血量：{dcq_hp}")
        else:
            print(f"丁春秋获胜，剩余血量：{dcq_hp},天山童姥剩余血量：{self.tl_hp}")
            # 童姥败了，虚竹类知道后，虚竹就会出手
            self.tl_result = False


if __name__ == '__main__':
    # 初始化天山童姥会遇到的人
    people = ['无崖子', '李秋水', '丁春秋']
    # 初始化天山童姥的血量和攻击力
    tonglao = TongLao(random.randint(1000, 1500), random.randint(100, 150))

    # tonglao.see_people(random.choice(people))

    # 依次循环天山童姥会看到的人
    for i in people:
        # 调用童姥类的see_people方法，显示看到不同人的不同反应
        # 判断如果为True，则表示遇到丁春秋，要开打
        if tonglao.see_people(i):
            # 使用天山折梅手攻击丁春秋，随机初始化丁春秋的血量和攻击力
            dcq_hp = random.randint(1500, 2001)
            dcq_power = random.randint(100, 201)
            # 返回一回合的胜负结果
            tonglao.fight_zms(dcq_hp, dcq_power)
