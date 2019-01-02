# coding: utf8

import itchat
from pymongo import MongoClient

client = MongoClient()  # 连接mongoDB
db = client.BTC  # 连接数据库
memberlist = db.member  # 找到合集
counts = db.countnum  # 钱和计数的记录
@itchat.msg_register(itchat.content.TEXT)
def print_content(msg):
    n = 0
    for i in msg['Text'].split('\n'):

        if len(i.split(':'))  > 1 or len(i.split('：')) >1:
            head = i.split(':')[0]
            try:
                content = i.split(':')[1]
            except Exception as e:
                content = i.split('：')[1]
            if head == '身份证姓名':
                content = content.strip()
                print("name = '{0}'".format(content[:1].strip()))
                print("mainname = '{0}'".format(content[1:].strip()))
                print("allname = '{0}'".format(content.strip()))
            elif i.split('：')[0] == '身份证姓名':
                content = content.strip()
                print("name = '{0}'".format(content[:1].strip()))
                print("mainname = '{0}'".format(content[1:].strip()))
                print("allname = '{0}'".format(content.strip()))
            elif head == '单    数' or head == '单数' or head == '单 数':
                print("i = 1 #起始账号")
                print("num = {0} #一共多少单".format(content.strip()))
            elif i.split('：')[0] == '单    数' or i.split('：')[0] == '单 数' or i.split('：')[0] == '单数':
                print('i = 1 #起始账号')
                print("num = {0} #一共多少单".format(i.split('：')[1].strip()))
            elif head == '地    址' or head =='地址' or head == '身份证地址':
                print("address = '{0}'".format(content.strip()))
            elif i.split('：')[0] == '地    址' or i.split('：')[0] == '身份证地址' or i.split('：')[0] == '地址':
                print("address = '{0}'".format(content.strip()))
            elif head == '出生年月日' or head == '出生年月' or head == '出生日期':
                if len(content.split('年')) == 1:
                    try:
                        print("year = '{0}'".format(content.split('.')[0].strip()))
                        print("month = '{0}'".format(content.split('.')[1].strip()))
                        print("day = '{0}'".format(content.split('.')[2].strip()))
                    except Exception as e:
                        print("year = '{0}'".format(content.strip()[:4]))
                        print("month = '{0}'".format(content.strip()[4:6]))
                        print("day = '{0}'".format(content.strip()[6:]))

                else:
                    print("year = '{0}'".format(content.split('年')[0].strip()))
                    try:
                        print("month = '{0}'".format(content.split('年')[1].split('月')[0].strip()))
                        print("day = '{0}'".format(content.split('年')[1].split('月')[1].split('日')[0].strip()))
                    except Exception as e:
                        print("month = '{0}'".format(content.strip()))
                        print("day = '{0}'".format(content.strip()))

            elif head == '性    别' or head == '性别' or head == '性     别':
                n = 1
                print("sex = '{0}'".format(content.strip()))
            elif i.split('：')[0] == '性    别' or i.split('：')[0] == '性别' or i.split('：')[0] == '性     别':
                n = 1
                print("sex = '{0}'".format(content.strip()))
            elif head == '手机号码':
                print("tel = '{0}'".format(content.strip()))
            elif i.split('：')[0] == '手机号码':
                print("tel = '{0}'".format(content.strip()))
            elif head == '网易邮箱' or head == '163邮箱' or head == '邮箱' or head == '邮    箱' or head == '邮     箱' or head == '邮   箱':
                print("email = '{0}' #邮箱 非常重要！".format(content.strip()))
                if n != 1:
                    print("sex = '女")
            elif i.split('：')[0] == '网易邮箱' or i.split('：')[0] == '163邮箱' or i.split('：')[0] == '邮    箱' or i.split('：')[0] == '邮 箱' or i.split('：')[0] == '邮     箱':
                print("email = '{0}' #邮箱 非常重要！".format(content.strip()))
                if n != 1:
                    print("sex = '女")
            elif head == '密码' or head == '邮箱密码' or head == '网易密码':
                print("mailusermailpassword = '{0}'".format(content.strip()))
                print("pw = '{0}'".format(content.strip()))
            elif i.split('：')[0] == '密码' or i.split('：')[0] == '邮箱密码' or i.split('：')[0] == '网易密码':
                print("mailusermailpassword = '{0}'".format(i.split('：')[1].strip()))
                print("pw = '{0}'".format(content.strip()))
            elif head == '支持者' or head == '接点人':
                print("connectname = '{0}'".format(str(content.strip)))
            elif i.split('：')[0] == '支持者' or i.split('：')[0] == '接点人':
                print("connectname = '{0}'".format(i.split('：')[1].strip()))
            elif head == '推荐人':
                m = memberlist.find_one({'name':'{0}'.format(content.strip)})['handler']
                print("handler = '{0}'".format(m))
            elif i.split('：')[0] == '推荐人':
                m = memberlist.find_one({'name': '{0}'.format(i.split('：')[1].strip())})['handler']
                print("handler = '{0}'".format(m))




itchat.auto_login(hotReload=True)
itchat.run()




