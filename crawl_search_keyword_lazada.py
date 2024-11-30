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
    'Cookie': 'JSID=101eab2b9458e6c9ca5b707d09eb728f; CSRFT=e711d81a54881; TID=fe7494058661f5d4542018253e68de34; _lang=vi_VN; t_fv=1695517001338; t_uid=LsW0fa4M3Ks8XYcV4l7zKxaQj5QHmeRZ; cna=1cI6HFtSfksCAXZFAxIkmTZU; lzd_cid=f89690c1-63de-4840-dfbb-dceb1c67e1a1; lwrid=AQGMoF8Dx6hMBvyYEc6vxe5uIyxx; lzd_sid=186dc9f382501313357155432138802c; _tb_token_=ef6563670551f; _ga=GA1.2.1179632289.1706846430; AMCVS_126E248D54200F960A4C98C6%40AdobeOrg=1; _ga_6BKZ3KVR8Y=GS1.2.1713597936.1.0.1713597936.0.0.0; lazada_share_info=977471931_10_7900_200053113878_977471931_null; _grayscale=41; _bl_uid=zmlddz9w9OCot6lpkohjubyxtjX0; _gcl_au=1.1.988091975.1722420347; __wpkreporterwid_=0cd14da2-8847-4886-841a-c2fcdcc80ad0; asc_seller_mp_type=NORMAL; _uetvid=60e271e0a68e11ed806871409812ed5b; _fbp=fb.1.1724897922114.611610671608138109; _ga_3V5EYPLJ14=GS1.2.1724897922.12.1.1724897922.60.0.0; AMCV_126E248D54200F960A4C98C6%40AdobeOrg=-1124106680%7CMCIDTS%7C19965%7CMCMID%7C15638754640610053303222163502599952706%7CMCAAMLH-1725502722%7C3%7CMCAAMB-1725502722%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1724905122s%7CNONE%7CvVersion%7C5.2.0; __itrace_wid=aef7d81b-a089-4d45-aa8d-d918b4fd4f27; hng=VN|vi|VND|704; hng.sig=EmlYr96z9MQGc5b9Jyf9txw1yLZDt_q0EWkckef954s; pdp_sfo=1; xlly_s=1; lwrtk=AAEEZvag2MpxE4DQd/bedDiXq2xJWw61aLvFVM3Fdhdh1pI/Q1snFgU=; t_sid=8C88E1H1TqZoW5SHiCoHH6qKUL0p0EyZ; utm_channel=NA; _m_h5_tk=8a880e0369935e81d9cc2e127316b8e6_1727426706762; _m_h5_tk_enc=97cf3b83f20a424750f3e4a33041394d; x5sec=7b22617365727665722d6c617a6164613b33223a22617c43502b6a32626347454d58566d5054392f2f2f2f2f77456943584a6c5932467764474e6f5954436334636579413070514d444d774f575a6d4d4441774d4441774d4441774d4441774d4441774d4441774d4441774d4441774d4441774d4441784d4441774d4441774d4441774d4441304e7a55774e54526b4e7a55344e54466d4e54593459546b32596a6734595759354d4441774d4441774d44413d222c22733b32223a2235336366336662366630376634333130227d; epssw=6*obsss6Uy_snlkRIaNACsUcacKsrwO6apoO6ja3CL-_aGvLNSZY3iEfe9dXpcY_RO6jpjwAltvdOw7EssbRsssst13qs695B66wvzkwiOOXj4d70lhf6EOaVXOyADwUFEd7oHjibh-A-89TwapwbuUFWifCOfsssssh3sss3h_6-sx-fOOWQEVvgNojzssRf2shKpMs3sndHFssssMMNTs3UtqyPftlxPvqtHg7tedCMWAjuKOQYBumryT4To_KnpWrGeqe4QwzzvUodzWJvp6KfRTS_Ezgmf_p7C6Xos36z.; isg=BKKiEjkrMAva-ymSyHhGXIQT8y4E86YN3ejMu-w7VJVAv0I51IJYHSh87-NDrx6l; tfstk=fn6ZMcfZIKbQP6wjhhJ24nvGnAv9Qd47gtTXmijDfFYiCAgcTwQqclUY66lc8eB_XENT0Z7kJZRYXETDuZsc1kw7FGI9HKb4P8wStnFe2O8mlKfSKJHLPzw7F1yaLUz5G3OYcD-v-hxDmFqUKnxynhDDik8H03hmSZbcxk-2DcDMifDHt3xMnEbDnkSHz1WlH2-Xsu66hVAnzyRJrGYGlZ63lCcOjeuqu95ULUSiZxDcLhRGhwq9GC9csG_eN1zrQLsGwZKlSV4wYOSP3_b3dAJVx_X2K94nAFfRYtJ1IowMKO7NIB7m0XRGwN1kT9aZpUfhYiOF9oh6l_KckQBbyALGmgBRNLyq0H5PxpSrkqKh3yWA_qc2sHKePkrFNmXQ4ShdWFGxMCE9YUZMsjhvsHKePkrEMjdOcH87jCf..'
}

params = {
    'ajax':'true',
    'isFirstRequest':'true',
    'page':1,
}

def convert_cookies_to_string(cookie_dict):
    return '; '.join('{}={}'.format(cookie["name"], cookie["value"]) for cookie in cookie_dict)

def convert(lst):
    keys = lst[::2]  # slice the list to get keys
    values = lst[1::2]  # slice the list to get values
    # res_dict = dict(zip(keys[i], values[i] for i in range(len(keys))))
    return None

def get_json(url, _headers, _params):
    time.sleep(2)
    # ua = UserAgent()
    # user_agent = ua.random
    # _headers.__setitem__('User-Agent',  user_agent)
    response = requests.get(url, headers=_headers, params=_params)

    # Load the JSON data
    while response.text.__contains__('<script>sessionStorage.x5referer = window.location.href;var url = window.location.protocol') or response.text.__contains__('dialogSize'):
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
        headers.__setitem__('Cookie', "'" + convert_cookies_to_string(driver.get_cookies())+ "'")
        #print(headers.get('Cookie'))
        driver.quit()
        #time.sleep(2000)
        response = requests.get(url, headers=headers, params=_params)
    #Check if response is None
    if response:
        return json.loads(response.text)
    else:
        return None

def crawl_product(url, keyword):
    # Load the JSON data
    params.__setitem__('q', keyword)
    data = get_json(url, headers, params)
    if data is None:
        return None
    # Go to the Google home page
    print('crawl')
    #Return pandas's instance if data is None
    if data.__contains__('<!DOCTYPE HTML>'):
        return pd.DataFrame()
    #Initialize df_final
    df = pd.DataFrame()
    time.sleep(2)
    # Convert to DataFrame
    mainInfo = pd.json_normalize(data['mainInfo'])
    pageSize = round(int(mainInfo.get('totalResults'))/40)
    print(pageSize)
    for i in range(1,pageSize+1):
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
        reff = pd.json_normalize(data['mods'],['listItems'])
        df_crawl = pd.DataFrame(data = reff)
        df = pd.concat([df,df_crawl], ignore_index=True)
    #print(result)
    # df_product = pd.DataFrame(result)
    return df

def crawl_product_by_keyword():
    keywords = ['điện thoại']
    df_final = pd.DataFrame()
    for keyword in keywords:
        df_temp = crawl_product(url='https://www.lazada.vn/catalog/', keyword= keyword)
        df_final =  pd.concat([df_final,df_temp], ignore_index=True)
    df_final.to_csv('final1.csv', index=False)

if __name__ == '__main__':
    crawl_product_by_keyword()