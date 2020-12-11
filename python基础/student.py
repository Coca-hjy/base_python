

text="欢迎走入学生管理系统"
print(text)
while True:
        
    print("***********功能菜单************")
    print("1.录入学生信息")
    print("2.查找学生信息")
    print("3.删除学生信息")
    print("4.修改学生信息")
    print("5.排序")
    print("6.统计学生总人数")
    print("7.显示学生总体信息")
    print("0.退出系统")
    

    choice=int(input("请输入您选择的序列号:"))
    if choice == 1:
            # mark=[]
        username=input("输入您的名字:")
        id=input("请输入您的学生ID:")
        P_garde=int(input("输入您python成绩:"))
        E_garde=int(input("输入您英语成绩:"))
        C_python=int(input("输入您C语言成绩:"))
        C_choice=input("是否继继续添加y/n:")
            
        f1=open("text.txt","w",encoding="utf-8")
        
        a="username%s,id%s,P_grade%s,E_grade%s,C_python%s" %(username,id,P_garde,E_garde,C_python)
        print(f1.write(a))
    
        if C_choice == 'y':
            continue
            
        else:
            print("录入信息完毕!")
            break
            
    