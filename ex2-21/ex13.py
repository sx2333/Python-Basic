from sys import argv  # 引入模块
# read the WYSS section for how to run this
script, first, second, third = argv  #解包 

print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)

# 记住在命令行(vscode下面的终端)输入 python ex13.py _ _ _(横线上为三个变量)