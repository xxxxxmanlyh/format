from selenium import webdriver
import time
from selenium.webdriver.support.select import Select
import poplib
from email.parser import Parser
from pymongo import MongoClient
from selenium.webdriver.common.by import By


handler = '包小兰'
maxlist = ['刘勇豪','高二敏','牟艳丽','朱冬','包小兰', '郑佩', '崔薇', '包花善', '柳玉梅', '王燕', '包天白', '魏儒嘉', '包爱军','包小兰2']
namelist = []
account_1 = ""
pw = ""
maxnum = ""
sponsor = ""
usermail = ""
mailusermailpassword = ""
mainaccount = 'bjyh001'
datetime = time.strftime('%Y年%m月%d日',time.localtime(time.time()))

client = MongoClient()#连接mongoDB
db = client.BTC #连接数据库
memberlist = db.member #找到合集
cashnum = db.cashnum  # 钱的记录
countnum = db.count #圈米计数记录

#获得所需串米人的资
def get_ziliao(name):
    global account_1
    global pw
    global maxnum
    global sponsor
    global usermail
    global mailusermailpassword
    if memberlist.find_one({'name': name}) == 'None':
        print("没有找到该名字的资料，请正确填写")
    account_1 = memberlist.find_one({'name': name})['account']
    pw = memberlist.find_one({'name': name})['pw']
    maxnum = memberlist.find_one({'name': name})['acc_number']
    sponsor = account_1+"001"
    usermail = memberlist.find_one({'name': name})['Email']
    mailusermailpassword = memberlist.find_one({'name': name})['Emailpw']

#算钱小数据库
def get_cashnum(name,datetime,cash):
    handler = memberlist.find_one({'name':name})['handler']
    # 增
    data = {
        'name':name,
        'datetime':datetime,
        'cash':cash,
        'handler':handler
    }
    cashnum.insert_one(data)
#钱数汇总
def allthemoney(datetime):
    client = MongoClient()  # 连接mongoDB
    db = client.BTC  # 连接数据库
    cashnum = db.cashnum  # 钱的记录
    cur = cashnum.find()
    price = 0
    handler = cashnum.find_one({'name': namelist[0]})['handler']
    for i in cur:
        if i['handler'] == handler and i['datetime'] == datetime:
            price = price + i['cash']
            print('{0}需发人民币：{1}'.format(i['name'], i['cash']))
            cashnum.remove({'name':i['name']})
    print("{0}{1}团队总共需要发人民币：{2}元".format(datetime,handler,price))


#邮箱连接
def get_parsed_msg(usermail,password):
    # 邮箱个人信息
    useraccount = usermail
    password = password
    if useraccount.split("@")[1:][0] == "126.com":
        # 邮件服务器地址
        pop3_server = 'pop.126.com'
    elif useraccount.split("@")[1:][0] == "163.com":
        # 邮件服务器地址
        pop3_server = 'pop.163.com'
    # 开始连接到服务器
    try:
        server = poplib.POP3(pop3_server)
    except Exception as e:
        time.sleep(10)
        server = poplib.POP3(pop3_server)
    # 可选项： 打开或者关闭调试信息，1为打开，会在控制台打印客户端与服务器的交互信息
    #server.set_debuglevel(1)
    # 可选项： 打印POP3服务器的欢迎文字，验证是否正确连接到了邮件服务器
    #print(server.getwelcome().decode('utf8'))
    # 开始进行身份验证
    server.user(useraccount)
    server.pass_(password)
    # 使用list()返回所有邮件的编号，默认为字节类型的串
    resp, mails, octets = server.list()
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

##获取邮箱邮件token数值
def gettoken(wd):
    acounttime = 0
    maillen = get_parsed_msg(usermail, mailusermailpassword)[1]
    time.sleep(2)
    wd.find_element_by_id('submit-token').click()  # 点击发送token请求
    time.sleep(5)
    try:
        if wd.find_element_by_class_name('toast-title').text == 'Token request failed':
            wd.find_element_by_xpath('//a[@class="btn btn-flat btn-danger btn-xs cancel-token pull-right col-md-3 btn-ripple"]').click()
            time.sleep(2)
            wd.find_element_by_id('submit-token').click()
    except Exception as e:
        pass
    while maillen > 0:
        time.sleep(5)
        maillens = get_parsed_msg(usermail, mailusermailpassword)[1]
        if maillens > maillen:
            msg = get_parsed_msg(usermail, mailusermailpassword)[0]
            parts = msg.get_payload()
            content = str(parts[0]).split('is is')[1:][0][2:60].strip()
            wd.find_element_by_id("partition_transfer_partition_token").send_keys(content)

            time.sleep(1)
            maillen = -1
            acounttime = 0
        else:
            if acounttime >= 900:
                wd.find_element_by_xpath(
                    '//a[@class="btn btn-flat btn-danger btn-xs cancel-token pull-right col-md-3 btn-ripple"]').click()
                time.sleep(2)
                wd.find_element_by_id('submit-token').click()
                while maillen > 0:
                    time.sleep(5)
                    maillens = get_parsed_msg(usermail, mailusermailpassword)[1]
                    if maillens > maillen:
                        msg = get_parsed_msg(usermail, mailusermailpassword)[0]
                        parts = msg.get_payload()
                        content = str(parts[0]).split('is is')[1:][0][2:60].strip()
                        wd.find_element_by_id("partition_transfer_partition_token").send_keys(content)

                        time.sleep(1)
                        maillen = -1
                        acounttime = 0
                    else:
                        time.sleep(8)

            else:
                time.sleep(8)
                acounttime = acounttime + 8
#提现格式计算
def tixian(missUSD,rewardUSD,name):
    print(datetime)
    missRMB = (float(missUSD)) * 6.8
    rewardRMB = float(rewardUSD) * 6.8
    allUSD = float(missUSD) + float(rewardUSD)
    print(name)
    print("🌹:(" + str(missUSD)+")＄*6.8=" + str(int(missRMB)) + "元")
    allUSD = float(missUSD) + float(rewardUSD)
    print("🌻:" + str(rewardUSD) + "＄*6.8=" + str(int(rewardRMB)) + "元")
    print("总计:" + str(int(missRMB + rewardRMB)) + "元")
    print("(" + str(allUSD) + "美金)×6.8=(" + str(int(missRMB + rewardRMB)) + ")人民币")
    return int(missRMB + rewardRMB)

# print("需要圈米的姓名：")
# name = input()

cursponer = memberlist.find()
for i in cursponer:
    if i['handler'] == handler:
        if i['name'] in maxlist:
            pass
        else:
            if countnum.find_one({'name': i['name'],'handler': handler})['countnum'] > i['acc_number']:
                pass
            else:
                namelist.append(i['name'])
for name in namelist:
    i = 1
    if countnum.find_one({'name': name, 'handler': handler})['countnum'] == 0:
        i = countnum.find_one({'name': name, 'handler': handler})['countnum'] + 1
    else:
        i = countnum.find_one({'name': name, 'handler': handler})['countnum']
    get_ziliao(name)

    print("{0}的账户一共有{1}个".format(name, maxnum))
    while i <= maxnum:
        wrong = 1
        curse = 1
        if i >= 9:
            account = account_1 + "0" + str(i + 1)
            if name == '寿立庆' and i == 9:
                account = account_1 + "00" + str(i + 1)
        else:
            account = account_1 + "00" + str(i + 1)
            if name == '江国华' and i == 3:
                account = account_1 + str(i + 1)

        if i == maxnum:
            account = account_1 + "001"
            sponsor = mainaccount
            if account == sponsor:
                break
            print("开始第{0}个账户圈米".format(1))
            # itchat.send("开始第{0}个账户圈米".format(1), toUserName=fromusername)
        elif i < maxnum:
            sponsor = account_1 + "001"
            print("开始第{0}个账户圈米".format(i + 1))
            # itchat.send("开始第{0}个账户圈米".format(i + 1), toUserName=fromusername)

        comm = 0
        re = 0
        wd = webdriver.Chrome("/usr/local/bin/chromedriver")
        #chrome_options = webdriver.ChromeOptions()
        # chrome_options.add_argument('--headless')
        # chrome_options.add_argument('--disable-gpu')
        # wd = webdriver.Chrome(chrome_options=chrome_options, executable_path='/usr/local/bin/chromedriver')
        wd.implicitly_wait(10)
        wd.get("https://www.bitbackoffice.com/auth/login")  # 打开登录界面
        locator = (By.XPATH, '//a[@href="/transfers"]')
        try:
            wd.find_element_by_id("user_username").clear()
        except Exception as e:
            wd.refresh()
            wd.find_element_by_id("user_username").clear()
        wd.find_element_by_id("user_username").send_keys(account)  # 清除输入框并且输入账户
        wd.find_element_by_id("user_password").clear()
        wd.find_element_by_id("user_password").send_keys(pw)  # 清除输入框并且输入密码
        wd.find_element_by_class_name("button-blue").click()  # 点击登录
        wd.get("https://www.bitbackoffice.com/transfers")
        try:
            commissions = wd.find_element_by_xpath('//div[@class="col-md-3 col-sm-6"][2]/div/div/p').get_attribute(
                'data-balance')  # 获取动态钱包钱数
            rewards = wd.find_element_by_xpath('//div[@class="col-md-3 col-sm-6"][4]/div/div/p').get_attribute(
                'data-balance')  # 获取静态钱包钱数
        except Exception as e:
            wd.refresh()
            time.sleep(2)
            try:
                commissions = wd.find_element_by_xpath(
                    '//div[@class="col-md-3 col-sm-6"][2]/div/div/p').get_attribute('data-balance')  # 获取动态钱包钱数
                rewards = wd.find_element_by_xpath('//div[@class="col-md-3 col-sm-6"][4]/div/div/p').get_attribute(
                    'data-balance')  # 获取静态钱包钱数
            except Exception as e:
                wd.refresh()
                time.sleep(2)
                try:
                    commissions = wd.find_element_by_xpath(
                        '//div[@class="col-md-3 col-sm-6"][2]/div/div/p').get_attribute(
                        'data-balance')  # 获取动态钱包钱数
                    rewards = wd.find_element_by_xpath(
                        '//div[@class="col-md-3 col-sm-6"][4]/div/div/p').get_attribute(
                        'data-balance')  # 获取静态钱包钱数
                except Exception as e:
                    print("密码或者账号错误,开始下一个账户")
                    wrong = 0
        # itchat.send("第{0}个账户动态钱包：{1}美金，静态：{2}美金".format(i + 1,commissions,rewards), toUserName='{0}'.format(fromusername))
        if i+1 == maxnum :
            print("第1个账户动态钱包：{0}美金，静态：{1}美金".format( commissions, rewards))
        else:
            print("第{0}个账户动态钱包：{1}美金，静态：{2}美金".format(i + 1, commissions, rewards))
        if wrong == 0:
            wrong = 1
            commissions = '0.0'
            rewards = '0.0'
        if int(commissions.split('.')[1]) == 0:
            intcommissions = int(commissions.split('.')[0])
        elif int(commissions.split('.')[1]) > 0:
            intcommissions = float(commissions)
        if int(rewards.split('.')[1]) == 0:
            intrewards = int(rewards.split('.')[0])
        elif int(rewards.split('.')[1]) > 0:
            intrewards = float(rewards)
        while intcommissions > 0 or intrewards > 0:
            gettoken(wd)
            wd.find_element_by_id('search-user').send_keys(sponsor)
            time.sleep(1)
            if wd.find_element_by_id('search-user').text == '':
                wd.find_element_by_id('search-user').clear()
                wd.find_element_by_id('search-user').send_keys(sponsor)
            wd.find_element_by_id("search-btn").click()
            a = 5
            while i < 10000:
                time.sleep(a)
                try:
                    sname = wd.find_element_by_xpath('//*[@id="transfer-to"]').text
                except Exception as e:
                    wd.find_element_by_id('search-user').send_keys(sponsor)
                    time.sleep(1)
                    wd.find_element_by_id("search-btn").click()
                if sname == 'Searching...':
                    a = a + 2
                    wd.find_element_by_id('search-user').clear()
                    wd.find_element_by_id('search-user').send_keys(sponsor)
                    wd.find_element_by_id("search-btn").click()
                else:
                    break

            if intcommissions > 0 and intrewards == 0:
                Select(wd.find_element_by_id("partition_transfer_partition_user_wallet_id")).select_by_visible_text(
                    'commissions wallet ${0}'.format(commissions))
                wd.find_element_by_id('partition_transfer_partition_amount').send_keys(commissions)
                wd.find_element_by_id('submit-transfer').click()
                comm = commissions
                while i < 1000:
                    try:
                        commissions = wd.find_element_by_xpath(
                            '//div[@class="col-md-3 col-sm-6"][2]/div/div/p').get_attribute('data-balance')
                    except Exception as e:
                        wd.refresh()
                        commissions = wd.find_element_by_xpath(
                            '//div[@class="col-md-3 col-sm-6"][2]/div/div/p').get_attribute('data-balance')
                    rewards = wd.find_element_by_xpath(
                        '//div[@class="col-md-3 col-sm-6"][4]/div/div/p').get_attribute('data-balance')
                    if int(commissions.split('.')[1]) == 0:
                        intcommissions = int(commissions.split('.')[0])
                    elif int(commissions.split('.')[1]) > 0:
                        intcommissions = float(commissions)
                    if int(rewards.split('.')[1]) == 0:
                        intrewards = int(rewards.split('.')[0])
                    elif int(rewards.split('.')[1]) > 0:
                        intrewards = float(rewards)
                    if intcommissions == 0 and intrewards == 0:
                        curse = 0
                        print("{0}账户圈米完成,动态账户：{1}，静态金额：{2},已转入{3}账号中".format(account, comm, re, sponsor))
                        # itchat.send("{0}账户圈米完成,🌹账户：{1}，🌻金额：{2},已转入{3}账号中".format(account, comm, re, sponsor),
                        # toUserName=fromusername)
                        wd.quit()
                        break
                    else:
                        time.sleep(2)
                        continue
            elif intrewards > 0 and intcommissions == 0:
                try:
                    Select(wd.find_element_by_id("partition_transfer_partition_user_wallet_id")).select_by_visible_text(
                        "rewards wallet ${0}".format(rewards))
                except Exception as e:
                    wd.refresh()
                    Select(wd.find_element_by_id("partition_transfer_partition_user_wallet_id")).select_by_visible_text(
                        "rewards wallet ${0}".format(rewards))
                wd.find_element_by_id('partition_transfer_partition_amount').send_keys(rewards)
                wd.find_element_by_id('submit-transfer').click()
                re = rewards
                while i < 1000:
                    try:
                        commissions = wd.find_element_by_xpath(
                            '//div[@class="col-md-3 col-sm-6"][2]/div/div/p').get_attribute('data-balance')
                    except Exception as e:
                        wd.refresh()
                        commissions = wd.find_element_by_xpath(
                            '//div[@class="col-md-3 col-sm-6"][2]/div/div/p').get_attribute('data-balance')
                    rewards = wd.find_element_by_xpath(
                        '//div[@class="col-md-3 col-sm-6"][4]/div/div/p').get_attribute('data-balance')
                    if int(commissions.split('.')[1]) == 0:
                        intcommissions = int(commissions.split('.')[0])
                    elif int(commissions.split('.')[1]) > 0:
                        intcommissions = float(commissions)
                    if int(rewards.split('.')[1]) == 0:
                        intrewards = int(rewards.split('.')[0])
                    elif int(rewards.split('.')[1]) > 0:
                        intrewards = float(rewards)
                    if intcommissions == 0 and intrewards == 0:
                        curse = 0
                        print("{0}账户圈米完成,动态账户：{1}，静态金额：{2},已转入{3}账号中".format(account, comm, re, sponsor))
                        # itchat.send("{0}账户圈米完成,🌹账户：{1}，🌻金额：{2},已转入{3}账号中".format(account, comm, re, sponsor), toUserName=fromusername)
                        wd.quit()
                        break
                    else:
                        time.sleep(2)
                        continue
            elif intcommissions > 0 and intrewards > 0:
                if intrewards > intcommissions:
                    Select(wd.find_element_by_id("partition_transfer_partition_user_wallet_id")).select_by_visible_text(
                        'rewards wallet ${0}'.format(rewards))
                    wd.find_element_by_id('partition_transfer_partition_amount').send_keys(rewards)
                    wd.find_element_by_id('submit-transfer').click()
                    re = rewards
                    intrewards = 0

                else:
                    Select(wd.find_element_by_id("partition_transfer_partition_user_wallet_id")).select_by_visible_text(
                        'commissions wallet ${0}'.format(commissions))
                    wd.find_element_by_id('partition_transfer_partition_amount').send_keys(commissions)
                    wd.find_element_by_id('submit-transfer').click()
                    comm = commissions
                    intcommissions = 0
                time.sleep(5)
            else:
                break
        if curse == 1:
            curse = 0
            if intcommissions == 0 and intrewards == 0:
                # if i == maxnum:
                # itchat.send("第{0}个账户内没有米".format(1), toUserName=fromusername)
                # else:
                # itchat.send("第{0}个账户内没有米".format(i + 1), toUserName=fromusername)
                wd.quit()
        if i == maxnum:
            sigleprice = tixian(comm, re, name)
            get_cashnum(name, datetime, sigleprice)

        i = i + 1
        countnum.update({'name': name, 'handler': handler}, {'$set': {'countnum': i}})

if len(namelist) > 0:
    cur = cashnum.find()
    countcur = countnum.find()
    price = 0
    handler = cashnum.find_one({'name': namelist[0]})['handler']
    for i in cur:
        if i['handler'] == handler and i['datetime'] == datetime:
            price = price + i['cash']
            print('{0}需发人民币：{1}'.format(i['name'], i['cash']))
            # itchat.send('{0}需发人民币：{1}'.format(i['name'], i['cash']),toUserName='{0}'.format(fromusername))
            cashnum.remove({'name': i['name']})
    print("{0}{1}团队总共需要发人民币：{2}元".format(datetime, handler, price))
    for i in countcur:
        if i['handler'] == handler:
            countnum.update({'name': i['name']}, {'$set': {'countnum': 0}})




