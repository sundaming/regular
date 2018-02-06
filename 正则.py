import re
# 1.需求：匹配出0-100之间的数字
print(re.match(r'[0-9]$|[0-9]\d$ 0$|100$', '5'))
# 2.需要：提炼出<h1>匹配分组</h1>中的内容：匹配分组。
# 得到<h1>匹配分组</h1>中的内容
content = '<h1>匹配分组</h1>'
print(re.match(r'<.+>(.+)</.+>', content).group(1))
# 3.需求：匹配出163、126、qq、gmail 邮箱
# 要求邮箱名字部分，大于等4小于等于20个字符，例如1234.@126.com，1234就是名字的长度
print(re.match(r'(\w{4,20})@(163|126|qq|gmail)\.(com|net)$', '123kkk4@163.com'))
# 4.练习：010-12345678获取区号和号码
num = '010-12345678'
print(re.match(r'([^-\D)]{3,4})-*(\d{8}$)', num).group(1))
print(re.match(r'([^-\D)]{3,4})-*(\d{8}$)', num).group(2))
# 5.需求：匹配出<html><h1>atguigu</h1></html>
# 6.使用\number
# 需求：匹配出<html><h1>atguigu</h1></html>

# 7.使用(?P<name>)?(?P=name)
# 需求：匹配出<html><h1>atguigu</h1></html>
