formatter = "{} {} {} {}"

print(formatter.format(1, 2, 3, 4))  # 格式化字符串
print(formatter.format("one", "two", "there", "four"))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
      "我要吃",
      "煎饼果子",
      "要加两个蛋",
      "再加包辣条"
)
)