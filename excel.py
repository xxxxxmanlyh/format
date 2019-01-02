from pymongo import MongoClient
client = MongoClient()

db = client.BTC
ziliao = db.ziliao
memberlist = db.member#最新表单
cur = memberlist.find()
curos = ziliao.find()

counts = db.countnum
aa = counts.find()


countnum = db.count
countcur = countnum.find()
# num = 0
#
# for i in cur:
#     num = num +1
#
# print(num)
# print(counts.find_one({'name': '包小兰2', 'handler': '包小兰'}))

# for i in cur:
#     print(i)

# counts.update_one({'name':'张丽','handler':'刘勇豪'},{'$set': {'datetime':'2018年08月05日'}})
# counts.update_one({'name':'包天白','handler':'包小兰'},{'$set': {'comm':160,'re':21.36,'datetime':'','countnum':3}})
# counts.update_one({'name':'郑佩','handler':'包小兰'},{'$set': {'comm':0,'re':21.36,'datetime':'','countnum':3}})
# counts.update_one({'name':'王燕','handler':'包小兰'},{'$set': {'datetime':'2018年06月28日','countnum':8}})
# counts.update_one({'name':'崔薇','handler':'包小兰'},{'$set': {'datetime':'2018年06月28日'}})
# counts.update_one({'name':'包花善','handler':'包小兰'},{'$set': {'datetime':'2018年06月28日'}})
# counts.update_one({'name':'柳玉梅','handler':'包小兰'},{'$set': {'datetime':'2018年06月28日'}})
# counts.update_one({'name':'翁莹莹2','handler':'刘勇豪'},{'$set': {'acc_number':3}})
# counts.update_one({'name':'翁莹莹2','handler':'刘勇豪'},{'$set': {'countnum':3}})
# counts.update_one({'name':'张克成','handler':'刘勇豪'},{'$set': {'countnum':8}})
# counts.update_one({'name':'周爱莲','handler':'刘勇豪'},{'$set': {'countnum':8}})
# counts.update_one({'name':'寿立庆','handler':'刘勇豪'},{'$set': {'countnum':17}})



# for i in aa:
#     if i['handler'] == '刘勇豪':
#         print(i)


#
# for i in cur:
#     if i['name'] in ['张义霞','张义华','吴玉荣','周琦','吴玉香','吴俊', '耿鑫宇', '巩金玉','张广睿', '杨鑫', '罗津', '张义群', '周明华', '席迎晨', '魏玉红', '石桂敏', '白树春','周立海','孔右军','张立新','潘桂香', '刘宝洪', '王琳懿','王佳佳', '赵晨', '陈文平',]:
#         memberlist.update({'name':i['name']},{'$set':{'handler':'周义霞'}})
# for i in cursor:
#     if i['name'] == '张丽阁':
#         data = {
#             'name':i['name'],
#             'account':i['account'],
#             'acc_number':i['acc_number'],
#             'pw':i['pw'],
#             'Email':i['Email'],
#             'Emailpw':i['Emailpw'],
#             'handler':'王玲'
#
#         }
#         memberlist.insert_one(data)
# for i in countcur:
#     # if i['name'] in ['包小兰', '郑佩', '崔薇', '包花善', '柳玉梅', '王燕', '包天白', '魏儒嘉', '包爱军']:
#     #     countnum.update({'name': i['name']}, {'$set': {'handler': '包小兰'}})
#     # #增
#     # data = {
#     #     'name':i['name'],
#     #     'account':i['account'],
#     #     'countnum':0,
#     #     'handler':i['handler']
#     #
#     # }
#     # countnum.insert_one(data)
#     x = 0
#     if i['handler'] == '刘勇豪':
#         # countnum.update({'name': i['name']}, {'$set': {'countnum': 0}})
#         print(i)

# for i in countcur:
#     data = {
#         'name':i['name'],
#         'account':i['account'],
#         'countnum':0,
#         'comm':0,
#         're':0,
#         'datetime':'',
#         'cash':0,
#         'text':'',
#         'handler':i['handler']
#
#     }
#     counts.insert_one(data)



#删
# memberlist.remove({'name':'罗菲燕','handler':'陈永富'})
# memberlist.update({'name':'吕桂珍2'},{'$set':{'name':'吕桂珍'}})
# counts.remove({'name':'刘萍'})
#
# data = {
#     'name':'周晶晶',
#     'account':'bjzjjing',
#     'countnum':0,
#     'comm':0,
#     're':0,
#     'datetime':'',
#     'cash':0,
#     'text':'',
#     'handler':'刘勇豪'
#
# }
# counts.insert_one(data)
#
# data = {
#     'name':'鄢林华',
#     'account':'xjylhua',
#     'countnum':0,
#     'comm':0,
#     're':0,
#     'datetime':'',
#     'cash':0,
#     'text':'',
#     'handler':'徐莉媛'
#
# }
# counts.insert_one(data)




#改
# countnum.update({'name':'张克成'},{'$set':{'countnum':3}})

# 增
# data = {
#     'name':'鄢林华',
#     'account':'xjylhua',
#     'countnum':0,
#     'handler':'徐莉媛'
#
# }
# countnum.insert_one(data)

# for i in countcur:

    # data = {
    #     'name':'信妍',
    #     'account':'bjxyan',
    #     'countnum':7,
    #     'handler':'王晓英'
    #
    # }
    #countnum.insert_one(data)
    # countnum.update({'account':'bjwtt'},{'$set':{'countnum':22}})
    # if i['handler'] == '刘勇豪':
    #     print(i['name'])
    #     countnum.update({'name': i['name']}, {'$set': {'countnum': 0}})

#print(memberlist.find_one({'name':'朱'}))
# 增
# data = {
#     'name':'朱桦',
#     'account':'bjzhuhua',
#     'acc_number':1,
#     'pw':'3353300lll',
#     'Email':['17726743456@163.com','a17726743456@163.com','b17726743456@163.com'],
#     'Emailpw':['ly654321','ly654321','ly654321'],
#     'handler':'刘玉芬'
#
# }
# memberlist.insert_one(data)

# data = {
#     'name':'蔡光源',
#     'account':'gscgyuan',
#     'acc_number':3,
#     'pw':'cgy_686868',
#     'Email':'18009358722@163.com',
#     'Emailpw':'cgy686868',
#     'handler':'刘勇豪',
#         }
# memberlist.insert_one(data)

#删
# memberlist.remove({'name':'季霞','handler':'刘勇豪'})
# 改
# memberlist.update_one({'name':'张颖', 'handler':'刘勇豪'},{'$set':{'acc_number':7}})
#ziliao.remove(spec_or_id={"_id":ObjectId('5050457a1308122ec272d24c')},safe=True)w
#查
#print(ziliao.find_one({'name':'郑珮'}))

#遍历数据
# a = ['李秀敏','裴艳丽','杨印梅','郭小立','李英俊','朱晓光',
#      '卢小娟','刘玉杰','宋建英','项丽清','张丽媛']
# x = 0
# b = [ '王艺霏', '金花', '张丽阁','刘勇豪','江国华','胡治国', '张建国','徐恒春', '曹戈冲', '毛占伟', '张宏杰', '张晓希','赵海娅','张朋玲','李磊','邬美丽','王彬','张云云','乔凤民','程垒','朱义国','张桂芬','张欣','张小飞','孙莹',
#      '王晓英','范为','李想','靳桂兰','王志英','张小杰','王晓燕','赵保玉','文平','白鹤鸣','朱莹莹','张婷','吴建君','奚巧燕','王敏燕','冯亚芳','金亚娣','葛云莲','储彩球',
#      '赵士超', '王若泰','朱晓光','卢小娟','杨倪','陈柱','申艳华','施优琴','庄红娟','杨政','华小英', '王爱华', '陈明双', '朱云华', '杨印梅', '黄海凇', '李英俊','郭一辰','罗春辉','刘玉芬', '冯明强','吴庆军',
#       '胡刚禄', '吴玉玲', '徐燕宇', '刘玉杰', '应鹰', '王培珍','张燕', '李娟娟', '张彩云', '孙炳权', '崔淑玲', '武凯鹏', '高晓瑞','韩春丽','陆雪芬','']
# n = 1
# for i in cursor:
#     x = i['acc_number'] + x
#     a.append(i['name'])
#     print(i)
# print(a)
# print(x)
#
# for i in cur:
#
#     if i['name'] in ['潘丽平','翁金林','翁金勇','杨晶','刘泽春','陈玉梅','翁莹莹','翁丹丹','王丹','赵辉','王德文','曹振林','宁其侠']:
#         # data = {
#         #     'name':i['name'],
#         #     'account':i['account'],
#         #     'acc_number':i['acc_number'],
#         #     'pw':i['pw'],
#         #     'Email':i['Email'],
#         #     'Emailpw':i['Emailpw'],
#         #     'handler':'江国华'
#         #
#         # }
#         # memberlist.insert_one(data)
#         memberlist.update({'name': i['name']}, {'$set': {'handler': '郝宝玲'}})


# 增
# data = {
#     'name':'刘文娟',
#     'account':'bjlwju',
#     'acc_number':3,
#     'pw':'hp985721',
#     'Email':'13212802009@163.com',
#     'Emailpw':'zhang87743511',
#     'handler':'李玲玲'
#
# }
# memberlist.insert_one(data)
# memberlist.update({'name':'刘勇豪','handler':'刘勇豪'},{'$set':{'Emailpw':'xmanjw97'}})
# memberlist.update({'name':'王春丽','handler':'李稼伶'},{'$set':{'handler':'李玲玲'}})
# memberlist.update({'name':'王虹','handler':'徐莉媛'},{'$set':{'account':'hbwangh'}})
# memberlist.update({'name':'梁雪瑞','handler':'李秀敏'},{'$set':{'Email':'15868072627@163.com','Emailpw':'xr2627'}})
# memberlist.update({'name':'吕振宁','handler':'周丽丽'},{'$set':{'Email':'hljlzning@163.com','Emailpw':'lzn12345'}})
# memberlist.update({'name':'钟洪强','handler':'陈永富'},{'$set':{'Email':'13760169872@163.com','Emailpw':'JLFAIQIUJU2826'}})
# memberlist.update({'name':'文惊燕','handler':'刘玉芬'},{'$set':{'Email':'wenjingyan88@163.com','Emailpw':'13521054987'}})
# memberlist.update({'name':'于萨','handler':'刘玉芬'},{'$set':{'Email':'15373897471@163.com','Emailpw':'xjy333777'}})

# memberlist.remove({'name':'刘英玲','handler':'郝婧萱'})
zll=[]
lyh=[]
clp=[]
wl=[]
wsb=[]
wxy=[]

for i in cur:
    # if i['handler'] == '杨晓庆':
    #     zll.append(i['name'])
    # if i['handler'] == '刘勇豪':
    #     lyh.append(i['name'])
    # if i['handler'] == '王玲':
    #     clp.append(i['name'])
    # if i['handler'] == '陈连萍':
    #     wl.append(i['name'])
    # if i['handler'] == '包小兰':
    #     wsb.append(i['name'])
    # if i['handler'] == '李秀敏':
    #     wxy.append(i['name'])
    print(i)


# print(zll)
# print(lyh)
# print(clp)
# print(wl)
# print(wsb)
# print(wxy)