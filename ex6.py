types_of_people = 10   # 声明变量人种数量
x = f"there are {types_of_people} types of people."  # 将格式化后的字符串赋值给x

binary = "binary"  # 声明变量binary
do_not = "don't"  # 声明变量do_not
y = f"Those who know {binary} and those who {do_not}."  #将格式化后的字符串赋值给y

print(x)
print(y)

print(f"I said: {x}")
print(f"I also said: '{y}'")

hilarious = "False"
joke_evaluation = "Isn't that joke so funny?! {}"

print(joke_evaluation.format(hilarious))  #

w = "This is the left side of..."
e = "a string with a right side."
print(w + e)