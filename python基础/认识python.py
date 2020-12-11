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


第三章：字符串,列表,元祖,字典

3.1 字符串介绍
   eg:接收用户输入的年份，判断用户的生肖
      鼠牛虎兔龙蛇马羊猴鸡狗猪
      
      chinese_zodiac="猴鸡狗猪鼠牛虎兔龙蛇马羊"
      str_year=input("请输入您的出生年份:")
      int_year=int(str_year)
      zodiac_num=int_year%12

      print("您的生肖是%s"%chinese_zodiac[zodiac_num])

      
    字符串的定义:双引号或者单引号中的数据，就是字符串
3.2 字符串的输出 
3.3 字符串的输入
3.4 下标和切片
        1.下标：
            定义:如果想取出部分字符，那么可以通过下标的方法且oython中下标从0开始
        2.切片
            定义：切片是指对操作的对象截取其中一部分的操作。字符串，列表，元祖都支持切片操作
            切片的语法：[起始：结束：步长]
3.5 字符串常规操作
     1.find--检测str是否包含在mystr中,如果是返回开始的索引值,否则返回-1
             mystr.find(str,0,len(mystr))
     2.index--跟find()方法一样，只不过如果str不在mystr中会报一个异常
     3.count--返回str在start和end之间在mystr里面出现的次数
     4.replace--在mystr中的str1替换成str2，如果count指定，则替换不超过count次
     5.split--以str为分隔符切片 mystr，如果 maxsplit有指定值，则仅分隔 maxsplit 个子字符串
     6.capitalize--把字符串的第一个字符大写
     7.title--把字符串的每个单词首字母大写
     8.startswith--检查字符串是否是以 obj 开头, 是则返回 True，否则返回 False
     9.endswith--检查字符串是否以obj结束，如果是返回True,否则返回 False
     10.lower--转换 mystr 中所有大写字符为小写
     11.upper--转换 mystr 中的小写字母为大写
     12.strip--删除mystr字符串两端的空白字符
     13.partition--把mystr以str分割成三部分,str前，str和str后
     14.splitlines--按照行分隔，返回一个包含各行作为元素的列表
     15.isalpha--如果 mystr 所有字符都是字母 则返回 True,否则返回 False
     16.isdigit--如果 mystr 只包含数字则返回 True 否则返回 False
     17.isalnum--如果 mystr 所有字符都是字母或数字则返回 True,否则返回 False
     18.isspace--如果 mystr 中只包含空格，则返回 True，否则返回 False
     19.join--mystr 中每个字符后面插入str,构造出一个新的字符串

3.6 列表介绍
    1.列表的格式
    2.打印列表(按索引)
3.7 列表的循环遍历及常规操作
    1.使用for循环:
    namesList = ['xiaoWang','xiaoZhang','xiaoHua']
    for name in namesList:
        print(name)
    2.使用while循环:
    namesList = ['xiaoWang','xiaoZhang','xiaoHua']

    length = len(namesList)

    i = 0

    while i<length:
        print(namesList[i])
        i+=1
    3.列表的相关操作
        1.添加元素("增"append, extend, insert)
        2.修改元素
        3.查找元素("查"in, not in, index, count)
        4.删除元素("删"del, pop, remove)
        5.排序(sort, reverse)
3.10-3.16 元祖，字典
    1.简介：Python的元组与列表类似，不同之处在于元组的元素不能修改。元组使用小括号，列表使用方括号
    2.访问元祖按索引
      修改元祖--python中不允许修改元组的数据，包括不能删除其中的元素
      元组的内置函数count, index--index和count与字符串和列表中的用法相同
    3.字典
        1.根据键访问值，若访问不存在的键，则会报错。在我们不确定字典中是否存在某个键而又想获取其值时，可以使用get方法，还可以设置默认值
        2.修改元素
          添加元素
          删除元素(del删除指定的元素   clear清空整个字典)
          len()--测量字典中，键值对的个数
          keys--返回一个包含字典所有KEY的列表
          values--返回一个包含字典所有value的列表
          items--返回一个包含所有（键，值）元祖的列表
          has_key--dict.has_key(key)如果key在字典中，返回True，否则返回False


4.函数
    a.函数的使用：如果在开发程序时，需要某块代码多次，但是为了提高编写的效率以及代码的重用，所以把具有独立功能的代码块组织为一个小模块，这就是函数
    b.定义函数的格式：
                    def 函数名():
                        代码
      调用函数:定义了函数之后，就相当于有了一个具有某些功能的代码，想要让这些代码能够执行，需要调用它,调用函数很简单的，通过 函数名() 即可完成调用
    c.四种函数的类型:
                1.无参数，无返回值的函数(此类函数，不能接受参数，也没有返回值，一般情况下，打印提示灯类似的功能，使用这类的函数)
                  def printMenu():
                    print('--------------------------')
                    print('      xx涮涮锅 点菜系统')
                    print('')
                    print('  1.  羊肉涮涮锅')
                    print('  2.  牛肉涮涮锅')
                    print('  3.  猪肉涮涮锅')
                    print('--------------------------')
                2.无参数，有返回值的函数(此类函数，不能接收参数，但是可以返回某个数据，一般情况下，像采集数据，用此类数据)
                3.有参数，无返回值的函数(此类函数，能接收参数，但不可以返回数据，一般情况下，对某些变量设置数据而不需结果时，用此类函数)
                4.有参数，有返回值的函数(此类函数，不仅能接收参数，还可以返回某个数据，一般情况下，像数据处理并需要结果的应用，用此类函数)

                def calculateNum(num):

                    result = 0
                    i = 1
                    while i<=num:

                        result = result + i

                        i+=1

                    return result

                result = calculateNum(100)
                print('1~100的累积和为:%d'%result)
            6.总结:
                函数根据有没有参数，有没有返回值可以相互组合
                定义函数时，是根据实际的功能需求来设计的，所以不同开发人员编写的函数类型各不相同
                
4.9 局部变量，全局变量
    a.局部变量，就是在函数内部定义的变量;
      不同的函数，可以定义相同的名字的局部变量，但是各用个的不会产生影响;
      局部变量的作用，为了临时保存数据需要在函数中定义变量来进行存储，这就是它的作用.
    b.在函数外边定义的变量叫做全局变量;
      全局变量能够在所有的函数中进行访问;
      如果在函数中修改全局变量，那么就需要使用global进行声明，否则出错;
      如果全局变量的名字和局部变量的名字相同，那么使用的是局部变量.
    c.可变类型的全局变量
    d.总结:在函数中不使用global声明全局变量时不能修改全局变量的本质是不能修改全局变量的指向，即不能将全局变量指向新的数据。
      对于不可变类型的全局变量来说，因其指向的数据不能修改，所以不使用global时无法修改全局变量。
      对于可变类型的全局变量来说，因其指向的数据可以修改，所以不使用global时也可修改全局变量。      
4.15 匿名函数
    Lambda函数能接收任何数量的参数但只能返回一个表达式的值；

    匿名函数不能直接调用print，因为lambda需要一个表达式；

    lambda x,y:x+y
4.16 函数使用时的注意事项
        a.自定义函数：无参数，无返回值
                     无参数有返回值(一个函数到底有没有返回值，就看有没有return，因为只有return才可以返回数据；在开发中往往根据需求来设计函数需不需要返回值;函数中，可以有多个return语句，但是只要执行到一个return语句，那么就意味着这个函数的调用完成)
                     有参数，无返回值(在调用函数时，如果需要把一些数据一起传递过去，被调用函数就需要用参数来接收;参数列表中变量的个数根据实际传递的数据的多少来确定)
                     有参数有返回值
                     函数名不能重复
        b.调用函数: 调用的方式为:函数名([实参列表])
                    调用时，到底写不写实参(如果调用的函数在定义时有形参,那么在调用的时候就应该传递参数)
                    调用时，参数的个数和先后顺序应该和定义函数中要求的一致
                    如果调用的函数有返回值，那么就可以用一个变量来进行保存这个值
        c.作用域
            在一个函数中定义的变量，只能在本函数中用(局部变量)；
            在函数外定义的变量，可以在所有的函数中使用(全局变量)


第五章
5.1文件的打开和关闭
        open()
        格式：1.打开文件，或者新建立一个文件
              2.读/写数据
              3.关闭文件
        访问模式                说明
        r                       以只读方式打开文件.文件的指针将会放在文件的开头.这是默认模式
        w                       打开一个文件只用于写入。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。
        a                       打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入
        rb                      以二进制格式打开一个文件用于只读。文件指针将会放在文件的开头。这是默认模式。
        wb                      以二进制格式打开一个文件只用于写入。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件
        ab                      以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入
        r+                      打开一个文件用于读写。文件指针将会放在文件的开头
        w+                      打开一个文件用于读写。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件
        a+                      打开一个文件用于读写。如果该文件已存在，文件指针将会放在文件的结尾。文件打开时会是追加模式。如果该文件不存在，创建新文件用于读写。
        
        关闭文件
        close()

'''
