# this one is like your scripts with argv
def print_two(*args):  # def用来创建一个函数(def即define)，print_two为函数的名字，（）中的*args为变量名
    arg1, arg2 = args  # 对比print_two()和print_two_again二者变量的区别
    print(f"arg1: {arg1}, arg2: {arg2}")

# ok, that *args is actually pointless, we can just do this
def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")

# this just takes one argument
def print_one(arg1):
    print(f"arg1: {arg1}")

# this one takes no arguments
def print_none() :
    print("I got noting'.")

print_two("Zed","Shaw","zhang")  # 调用这个函数
print_two_again("ZED","Shaw")
print_one("first!")
print_none()

# 这个函数的作用就是简单的接收参数并打印