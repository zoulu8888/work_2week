#!/usr/bin/env Python
# -*- coding:utf-8 -*-
# Unit conversion tool.py
# author: Paul


# 1.导入标准库(这段脚本不需要)
# 2.第三方的库(这段脚本不需要)
# 3.自定义的库(这段脚本不需要)

"""
1.添加Transfer类，作为主体程序，处理输入输出

2.温度,长度,货币转换分别建立独立的类，每个类至少有2个方法，各处理一个方向转换（举例：美元到人民币，人民币到美元）

3.Transfer类根据不同输入内容，自动选择相应的功能类去处理逻辑

4.各个类中的每个方法必须添加说明doc-string（即def下一行加一句注释），每个类必须添加注释说明，解释作用(缺一条减10分)

"""



def welcome():
    """建立欢迎函数，处理目录输出"""
    global jump
    jump = True
    while jump:
        print('欢迎使用万能转换器(输入Q退出）'.center(60,'*'))
        tool_menu = {
            'T':'温度转换',
            'L':'长度转换',
            'C':'货币转换'
        }
        for k,v in tool_menu.items():
            print(k,v)
        user_choose = input('请选择需要转换的类型（输入Q退出）:')
        user_choose = user_choose.upper() 
        choose(user_choose)

def choose(user_choose):
    """建立模式选择函数，并调用相应的类处理函数"""
    global jump
    if user_choose == 'T':
        Temper()
    elif user_choose == 'L':
        Length()
    elif user_choose == 'C':
        Currency()
    elif user_choose == 'Q':
        jump = False
    else:
        print('输入错误，请重新输入！（输入Q退出）'.center(60,'*'))
        


def Temper():
    """建立温度处理函数，并调用相应的类方法"""
    global jump
    user_input = input('请输入您需要转换的温度(示例32C或50F，输入Q退出，输入U返回上一级)：')
    user_input = user_input.upper()
    if user_input.endswith('C'):
        TEMPER1 = TEMPER(user_input)
        TEMPER1.C_to_F()
    elif user_input.endswith('F'):
        TEMPER1 = TEMPER(user_input)
        TEMPER1.F_to_C()
    elif user_input == 'Q':
        jump = False
    elif user_input == 'U':
        welcome()
    else:
        print('输入错误！请重新输入！')
        Temper()



class TEMPER:
    """建立温度类，并定义双向转换方法"""
    def __init__(self,temp):    
        "初始化参数"
        self.temp = temp
    def C_to_F(self):
        "摄氏度到华氏度"
        self.temp = float(self.temp.strip('C').strip('F'))
        Tf = (9/5) * self.temp + 32
        print(f'当前输入的摄氏度{self.temp}C转换结果为{Tf}F'.center(60, "="))
    def F_to_C(self):
        "华氏度到摄氏度"
        self.temp = float(self.temp.strip('F').strip('C'))
        Ft = (5/9) * (self.temp - 32)
        print(f'当前输入的华氏度{self.temp}F转换结果为{Ft}C'.center(60, "*")) 


def Length():
    """建立长度处理函数，并调用相应的类方法"""
    global jump
    user_input = input('请输入您需要转换的长度(示例32M或50FT，输入Q退出，输入U返回上一级)：')
    user_input = user_input.upper()
    if user_input.endswith('M'):
        LENGTH1 = LENGTH(user_input)
        LENGTH1.M_to_Ft()
    elif user_input.endswith('FT'):
        LENGTH1 = LENGTH(user_input)
        LENGTH1.Ft_to_M()
    elif user_input == 'Q':
        jump = False
    elif user_input == 'U':
        welcome()
    else:
        print('输入错误！请重新输入！')
        Length()



class LENGTH:
    """建立长度类，并定义双向转换方法"""
    def __init__(self,temp):    
        "初始化参数"
        self.temp = temp
    def M_to_Ft(self):
        "米到英寸"
        self.temp = float(self.temp.strip('M').strip('FT'))
        FT = 3.2808 * self.temp
        print(f'当前输入的{self.temp}米转换结果为{FT}英寸'.center(60, "*"))
    def Ft_to_M(self):
        "英寸到米"
        self.temp = float(self.temp.strip('FT').strip('M'))
        M = 0.3048 * self.temp
        print(f'当前输入的{self.temp}英寸转换结果为{M}米'.center(60, "*"))



def Currency():
    """建立货币处理函数，并调用相应的类方法"""
    global jump
    user_input = input('请输入您需要转换的货币(示例32人民币或50美元，输入Q退出，输入U返回上一级)：')
    user_input = user_input.upper()
    if user_input.endswith('人民币'):
        CURRENCY1 = CURRENCY(user_input)
        CURRENCY1.R_to_D()
    elif user_input.endswith('美元'):
        CURRENCY1 = CURRENCY(user_input)
        CURRENCY1.D_to_R()
    elif user_input == 'Q':
        jump = False
    elif user_input == 'U':
        welcome()
    else:
        print('输入错误！请重新输入！')
        Currency()

class CURRENCY:
    """建立货币类，并定义双向转换方法"""
    def __init__(self,temp):    
        "初始化参数"
        self.temp = temp
    def R_to_D(self):
        "人民币到美元"
        self.temp = float(self.temp.strip('人民币'))
        dollor = self.temp * 0.1455
        print(f'当前输入的{self.temp}人民币转换结果为{dollor}美元'.center(60, "*"))
    def D_to_R(self):
        "美元到人民币"
        self.temp = float(self.temp.strip('美元'))
        rmb = self.temp * 6.8733
        print(f'当前输入的{self.temp}美元转换结果为{rmb}人民币'.center(60, "*"))



def main():
    "主函数"
    welcome()

if __name__ == '__main__':
    main()