cars = 100           #声明总计可用车辆
space_in_a_car = 4.0 #声明一辆车的总计可做人数
drivers = 30         #声明司机总数
passengers = 90      #声明乘客总数
cars_not_driven = cars - drivers  #声明空闲车辆
cars_driven = drivers  
carpool_capacity = cars_driven * space_in_a_car #声明总计可载人数
average_passengers_per_car = passengers / cars_driven #声明每辆车的平均载人数

print("There are",cars,"cars available.")   
print("There are only",drivers,"drivers available.")
print("There will be",cars_not_driven,"empty cars today.")
print("We can transport",carpool_capacity,"people today.")
print("we have",passengers,"to carpool today.")
print("We need to put about",average_passengers_per_car,"in each car.")