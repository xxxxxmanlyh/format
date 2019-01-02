from selenium import webdriver
import time
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
import poplib
from email.parser import Parser
from pymongo import MongoClient


account = 'bjslq'
password = 'slq123123'
num = 6
lastnum = 17

while num <= lastnum:
    wd = webdriver.Chrome("/usr/local/bin/chromedriver")
    wd.implicitly_wait(300)

    wd.get("https://backoffice.airbitclub.com/auth/login")    # 打开登录界面
    wd.find_element_by_id("user_username").clear()
    if num > 9:
        trueaccount = account+'0'+ str(num)
    else:
        trueaccount = account+'00'+ str(num)

    wd.find_element_by_id("user_username").send_keys(trueaccount)   # 清除输入框并且输入账户
    wd.find_element_by_id("user_password").clear()
    wd.find_element_by_id("user_password").send_keys(password) #清除输入框并且输入密码
    wd.find_element_by_class_name("button-blue").click()   #点击登录
    time.sleep(10)
    wd.find_element_by_xpath('//*[@id="rew-daily-home"]').click()

    comms = wd.find_element_by_xpath('//*[@id="new_partition_bond_payment_partition"]/ul/li/span').text #动态钱包
    # comms = comms.split('$')[1]
    print('动'+comms)
    reward = wd.find_element_by_xpath('//*[@id="new_partition_bond_payment_partition"]/ul/ul/ul/li/span').text #静态钱包
    # reward = reward.split('$')[1]
    print('静' + reward)
    saving = wd.find_element_by_xpath('//*[@id="new_partition_bond_payment_partition"]/ul/ul/ul/ul/li[1]/span').text #储蓄钱包
    # saving = saving.split('$')[1]
    print('储蓄' + saving)
    repay = wd.find_element_by_xpath('//*[@id="new_partition_bond_payment_partition"]/ul/ul/ul/ul/li[2]/label').text #需要复投总额
    # repay = float(repay.split('$')[0])
    # repay = repay.split('$')[1]
    print('总额' + repay)

    if int(saving.split('.')[1]) > 0:
        saving = float(saving)
        wd.find_element_by_id('partition_bond_payment_partition_bond_payment_wallet_partitions_attributes_3_amount').send_keys(saving)
    else: saving = 0

    if repay - saving > 0 :
        if int(reward.split('.')[1]) > 0:
            reward = float(reward)
            if reward > (repay -saving):
                wd.find_element_by_id('partition_bond_payment_partition_bond_payment_wallet_partitions_attributes_2_amount').send_keys(repay -saving)
            else: wd.find_element_by_id('partition_bond_payment_partition_bond_payment_wallet_partitions_attributes_2_amount').send_keys(reward)
    else: wd.find_element_by_id('partition_bond_payment_partition_bond_payment_wallet_partitions_attributes_3_amount').send_keys(repay)

    if repay - saving - reward > 0 :
        if int(comms.split('.')[1]) > 0:
            comms = float(comms)
            if comms > (repay - saving - reward):
                wd.find_element_by_id(
                    'partition_bond_payment_partition_bond_payment_wallet_partitions_attributes_0_amount').send_keys(repay - saving - reward)
            else:print('钱不够')


    if float(wd.find_element_by_id('partition_bond_payment_partition_input_amount').get_attribute('value')) == repay :

        wd.find_element_by_id('renewal-payment-btn').click()
        num = num + 1





