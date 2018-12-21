# 函数
==定义: 函数是指将一组语句的集合通过一个名字(函数名)封装起来，要想执行这个函数，只需调用其函数名即可==

### 特性:
- 减少重复工作
- 方便后期修改，更容易扩展（调用多次也只要改函数本身）
- 计算机的函数不等于属于中的函数
- 保持代码一致性
- 

### 函数的创建
```
Python 定义函数使用 def 关键字，一般格式如下：

def 函数名（参数列表）:
    函数体
def hello():
    print('hello')
   
hello()#调用
```

### 函数的命名规则


```
- 函数名必须以下划线或字母开头，可以包含任意字母、数字或下划线的组合。不能使用任何的标点符号；
- 函数名是区分大小写的。
- 函数名不能是保留字。
```

### 形参和实参
```
形参：形式参数，不是实际存在，是虚拟变量。在定义函数和函数体的时候使用形参，目的是在函数调用时接收实参（实参个数，类型应与实参一一对应）

实参：实际参数，调用函数时传给函数的参数，可以是常量，变量，表达式，函数，传给形参   

区别：形参是虚拟的，不占用内存空间，.形参变量只有在被调用时才分配内存单元，实参是一个变量，占用内存空间，数据传送单向，实参传给形参，不能形参传给实参
```


```
def add(x,y): #形参，不传值不占内存
    print(x+y)
    
add(6+2)
```


```
##***************代码重用

def logger(n):
    with open('日志记录','a') as f:
        f.write('end action%s\n'%n)

def action1():
    print ('starting action1...')
    logger(1)


def action2():
    print ('starting action2...')
    logger(2)


def action3():
    print ('starting action3...')
    logger(3)


action1()
action2()
action3()
```


```
##为日志加上时间
import time

def logger(n):
    time_format='%Y-%m-%d %X' #设定格式
    time_current=time.strftime(time_format) #调用方法并赋值

    with open('日志记录','a') as f:
        f.write('%s end action%s\n'%(time_current,n))

def action1():
    print ('starting action1...')
    logger(1)


def action2():
    print ('starting action2...')
    logger(2)


def action3():
    print ('starting action3...')
    logger(3)

```

### 不定长参数


```
你可能需要一个函数能处理比当初声明时更多的参数。这些参数叫做不定长参数，和上述2种参数不同，声明时不会命名。

# def add(x,y):
#     return x+y
 
def add(*tuples): #后面这个名字可以自己命名，一般叫args，把所有的参数都传进去做成元祖
    sum=0
    for v in tuples:
        sum+=v
 
    return sum
 
print(add(1,4,6,9))
print(add(1,4,6,9,5))


加了星号（*）的变量名会存放所有未命名的变量参数（元祖）。而加(**)的变量名会存放命名的变量参数（字典）
```


```
def print_info(name,age,sex='male'):
 
    print('Name:%s'%name)
    print('age:%s'%age)
    print('Sex:%s'%sex)
    return
 
print_info('alex',18)
print_info('铁锤',40,'female')

#如果我想要再传一个参数job = 'IT'进去，上面这个函数是做不到的，会报错。


```

```
def print_info(*args,**kwargs): #一个星号一般叫args，两个的一般较kwargs
    print(args)  #打印出来的是元组
    print(kwargs) #打印出来的是字典
    
```


```
def print_info(*args,**kwargs): #一个星号一般叫args，两个的一般较kwargs
    print(kwargs) #打印出来的是字典
    for i in kwargs:  #这个i是键，不包含值
        print('%s:%s'%(i,kwargs[i]))#根据参数可以打印任意相关信息了
 
    return
    
    
print_info(name='alex',age=18,sex='female',hobby='girl',nationality='Chinese',ability='Python')
```

### 函数的返回值


```
要想获取函数的执行结果，就可以用return语句把结果返回

注意:

- 函数在执行过程中只要遇到return语句，就会停止执行并返回结果，so 也可以理解为 return 语句代表着函数的结束
- 如果未在函数中指定return,那这个函数的返回值为None  
- return多个对象，解释器会把这多个对象组装成一个元组作为一个一个整体结果输出。
- 作用是1、结束函数 2、返回某个对象 3、return下一行的语句都不会执行
```

```
def f():
    print('ok')
    return None #不写默认这样
    return 10 #写的话就将值返回给调用者f


```


```
def add(*tuples): #后面这个名字可以自己命名，一般叫args，把所有的参数都传进去做成元祖
    sum=0
    for v in tuples:
        sum+=v
    print(sum)#如果这样，只是打印输出，系统并没有得到结果，所以需要返回值
    return (sum) #这样系统就能的到结果，否则返回None
```

### 函数的作用域


```
def test():
    x = 2
    
    
print(x) # NameError: name 'x2' is not defined #函数外识别不到x
```

```
- 局部作用域不可以修改全局作用域的变量
```

```
count = 10

def outer():
    print(count)
    count = 5  #局部作用域不可以修改全局作用域的变量
```


```
count = 10

def outer():
    global count #声明是全局变量，就可以修改了,覆盖外面的作用域
    print(count) #输出10
    count = 5  
    print(count) #输出5
```


```
def outer():
    count = 10
    def inner():
        nonlocal count #如果是在嵌套函数中就用nonlocal声明变量
        count = 20
        print （count）
    
    inner()
    print(count)
outer()
```

小结 
- （1）变量查找顺序：LEGB，作用域局部>外层作用域>当前模块中的全局>python内置作用域；

- （2）只有模块、类、及函数才能引入新作用域；

- （3）对于一个变量，内部作用域先声明就会覆盖外部变量，不声明直接使用，就会使用外部作用域的变量；

- （4）内部作用域要修改外部作用域变量的值时，全局变量要使用global关键字，嵌套作用域变量要使用nonlocal关键字。nonlocal是python3新增的关键字，有了这个 关键字，就能完美的实现闭包了。 



```
def f(*args):
    print(args)
 
f(*[1,2,5]) #直接传列表加一个星号，一个一个元素传，没有星号就是整体传
 
def f(**kargs):
    print(kargs)
 
f(**{'name':'alex'}) #传字典就加两个星号
```

### 高阶函数

高阶函数是至少满足下列一个条件的函数:

- 接受一个或多个函数作为输入
- 输出一个函数


```
def add(x,y,f):
    return f(x) + f(y)
 
res = add(3,-6,abs)
print(res)
###############
def foo():
    x=3
    def bar():
        return x
    return bar　
```

