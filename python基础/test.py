'''
username=input("请您输入用户名:")
password=input("请您输入密码:")
if username=="小王" and password=="12345":
    print("欢迎来到我的世界")
else:
    print("输入错误！")
'''
# i = 1
# while i<=5:

#         j = 1
#         while j<=i:
#             print("* ",end='')
#             j+=1

#         print("\n")
        
#         i+=1

#typle练习
zodaic=("摩羯座","水瓶座","双鱼座","白羊座","金牛座","双子座","巨蟹座","狮子座","处女座","天秤座","天蝎座","射手座")
zodaic_days=((1,20),(2,19),(3,21),(4,20),(5,21),(6,22),(7,23),(8,23),(9,23),(10,24),(11,23),(12,22))
month=int(input("请输入您的出生月份:"))
day=int(input("请输入您的出生日期:"))

# index=0
# for zodiac_days in zodiac_days:
#     if month == 12 and day > 22:
#         index = 0
#     elif (month,day) > zodiac_days:
#         index += 1
# print(zodaic[index])

n=0
while (month,day) > zodaic_days[n]:
    if month ==12 and day >22:
        break
    n += 1
print(zodaic[n])