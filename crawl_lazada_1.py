from xmlrpc.client import gzip_decode

import pandas as pd
import requests
import time
import random
import json
from seleniumwire import webdriver
from selenium.webdriver.common.keys import Keys
from six import print_
from tqdm import tqdm
import csv
from pathlib import Path
from requests.utils import dict_from_cookiejar
from fake_useragent import UserAgent

headers = {

    'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'Accept': 'application/json, text/plain, */*',
    'X-CSRF-TOKEN': 'ef6563670551f',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
    'sec-ch-ua-platform': '"macOS"',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'host': 'www.lazada.vn',
    'Cookie': '_lang=vi_VN; t_fv=1695517001338; t_uid=LsW0fa4M3Ks8XYcV4l7zKxaQj5QHmeRZ; cna=1cI6HFtSfksCAXZFAxIkmTZU; lzd_cid=f89690c1-63de-4840-dfbb-dceb1c67e1a1; lwrid=AQGMoF8Dx6hMBvyYEc6vxe5uIyxx; lzd_sid=186dc9f382501313357155432138802c; _tb_token_=ef6563670551f; _ga=GA1.2.1179632289.1706846430; AMCVS_126E248D54200F960A4C98C6%40AdobeOrg=1; _ga_6BKZ3KVR8Y=GS1.2.1713597936.1.0.1713597936.0.0.0; lazada_share_info=977471931_10_7900_200053113878_977471931_null; _grayscale=41; _gcl_au=1.1.988091975.1722420347; asc_seller_mp_type=NORMAL; _uetvid=60e271e0a68e11ed806871409812ed5b; _fbp=fb.1.1724897922114.611610671608138109; _ga_3V5EYPLJ14=GS1.2.1724897922.12.1.1724897922.60.0.0; AMCV_126E248D54200F960A4C98C6%40AdobeOrg=-1124106680%7CMCIDTS%7C19965%7CMCMID%7C15638754640610053303222163502599952706%7CMCAAMLH-1725502722%7C3%7CMCAAMB-1725502722%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1724905122s%7CNONE%7CvVersion%7C5.2.0; hng=VN|vi|VND|704; hng.sig=EmlYr96z9MQGc5b9Jyf9txw1yLZDt_q0EWkckef954s; t_sid=IR9BI9kcXNtiR57myeg6kabhLigxVrwt; utm_channel=NA; _m_h5_tk=306fc243a8112032fdc91bb6c20002ef_1727192906008; _m_h5_tk_enc=9b7174aa9a4a8f909d4275ddbfe9bf97; lwrtk=AAEEZvMoahCkLRDjumwc15nkwkZBxZmNsk3OyqGYxfSazrgSka0MGOo=; xlly_s=1; isg=BC0t-U11N37jVdbTCzFhrdeqPM-nimFcbqGTum8yaUQz5k2YN9pxLHu00KIA5nkU; tfstk=gV0j_c1iKA3yKdjqvFdzAdMVAcU6aATFl1NttfQV6rUABOhLUPRcbnV_58GUb-pj50bstf02iPR0oj4gWpJe8VGmiP4dCJpWUbdTsPURWksSij4GZLu4CHhcf1OvkAUtBze8sWUOXRe9NzF_9PQYXZIRe8VTWPEYW8C8657OXNFvNbeu6Pe9yTQbaIwoGQXditDqaJhYFNQ1ESZYpe25WN37GbwKMHbOW4NbDVkJilr4WmhqFkoXdZaEMDDg9xBvh7gjOViKeU7b5bnK5z3Je_yxxbg_uqdwkz3jhqESB1s7DDDqvugyha2K2bGaV0AG0Ro36Aqn7pb0Hfhn-DzB51NSAbU54f7UdNgVf_Zh57weNQsGj3wtnLEG3StaD7VyQQO5YfqYZ7weNQsGjoFuaxdWNMlG.; epssw=5*mmLhbmsyfRnLg5Nm4NDOZ9DuWSEvcvBG0Ck_rH-7rTRrfWVTrH8mR8JzgbfR6k8mmHCRjCnh67AI_VhkERmmmmeRwRWYbRzltNA-TQvvV17taAmNdSVXa8CraynsdsYYsC8PPfFmmBPfGgXZdqvjxVsUmZL2wZ-UPXWhWWfSX4pCWMbQi71Ga-qATjDVS5AnaRmms6f8-Gc96lofPIl4KCKhrmg_rtvmmXIjYj-f4tHC_VKcCfUxst8DMLmL299kl3_zLoW7XXlDIskZE5commmmm9ZXzrtmrRmmzUjz; _m_h5_tk=808d4c8e22fb5792a41d282870d68bdb_1726840295113; _m_h5_tk_enc=e7f829ee99154b951225f3c1d9a3c2a4; hng=VN|vi|VND|704; hng.sig=zdydsNS1SsmgPDnK6hvJok_XUpANfcD7ya93aWHPt94; lzd_cid=074f31be-18b0-4b77-bc61-49a994ec3e23'
    }

params = {
    'ajax':'true',
    'isFirstRequest':'true',
    'page':1,
    'spm':'a2o4n.searchlist.cate_12.1.53f365e213dVAy'
}

def convert_cookies_to_string(cookie_dict):
    return '; '.join('{}={}'.format(cookie["name"], cookie["value"]) for cookie in cookie_dict)

def convert(lst):
    keys = lst[::2]  # slice the list to get keys
    values = lst[1::2]  # slice the list to get values
    # res_dict = dict(zip(keys[i], values[i] for i in range(len(keys))))
    return None

def convert_cookie(cookies):
    cookie_dict = convert(cookies)
    old_cookie_dict = dict(item.split("=", 1) for item in headers.__getitem__('Cookie').split("; "))
    temp=''
    for key, value in cookie_dict.items():
        for key_1, value_1 in old_cookie_dict.items():
            if key_1 == key:
                if key=='t_sid' or key=='_m_h5_tk' or key== '_m_h5_tk_enc' or key == 'lzd_cid' or key == 'lwrtk' or key =='isg' or key == 'tfstk' or key == 'epssw':
                    temp += '; '.join('{}={}'.format(key, value))
                else:
                    temp += '; '.join('{}={}'.format(key, value_1))
    headers.__setitem__('Cookie', temp)
    print(temp)

def get_json(url, _headers, _params):
    time.sleep(2)
    ua = UserAgent()
    user_agent = ua.random
    _headers.__setitem__('User-Agent',  user_agent)
    print(_headers.__getitem__('Cookie'))
    response = requests.get(url, headers=_headers, params=_params)
    # Load the JSON data
    #print(response.text)
    while response.text.__contains__('<script>sessionStorage.x5referer = window.location.href;var url = window.location.protocol'):
        print('bot')
        driver = webdriver.Firefox()
        index = response.text.find('"url":"')+6
        url1=''
        for i in range(index, len(response.text)):
            if response.text[i] != '"':
                url1=url1+response.text[i]
        driver.get(url1)
        time.sleep(50)
        driver.get(url)
        #headers.update({'Cookie': str({cookie["name"]: cookie["value"] for cookie in driver.get_cookies()})})
        headers.__setitem__('Cookie', "'" + convert_cookies_to_string(driver.get_cookies())+ "'")
        #print(headers.get('Cookie'))
        headers1 = driver.requests[0].headers
        driver.quit()
        #time.sleep(2000)
        #print(url)
        response = requests.get(url, headers=headers, params=_params)
        #print(response.text)
    if response:
        data = json.loads(response.text)
    else:
        return None
    #print(data)
    return data

def refresh_cookie(url):
    driver = webdriver.Firefox()
    driver.set_window_position(-10000,0)
    driver.get('http://lazada.vn')
    time.sleep(15)
    convert_cookie(driver.get_cookies())
    #headers.__setitem__('Cookie', "'" + convert_cookies_to_string(driver.get_cookies())+ "'")
    driver.quit()
    print(headers.__getitem__('Cookie'))

    print('refresh cookie')

def crawl_product(url):
    # Load the JSON data
    data = get_json(url, headers, params)
    if data is None:
        return None
    # Go to the Google home page
    print('crawl')
    if data.__contains__('<!DOCTYPE HTML>'):
        return pd.DataFrame()
    print(data)
    # for response in driver:
    #     print(response)
    df_final = pd.DataFrame()
    #time.sleep(2)
    # Convert to DataFrame
    mainInfo = pd.json_normalize(data['mainInfo'])
    pageSize = round(int(mainInfo.get('totalResults'))/40)
    print(pageSize)
    for i in range(1,pageSize):
        print(i)
        time.sleep(2)
        print('crawl product'+'\s'+'pages')
        params.__setitem__('page', i)
        print(url)
        data = get_json(url, headers, params)
        if data is None:
            return None
        if data.__contains__('<!DOCTYPE HTML>'):
            return pd.DataFrame()
        mods = pd.json_normalize(data['mods'])
        reff = pd.json_normalize(data['mods'],['listItems'])
        df = pd.DataFrame(data = reff)
        df_final = pd.concat([df_final,df], ignore_index=True)
    #time.sleep(random.randrange(3, 10))
    #print(result)
    # df_product = pd.DataFrame(result)
    return df_final

def crawl_category():
    _headers = {
        'Cookie':'JSID=101eab2b9458e6c9ca5b707d09eb728f; CSRFT=e711d81a54881; TID=fe7494058661f5d4542018253e68de34; _lang=vi_VN; t_fv=1695517001338; t_uid=LsW0fa4M3Ks8XYcV4l7zKxaQj5QHmeRZ; cna=1cI6HFtSfksCAXZFAxIkmTZU; lzd_cid=f89690c1-63de-4840-dfbb-dceb1c67e1a1; lwrid=AQGMoF8Dx6hMBvyYEc6vxe5uIyxx; lzd_sid=186dc9f382501313357155432138802c; _tb_token_=ef6563670551f; _ga=GA1.2.1179632289.1706846430; AMCVS_126E248D54200F960A4C98C6%40AdobeOrg=1; _ga_6BKZ3KVR8Y=GS1.2.1713597936.1.0.1713597936.0.0.0; lazada_share_info=977471931_10_7900_200053113878_977471931_null; _grayscale=41; _gcl_au=1.1.988091975.1722420347; asc_seller_mp_type=NORMAL; _uetvid=60e271e0a68e11ed806871409812ed5b; _fbp=fb.1.1724897922114.611610671608138109; _ga_3V5EYPLJ14=GS1.2.1724897922.12.1.1724897922.60.0.0; AMCV_126E248D54200F960A4C98C6%40AdobeOrg=-1124106680%7CMCIDTS%7C19965%7CMCMID%7C15638754640610053303222163502599952706%7CMCAAMLH-1725502722%7C3%7CMCAAMB-1725502722%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1724905122s%7CNONE%7CvVersion%7C5.2.0; hng=VN|vi|VND|704; hng.sig=EmlYr96z9MQGc5b9Jyf9txw1yLZDt_q0EWkckef954s; xlly_s=1; lwrtk=AAEEZu3Ut+qMLMaTqDGKZGwn8SHNnMMrCEVlC/FmBg+BTvkCE94BVf8=; _m_h5_tk=a298d4c82a3da8de815b8413f4d945fe_1726843082826; _m_h5_tk_enc=8b80e1222785155ebe31d360c297f523; x5sec=7b22617365727665722d6c617a6164613b33223a22617c434e546f74626347454b2b64677644342f2f2f2f2f77456943584a6c5932467764474e6f5954446b703675382f762f2f2f2f3842536c41774d7a42685a6d59774d4441774d4441774d4441774d4441774d4441774d4441774d4441774d4441774d4441774d4445774d4441774d4441774d4441774d4451334e5441314e4751334e5467314d5759314e6a68684f545a694f4468685a6a6b774d4441774d4441774d413d3d222c22733b32223a2235623336343731613462623530663031227d; t_sid=cUw1SzMSZQgmGX8GCayrNNZUXZGBJRSB; utm_channel=NA; isg=BFlZd8crWyXYAgLvP2396RsOaEMz5k2YssUnpnsO1QD_gnkUwzZdaMeQhF70F-XQ; tfstk=fl-qmpY4mGASp1n_ftSNLszHSpsAbicIsh11IdvGhsf0coNMzQdaCxhtkUzMa_C1CiGTj1JpBsxf5qCgQdvnHO9cCCoNNBpjHKc9_3RpwZx1hdNw4pdDlZxwBlWMICHA1x3WHKIOjXGBbD9vHERc9lc5jAvlOdszlDiBHK2k6lknAAL2smCdsGbcS8mlwOUgnC40rYWGCS4gmCDyE_B1IrjgoT4lBOFcjGAMEYW9PW-HX7W1ov9KJS6b5TbVtKo8jl-zAZ5Hn_ri03Wq66vcalqNM_o8ddAi_lsHJQ-N-Bia2i9ergX2zA4liw8DGTdZYofD4KxcGnc7csxvEet6ZAqG_UYh8evmNzWyrKtPPHcUbZLkMeQwfbidce9BXwxm0WC5JORFmUlu0Bjrg5Bkbb-9u54NoTBPOYkyRRxSLVUJMsaTWZHAU6McoPUOoTBPOYkzWPQvIT5InZf..; epssw=5*mmLHmNxtqm2Xg90kHnZoo4xxI3ZV_tfdN5QK0H-7rT2L-hVTN5pmR8BGgI9XRPsjbrCRjCnIVPl7jWzp2HCRmmEYvlXA_uo2zRAJTxWG2oSrr2mNdSVX1RCrdSimdEmNTHOPmmEdszPf-ucrAm4yusRX-ZL28XOjJKiNWWUwT4pCFbNlE71GnOcATGF5kosfmmmmmQEj8Gc96lofP8mBmCKT7UrzVSYmmkHc0qKhygyrdOV5PDTaOM0QO61R9NNNaOL_x-SCpEUG8xN8QvjrmmmmmNEzbRENjRmmzUXV'
    }
    _params= {
        "jsv": "2.6.1",
        "appKey": "24677475",
        "t": "1726831992882",
        "sign": "572c40544ea95873bac65455ac862a2f",
        "api": "mtop.lazada.guided.shopping.categories.categoriesLpCommon",
        "v": "1.0",
        "type": "originaljson",
        "isSec": "1",
        "AntiCreep": "true",
        "timeout": "20000",
        "dataType": "json",
        "sessionOption": "AutoLoginOnly",
        "x-i18n-language": "vi",
        "x-i18n-regionID": "VN",
        "appkey": "24677475",
        "data": "%7B%22regionId%22%3A%22VN%22%2C%22language%22%3A%22vi%22%2C%22platform%22%3A%22pc%22%2C%22isbackup%22%3A%22true%22%2C%22backupParams%22%3A%22language%2CregionID%2Cplatform%2CpageNo%22%2C%22moduleName%22%3A%22categoriesLpMultiFloor%22%7D"

    }
    data = get_json('https://acs-m.lazada.vn/h5/mtop.lazada.guided.shopping.categories.categorieslpcommon/1.0/?jsv=2.6.1&appKey=24677475&t=1726831992882&sign=572c40544ea95873bac65455ac862a2f&api=mtop.lazada.guided.shopping.categories.categoriesLpCommon&v=1.0&type=originaljson&isSec=1&AntiCreep=true&timeout=20000&dataType=json&sessionOption=AutoLoginOnly&x-i18n-language=vi&x-i18n-regionID=VN&appkey=24677475&data=%7B%22regionId%22%3A%22VN%22%2C%22language%22%3A%22vi%22%2C%22platform%22%3A%22pc%22%2C%22isbackup%22%3A%22true%22%2C%22backupParams%22%3A%22language%2CregionID%2Cplatform%2CpageNo%22%2C%22moduleName%22%3A%22categoriesLpMultiFloor%22%7D', _headers, _params)
    #print(data)
    rows=[]
    df_final = pd.DataFrame()
    for item in data['data']['resultValue']['categoriesLpMultiFloor']['data']:
        for level2 in item['level2TabList']:
            df_lv2 = pd.DataFrame()
            if 'level3TabList' in level2:
                for level3 in level2['level3TabList']:
                    df_lv3 = pd.DataFrame()
                    row = {
                        "categoryIcon": item['categoryIcon'],
                        "categoryName": item['categoryName'],
                        "childId": item['childId'],
                        "id": item['id'],
                        "level1CategoryId": item['level1CategoryId'],
                        "level2CategoryId": level2['categoryId'],
                        "level2CategoryName": level2['categoryName'],
                        "level2CategoryUrl": level2['categoryUrl'],
                        "level3CategoryId": level3['categoryId'],
                        "level3CategoryName": level3['categoryName'],
                        "level3CategoryUrl": level3['categoryUrl'],
                        "level3CategoryImg": level3.get('categoryImg', None),
                    }
                    rows.append(row)
                    temp_df = crawl_product('https:' + level2['categoryUrl'] +'/')
                    df_final = pd.concat([df_final, temp_df] , ignore_index=True)
                    print(df_final)
            else:
                # Handle level 2 without level 3
                row = {
                    "categoryIcon": item['categoryIcon'],
                    "categoryName": item['categoryName'],
                    "childId": item['childId'],
                    "id": item['id'],
                    "level1CategoryId": item['level1CategoryId'],
                    "level2CategoryId": level2['categoryId'],
                    "level2CategoryName": level2['categoryName'],
                    "level2CategoryUrl": level2['categoryUrl'],
                    "level3CategoryId": None,
                    "level3CategoryName": None,
                    "level3CategoryUrl": None,
                    "level3CategoryImg": None,
                }
                temp_df = crawl_product('https:' + level2['categoryUrl'] +'/')
                df_final = pd.concat([df_final, temp_df] , ignore_index=True)
                rows.append(row)
    # Create DataFrame
    df = pd.DataFrame(rows)

    # Display the DataFrame
    print(df)
    df.to_csv("category.csv", index=False)
    #df_final.to_csv('final.csv', index=False)

def crawl_all_product_from_cat():
    df_final = pd.DataFrame()
    url_lists = set([])
    with open('category.csv', newline='') as f:
        reader = csv.reader(f)
        # store the headers in a separate variable,
        # move the reader object to point on the next row
        next(reader)
        for row in reader:
            url_lv2 = row[7]
            url_lv3 = row[10]
            if bool(url_lv2) or  url_lv2.__contains__('level2CategoryUrl'):
                #temp_df = crawl_product('https:' + url_lv2 +'/')
                url_lists.add('https:' + url_lv2 +'/')
                #df_final = pd.concat([df_final, temp_df] , ignore_index=True)
            if  bool(url_lv3) or  url_lv3.__contains__('level3CategoryUrl'):
                # temp_df = crawl_product('https:' + url_lv3 +'/')
                # df_final = pd.concat([df_final, temp_df] , ignore_index=True)
                url_lists.add('https:' + url_lv3 +'/')
                #print('https:' + url_lv3 +'/')
    sorted(url_lists)
    for url in url_lists:
        refresh_cookie(url)
        print('start from:' + url)
        temp_df = crawl_product(url)
        if temp_df is None or temp_df.empty:
            continue
        df_final = pd.concat([df_final, temp_df] , ignore_index=True)
    df_final.to_csv("product1.csv", index=False)
if __name__ == '__main__':
    crawl_all_product_from_cat()