from sys import argv  # 导入模块

script, filename = argv  # 拆包

txt = open(filename)  # 打开用户输入的文件，创建一个file对象

print(f"这是你的文件{filename}")  # 提示
print(txt.read())  # 读取文件
txt.close()  # 关闭文件

print("请再次输入文件的名称")
file_again = input(">")  # 将用户输入的值赋值给file_again

txt_again = open(file_again)  # 打开用户输入的文件，创建一个file对象

print(txt_again.read())  # 读取文件
txt_again.close()  # 关闭文件
