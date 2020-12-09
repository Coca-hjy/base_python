'''
变量：
    定义：在python中用来存储数据的
    分类：Number(数字)--(int(有符号整形),(long(长整形[也可以代表八进制和十六进制])),float(浮点型),complex(复数))
         布尔类型(True,Flase)
          String(字符串)
          List(列表)
          Type(元祖)
          Dictionary(字典)
标示符和关键字：
    标示符：
        定义：开发人员在程序中自定义的一些符号和名称.标示符是自己定义的，如变量名，函数等等
        规则：标示符由字母，下划线和数字组成，且数字不能开头
        命名规则：见名如意
                 驼峰命名法
    关键字：
          定义：python一些具有特殊功能的标示符
          （and,as,assert,break,class,contiue,def,del,elif,else,except..）
          通过命令查看当前系统python的关键字
          （1.import keyword
            2.keyword.kwlist
          ）
格式化输出：
        格式化定义：在程序中，看到了%这样的操作，这就是python中格式化输出
            age=18
            name="xiaoming"
            print("我的姓名是%,年龄是%d" %(name,age))
        常用的格式化符号:(
            %c--符号   %s--通过str()字符串转换来格式化   %i--有符号十进制数
            %d--有符号十进制整数  %u--无符号十进制整数   %o--八进制整数
            %x--十六进制整数(小写字母)  %X--十六进制整数(大写字母)
            %e--索引符号(小写'e')  %E--索引符号(大写'E')  %f--浮点实数
            %g--%f和%e的简写     %G--%f和%E的简写
        换行输出：在输出的时候，如果有\n那么，此时的\n后的内容将会再另外一行显示
        print('123456------')  -->在一行显示
        print('123456\n------') -->\n后的将会在下一行显示
        )

        输入:
        1.raw_input():
                定义：在python中，获取键盘输入的数据的方法是采用raw_python函数
                如何使用:password=raw_python("请输入密码:")
                        print('您刚刚输入的密码是:',password)
                        注意:raw_input() 的小括号中放入的是，提示信息，用来在获取数据之前给用户的一个简单提示
                             raw_input()在从键获取了数据以后，会存放到等号右边的变量中
                             raw_input()会在用户输入的任何值都作为字符串来对峙
        1.2 input()
        input()与raw_input()类似，但是其接受的输入必须是表达式
        input()几首表达式输入，并把表达式的结果赋值给等号左边的变量
运算符：
        算术运算符，赋值运算符，符合赋值运算符
常用的数据类型转换：
                    函数                    说明
                    int(x[,base])           将x转换为一个整数
                    long(x[,base])          将x转换为一个长整数
                    float(x[,base])         将x转换到一个浮点数
                    complex(real[,imag])    创建一个复数
                    str(x)                  将对象x转换为一个字符串
                    repr(x)                 将对象x转换为表达式字符串
                    eval(str)               用来计算在字符串中的有效python表达式，并返回一个对象
                    typle(s)                将序列s转换为一个元祖
                    list(s)                 将序列s转换为一个列表
                    chr(x)                  将一个整数转换为一个字符
                    unichr(x)               将一个整数转换为一个unicode字符串
                    ord(x)                  将一个字符转换为它的整数值
                    hex(x)                  将一个整数转换为一个十六进制字符串
                    oct(x)                  将一个整数转换为一个八进制的字符串
判断语句介绍：满足则运行，不满足则不允许做

if 判断语句

比较，关系运算符:
逻辑运算符：

运算符	        逻辑表达式	    描述	                                                           实例
and	x and y	  布尔"与"         如果 x 为 False，x and y 返回 False，否则它返回 y 的计算值。	        (a and b) 返回 20。
or	x or y	  布尔"或"         如果 x 是 True，它返回 True，否则它返回 y 的计算值。	                (a or b) 返回 10。
not	not x	  布尔"非"         如果 x 为 True，返回 False 。如果 x 为 False，它返回 True。	        not(a and b) 返回 False
***********************************************************************************************************************

第二章：

2.1  if-else:
        使用格式：if

2.2 elif:
        if:xxxx
        elif:xxxx
        elif:xxxx
        直至条件满足
        注意点------->:可以与else使用；
                       elif必须与if一起使用，否则报错
2.3 if 嵌套：
(当需要满足条件去做事情的这种情况需要用if
当满足条件时做事情A，不满足条件做事情B的这种情况使用if-else) 

if应用：猜拳游戏
import random

    player = input('请输入：剪刀(0)  石头(1)  布(2):')

    player = int(player)

    computer = random.randint(0,2)

    # 用来进行测试
    #print('player=%d,computer=%d',(player,computer))

    if ((player == 0) and (computer == 2)) or ((player ==1) and (computer == 0)) or ((player == 2) and (computer == 1)):
        print('获胜，哈哈，你太厉害了')
    elif player == computer:
        print('平局，要不再来一局')
    else:
        print('输了，不要走，洗洗手接着来，决战到天亮')

2.5 循环介绍
        应用场景：  一般情况下，需要多次重复执行的代码，都可以使用循环的方式来完成
                    循环不是必须要使用的，但是为了提高代码的重复使用率，所以有经验的开发者都会采用循环
        eg：i = 0
            while i<10000:
            print("媳妇儿，我错了")
            i+=1
2.6 while循环：
                格式：  while条件：
                            条件A满足时，做事情A
                            条件B满足时，做事情B
                            条件C满足时，做事情C
                            .....
                代码解析：i = 0
                         while i<5:
                         print("当前是第%d次执行循环"%(i+1))
                         print("i=%d"%i)
                         i+=1
2.7 while循环应用：
                1.计算1-100的累计和(包含1-100)
                i = 1
                sum = 0
                while i<=100:
                    sum = sum + i
                    i += 1
                print("1~100的累积和为:%d"%sum)

                2. 计算1~100之间偶数的累积和（包含1和100）
                #encoding=utf-8

                i = 1
                sum = 0
                while i<=100:
                    if i%2 == 0:
                        sum = sum + i
                    i+=1

                print("1~100的累积和为:%d"%sum)
2.8 while循环的嵌套以及应用：
        while嵌套及应用：
            1.实现打印如下图形：
            *
            * *
            * * *
            * * * *
            * * * * *
            代码实现：
            i = 1
            while i<=5:

            j = 1
            while j<=i:
                print("* ",end='')
                j+=1

            print("\n")
            i+=1
        while嵌套应用二：
            九九乘法表代码实现：
                i = 1
                while i<=9:
                    j=1
                    while j<=i:
                        print("%d*%d=%-2d "%(j,i,i*j),end='')
                        j+=1
                    print('\n')
                    i+=1
2.9 for 循环：
            格式：
                    for 临时变量in列表或者字符串等：
                        循环满足条件时执行的代码
                    else：
                        循环不满足条件时执行的代码

2.10 break和continue
     break--->结束整个循环
     continue--->结束本次循环，继续执行下一次的循环

     注意点:break/continue只能用在循环中，除此以外不能单独使用
            break/continue在嵌套循环中，只对最近的一层循环起作用

    break在for循环中的用法：           
    name = 'dongGe'             
    for x in name:
        print('----')
        if x == 'g': 
            break
        print(x)
    break在while循环中的用法：
    i = 0
    while i<10:
        i = i+1
        print('----')
        print(i)

    continue在for循环中的用法:
    name = 'dongGe'
    for x in name:
        print('----')
        if x == 'g': 
            continue
        print(x)
    continue在while循环中的用法:
    i = 0
    while i<10:
        i = i+1
        print('----')
        if i==5:
            continue
        print(i)
'''
