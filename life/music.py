# 定义一个音乐类
class Music:

    # 构造方法，初始化实例变量:语言，歌手以及曲风
    def __init__(self, language, singer, style):
        self.language = language
        self.singer = singer
        self.style = style

    # 定义唱歌方法，输出是谁演唱的什么类型/什么歌名/什么风格的歌曲
    def sing(self, song):
        print(f'这是一首{self.singer}演唱的{self.language}类型的歌曲,这首歌的歌名为{song}，歌曲风格为{self.style}')


# 创建中国风音乐对象
chinese_music = Music('中国风', '周杰伦', '古典风格')
# 中国风音乐代表作
chinese_music.sing('青花瓷')

# 创建欧美风音乐对象
europe_music = Music('欧美风', 'Taylor Swift', '抒情歌曲')
# 欧美风音乐代表作
europe_music.sing('love story')
