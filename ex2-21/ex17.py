from sys import argv
from os.path import exists

script, from_file, to_file = argv

print(f"Copying from {from_file} to {to_file}")

# 如何将两行合并成一行?
in_file = open(from_file)  # 打开文件
indata = from_file.read()  # 读取文件内容，并将值赋给一个变量

print(f"The input file is {len(indata)} bytes long")  # len()查看数据长度

print(f"Does the output file exist? {exists(to_file)} ")
print("ready,hit return to continue, hit CTRL-C to abort.")
input()

out_file = open(to_file, 'w')  # 文件进入读写模式
out_file.write(indata)  # 将indata的数据，即from_file的内容，写入to_file文件

print("好了，文件已经处理完了。")

out_file.close()
in_file.close()  # 关闭文件，记住关闭open()函数打开的文件