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


#字符串，列表，元祖，字典
#3.2 字符串输出
# name="xiaoming"
# position="讲师"
# address="北京市昌平区建材城西路金燕龙办公楼一层"

# print("------------------")
# print("姓名:%s" %name)
# print("职位:%s" %position)
# print("地址:%s" %address)
# print("------------------")

# #3.3 字符串输入
# userName = input('请输入用户名:')
# print("用户名为：%s"%userName)

# password = input('请输入密码:')
# print("密码为：%s"%password)

#3.8 列表的常规操作
#append
# A = ['xiaoWang','xiaoZhang','xiaoHua']

# print("-----添加之前，列表A的数据-----")
# for tempName in A:
#     print(tempName)

# #提示、并添加元素
# temp = input('请输入要添加的学生姓名:')
# A.append(temp)

# print("-----添加之后，列表A的数据-----")
# for tempName in A:
#     print(tempName)
#typle练习
'''
zodiac=("摩羯座","水瓶座","双鱼座","白羊座","金牛座","双子座","巨蟹座","狮子座","处女座","天秤座","天蝎座","射手座")
zodiac_days=((1,20),(2,19),(3,21),(4,20),(5,21),(6,22),(7,23),(8,23),(9,23),(10,24),(11,23),(12,22))
month=int(input("请输入您的出生月份:"))
day=int(input("请输入您的出生日期:"))

# index=0
# for zodiac_days in zodiac_days:
#     if month == 12 and day > 22:
#         index = 0
#     elif (month,day) > zodiac_days:
#         index += 1
# print(zodiac[index])

n=0
while (month,day) > zodiac_days[n]:
    if month ==12 and day >22:
        break
    n += 1
print(zodiac[n])
'''

#接收用户输入的年月日，判断用户的星座和生肖


# chinese_zodiac="猴鸡狗猪鼠牛虎兔龙蛇马羊"
# zodiac=("摩羯座","水瓶座","双鱼座","白羊座","金牛座","双子座","巨蟹座","狮子座","处女座","天秤座","天蝎座","射手座")
# zodiac_days=((1,20),(2,19),(3,21),(4,20),(5,21),(6,22),(7,23),(8,23),(9,23),(10,24),(11,23),(12,22))
# year=int(input("请输入您的出生年份:"))
# month=int(input("请输入您的出生月份:"))
# day=int(input("请输入您的出生日期:"))
# n=0
# while zodiac_days[n] < (month,day):
#     if month == 12 and day > 25:
#         break
#     n += 1
# print("您的生肖是%s,您的星座是%s"%(chinese_zodiac[year%12],zodiac[n]))





#dict
#输入1 继续运行此操作   输入0 退出
'''
    无限次接收输入用户的年月日，判断用户的生肖和星座，并且统计出各个生肖和星座的人数
'''

'''
chinese_zodiacs="猴鸡狗猪鼠牛虎兔龙蛇马羊"
zodiacs=("摩羯座","水瓶座","双鱼座","白羊座","金牛座","双子座","巨蟹座","狮子座","处女座","天秤座","天蝎座","射手座")
zodiac_days=((1,20),(2,19),(3,21),(4,20),(5,21),(6,22),(7,23),(8,23),(9,23),(10,24),(11,23),(12,22))

# chinese_zodiacs_dict={}
# for chinese_zodiac in chinese_zodiacs:
#     chinese_zodiacs_dict[chinese_zodiac]=0
# print(chinese_zodiacs_dict)



# {key:value:for key in keys}
#字典的推导式

chinese_zodiacs_dict={chinese_zodiac:0 for chinese_zodiac in chinese_zodiacs}
zodiac_dict={zodiac:0 for zodiac in zodiacs}
# print(chinese_zodiacs_dict)
# print(zodiac_dict)

while True:
    year=int(input("请您输入你的呢出生年份："))
    month=int(input("请输入您的出生月份:"))
    day=int(input("请输入您的出生日期:"))

    num=0
    for zodiac_day in zodiac_days:
        if (month,day) > zodiac_day:
            num += 1
        elif month == 12 and day > 22:
            num = 0
    chinese_zodiacs_dict[chinese_zodiacs[year%12]] += 1
    zodiac_dict[zodiacs[num]] += 1

    print(chinese_zodiacs_dict)
    print(zodiac_dict)
'''
# zodiac_dict={}









#第三章作业集锦
# a="hello world"
# print(a.count("l"))
# print(a.count("h"))

# sheng=input("请输入您的家庭省份:")
# shi=input("请输入您的家庭市区:")
# xian=input("请输入您的家庭县区域:")

# print("最终您的家庭地址是:%s" %sheng+shi+xian)


'''
print("欢迎来到我的世界！")
username=input("请输入您的账号:")
password=input("请输入您的密码:")
if username == "472458040" and password == "123":
    print("登录成功！")
    choice=["1.添加名片","2.删除名片","3.修改名片","4.查询名片","5.退出系统"]
    print(choice)
    input("请输入您要选择的序列号:")
        # if choice == 0:
        #     print("请您添加您想要的内容：")
        # else:
        #     print(choice)
        #     input("请输入您要选择的序列号:")
    
else:
    print("登录失败,请重新登录:")
    username=input("请输入您的账号:")
    password=input("请输入您的密码:")
    
'''

while True:
    print("*"*30)
    
    print("1.添加名片")
    print("2.删除名片")
    print("3.修改名片")
    print("4.查询名片")
    print("5.退出系统")
    a=int(input("请输入您需要的序列号:"))
    
    if  a == 5:
        print("退出成功!")
        break




