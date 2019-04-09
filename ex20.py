from sys import argv  # 导入模块

script, input_file = argv  # 拆包

def print_all(f):  # 定义函数print_all，作用是用来读取文件内容
    print(f.read())

def rewind(f):  # 定义函数rewind，作用是用来将文件的指针指回开头
    f.seek(0)

def print_a_line(line_count, f):  # 定义函数print_a_line，line_count用来接收要读取的行数，f用来接收要读取的文件名。
    print(line_count, f.readline(), end="")  # 注意 end="" ，在readline()函数返回的内容中包含文件本来就含有\n，print在打印是会添加一个\n

current_file = open(input_file)  # 打开文件input_file

print("First let's print the whole file:\n")

print_all(current_file)  # 调用函数pint_all读取文件并打印

print("Now let's rewind, kind of like a tape.")
rewind(current_file)  # 将文件的指针调回开头

print("Let's print three lines:")

current_line = 1
print_a_line(current_line, current_file)

current_line += 1  # "+="这个符号的作用为两个值相加再将这个值赋值给左边的变量
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

current_file.close()
