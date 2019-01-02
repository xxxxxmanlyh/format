from selenium import webdriver
import time
import poplib
from email.parser import Parser
from pymongo import MongoClient
client = MongoClient()

db = client.BTC
memberlist = db.member




# email = '13608991198@163.com' #邮箱 非常重要！
# mailusermailpassword = 'zdx6767'
# pw = 'zdx654321'
#
# email = '18190720528@163.com' #邮箱 非常重要！
# mailusermailpassword = 'hpy1964gpl0513'
# pw = 'hpy1964gpl0513'


# pw = "mao2018323"
# email = "wangaihua2018323@163.com"#邮箱 非常重要！
# mailusermailpassword = "mao2018323"


# pw = "zyh654321"
# email = "15888561212@163.com"#邮箱 非常重要！
# mailusermailpassword = "zyh1212"

# email = 'zhaiyewang99@163.com'
# mailusermailpassword = 'liu7217234'
# pw = "liu7217234"#瞿叶旺属于刘勇豪
#
# email = 'wangxiaozhi99@163.com'
# mailusermailpassword = 'liu7217234'
# pw = "liu7217234"#王晓芝属于刘勇豪


i = 1
# arry = ['D61981EF11877221','D5954A1B8AFC9325','F91F66DD58065E42','3BF46AD9ADB4E74D','A4C1B3122E4B91B6','4F9A10B2C31D5A87','3A2094F00E47E00E']

arry = ['5cEU9M9E','F3tEeeoi','aXFcmpuu','DJpS914j','4EjtvOCb','dpRZ0iEh','zHFqrtoN',
        'A3D967019E68F682', 'g6Uy4N1U', 'C6ABA2FCEB1D4B0F', '5E18A3446DF2455B', '45762A1CE04640D2','9A278893D55B1CD9', '6B0362E4F14D080A',
        '8E2E5C303EF8E0BF', '43AA92F93D7CF08E', '0AC4A7D16313A44B', '096E8BF88CFC218E', 'F6720B678F34BECE','770C1B6A6672F755', '6E0446378842B8D1',
        'A15370387AC5FEBD', '1437C5307B66E5BD', '67F9DF7B1E0A2C6B', 'C655CA93765E9D6C', '713770AF3219C649','07609FDF925F3EC1', 'D5F4065904566409',
        'D7EEF0F49B183E62', '696607653445B648', '3ED1ADF39B3EC8C8']


email = 'bjxhying4115@163.com'
mailusermailpassword = 'xhy12345'
pw = "xhy12345*"#徐洪英属于郝婧萱











account = []
z = memberlist.find_one({'Email': email})
# z = memberlist.find_one({'name': allname,'handler':handler})
print('姓名：'+ z['name'])

if z['acc_number'] == 1:
    print('账户：{1}001    密码：{0} '.format( z['pw'], z['account']))
else:
    print('账户:{2}001-00{0}    密码：{1} '.format(z['acc_number'],z['pw'],z['account']))
if len(email) ==3:
    print('{0}   {1} \n{2}     {3}  \n{4}     {3}'.format(email[0],mailusermailpassword[0],email[1],mailusermailpassword[1],email[2]))
else:
    print('邮箱：{0}   邮箱密码：{1}'.format(email, mailusermailpassword, email,
                                                        mailusermailpassword))
    print('bitfoliex钱包账户为本账户邮箱，密码为：{0}'.format(arry[0]))
if i > 2:
    print('账户001-00X形式的意思为多账户的意思。即账户为XXX001,XXX002以此类推')


for n in range(1,z['acc_number']+1):
    if n <=9:
        account.append(z['account']+'00'+str(n))
    else:
        account.append(z['account'] + '0' + str(n))

print(account)

def get_parsed_msg(email,password):
    # 邮箱个人信息
    useraccount = email
    password = password
    if useraccount.split("@")[1:][0] == "126.com":
        # 邮件服务器地址
        pop3_server = 'pop.126.com'
    elif useraccount.split("@")[1:][0] == "163.com":
        # 邮件服务器地址
        pop3_server = 'pop.163.com'
    # 开始连接到服务器
    server = poplib.POP3(pop3_server)
    # 可选项： 打开或者关闭调试信息，1为打开，会在控制台打印客户端与服务器的交互信息
    #server.set_debuglevel(1)
    # 可选项： 打印POP3服务器的欢迎文字，验证是否正确连接到了邮件服务器
    #print(server.getwelcome().decode('utf8'))
    # 开始行身份验证
    server.user(useraccount)
    server.pass_(password)
    # 使用list()返回所有邮件的编号，默认为字节类型的串
    resp, mails, octets = server.list()
    #print('邮件总数： {}'.format(len(mails)))
    # 下面单纯获取最新的一封邮件
    total_mail_numbers = len(mails)
    # 默认下标越大，邮件越新，所以total_mail_numbers代表最新的那封邮件
    response_status, mail_message_lines, octets = server.retr(total_mail_numbers)
    msg_content = b'\r\n'.join(mail_message_lines).decode('gbk')
    # 邮件原始数据没法正常浏览，因此需要相应的进行解码操作
    msg = Parser().parsestr(text=msg_content)
    #print('解码后的邮件信息:\n{}'.format(msg))
    # 关闭与服务器的连接，释放资源
    server.close()
    return msg,total_mail_numbers

while i <= z['acc_number']:
    if i == 1:
        emails = email
        mailusermailpasswords = mailusermailpassword
    elif i == 2:
        emails = email
        mailusermailpasswords = mailusermailpassword
    else:
        emails = email
        mailusermailpasswords = mailusermailpassword
    print("这是第{0}个账户的修改密码".format(i))
    wd = webdriver.Chrome("/usr/local/bin/chromedriver")
    # chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_argument('--headless')
    # chrome_options.add_argument('--disable-gpu')
    # wd = webdriver.Chrome(chrome_options=chrome_options, executable_path='/usr/local/bin/chromedriver')
    wd.get("https://backoffice.airbitclub.com/auth/login")  # 打开登录界面
    wd.find_element_by_id("user").clear()
    wd.find_element_by_id("user").send_keys(account[i-1])   # 清除输入框并且输入账户
    wd.find_element_by_id("password").clear()
    wd.find_element_by_id("password").send_keys(arry[(i-1)]) #清除输入框并且输入密码
    wd.find_element_by_name('action').click()  #点击登录
    time.sleep(5)
    wd.get('https://backoffice.airbitclub.com/zh-CN/app/profile')
    time.sleep(2)
    wd.find_element_by_xpath('/html/body/app-root/app-backoffice/div/app-modal/div/i').click()
    # time.sleep(2)
    wd.find_element_by_xpath('//*[@id="password"]').send_keys(pw) #输入密码
    wd.find_element_by_xpath('//*[@id="confirm"]').send_keys(pw)#再次输入密码
    print(emails,mailusermailpasswords)
    wd.find_element_by_xpath('//*[@id="send-group-information"]/i').click()#点击发送token请求
    maillen = get_parsed_msg(emails,mailusermailpasswords)[1]
    i = i + 1
    while maillen >0:
        maillens = get_parsed_msg(email, mailusermailpassword)[1]
        if maillens > maillen:
            msg = get_parsed_msg(email, mailusermailpassword)[0]
            parts = msg.get_payload()
            try:
                content = str(msg).split('<hr style=3D"border-bottom:1px solid #FFC300;">')[1][:6].strip()
                print(content)
            except Exception as e:
                while maillens > 0:
                    maillenmax = get_parsed_msg(email, mailusermailpassword)[1]
                    if maillenmax > maillens:
                        msg = get_parsed_msg(email, mailusermailpassword)[0]
                        parts = msg.get_payload()
                        content = str(msg).split('<hr style=3D"border-bottom:1px solid #FFC300;">')[1][:9].strip()
                        break
                    else:
                        time.sleep(5)
                    print(content)
            wd.find_element_by_xpath('//*[@id="send-group-information"]/input').send_keys(content)
            time.sleep(1)
            wd.find_element_by_xpath('//*[@id="header"]/div[2]/app-profile/div/div[3]/div[2]/form/button').click()
            time.sleep(5)
            wd.quit()
            break
        else:
            time.sleep(5)

print('姓名：'+ z['name'])
if z['acc_number'] == 1:
    print('账户：{1}001    密码：{0} '.format( z['pw'], z['account']))
else:
    print('账户:{2}001-00{0}    密码：{1} '.format(z['acc_number'],z['pw'],z['account']))
if len(email) ==3:
    print('{0}   {1} \n{2}     {3}  \n{4}     {3}'.format(email[0],mailusermailpassword[0],email[1],mailusermailpassword[1],email[2]))
else:
    print('邮箱：{0}   邮箱密码：{1}'.format(email, mailusermailpassword, email,
                                                        mailusermailpassword))
    print('bitfoliex钱包账户为本账户邮箱，密码为：{0}'.format(arry[0]))
if i > 2:
    print('账户001-00X形式的意思为多账户的意思。即账户为XXX001,XXX002以此类推')