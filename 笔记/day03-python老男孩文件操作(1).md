# 一、文件操作基本流程

### ==能调用方法的一定是对象==
### ==文件本身也是对象==

## 1、建立文件对象（Open方法）



```
open('文件路径（如果在同一个目录，直接写文件名就行）','r(读模式').read()

# 用read方法把数据读出来

f = open('小重山','r',encoding = 'utf8')
# 如果把读模式改成W写模式，是不可读的，结论是读模式只能读，写模式只能写
data = f.read() #不加参数的话默认全读
data = f.read(5) #读前5个字符
print (data)

#关闭文件，把缓冲区的文件写入磁盘
f.close()


#写方法
f = open('小重山','w',encoding = 'utf8')
data = f.write('hello word!'')

# 如果文件存在，就清空文件内的所有数据，如果文件不存在，就创建文件。就是说，每次打开都是从头开始写的。



```
注意 if in the win，hello文件是utf8保存的，打开文件时open函数是通过操作系统打开的文件，而win操作系统默认的是gbk编码，所以直接打开会乱码，需要f=open('hello',encoding='utf8')，hello文件如果是gbk保存的，则直接打开即可。

```


```
1、w是格式化以后写
2、a是打开后追加写

# 二、文件操作的具体方法
```

f = open('小重山','r',encoding = 'utf8')

a = f.readline() #取出第一行的数据

print(f.readline())
print(f.readline()) # 两个输出，先打印第一行，再打印下一行，与read类似，每一次调用完以后，光标就跳到一行的最后。



print(f.readlines()) #返回全部多行，并放入列表


for i in f.readlines():  #既然是列表，就可以用这个方法读出
    print(i.strip())  #与直接用read方法是一样的输入，但是无法对其操作，下面这个例子的方法，就可以指定行追加


```

    
```
f = open('小重山','r',encoding = 'utf8')
num = 0
for i in f.readlines():
    num += 1
    if num == 6:       # 在第六行文字后面加上****字符串
        i = ''.join([i.strip(),'****']) #字符串的拼接用join的效率最高
    print (i.strip())
    # 但是realines有个缺点，就是所有东西都放在缓冲，如果文件太大，就造成了负担，应该用下面这种迭代器的方法
f.close()

```


```
f = open('小重山','r',encoding = 'utf8')
num = 0
for i in f:  #for内部将f对象做成一个迭代器，用一行取一行
    num += 1
    if num == 6:       # 在第六行文字后面加上****字符串
        i = ''.join([i.strip(),'****']) #字符串的拼接用join的效率最高
    print(i.strip()) #就类似机器猫，口袋里有很多东西，但是用的时候才取出来。不会对内存造成负担，这是最优的打开文件的方式,但是效率没有上面这种好，因为有迭代器算法，可以说是空间换时间。


```


```
print(f.read(10)) #打印前10个字符 默认从0开始数，换行符也算。
print（f.tell())  #告诉我光标现在的位置，英文一个字符，中文一个占3个字符
# 比如read两个中文，tell后的位置返回的是6.


#有个调整光标位置的方法
f.seek(0) #光标移到最前面，实现了光标移动，这个很重要，端点续传。


```


### 以上的办法都是将读书来的数据暂时放在缓存里，close后才保存进磁盘，这就有个问题，比如一些都数据较为敏感的行业-银行，一旦断电，数据就没了，所以有了以下的方法。
```
f = open('hello',w)
f.write('alex is 35') #返回值是返回字符数。比如这个是10
# 但是这个操作并没有将文件存入磁盘，还在缓存。
f.flush() #这个动作帮我们把缓存的数据转入进磁盘
# 这个方法可以用来做进度条 ==========         %92


```

```
import sys,time
for i in range(30):
    sys.stdout.write('*') #这条命令的作用是终端界面输出指定字符的作用
    sys.stdout.flush() #上面这条执行只是放缓冲区，用flush来写入输出
    time.sleep(0.2)  
    
for i in range(30):
    print('*',end = '',flush=True) #效果是一样的
    time.sleep(0.2)  
```


```
# 截断操作
f = open('小重山','a',encoding = 'utf8') #w是先格式化再写入
f.truncate() #括号里填的值是光标的位置，光标之后全清空，默认是0.
f.close()

```


```
# 修改后写入副本，只能这么操作
f_read = ('小重山'，'r',encoding='utf8')
f_write = ('小重山'，'w',encoding='utf8')
num=0
for line in f_read:
    num += 1
    if line ==6:
    # line = 'hello python \n'
      line = ''.join([line.strip(),'hello python\n'])
    print (line)
f_read.close()
f_write.close()
    
```



```
# with 语句
# 用这种不用close，以后都用这种方式
with open ('log',r'') as f:
    f.readine()
    f.read()       #输出要退出with代码框
    
print()
```


```
#同时管理多个文件对象
with open('log1','r') as f_read,open('log2','w') as f_write  #通过以上这段代码可以拿到两个句柄
    for line in f_read:
        f_write_write(line)
        
```
# 深浅拷贝


```
s=[1,'alex,'alvin'] #想拿出来做一个副本

s1 = [1,'alex,'alvin'] #这样可以，修改s1不影响s,数据多就不能这样了



```

```
s=[1,'alex,'alvin'] #想拿出来做一个副本
s2 = s.copy() #拷贝的方法，这样修改s2也不会影响到s
```



```
s=[[1,2],'alex,'alvin'] #想拿出来做一个副本
s3=s.copy() #这个方法拷贝[1,2]的地址，还有后两个字符是开辟了新的空间存储
s3[1] = 'linux' #修改不影响到s

s3[0][1] = 3 #修改字符串的时候没影响到s，但是修改列表影响到s了，同步被修改，说明这个copy方法是有联系的，不是独立的内存空间，这就是浅拷贝。


```
![image](https://note.youdao.com/yws/api/personal/file/6D43E0C54785421DB6BF2347A9FFDCE1?method=download&shareKey=78518e0c5a5e4c9662137d9b11c1fb22)

![image](https://note.youdao.com/yws/api/personal/file/75720DE3D09F4BB1849DDB283EB3A1E8?method=download&shareKey=417b9137ab9c0aeb945454ec012d49c8)

### ==用copy只会拷贝第一层==


```

a= [[1,2],3,4]

b=a

a[2] = 'from a'
print(a,b)

#只要不是普通的字符串，是这种多重类型，改了a，b也一样会变化。
```
### 深拷贝等于完全克隆一份，跟原来完全没关系，需要单独的模块来执行
```
深拷贝一般不用，因为太占内存
inport copy

xiaosan = copy.deepcopy(husband)
```

# ==集合set==

## 1、创建
```
a =(1,3,4) #输出一样的列表不是集合，是列表
#创建集合只有一种办法
s = set('alex li')
print(s) #{'e','x','a',' ','i','l'}
# 输出不重复的字符，相同的只保留一个，这就是去重操作，输出是无序的不重复的，没有索引关系的。


#set的值必须是可哈希的，就是不可变的，与字典的key值类似，比如下面这个会报错。
li = [[1,2],3,'alex'] #[1,2]是可变的，所以报错
s=set(li)
print (s)

#set本身整体是非可哈希的，可添加和删除元素，意味着集合不可以作为字典的key.
```


```
frozenset与set相反，不可以添加修改删除。不可变的固定元素。
```
## 2、访问集合

```
#因为集合是无序的，没有索引关系的，所以访问要通过遍历来实现，或者用in或者not in来判断是否在集合里面，返回布尔值。
for i in s1:
    print(i)
    
#判断在不在 print('a' in S1)
# 返回的是布尔值

```

## 3、更新集合


```
s.add('uu') # 之前列表用的是append
当做一个uu无序的更新进去
```


```
s.update('ops') #分成 'o' 'p' 's'分别更新进去

s.update([12,'eee']) #如果这么写，就更新进去 '12'与 'eee'


```

```
s.remove() #删除元素，想删哪个就输入哪个

s.clear() #清空集合，集合还在

del s #删除整个集合，没了


```

```
a = set([1,2,3,4,5])
b = set([4,5,6,7,8])
print(a.intersection(b) #取交集 {4,5}


print(a.union(b) #取并集 {1,2,3，4,5，6,7,8}

print(a.difference(b) #取差集 {1,2,3}，a里面有的b没有的

print(a.symmetric_difference(b))#反向交集，又叫对称差集 {1,2,3,6,7,8}

```


```
print(a.issuperset(b)) #a完全包含b
print(a.issubset(b) # a是否都在b里

```
