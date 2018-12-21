## 一、如何定义一个类

- class 类的名称：缩进+内容
- 举例: 人，学生，车，电脑，日志，游戏war3
- 私有变量：__name,不能被继承
- 内部变量：_开头
- 通过方法修改私有数据，对数据进行保护
- 查看类型：isinstance，type
- 属性只读：@property，@x.setter


```
class People:
    """一个人类"""
    def __init__(self, name, age): # 初始化方法，头尾双下划线都表示特殊方法
        self.name = name # 类的属性，也就是特点，特征
        self.age = age
def walk(self): # 普通方法，函数，method， function
    "人类会走路"
    print(f'{self.name} is walking') # 表示动作，行动，能干的事儿
```
