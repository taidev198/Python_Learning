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

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:83.0) Gecko/20100101 Firefox/83.0',
    'Accept': 'application/json, text/javascript',
    'Accept-Language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'Referer': 'https://www.lazada.vn',
    'Connection': 'keep-alive',
    'TE': 'Trailers',
    'Content_Type': 'application/x-www-form-urlencoded',
    'Cookie': 'JSID=101eab2b9458e6c9ca5b707d09eb728f; CSRFT=e711d81a54881; TID=fe7494058661f5d4542018253e68de34; _lang=vi_VN; t_fv=1695517001338; t_uid=LsW0fa4M3Ks8XYcV4l7zKxaQj5QHmeRZ; cna=1cI6HFtSfksCAXZFAxIkmTZU; lzd_cid=f89690c1-63de-4840-dfbb-dceb1c67e1a1; lwrid=AQGMoF8Dx6hMBvyYEc6vxe5uIyxx; lzd_sid=186dc9f382501313357155432138802c; _tb_token_=ef6563670551f; _ga=GA1.2.1179632289.1706846430; AMCVS_126E248D54200F960A4C98C6%40AdobeOrg=1; _ga_6BKZ3KVR8Y=GS1.2.1713597936.1.0.1713597936.0.0.0; lazada_share_info=977471931_10_7900_200053113878_977471931_null; _grayscale=41; _bl_uid=zmlddz9w9OCot6lpkohjubyxtjX0; _gcl_au=1.1.988091975.1722420347; __wpkreporterwid_=0cd14da2-8847-4886-841a-c2fcdcc80ad0; asc_seller_mp_type=NORMAL; _fbp=fb.1.1724897922114.611610671608138109; __itrace_wid=aef7d81b-a089-4d45-aa8d-d918b4fd4f27; hng=VN|vi|VND|704; hng.sig=EmlYr96z9MQGc5b9Jyf9txw1yLZDt_q0EWkckef954s; _uetvid=60e271e0a68e11ed806871409812ed5b; AMCV_126E248D54200F960A4C98C6%40AdobeOrg=-1124106680%7CMCIDTS%7C19984%7CMCMID%7C15638754640610053303222163502599952706%7CMCAAMLH-1727161986%7C3%7CMCAAMB-1727161986%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1726564386s%7CNONE%7CvVersion%7C5.2.0; miidlaz=miidgg5v301i81bahgc1099; exlaz=c_lzd_byr:mm_150601309_51753143_2010703162!vn1415006:clkgg5v301i81bahg41098::; lzd_click_id=clkgg5v301i81bahg41098; _ga_3V5EYPLJ14=GS1.2.1726622310.14.1.1726622310.60.0.0; t_sid=DjBV7BJRJu1ReKXqAgVw102Wj5tz48pz; utm_channel=NA; _m_h5_tk=f334cb193f96da87adc1ebafb6fef1d7_1726761556078; _m_h5_tk_enc=3762b6ee33ee2db45105e8f9e18ebc1e; lwrtk=AAEEZuyTcxPP7K6S7TGzpmOBqpjw6IbyLLvFVM3Fdhdh1pI/Q1snFgU=; xlly_s=1; epssw=5*mmLiY8giREddBznt7PvH39DuI3Vvc4YC0Dk_rChplg3e5khwxTzk3KLe0kNMRj8PfDVeA5m7BiOe8Wlb5UKlpLHKovQrmaRqsZofpRmmsA5XN5T0KkD2VNcCmmmmmmrN5i8iS6y3EN5hIyFhaZYYrr7cdSL_acYccjhmWEmdb5mYNBPb80B_8W_dmxReQaBdM_LAj-OFOqTlJ6UDhJ7u92ZLmn3cic1SaRo0ixJ-e139kmmmPzPUFXD2PpCLmBPfChm7E1dr1RmJVTeiB_y3AM9cVKoci01-5sebkg8Z5mR8PoWVO3Cy2V8MfyMXCGoMPVVVVVWm1blmSbWmmTTAmm..; isg=BF9fabxSRfqe_ES5NQ9T5zGM7rXpxLNmtZ7WU_GsH46DgH0C-ZCPtqwTQgj-GIve; tfstk=fyexHTOaLgKY67xJwC1osszxSqsu6REVerrBIV0D1zU8Ak8m1PfV1AUUWfOgjxt6B44-ojgin8K_-4pG0IqXWA3ShfPmSq0tBlzdqwXhKorqQx_h-9xpLc8qhmis1dssFcmZX_4f_orqQAGu-kIY0CLr7pasCPMSNDnZCmGsfLs-XD3sCqG6PQiIPAg_5mTWNDmwhC96GgESzcMs5UrlwVRj-dFaL5oq3K66ppe-ViuQDKptq8oYL2EbHrU4edGxRogJBwPAzKuSv8_woVy8V-iaPTvxBuiTJxNRPKUTcWzZAr6JlmFbvkc8Qw9t47aqZmFRfQgbAqMjyRSwQqN0fRcThwtil-z0eXywka0gtu2jwy_kePlTGWMbBwB54s23p7zW-2nMGgIJ_Clj4JQ6NBH9iLqo22jomCRZw_o--gIJ_Clj403hqhdw_bCP.',
}

params = {
    'ajax':'true',
    'isFirstRequest':'true',
    'page':1,
    'spm':'a2o4n.searchlist.cate_12.1.53f365e213dVAy'
   }
def parser_product(json):
    d = dict()
    d['pageSize'] = json.get('mods').get('listItems')
#     d['sku'] = json.get('sku')
#     d['short_description'] = json.get('short_description')
#     d['price'] = json.get('price')
#     d['list_price'] = json.get('list_price')
#     d['price_usd'] = json.get('price_usd')
#     d['discount'] = json.get('discount')
#     d['discount_rate'] = json.get('discount_rate')
#     d['review_count'] = json.get('review_count')
#     d['order_count'] = json.get('order_count')
#     d['inventory_status'] = json.get('inventory_status')
#     d['is_visible'] = json.get('is_visible')
# #    d['stock_item_qty'] = json.get('stock_item').get('qty')
# #    d['stock_item_max_sale_qty'] = json.get('stock_item').get('max_sale_qty')
#     d['product_name'] = json.get('meta_title')
#     d['brand_id'] = json.get('brand').get('id')
#     d['brand_name'] = json.get('brand').get('name')
    return d

def get_json(url, _headers, _params):
    time.sleep(3000)
    response = requests.get(url, headers=_headers, params=_params)
        # if response.status_code == 200:
        #     print('Crawl data {} success !!!'+ str(pid))
        # Load the JSON data
    if response.text.__contains__('<script>sessionStorage.x5referer = window.location.href;var url = window.location.protocol'):
        # driver = webdriver.Firefox()
        # driver.get(url)
        # time.sleep(3500)
        # driver.quit()
        time.sleep(300000)
        response = requests.get(url, headers=_headers, params=_params)
    data = json.loads(response.text)
    #print(data)
    return data


def crawl_product(url, driver):
    # Load the JSON data
    #data = get_json(url, headers, params)
    # Go to the Google home page
    #driver.get(url)
            print('crawl')
    # for response in driver:
    #     print(response)
            df_final = pd.DataFrame()
    # # Access requests via the `requests` attribute
    # for request in driver.requests:
    #     print('test')
        # if request.response and request.url.__contains__(url+'?ajax=true'):
        #     print(gzip_decode(request.response.body).decode('utf-8'))
            data= get_json(url, headers, params)
            time.sleep(3000)
            # Convert to DataFrame
            mainInfo = pd.json_normalize(data['mainInfo'])
            pageSize = round(int(mainInfo.get('totalResults'))/40)
            for i in range(1,pageSize):
                time.sleep(1000)
                if i == 10:
                    time.sleep(300000)
                print('crawl product'+'\s'+'pages')
                params.__setitem__('page', i)
                print(url)
                data = get_json(url, headers, params)
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
    options = {
        'disable_capture': True,  # Don't intercept/store any requests
        "prefs": {
        # block image loading
        "profile.managed_default_content_settings.images": 2,
    }
    }
    #driver = webdriver.Firefox(seleniumwire_options =options)
    for url in url_lists:
        print('start')
        temp_df = crawl_product(url, 'null')
        df_final = pd.concat([df_final, temp_df] , ignore_index=True)
    df_final.to_csv("product1.csv", index=False)
    #driver.quit()
if __name__ == '__main__':
    crawl_all_product_from_cat()