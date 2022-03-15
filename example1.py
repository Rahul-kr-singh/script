from bs4 import BeautifulSoup
import mysql.connector
import requests

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="new_stage_data"
)
cur = mydb.cursor()
cur.execute("SELECT l2_url,l3_image,l3_name,id FROM `category_image_1401`  ")
my_result = cur.fetchall()

for fetch in my_result:
    l2_url = fetch[0]
    im1 = fetch[1]
    l3 = fetch[2]
    id = fetch[3]
    page = requests.get(l2_url)
    soup = BeautifulSoup(page.content, "html.parser")
    if soup.find('div', class_='catItem single_l3').find_all('img'):
        val = ''
        flag = 0
        for x in soup.find('div', class_='catItem single_l3').find_all('img'):
            attr = (x.get('title'))
            # im = "https://cdn.raptorsupplies.com/pub/media/catalog/category/resize/" + im1
            if l3 == attr:
                flag = 1
                val = attr
                break
        if flag == 1:
            prod = ('l3 name  same')
            sql = ("UPDATE `category_image_1401` SET l3_name_test ='" + str(prod) + "' WHERE   id='" + str(
                id) + "'")
            cur.execute(sql)
            mydb.commit()
            print(cur.rowcount, "records successful Done")
        elif soup.find('div', class_='catItem single_l3').find_all('img'):
            for x in range(2, 11):
                page_url = l2_url + "?page=" + str(x)
                # print(page_url)
                page = requests.get(page_url)
                soup = BeautifulSoup(page.content, "html.parser")
                s = 0
                z = []
                flag = 0
                for x in soup.find('div', class_='catItem single_l3').find_all('img'):
                    s += 1
                    attr = (x.get('title'))
                    img = x.get('data-src')
                    z.append(attr)
                if s > 0:
                    for pd in z:
                        if l3 == pd:
                            flag = 1
                            break
                    if flag == 1:
                        prod = ('l3 name  same')
                        sql = ("UPDATE `category_image_1401` SET l3_name_test ='" + str(prod) + "' WHERE   id='" + str(
                            id) + "'")
                        cur.execute(sql)
                        mydb.commit()
                        print(cur.rowcount, "records successful Done")
                else:
                    break
        else:
            print("l3 not exist")
