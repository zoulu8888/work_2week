# 一、为什么需要函数
==作用==：
- 合并重复
- 测试方便
- 修改方便
- 打包
- 映射

# 二、KV编程论：解释函数

函数（function），最早由中国清朝数学家李善兰翻译，出于其著作
《代数学》。之所以这么翻译，他给出的原因是“凡此变数中函彼变
数者，则此为彼之函数”，也即函数指一个量随着另一个量的变化而
变化，或者说一个量中包含另一个量。函数的定义通常分为传统定义
和近代定义，函数的两个定义本质是相同的，只是叙述概念的出发点
不同，传统定义是从运动变化的观点出发，而近代定义是从集合、映射的观点出发。

def function_name(s):
statement(s)

```
def choose_num(start,end):
    num = random.randin(start,end)
    return num

choose_num(4,8) #随机抽取4-8中的数
```
# 三、几种参数的用法

### 关键词参数（k=v）
```
def choose_num(start, end=10):
    num = random.randint(start, end)
    return num
    
    # 默认参数要放在非默认参数后面！ 否则报错。
    # 默认值是可以替换掉的，比如：
    choose_num(2,50)
```

```
#也可以定义两个默认参数
def choose_num(start, end=10, n=5):
    numbers = []
    for x in range(n):
        num = random.randint(start, end)
        numbers.append(num)
    return numbers
```


```
# 默认值只计算一次！注意列表当参数默认值,
def f(a, L=[]):
    L.append(a)
    return L
    
    
print(f(1))
print(f(3))
print(f(5))

out:
[1]
[1, 3]
[1, 3, 5]

#如果想不记录之前的要这么做，但是空不是列表，无法追加，所以加一个判断语句
def f(a, L=None):
    L.append(a)
    return L
    
f(3)

def f(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L
    
    
print(f(1))
print(f(3))
print(f(5))

out:
[1]
[3]
[5]

```


```
def car(color, price='10',             user='de8ug'):
    print(f'{user}有一辆{color}色的车，价值{price}块~')
    
car(price=90) # 这样调用时错的，非默认参数color必须赋值
```

### 任意参数
### *args **kwargs： args->tuple(元组）, kwargs->dict（字典）


```
def car(*args):
    print(args)
    for k in args:
        print(k)
        
car("red", 10, 'de8ug')
out:
('red', 10, 'de8ug')
red
10
de8ug
```


```
def car(**kw):
    for k,v in kw.items():
    print(f'{k}::{v}')
    
# car('red', 20, 'de8ug') #因为是字典类型，所以我们传值的时候一定要用K=V的类型来操作，否则报错
car(color='red', price=20, user='de8ug')

out:
color::red
price::20
user::de8ug
```


```
def car(color, price, *args, **kw):
    print('args:', args)
    print('kw:', kw)
    for k in args:
        print(k)
    for k,v in kw.items():
        print(f'{k}::{v}')
        
        
# car('red', 20, 'de8ug')
car('asfs', 'T', color='red', price=20, user='de8ug')

out:
args: ('asfs', 'T')
kw: {'color': 'red', 'price': 20, 'user': 'de8ug'}
asfs
T c
olor::red
price::20
user::de8ug
```


```
kwargs = {'color':'red', 'price':30}
def car(**kw):
    print(kw)
    
    
car(**kwargs)# 如果要传输字典，要确保之前有两个星号

out:
{'color': 'red', 'price': 30}
```

```
kwargs = {'color':'red', 'price':'de8ug'}
def car(color='blue', price=99):
    print(color, price)
    
car(**kwargs) #KEY要一致才能这么操作解析，否则报错，比如把字典中color改成colors报错。
# *args

out:
red de8ug
```


```
def car(color='blue', *, price):
    print(color, price)
#之前的例子中有讲过，默认值必须放在最后，当前这个例子是例外，加了个星号，表示前面用默认值，后面的必须强制赋值，并且必须像下面这样写明赋值，否则报错，好好理解下。
car(price=30)
```

### lambda表达式，匿名函数


```
def plus1(x):
    return x + 1
plus1(19)
```

# 其实不大推荐这么写，只是写起来比较简短
```
add = lambda x: x+1
add(17)
```


```
def all_up(s):
    return s.strip().upper()
all_up('python')

all_up_again = lambda s: s.strip().upper()
all_up_again('py')
```


```
my_list = [1,2,3,4,5,6,7,9,12,11] # 找到列表里面所有奇数，并返回一个新列表
def odd(*L):
    new_list = []
    for k in L:
        if k % 2 == 1:
        new_list.append(k)
    return new_list
    
odd(*my_list)

# filter过滤，一个个数过来
list(filter(lambda x: x%2 == 1, my_list)) #等价于上面这个

out:
[1, 3, 5, 7, 9, 11]

```

### 函数注释与文档说明


```
def add(x, y):
"""Add x and y together."""
return x + y
```
#这么写有个好处，可以用内置函数直接调用这个函数的说明


```
add.__doc__

out:
'Add x and y together.'

```


```
def add(x:int, y:'这个数随便') -> int:
"""Add x and y together.
多添加一行"""
    return x + y
    
add.__doc__
out:
'Add x and y together.\n 多添加一行'

add.__annotations__
out:
{'return': int, 'x': int, 'y': '这个数随便'}
```
### pass, 抢地盘，凑语法,类似打草稿

```
def add():
    pass #用这个pass占地方
```

# 四、你了解作用域么

- 变量作用域
- 函数嵌套
- 函数闭包


```
# 变量作用域，在自己屋子干自己的事儿
# LEGB：Local, Enclosing, Global, Builtin
# 翻译：本地（局部），封闭，全局，内置
x = 1 # 全局变量
def add():
    x += 1 # 局部变量赋值错误， x = x+1
    print(x)
add()  #报错

#这么写就可以：
x = 1 # 全局变量
def add():
    a = X
    a += 1 
    print(a)
add()  #
```

```
#或者写成这样
def add_a():
    x = 1 
    def add():
        nonlocal x #在嵌套闭包中使用，新建一个空间放这个值。
        x += 1 
        print(x)
    return add
a = add_a()
a()
```


### 函数嵌套

```
def calc(x, y):
    def add(x, y):
        print('x+y:', x + y)
    def sub(x, y):
        print('x-y:', x - y)
    def mul(x, y):
        print('x*y:', x * y)
    add(x, y)#可以在函数内部直接运行上面那些函数。
    sub(x, y)
    
calc(2,5)
out:
x+y: 7
x-y: -3
```

# 四、程序异常处理

```
使用异常处理模块来捕获错误和代码异常，或清理代码
# https://docs.python.org/3.6/reference/compound_stmts.html#try
try_stmt ::= try1_stmt | try2_stmt
try1_stmt ::= "try" ":" suite
("except" [expression ["as" identifier]] ":" suite)+
["else" ":" suite]
["finally" ":" suite]
try2_stmt ::= "try" ":" suite
"finally" ":" suite

```

```
x = 'hello

```


```
def test():
    try:
        my_dict = {}
        print(my_dict['name'])
    except Exception as e: # 直接写Exception不够明确
        print(e)
    finally:
        print('over')
test()



def test():
    try:
        my_dict = {}
        print(my_dict['name'])
    except KeyError as e:
        print('这个key不存在',e)
    finally:
        print('over')
test()

out:
这个key不存在 'name'
over
```

# 四、案例-登陆验证命令行版本


```
info = {
'user': 'de8ug',
'pwd': '123'
} #
username = input('username:')
# password = input('password:')
# if username == info['user'] and password == info['pwd']:
# return 'ok'
# else:
# return 'error'
def login():
    username = input('username:')
    password = input('password:')
    if username == info['user'] and     password == info['pwd']:
    return 'ok'
    else:
        return 'error'
        
login()

```


```
info = {
'user': 'de8ug',
'pwd': 'aA123'
}
def login():
    username = input('username:')
    passport = input('passport:')
    age = input('age:')
# if int(age) < 18:
# print('禁止登陆!')
    try:
        if int(age) < 18:
             print('禁止登陆!')
        if username == info['user'] and passport == info['pwd']:
            return 'ok'
        else:
            return 'error'
    except Exception as e:
        print(e)
        age = 1
        return 'default age=1'
    return 'ok'
    
    
login()
```

# 五、案例-密码生成器


```
import string
import random
count = 8
str_from = string.ascii_letters + string.digits
"".join([random.choice(str_from) for _ in range(count)])
```


```
import string
import random
def random_pwd(count):
    "生成随机密码，位数=count"
    str_from = string.ascii_letters + string.digits
    return "".join([random.choice(str_from) for _ in range(count)])
    
print(random_pwd(5))
print(random_pwd(7))

```


```
import base64
s = input('pwd:')
# encode，编码，人 -》 计算机
# decode，解码，计算机 -》 人
ss = base64.b64encode(s.encode('utf-8')) # bytes
# b64encode只认识encode转换出来的码
ss.decode('utf-8')
# 再用decode解码出我们能认识的字符
```


```
import base64
import pyperclip  #这个代码库要先安装 pip install pyperclip
"""
知识点：
- base64
- encode
- decode
- 直接复制到剪切板
- 函数演变
- 代码规范
"""
def custom_pwd(origin_pwd, salt='de8ug', count=8, offset=3):
    print('before salt:', origin_pwd)
    new_pwd = base64.b64encode((origin_pwd + salt).encode('utf-8'))
    new_pwd = new_pwd.decode('utf-8')
    print('after salt:', new_pwd)
    if len(new_pwd) < count:
        new_pwd = new_pwd.ljust(count, 'a')
        
    pyperclip.copy(new_pwd[offset : count + offset])
    return 'ok, 找地方粘贴密码去吧！'
print('生成密码：', custom_pwd('sdfsda')) # hZGU4dWc,mc2RhZGU
```
# 六、51备忘录V0.26

