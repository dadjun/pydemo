#!usr/bin/python
# -*- coding: utf-8 -*-
import random
#from basic import time
import time
import json
import requests
from openpyxl import Workbook
import pymysql.cursors
from hyper.contrib import HTTP20Adapter


def get_conn():
    '''建立数据库连接'''
    conn = pymysql.connect(host='192.168.0.202',
                                user='root',
                                password='hylink5721_test',
                                db='xfdc_template',
                                charset='utf8mb4',
                                cursorclass=pymysql.cursors.DictCursor)
    return conn


def insert(conn, info):
    '''数据写入数据库'''
    with conn.cursor() as cursor:
        sql = "INSERT INTO `python` (`shortname`, `fullname`, `industryfield`, `companySize`, `salary`, `city`, `education`) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        cursor.execute(sql, info)
    conn.commit()




def get_json(url, page, lang_name):
    '''返回当前页面的信息列表'''
    headers1 = {
        'Host': 'www.lagou.com',
        'Connection': 'keep-alive',
        'Content-Length': '23',
        'Origin': 'https://www.lagou.com',
        'X-Anit-Forge-Code': '0',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'X-Requested-With': 'XMLHttpRequest',
        'X-Anit-Forge-Token': 'None',
        'Referer': 'https://www.lagou.com/jobs/list_python?city=%E5%85%A8%E5%9B%BD&cl=false&fromSearch=true&labelWords=&suginput=',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7'
    }

    headers = {
        'Host': 'www.lagou.com',
        'Connection': 'keep-alive',
        'Content-Length': '23',
        'Origin': 'https://www.lagou.com',
        'X-Anit-Forge-Code': '0',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0.1; Moto G (4)) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Mobile Safari/537.36',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'X-Requested-With': 'XMLHttpRequest',
        'X-Anit-Forge-Token': 'None',
        'Referer': 'https://www.lagou.com/jobs/list_python?city=%E5%85%A8%E5%9B%BD&cl=false&fromSearch=true&labelWords=&suginput=',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7',
        #'sec-fetch-dest':' empty',
        #'sec-fetch-mode':' cors',
        #'sec-fetch-site': 'same-origin',
        'x-anit-forge-code':'0',
        'x-anit-forge-token': 'None',
        ':authority':'www.lagou.com',
        ':method':'POST',
        ':path':'/jobs/positionAjax.json?needAddtionalResult=false',
        ':scheme':'https',
        #'cookie':'user_trace_token=20200508123619-9bbf95b2-542f-427a-b2b5-7c42ede582db; LGUID=20200508123619-5e629292-4cca-4d61-8667-e6047bc36e04; _ga=GA1.2.543028619.1588912582; LG_HAS_LOGIN=1; RECOMMEND_TIP=true; showExpriedIndex=1; showExpriedCompanyHome=1; showExpriedMyPublish=1; privacyPolicyPopup=false; index_location_city=%E6%B7%B1%E5%9C%B3; JSESSIONID=ABAAAECABIEACCAD1D3D902FDDFE0427F1E05130C969435; WEBTJ-ID=20200706161826-1732334712d9f0-0f0a051f45bb6c-f7d1d38-2073600-1732334712e559; sensorsdata2015session=%7B%7D; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22171f2929b45157-06cda6eb1f6cfc-4313f6a-2073600-171f2929b46980%22%2C%22%24device_id%22%3A%22171f2929b45157-06cda6eb1f6cfc-4313f6a-2073600-171f2929b46980%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24os%22%3A%22Windows%22%2C%22%24browser%22%3A%22Chrome%22%2C%22%24browser_version%22%3A%2283.0.4103.61%22%7D%7D; _gid=GA1.2.1346598799.1594188079; hasDeliver=110; TG-TRACK-CODE=index_search; X_MIDDLE_TOKEN=4ccb4e4148a2e34138878ecc07fc6dbb; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1593682292,1593765614,1594023506,1594371833; PRE_UTM=; PRE_HOST=; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2Fjobs%2Flist%5F%25E9%25AB%2598%25E7%25BA%25A7%25E4%25BA%25A7%25E5%2593%2581%25E7%25BB%258F%25E7%2590%2586%3FlabelWords%3D%26fromSearch%3Dtrue%26suginput%3D; _gat=1; PRE_SITE=https%3A%2F%2Fwww.lagou.com; LGSID=20200710175530-202ad418-a6bc-4047-bda6-bbd6459a058c; login=false; unick=""; _putrc=""; LG_LOGIN_USER_ID=""; SEARCH_ID=129ac4181a4c428289450f2a0543a9dd; X_HTTP_TOKEN=f142a498efedb21d53257349518a697a16aabacd13; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1594375237; LGRID=20200710180035-2066c9e6-45b0-4b5f-b8ca-e5262fb4000b'
    }
    headersget = {
        'referer': 'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput=',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3741.400 QQBrowser/10.5.3863.400',
    }


    sessions = requests.session()
    ss = sessions.get('https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput=',headers=headersget)

    sessions.mount('https://www.lagou.com', HTTP20Adapter())
    cookie = ss.cookies
    data = {'first': 'false', 'pn': page, 'kd': lang_name}
    jsonLagou = sessions.post(url, data=data, headers=headers, cookies=cookie)

    #s = requests.Session()  # 创建一个session对象
    #s.get('https://www.lagou.com', headers=headers, timeout=3)  # 用session对象发出get请求，请求首页获取cookies
    #cookie = s.cookies  # 为此次获取的cookies
    #response = s.post(url, data=data, headers=headers, cookies=cookie, timeout=3)  # 获取此次文本

    #json = requests.post(url, data, headers=headers1, cookies=cookie).json()
    json_list = json.loads(jsonLagou.content)
    aa = json_list['content']['positionResult']
    list_con = json_list['content']['positionResult']['result']
    info_list = []
    for i in list_con:
        info = []
        info.append(i.get('companyShortName', '无'))
        info.append(i.get('companyFullName', '无'))
        info.append(i.get('industryField', '无'))
        info.append(i.get('companySize', '无'))
        info.append(i.get('salary', '无'))
        info.append(i.get('city', '无'))
        info.append(i.get('education', '无'))
        info.append("".join(i.get('skillLables', '无')))
        info.append("".join(i.get('positioinLables', '无')))
        info_list.append(info)
    return info_list


def main():
    lang_name = '数据产品经理'
    wb = Workbook()  # 打开 excel 工作簿
    conn = get_conn()  # 建立数据库连接  不存数据库 注释此行
    for i in ['深圳']:   # 五个城市
        page = 1
        ws1 = wb.active
        ws1.title = lang_name
        url = 'https://www.lagou.com/jobs/positionAjax.json?city={}&needAddtionalResult=false'.format(i)
        while page < 31:   # 每个城市30页信息
            info = get_json(url, page, lang_name)
            page += 1
            print(i, 'page', page)

            time.sleep(random.randint(10, 20))
            for row in info:
                #insert(conn, tuple(row))  # 插入数据库，若不想存入 注释此行
                ws1.append(row)
    conn.close()  # 关闭数据库连接，不存数据库 注释此行
    wb.save('{}职位信息.xlsx'.format(lang_name))

if __name__ == '__main__':
    main()