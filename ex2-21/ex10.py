tabby_cat = "\tI'm tabbed in."  # \t表示将光标向右移动一个制表符位
persian_cat = "I'm split\non a table"  # \n表示将光标移到下一行的开头
bcakslash_cat = "I'm \\ a \\ cat."  # \\可以打印出一个反斜杠

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishes
\t* Catnip\n\t* Grass  
"""  #这里单引号或者双引号皆可，看各人风格。这里的换行是直接用空白换行

print(tabby_cat)
print(persian_cat)
print(bcakslash_cat)
print(fat_cat)