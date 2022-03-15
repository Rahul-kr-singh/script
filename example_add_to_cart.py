import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
driver = webdriver.Chrome('C:/Users/ashish/Downloads/chromedriver_win32//chromedriver.exe')
url = ['https://www.raptorsupplies.co.uk/c/jaw-coupling-hubs',
       'https://www.raptorsupplies.co.uk/p/lovejoy/l-type-hubs-with-keyway-inch-bores',
       'https://www.raptorsupplies.co.uk/pd/morse-drum/2-5154-a',
       'https://www.raptorsupplies.co.uk/b/akro-mils',
       'https://www.raptorsupplies.co.uk/b/dodge-bearings'
       ]
a = 0
for fetch in url:
    a += 1
    if a == 1:
        print('l3 add to cart button check')
        driver.get(fetch)
        driver.maximize_window()
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="atc_0"]/span').click()
        time.sleep(5)
        driver.find_element_by_xpath('//*[@id="myHeader"]/div[1]/div[3]/ul/li[4]/a/span[1]').click()
        s = driver.current_url

        print(s)
        time.sleep(5)
        print('lovely l3 page  add to cart button clicked !')

    elif a == 2:
        print('mother add to cart button')
        driver.get(fetch)
        driver.maximize_window()
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="parent_"]/table/tbody/tr[3]/td[12]/form/div[1]/span').click()
        time.sleep(5)
        driver.find_element_by_xpath('//*[@id="myHeader"]/div[1]/div[3]/ul/li[4]/a/span[1]').click()
        s = driver.current_url
        print(s)
        time.sleep(5)
        print('wow add to cart button clicked mother !')
    elif a == 3:
        print('product add to cart button')
        driver.get(fetch)
        driver.maximize_window()
        time.sleep(2)
        driver.find_element_by_id('product-addtocart-button').click()
        s = driver.current_url
        print(s)
        time.sleep(5)
        print('nice product page add to cart button clicked !')
    elif a == 4:
        print('brand akro-mils add to card  check')
        driver.get(fetch)
        driver.maximize_window()
        time.sleep(5)
        driver.find_element_by_xpath('//*[@id="dyn_data_less"]/div[1]/div[2]/div/form/div[1]').click()
        time.sleep(5)
        driver.find_element_by_xpath('//*[@id="myHeader"]/div[1]/div[3]/ul/li[4]/a/span[1]').click()
        s = driver.current_url
        print(s)
        time.sleep(2)
        print('very nice akro mils page add to cart button clicked ! ')
    else:

        print('url not working')

driver.close()
print("driver successfully close")
