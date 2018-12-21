# KV编程轮各种模式匹配都只是代数

## 一、KV编程论

```
https://docs.python.org/3/library/re.html
re：regular expression，有规律的表达式，进行各种匹配操
作用：文本解析，对复杂的字符串进行特定信息提取
通过在线工具了解基本概念。
在线工具：#正则表达式测试平台
https://www.regexpal.com/
http://tool.oschina.net/regex
```

## 二、匹配一次还是多次
```
import re
s = """
1234-1234-113
133-1234-2123
135-4567-3456
de8ug@foxmail.com
lilei@qq.com
hmm.lee@google.com
http://baidu.com
https://github.com
http://taobao.com
"""
target = '\d{4}'
target = '\d{4}-\d{4}-\d{3}'
target = '\d{3}-\d{4}-\d{4}'
target = '\d+-\d+-\d+'
# target = '[\d+-?]+'
# target = '\w{5}@\w{2}.com'
match = re.search(target, s)
if match:
    print('找到,', target, match)
    print(match.group())
else:
    print('啥都没找到')
```


```
# 使用compile生成regex对象
regex = re.compile('1234')
match = regex.match(s) #
# match = regex.search(s) # 1234
print(match)
if match:
    print('find:',match.group())
else:
    print('no')
```
## 三、如果想分组匹配怎么办
```
re_ip = re.compile(r'''
((2[0-4]\d|25[0-5]|[01]?\d\d?)\.) # ip的一组数字，包含数字后面的点
{3} # 表示三组数字
(2[0-4]\d|25[0-5]|[01]?\d\d?) # 最后一组数字
''',re.X) # 正则可以换行，可以注释
match = re_ip.match('192.162.3.4')
print(match)

# re.X表示可以换行可以加注释，前面要用三引号
```
## 四、匹配要不要贪心一点


```
re_quote = re.compile(r'"(.*?)"')
text1 = 'Computer says "no."'
find1 = re_quote.findall(text1)
print(find1)
text2 = 'Computer says "no." Phone says "yes."'
find2 = re_quote.findall(text2)
print(find2)
```

## 五、正则表达式可以直接替换掉内容吗
```
regex = re.compile(r'de8ug')
regex.sub('***$$$$*', 'sdjflsjsgde8ug09709098de8ugsdfsf234')
```

```
# 通过分组替换字符串格式，mm/dd/yy -> yy-mm-dd
s = '替换日期格式：10/01/2008，12/25/2018'
re_date = re.compile(r'(\d+)/(\d+)/(\d+)')
re_date.sub(r'\3-\1-\2', s) # 3 1 2 分别对应上一行分组每个（）的位置
```


```
# 替换字符串中间多余空格
s = ' de8ug 正则 python 好难学， 坚持一下吧，没 几个 了 '
s.strip()
re_blank = re.compile(r'\s+') # 匹配任意空白字符，相当于 [ \t\n\r\f\v]
re_blank.sub('', s)
```


```
memo_text = '''
1.1 去找小8写个程序
1.2 记一下王总的电话 13912345678
1.3 修改Python程序的bug
1.4 路上买二斤西红柿，遇见卖鸡蛋的就买一斤
1.5 事情太多，忘了今天要干啥
'''
re_date = re.compile(r'\d.\d')
re_date = re.compile(r'\d\.\d')
re_date = re.compile(r'\d+\.\d+')
re_date = re.compile(r'(\d+)\.(\d+)')
re_date = re.compile(r'(?P<month>\d+)\.(?P<day>\d+)')
re_date.findall(memo_text)
# print(re_date.sub(r'\1月\2日', memo_text))
print(re_date.sub(r'\g<month>月\g<day>日', memo_text))

out:
1月1日 去找小8写个程序
1月2日 记一下王总的电话 13912345678
1月3日 修改Python程序的bug
1月4日 路上买二斤西红柿，遇见卖鸡蛋的就买一斤
1月5日 事情太多，忘了今天要干啥
```

## 六、案例：找找她的联系方式
```
手机号,电话号：
手机号码傻瓜版: ^1\d{10}$
匹配形式如 0511-4405222 或 021-87888822
电话号码必备区号版： \d{3}-\d{8}|\d{4}-\d{7}
邮箱：
电子邮件的验证： (\w+@(\w+\.)+\w{2,3})?
验证Email地址： ^\w+[-+.]\w+)*@\w+([-.]\w+)*\.
\w+([-.]\w+)*$
验证Email地址： .+@.+\.[a-z]+
身份证：
身份证号: ^(\d{15}|\d{17}(\d|X))$
```

## 七、案例：登入验证正则版


```
- 字符大小写
- 长度限制
- 数字范围
- 手机
- 邮箱
用户名或密码的一些潜规则
- 匹配腾讯QQ号： [1-9][0-9]{4,}腾讯QQ号从10000开始
- 只能输入汉字： ^[\u4e00-\u9fa5]{1,8}$
只能输入由数字和26个英文字母组成的字符串：“^[A-Za-z0-9]+
$”
-
验证用户密码:“^[a-zA-Z]\w{7,17}$”正确格式为：以字母开头，
长度在8-18之间， 只能包含字符、数字和下划线。
-
常用正则表达式
```
## 八、案例：51备忘录v0.27
