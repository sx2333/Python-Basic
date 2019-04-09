def add(a, b):  # 定义各类函数
    print(f"ADDING {a} + {b}")
    return a + b

def subtract(a, b):
    print(f"SUBTRACTING {a} - {b}")
    return a - b

def multiply(a, b):
    print(f"MULTIPLYING {a} * {b}")
    return a * b

def divide(a, b):
    print(f"DIVIDING {a} / {b}")
    return a / b

add(30, 26)
print("让我们用这些函数做些计算。")

age = add(28, 7)  # 目前的理解为python从右往左读代码时先调用了add函数，所以控制台先打印出了‘ADDing {a} + {b}’
height = subtract(178, 8)
weight = multiply(80, 2)
iq = divide(100, 2)

print(f"age:{age}, height:{height}, weight:{weight}, iq:{iq}")

# A puzzle for the extra credit, type it in anyway.
print("Here is a puzzle.")

what = multiply(weight, divide(iq, 2))

# 简单的数学公式计算
sample = subtract(add(24, divide(34, 100)), 1023)