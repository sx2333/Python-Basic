#coding=GBK
print("你多少岁?", end='')  # end=''的作用告诉print不要用换行符结束这一行跑到下一行去
age = input()            # 用户输入数值
print("你有多高？",end='')
height = float(input())  
height = int(height)
print("你的体重为？", end='')
weight = input()
print(f"so, 你今年{age}岁，身高为{height}，体重为{weight}.")

