from selenium import webdriver
import time
import poplib
from email.parser import Parser
from pymongo import MongoClient
client = MongoClient()

db = client.BTC
memberlist = db.member

i = 7

arry = ['58E393F8ADD86998','727D19E911E17531','70A9112DC44B8093','DD5CECD003F11F91','907F1AA5E1277AB0','E3B96F05C14FD46E','7331D1A5E3F1940E',
        '709E0C1C21934388', '6A0B4194062CDD54', '406AD3946D25BB4E', 'D5880DBAD9DA51AD', '314528EE18A1F40D','35FB44606D6AD7AF', 'E922C282D1F4F3B8',
        'DDDE058C89159100', 'F6654511375C297A', '0AC4A7D16313A44B', '096E8BF88CFC218E', 'F6720B678F34BECE','770C1B6A6672F755', '6E0446378842B8D1',
        'A15370387AC5FEBD', '1437C5307B66E5BD', '67F9DF7B1E0A2C6B', 'C655CA93765E9D6C', '713770AF3219C649','07609FDF925F3EC1', 'D5F4065904566409',
        'D7EEF0F49B183E62', '696607653445B648', '3ED1ADF39B3EC8C8']


email = 'l13910516475@163.com'
mailusermailpassword = 'ljp6475'
pw = "ljp54321"#王寿涛属于刘勇豪


account = []
z = memberlist.find_one({'Email': email})
# z = memberlist.find_one({'name': '张颖2'})
print(z['name'])
if z['acc_number'] == 1:
    print('{1}001    {0} '.format( z['pw'], z['account']))
else:
    print('{2}001-00{0}    {1} '.format(z['acc_number'],z['pw'],z['account']))
if len(email) ==3:
    print('{0}   {1} \n{2}     {3}  \n{4}     {3}'.format(email[0],mailusermailpassword[0],email[1],mailusermailpassword[1],email[2]))
else:
    print('{0}   {1} \n{2}     {3}'.format(email, mailusermailpassword, email,
                                                          mailusermailpassword))
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
    wd.find_element_by_id("user_username").clear()
    wd.find_element_by_id("user_username").send_keys(account[i-1])   # 清除输入框并且输入账户
    wd.find_element_by_id("user_password").clear()
    wd.find_element_by_id("user_password").send_keys(arry[(i-1)]) #清除输入框并且输入密码
    wd.find_element_by_class_name("button-blue").click()   #点击登录

    wd.get('https://backoffice.airbitclub.com/user_profile')
    time.sleep(2)
    wd.find_element_by_xpath('//*[@id="user_password"]').send_keys(pw) #输入密码
    wd.find_element_by_xpath('//*[@id="user_password_confirmation"]').send_keys(pw)#再次输入密码
    print(emails,mailusermailpasswords)
    wd.find_element_by_xpath('//*[@id="submit-token-change-password"]').click()#点击发送token请求
    maillen = get_parsed_msg(emails,mailusermailpasswords)[1]
    i = i + 1
    while maillen >0:
            maillens = get_parsed_msg(emails, mailusermailpasswords)[1]
            if maillens > maillen:
                    msg=get_parsed_msg(emails,mailusermailpasswords)[0]
                    parts = msg.get_payload()
                    try:
                        content = str(parts[0]).split('is is')[1:][0][2:60].strip()
                    except Exception as e:
                        while maillens > 0:
                            maillenmax = get_parsed_msg(emails, mailusermailpasswords)[1]
                            if maillenmax > maillens:
                                msg = get_parsed_msg(emails, mailusermailpasswords)[0]
                                parts = msg.get_payload()
                                content = str(parts[0]).split('is is')[1:][0][2:60].strip()
                                break
                            else:
                                time.sleep(5)
                    print(content)
                    wd.find_element_by_id("user_token").send_keys(content)
                    time.sleep(1)
                    wd.find_element_by_id('update-password-home').click()
                    time.sleep(5)
                    wd.quit()
                    break
            else:
                    time.sleep(5)