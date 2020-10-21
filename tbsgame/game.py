from random import randint,choice

"""
规则：
1、双方初始hp随机选取
2、双方每次攻击力随机在100至200之间
3、攻击可随机失效
4、任一方的hp小于等于0，则游戏结束
"""

#判断是否游戏结束
def judge(my_hp, enemy_hp):
    """
    :param my_hp: 我方剩余血量
    :param enemy_hp: 敌方剩余血量
    :return: True表示游戏结束，False表示游戏继续
    1、如果my_hp和enemy_hp均为0，则平局
    2、如果只有my_hp小于等于0，则敌方胜利
    3、如果只有enemy_hp小于等于0，则我方胜利
    4、以上情况均没有出现，则游戏继续
    """
    if my_hp == 0 and enemy_hp == 0:
        print("游戏结束!双方平局")
        return True
    elif my_hp > 0 and enemy_hp <= 0:
        print(f"游戏结束!我方胜利，我方剩余血量：{my_hp}")
        return True
    elif my_hp <= 0 and enemy_hp > 0:
        print(f"游戏结束!敌方胜利，敌方剩余血量：{enemy_hp}")
        return True
    else:
        return False


def fight(my_hp, enemy_hp):
    #初始化回合次数
    count = 1
    #如果游戏不结束，则一直循环
    while True:
        #输出当前为第几回合，并初始化此回合中我方和敌方的攻击力
        print(f"第{count}回合开始：")
        my_power = randint(100, 200)
        enemy_power = randint(100, 200)
        #随机判断我方此次攻击是否有效，1为有效，0为无效
        if randint(0, 1):
            enemy_hp = enemy_hp - my_power
            print(f"我方攻击有效，攻击力为{my_power},敌方剩余血量：{enemy_hp}")
        else:
            print(f"我方攻击无效，敌方剩余血量：{enemy_hp}")
        #调用judge函数判断游戏是否结束
        if judge(my_hp, enemy_hp):
            break
        # 随机判断敌方此次攻击是否有效，1为有效，0为无效
        if randint(0, 1):
            my_hp = my_hp - enemy_power
            print(f"敌方攻击有效，攻击力为{enemy_power},我方剩余血量：{my_hp}")
        else:
            print(f"敌方攻击无效，我方剩余血量：{my_hp}")
        # 调用judge函数判断游戏是否结束
        if judge(my_hp, enemy_hp):
            break

        count += 1


if __name__ == '__main__':
    # 初始化开局数据
    hp = [x for x in range(1000,2000)]
    my_hp = choice(hp)
    enemy_hp = choice(hp)
    print(f"我方总血量：{my_hp}，敌方总血量：{enemy_hp}")
    fight(my_hp, enemy_hp)
