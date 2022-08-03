#IPTV直播源地址加解密
#开源地址：https://github.com/Cyril0563/IPTV_Base64
#作者：Cyril0563
#时间：2022-08-03

import base64

#加密-----------
# str = 'abcdefg'
# str_b = base64.b64encode(str.encode('utf-8'))
# #将str_b转换为字符型
# str_b_str = str_b.decode('utf-8')
# print(str_b_str)
#---------------

#解密-----------
# str_b = 'YWJjZGVmZw=='
# str_b_str = str_b.encode('utf-8')
# str_b_str_decode = base64.b64decode(str_b_str)
# str_b_str_decode_str = str_b_str_decode.decode('utf-8')
# print(str_b_str_decode_str)
#---------------

#菜单
print('************')
print('IPTV直播源地址加解密')
print('1.加密')
print('2.解密')
print('0.退出')
print('************')

#判断
while True:
    num = input('请选择序号进行操作：')
    if num == '1':
        str = input('请输入要加密的地址链接：')
        str_b = base64.b64encode(str.encode('utf-8'))
        #将str_b转换为字符型
        str_b_str = str_b.decode('utf-8')
        print(str_b_str)
    elif num == '2':
        str_b = input('请输入要解密的字符串：')
        str_b_str = str_b.encode('utf-8')
        str_b_str_decode = base64.b64decode(str_b_str)
        str_b_str_decode_str = str_b_str_decode.decode('utf-8')
        print(str_b_str_decode_str)
    elif num == '0':
        print('退出')
        break
    else:
        print('序号输入错误，请重新输入')
    print('************')
    print('1.加密')
    print('2.解密')
    print('0.退出')
    print('************')
