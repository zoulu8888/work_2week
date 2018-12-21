#!/usr/bin/env Python
# -*- coding:utf-8 -*-
# Unit conversion tool.py
# author: Paul


# 1.导入标准库(这段脚本不需要)
# 2.第三方的库(这段脚本不需要)
# 3.自定义的库(这段脚本不需要)

"""
二 使用面向对象技术，重构51备忘录程序（50分）

1.添加Memo类，至少包含id，name，thing，date四个属性，date可以暂时使用字符串表示，比如‘1.2’，‘3.8’，暂时不用考虑时间相关模块

2.id属性为只读，其他属性可读写

3.添加MemoAdmin类，作为主体程序，管理Memo类构成的列表，进行Memo的增删改查。

4.所有Memo记录使用pickle进行读写，数据文件为db.pkl, 读写方法为save和load

5.各个类中的每个方法必须添加说明doc-string（即def下一行加一句注释），每个类必须添加注释说明，解释作用(缺一条减10分)

"""
import pickle


class Memo(object):
    """备忘录类的创建"""
    def __init__(self, name, date, thing):
        "加下划线为只读，其它是可读写"
        self._id = 0  
        self.name = name
        self.date = date
        self.thing = thing

    @property
    def id(self):
        "只读函数内调用操作"
        return self._id

    @id.setter
    def id(self, val):
        self._id = val


class MemoAdmin(object):
    """备忘录管理类的创建"""
    def __init__(self, memo_list):
        """初始化"""
        self.memo_list = memo_list
    
    @staticmethod  #定义静态方法，可直接调用
    def deal_input_data():
        """输入并拆分字符串"""
        input_memo = input('请输入事件 eg（1.1-小8-学习python):').strip()
        input_list = input_memo.split('-')
        if len(input_list) == 3:
            return input_list

    def add(self):
        """增操作"""
        memo_date_list = MemoAdmin.deal_input_data()
        memo = Memo(*memo_date_list)
        memo.id = len(self.memo_list) + 1
        self.memo_list.append(memo)

    def del_memo(self):
        """删操作"""
        memo_date_list = MemoAdmin.print_all(self)
        # if len(self.memo_list) == 0:
        #     print('备忘录中没有记录，请去添加记录')
        # for memo in self.memo_list:
        #     print(memo.id, memo.date, memo.name, memo.thing)
        num = input('请需要需要删除几号记录：')
        self.memo_list.pop(int(num)-1)

    def modify(self):
        """改操作"""
        print('修改备忘录：'.center(31, ':'))
        memo_date_list = MemoAdmin.print_all(self)
        mod = input('输入要修改第几条:')
        mod1 = int(mod)
        for memo in self.memo_list:
            if memo.id == mod1:
                memo.name = input('name:')
                memo.date = input('date:')
                memo.thing = input('thing:')
            print(memo.id, memo.date, memo.name, memo.thing)
        
    def query(self):
        """查操作"""
        print('查询备忘录：'.center(31, ':')) 
        k = input('输入要查询第几条:')
        k1 = int(k)
        for memo in self.memo_list:
            if memo.id == k1:
                print(memo.id, memo.date, memo.name, memo.thing)

    def save(self):
        """保存操作"""
        with open('memo.pkl', 'wb') as f:
            f.write(pickle.dumps(self.memo_list))
        return True

    @classmethod
    def load(cls):
        """读操作"""
        try:
            with open('memo.pkl', 'rb') as f:
                memo_list = pickle.loads(f.read())
        except Exception as e:
            memo_list = []
        return cls(memo_list)

    def print_all(self):
        """打印操作"""
        if len(self.memo_list) == 0:
            print('备忘录中没有记录，请去添加记录')
        for memo in self.memo_list:
            print(memo.id, memo.date, memo.name, memo.thing)


def main():
    admin = MemoAdmin.load()
    memu_list = {
        '1': 'add',
        '2': 'del_memo',
        '3': 'modify',
        '4': 'query',
        '5': 'print_all',
        '6': 'quit'
    }
    #   memu_list = '''
    #      1: add
    #      2: del_memo
    #      3: modify
    #      4: query
    #      5: print_all
    #      6: quit
    # '''
    print(memu_list)
    memo_dict = {
        '1': 'add', '2': 'del_memo', '3': 'modify', '4': 'query', '5': 'print_all', '6': 'quit'
    }
    while True:
        select = input('请输入你的选择：')
        if select == '6':
            admin.save()
            break
        if select in memo_dict:
            run = getattr(admin, memo_dict.get(select), None)
            if run:
                run()
            else:
                    print('选项不存在，请检测菜单项添加是否正确')
        else:
            print('请重新输入选择')

if __name__ == "__main__":
    main()

