from selenium import webdriver
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
import poplib
from email.parser import Parser
from pymongo import MongoClient
from selenium.webdriver.common.action_chains import ActionChains

name = '徐'
mainname = '洪英'
allname = '徐洪英'
sex = '女'
address = '河南省固始县徐集乡沈岗村'
year = '1970'
month = '五月'
day = '3'
tel = '13939024828'
email = 'bjxhying4115@163.com' #邮箱 非常重要！
mailusermailpassword = 'xhy12345'
pw = 'xhy12345*'
i = 1 #起始账号
num = 1 #一共多少单
handler = '郝婧萱'
connectname = '陈玉梅'


listnum = '001'
country = "China"
state = "Henan"#Shaanxi
city = 'Xinyang' #Taiyüan Nei Mongol Qiqihar Ordos
account_1 = 'hnxhy'#用户名 非常重要！


password=[]

def get_sponsor(connectname,handler):
    client = MongoClient()
    db = client.BTC
    memberlist = db.member
    accountcur = memberlist.find()
    for i in accountcur:
        if i['name'] == connectname and i['handler'] == handler:
            account = i['account']
    return str(account)

sponsor = get_sponsor(connectname,handler)+listnum #起始球 非常重要！
# sponsor = 'xjfli001'
print(sponsor)


arry = {}
left = 2
right = 1
bian = right



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


def scroll(driver):
    driver.execute_script("""   
        (function () {   
            var y = document.body.scrollTop;   
            var step = 100;   
            window.scroll(0, y);   


            function f() {   
                if (y < document.body.scrollHeight) {   
                    y += step;   
                    window.scroll(0, y);   
                    setTimeout(f, 50);   
                }  
                else {   
                    window.scroll(0, y);   
                    document.title += "scroll-done";   
                }   
            }   


            setTimeout(f, 1000);   
        })();   
        """)

def insertDB(allname):
    client = MongoClient()
    # allname = '王利军'
    db = client.BTC
    memberlist = db.member
    counts = db.countnum
    if memberlist.find_one({'name': allname,'handler': handler}) == None:
        data = {
            'name': allname,
            'account': account_1,
            'acc_number': num,
            'pw': pw,
            'Email': email,
            'Emailpw': mailusermailpassword,
            'handler': handler,
        }
        memberlist.insert_one(data)
        data = {
            'name':allname,
            'account':account_1,
            'countnum': 0,
            'comm': 0,
            're': 0,
            'datetime': '',
            'cash': 0,
            'text': '',
            'handler':handler

        }

        counts.insert_one(data)
        print("email = '{0}'".format(email))
        print("mailusermailpassword = '{0}'".format(mailusermailpassword))
        print('pw = "{0}"#{1}属于{2}'.format(pw, allname,handler))
        print('arry = {0}'.format(password))
        print("{0}资料已加入数据库".format(allname))
    else:
        allname = '{0}2'.format(allname)
        data = {
            'name': allname,
            'account': account_1,
            'acc_number': num,
            'pw': pw,
            'Email': email,
            'Emailpw': mailusermailpassword,
            'handler': handler,
        }
        memberlist.insert_one(data)
        data = {
            'name':allname,
            'account':account_1,
            'countnum': 0,
            'comm': 0,
            're': 0,
            'datetime': '',
            'cash': 0,
            'text': '',
            'handler':handler

        }
        counts.insert_one(data)
        print("email = '{0}'".format(email))
        print("mailusermailpassword = '{0}'".format(mailusermailpassword))
        print('pw = "{0}"#{1}属于{2}'.format(pw, allname, handler))
        print('arry = {0}'.format(password))
        print("{0}资料已加入数据库".format(allname))

# insertDB(allname)

wd = webdriver.Chrome("/usr/local/bin/chromedriver")
wd.implicitly_wait(300)
wd.get("https://backoffice.airbitclub.com/zh-CN/login")    # 打开登录界面
wd.find_element_by_id("user").clear()
wd.find_element_by_id("user").send_keys("bjyh001")   # 清除输入框并且输入账户
# wd.find_element_by_id("user").send_keys("bjzli001")   # 清除输入框并且输入账户
wd.find_element_by_id("password").clear()
wd.find_element_by_id("password").send_keys('liu7217234') #清除输入框并且输入密码
# wd.find_element_by_id("password").send_keys('zl123123') #清除输入框并且输入密码
wd.find_element_by_name('action').click()   #点击登录

time.sleep(5)

wd.get('https://backoffice.airbitclub.com/zh-CN/app/binary')
time.sleep(2)
WebDriverWait(wd,20,1).until(EC.presence_of_element_located((By.XPATH,'/html/body/app-root/app-backoffice/div/app-modal/div/i'))).click()
# time.sleep(2)
# wd.find_element_by_xpath('//*[@id="verification-wrapper"]/i').click()


time.sleep(5)

while i <= num:
    if i > 9:
        account = account_1 + "0" + str(i)
    else:
        account = account_1 + "00" + str(i)
    if i == 2 or i == 3:
        sponsor = account_1+"00"+str(1)
    elif i == 4 or i == 5:
        sponsor = account_1+"00"+str(2)
    elif i == 6 or i == 7:
        sponsor = account_1+"00"+str(3)
    elif i == 8 and num == 9:
         sponsor = account_1+"004"
    elif i == 9 and num == 9:
        sponsor = account_1+"007"
    elif i == 8 or i == 9:
        sponsor = account_1+"00"+str(4)
    elif i == 10 or i == 11:
        sponsor = account_1+"00"+str(5)
    elif i == 12 or i == 13:
        sponsor = account_1+"00"+str(6)
    elif i == 14 or i == 15:
        sponsor = account_1+"00"+str(7)
    elif i == 16 or i == 17:
        sponsor = account_1 + "00" + str(8)
    elif i == 18 or i == 19:
        sponsor = account_1 + "00" + str(9)
    elif i == 20 or i == 21:
        sponsor = account_1 + "0" + str(10)
    elif i == 22 or i == 23:
        sponsor = account_1 + "0" + str(11)
    elif i == 24 or i == 25:
        sponsor = account_1 + "0" + str(12)
    elif i == 26 or i == 27:
        sponsor = account_1 + "0" + str(13)
    elif i == 28 or i == 29:
        sponsor = account_1 + "0" + str(14)
    elif i == 30 or i == 31:
        sponsor = account_1 + "0" + str(15)
    if num == 5 and i == 5:
        sponsor = account_1 + "00" + str(3)
    try:
        # wd.find_element_by_class_name("field-default ng-untouched ng-pristine ng-valid").send_keys(sponsor)
        wd.find_element_by_xpath('//*[@id="header"]/div[2]/app-binary/div/div[2]/div/div/input').send_keys(sponsor)
    except Exception as e:
        wd.refresh()
        wd.find_element_by_xpath('//*[@id="verification-wrapper"]/i').click()
        time.sleep(5)
        # wd.find_element_by_class_name("field-default ng-untouched ng-pristine ng-valid").send_keys(sponsor)
        wd.find_element_by_xpath('//*[@id="header"]/div[2]/app-binary/div/div[2]/div/div/input').send_keys(sponsor)
    #searchtree.send_keys(sponsor)
    time.sleep(2)
    wd.find_element_by_class_name("icon-search").click()


    wd.find_element_by_class_name("icon-newuser-new").click()  #注册新用户
    if i == 1 :
        wd.find_element_by_xpath('//*[@id="wrapper-register"]/div[2]/div[2]/app-personal-information/form/div[1]/div[2]/div[2]/input').send_keys(Keys.SPACE)
    else:
        wd.find_element_by_xpath('//*[@id="wrapper-register"]/div[2]/div[2]/app-personal-information/form/div[1]/div[2]/div[1]/input').send_keys(Keys.SPACE)
        time.sleep(2)
        wd.find_element_by_xpath('//*[@id="otherUsername"]').send_keys(account_1+'001')
        time.sleep(1)
        # wd.find_element_by_xpath('//*[@id="wrapper-register"]/div[2]/div[2]/app-personal-information/form/div[2]/div/div[1]/div/i').click()

    #maillen = get_parsed_msg(email, mailusermailpassword)[1]  # 获取没发密码之前的邮件数
    wd.find_element_by_id("username").send_keys(account) #用户名
    time.sleep(1)
    wd.find_element_by_xpath('//*[@id="wrapper-register"]/div[2]/div[2]/app-personal-information/form/div[3]/div/button/span').click()

    wd.find_element_by_id("firsname").send_keys(mainname) #姓名的名
    wd.find_element_by_id("lastName").send_keys(name) #姓名的姓

    Select(wd.find_element_by_id('month')).select_by_visible_text(month)
    Select(wd.find_element_by_id("day")).select_by_visible_text(day)
    Select(wd.find_element_by_id("year")).select_by_visible_text(year)
    if sex == '男':
        wd.find_element_by_xpath('//*[@id="wrapper-register"]/div[2]/div[2]/app-personal-information/form/div[5]/div[1]').click()
    elif sex == '女':
        wd.find_element_by_xpath('//*[@id="wrapper-register"]/div[2]/div[2]/app-personal-information/form/div[5]/div[2]').click()

    wd.find_element_by_id('email').send_keys(email)
    # wd.find_element_by_xpath('//*[@id="wrapper-register"]/div[2]/div[2]/app-personal-information/form/div[5]/div[3]/div[1]/i').click()
    # maillen = get_parsed_msg(email, mailusermailpassword)[1]

    wd.find_element_by_xpath('//*[@id="wrapper-register"]/div[2]/div[2]/app-personal-information/form/div[5]/div[4]/div/button').click()
    time.sleep(1)
    wd.find_element_by_xpath('//*[@id="wrapper-register"]/div[2]/div[2]/app-personal-information/form/div[5]/div[4]/div/ul/div/input').send_keys('China')
    time.sleep(1)
    wd.find_element_by_xpath('//*[@id="wrapper-register"]/div[2]/div[2]/app-personal-information/form/div[5]/div[4]/div/ul/li/p[1]').click()
    time.sleep(1)
    wd.find_element_by_id('phoneNumber').send_keys(tel)

    Select(wd.find_element_by_id("country")).select_by_visible_text(country)

    Select(wd.find_element_by_id("state")).select_by_visible_text(state)

    Select(wd.find_element_by_id("city")).select_by_visible_text(city)
    time.sleep(1)

    # while maillen > 0:
    #     maillens = get_parsed_msg(email, mailusermailpassword)[1]
    #     if maillens > maillen:
    #         msg = get_parsed_msg(email, mailusermailpassword)[0]
    #         parts = msg.get_payload()
    #         try:
    #
    #             content = str(parts).split('<hr style=3D"border-bottom:1px solid #FFC300;">')[1][:6].strip()
    #         except Exception as e:
    #             while maillens > 0:
    #                 maillenmax = get_parsed_msg(email, mailusermailpassword)[1]
    #                 if maillenmax > maillens:
    #                     msg = get_parsed_msg(email, mailusermailpassword)[0]
    #                     parts = msg.get_payload()
    #                     content = str(parts).split('<hr style=3D"border-bottom:1px solid #FFC300;">')[1][:6].strip()
    #                     break
    #                 else:
    #                     time.sleep(5)
    #         print(content)
    #         wd.find_element_by_id("emailConfirmation").send_keys(content)
    #         time.sleep(1)
    #         wd.find_element_by_xpath('//*[@id="wrapper-register"]/div[2]/div[2]/app-personal-information/form/div[5]/div[3]/div[2]/a/i').click()
    #         time.sleep(1)
    #         break
    #     else:
    #         time.sleep(1)

    wd.find_element_by_id("sponsorUsername").send_keys(sponsor) #推荐人
    # wd.find_element_by_id("sponsor").send_keys('gdygqiang001')  # 推荐人
    time.sleep(2)
    wd.find_element_by_xpath('//*[@id="wrapper-register"]/div[2]/div[2]/app-personal-information/form/div[7]/div/button/span').click()
    # time.sleep(3)
    # a = 3
    # while i <1000:
    #     time.sleep(a)
    #     if wd.find_element_by_xpath('//*[@id="wrapper-register"]/div[2]/div[2]/app-personal-information/form/div[7]/div/span').text == '':
    #         wd.find_element_by_id("sponsorUsername").click()
    #         time.sleep(2)
    #         wd.find_element_by_xpath(
    #             '//*[@id="wrapper-register"]/div[2]/div[2]/app-personal-information/form/div[7]/div/i').click()  # 搜索推荐人
    #         a = a+1
    #     else:
    #         a  = 3
    #         break
    # time.sleep(1)
    # # wd.find_element_by_id("partition_new_user_terms").send_keys(Keys.SPACE)  # 打勾
    # time.sleep(1)
    # wd.find_element_by_class_name("btn btn-grey").click()  # 全部填完 下一步
    # time.sleep(1)
    # wd.find_element_by_class_name('btn btn-default').click() #选择1000美金账户
    # wd.find_element_by_class_name('btn btn-grey terms-button').click() #条款和条件
    # time.sleep(1)
    # # 将滚动条移动到页面的底部
    # js = "var q=document.documentElement.scrollTop=100000"
    # wd.execute_script(js)
    # time.sleep(3)
    # wd.find_element_by_class_name('check-input').send_keys(Keys.SPACE)#打勾
    # wd.find_element_by_class_name('btn btn-grey').click() #发送
    #
    #
    #
    # comwallet = wd.find_element_by_xpath('//*[@id="wallets-section"]/div[2]/div[2]/span[2]').text.split("$")[1:]
    # crashwallet = wd.find_element_by_xpath('//*[@id="wallets-section"]/div[3]/div[2]/span[2]').text.split("$")[1:]
    # rewallet = wd.find_element_by_xpath('//*[@id="wallets-section"]/div[4]/div[2]/span[2]').text.split("$")[1:]
    # if comwallet[0].find(',') == 1 or comwallet[0].find(',') == 2:
    #     wd.find_element_by_id(
    #         'partition_new_user_payment_partition_attributes_payment_wallet_partitions_attributes_0_amount').send_keys(
    #         1000)
    #     wd.find_element_by_id('submit-user').click()
    # elif comwallet[0].find(',') == -1 and (rewallet[0].find(',') == 1 or rewallet[0].find(',') == 2):
    #     wd.find_element_by_id(
    #         'partition_new_user_payment_partition_attributes_payment_wallet_partitions_attributes_2_amount').send_keys(
    #         1000)
    #     wd.find_element_by_id('submit-user').click()
    # else:
    #     print("没有钱注册了")

    i = i+1


    aa = input()

    time.sleep(1)
    wd.find_element_by_xpath('//*[@id="wrapper-register"]/div[2]/div[2]/app-personal-information/form/button').click()  # 全部填完 下一步
    time.sleep(2)
    wd.find_element_by_xpath('//*[@id="3"]/button').click() #选择1000美金账户
    wd.find_element_by_xpath('//*[@id="wrapper-register"]/div[2]/div[2]/app-select-membership/form/div/div[2]/button[2]').click() #条款和条件
    time.sleep(3)
    wd.find_element_by_xpath('//*[@id="wrapper-register"]/div[2]/div[2]/app-select-membership/app-terms-and-conditions/form/div/div[36]/div').click()#打勾
    wd.find_element_by_xpath('//*[@id="wrapper-register"]/div[2]/div[2]/app-select-membership/app-terms-and-conditions/form/div/button').click() #发送
    time.sleep(2)
    wd.find_element_by_xpath('//*[@id="wrapper-register"]/div[2]/div[2]/app-confirmation/div/div[2]/button[2]').click()
    time.sleep(4)
    Select(wd.find_element_by_xpath('//*[@id="wrapper-register"]/div[2]/div[2]/app-payment-method/div[2]/div/select')).select_by_visible_text('ABC/S-CryptoWallets')
    time.sleep(1)
    wd.find_element_by_xpath('//*[@id="wrapper-register"]/div[2]/div[2]/app-payment-method/div[2]/app-wallets-register/div[1]/div[1]/input').send_keys(300)
    wd.find_element_by_xpath('//*[@id="wrapper-register"]/div[2]/div[2]/app-payment-method/div[2]/app-wallets-register/div[1]/div[2]/input').send_keys(700)
    time.sleep(5)
    wd.find_element_by_xpath('//*[@id="wrapper-register"]/div[2]/div[2]/app-payment-method/div[2]/app-wallets-register/div[2]/button[2]').click()
    if i - num == 1:
        insertDB(allname)
    time.sleep(5)
    try:
        WebDriverWait(wd,10,1).until(EC.presence_of_element_located((By.XPATH,'//*[@id="wrapper-register"]/div[2]/div[2]/app-payment-method/app-register-success/div/button'))).click()
    except Exception:
        time.sleep(5)
        WebDriverWait(wd, 10, 1).until(EC.presence_of_element_located((By.XPATH,
                                                                       '//*[@id="wrapper-register"]/div[2]/div[2]/app-payment-method/app-register-success/div/button'))).click()

    WebDriverWait(wd, 20, 1).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/app-root/app-backoffice/div/app-modal/div/i'))).click()
    time.sleep(2)
    # wd.find_element_by_xpath('//*[@id="verification-wrapper"]/i').click()


if len(password)>0:
    print("email = '{0}'".format(email))
    print("mailusermailpassword = '{0}'".format(mailusermailpassword))
    print('pw = {0}'.format(pw))
    print('arry = {0}'.format(password))



