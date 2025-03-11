import time

from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
#这是一个程序关于直接    完成评教系统进行评教的脚本，使用Selenium
q=Options()
q.add_argument('--no-sandbox')
q.add_experimental_option('detach',True)

driver=webdriver.Edge(service=Service('D:/edgedriver_win64 (1)/msedgedriver.exe'),options=q)
driver.get('https://ehall.xjtu.edu.cn/new/index.html')
driver.maximize_window()
driver.implicitly_wait(20)

driver.find_element(By.CLASS_NAME, 'amp-no-login-zh').click()
driver.find_element(By.NAME, 'username').send_keys(' ')    #此处填账号
driver.find_element(By.NAME, 'pwd').send_keys(' ')         #此处填密码
driver.find_element(By.ID, 'account_login').click()
driver.find_element(By.XPATH,'//*[@id="widget-hot-01"]/div[1]/widget-app-item[1]/div/div/div[2]/div[1]').click()
driver.find_element(By.XPATH,'//*[@id="ampDetailEnter"]').click()
windows=driver.window_handles
driver.switch_to.window(windows[1])
driver.find_element(By.LINK_TEXT,'学生').click()
driver.find_element(By.XPATH,'//*[@id="pjglTopCard"]/div/div[2]').click()
time.sleep(1)
driver.find_element(By.XPATH,'//*[@id="tabName-content-1"]/div/div[1]').click()
for _ in range(21):
    driver.find_element(By.XPATH,'/html/body/div[7]/div/div[1]/section/div/div[2]/div[2]/div[2]/div/div[2]/div[4]/div/span[2]').click()
    time.sleep(1)
    labels=driver.find_elements(By.CLASS_NAME,'bh-radio-label')
    for i in range(len(labels)):
        if(i*5<len(labels)):
            labels[i*5].click()

    driver.find_element(By.CLASS_NAME,'bh-txt-input__txtarea'). send_keys('老师教学热情'
                                                                                                                                            '洋溢，专业知识扎实，讲解条理清晰，易于理解。课堂互动丰富，能够激发学生兴趣。教材内容详尽，与实际紧密结合，有助于学生深入理解知识。老师耐心解答疑问，注重学生个性化发展，整体教学效果极佳')
    driver.find_element(By.XPATH,'//*[@id="txwjFooter"]/a[1]').click()
    time.sleep(1)#/html/body/div[11]/div[1]/div[1]/div[2]/div[2]/a[1]
    #driver.find_element(By.XPATH,'/html/body/div[10]/div[1]/div[1]/div[2]/div[2]/a[1]').click()
    driver.find_element(By.LINK_TEXT,'确认').click()
    time.sleep(5)


