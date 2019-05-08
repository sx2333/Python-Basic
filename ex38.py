ten_things = "apples oranges crows telephone light suger"

print("Wait there are not 10 things in that list, Let's fix that.")

stuff = ten_things.split(' ')  #单引号之间必须加空格，否则报错
more_stuff = ["day","night","song","frisbee","corn","banana","girl","boy"]

while len(stuff) != 10:
    next_one = more_stuff.pop()
    print("adding:", next_one)
    stuff.append(next_one)
    print(f"There are {len(stuff)} items now.")

print("THere we go:", stuff)

print("Let's do some things with stuff.")

print(stuff[1])  # 第二位
print(stuff[-1])  # 倒数第一位
print(stuff.pop())  # 列表第一位
print(' '.join(stuff)) #列表间加入空格输出
print('#'.join(stuff[3:5])) # 列表第四位和第六位加入#输出，是一个对列表进行切片的操作