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

eeee          
'''