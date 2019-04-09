def cheese_and_crackers(cheese_count, boxes_of_crackers): # 定义函数
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} crackers")
    print("就知道吃吃吃，胖不死你")
    print("Get a blanket. \n")

print("We can just give the function numbers directly:")
cheese_and_crackers(20, 30)  # 调用函数

print("现在让我们用脚本里的变量来试试。")
amount_of_cheese = 10  
amount_of_crackers = 40  # 声明变量

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print("我们可以在里面进行计算")
cheese_and_crackers(10 + 20, 6 - 5)  # 调用函数

print("我们可以在其中进行组合计算")
cheese_and_crackers(amount_of_cheese + 10, amount_of_crackers - 10)  # 调用函数

print("请输入cheese的值：")
salt_cheese = input(">")
print("请输入crackers的值：")
sweet_crackers = input(">")
cheese_and_crackers(salt_cheese, sweet_crackers)