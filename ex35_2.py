def start():
    print("你现在回到了高中。")
    print("现在有两个女孩，S和G。")
    print("你要选哪个？")

    choice = input("> ")

    if choice == "S" or "s":
        s_ending()
    elif choice == "G":
        G_ending()
    else:
        dead("洗洗睡吧。")

def s_ending():
    print("你选择了S，那么在高中毕业前你能说出那句话吗？")

    choice = input("> ")
    if "yes" in choice:
        print("你比我勇敢多了。")
    else:
        print("其实我们都一样。")

def G_ending():
    print("你居然选择了G，令人意外的选择。")
    dead("遗憾")
    exit(0)

def dead(why):
    print(why,"都是假的。")

start()
    
