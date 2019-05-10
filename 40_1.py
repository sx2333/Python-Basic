class song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:  #for line in 遍历字段中的每一行
            print(line)

happy_bday = song(["Happy birthday to you",
                   "I don't want to get sued",
                   "So I'll stop right there"])
                # happy_bday = song() 意指将happy_day设为song的一个实例
                # foo = x() 将foo设为类x的实例

bulls_on_parade = song(["They rally around the familly",
                        "with pockets full of shells"])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()