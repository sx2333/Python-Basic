from sys import argv  #导入模块

script, filename = argv  # 拆包  

print(f"我们将要擦除文件{filename}.")
print("如果你不想进行此操作，敲击 CTRL-C(^c).")
print("如果你想要进行此操作，敲击RETURN.")  # 提示用户进行操作

input("?")

print("Opening the file...")
target = open(filename,'w')  # 打开目标输入文件并进入读写模式

print("清空此文件，Goodbye！")

target.truncate()  # 清空目标文件

print("Now I'm going to ask you for three lines.")  # 提示用户输入三行文字

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file.")
target.write(line1 + "\n" + line2 +"\n" + line3)  # 将用户输入的文字写入文件

print("And finally, we close it.")
target.close()  # 关闭文件

txt = open(filename)
print("让我们看下刚刚修改后文件的内容.")
print(txt.read())

print("再次输入你要查看的文件名")
filename_2 = input(">")
txt2 = open(filename_2)

print(txt2.read())
txt2.close()