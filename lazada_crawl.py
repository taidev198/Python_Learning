import pandas as pd
import requests
import time
import random
from tqdm import tqdm

# cookies = {
#     # 'JSID':'101eab2b9458e6c9ca5b707d09eb728f',
#     # 'CSRFT':'e711d81a54881',
#     # 'TID':'fe7494058661f5d4542018253e68de34',
#     # '_lang':'vi_VN',
#     # 't_fv':'1695517001338',
#     # 't_uid':'LsW0fa4M3Ks8XYcV4l7zKxaQj5QHmeRZ',
#     # 'cna':'1cI6HFtSfksCAXZFAxIkmTZU',
#     # 'lzd_cid':'f89690c1-63de-4840-dfbb-dceb1c67e1a1',
#     # 'lwrid':'AQGMoF8Dx6hMBvyYEc6vxe5uIyxx',
#     # 'lzd_sid=186dc9f382501313357155432138802c; _tb_token_=ef6563670551f; _ga=GA1.2.1179632289.1706846430; AMCVS_126E248D54200F960A4C98C6%40AdobeOrg=1; _ga_6BKZ3KVR8Y=GS1.2.1713597936.1.0.1713597936.0.0.0; lazada_share_info=977471931_10_7900_200053113878_977471931_null; _grayscale=41; _gcl_au=1.1.988091975.1722420347; asc_seller_mp_type=NORMAL; _fbp=fb.1.1724897922114.611610671608138109; hng=VN|vi|VND|704; hng.sig=EmlYr96z9MQGc5b9Jyf9txw1yLZDt_q0EWkckef954s; xlly_s=1; _gid=GA1.2.1141461690.1726557186; _uetsid=48ef847074c411ef98644bbf994c7b47; _uetvid=60e271e0a68e11ed806871409812ed5b; AMCV_126E248D54200F960A4C98C6%40AdobeOrg=-1124106680%7CMCIDTS%7C19984%7CMCMID%7C15638754640610053303222163502599952706%7CMCAAMLH-1727161986%7C3%7CMCAAMB-1727161986%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1726564386s%7CNONE%7CvVersion%7C5.2.0; _ga_3V5EYPLJ14=GS1.2.1726557185.13.1.1726557629.60.0.0; lwrtk=AAEEZum6Jb1dJ2CXAXdfYvfG+iivPnm2V03OyqGYxfSazrgSka0MGOo=; _m_h5_tk=e368987430e8834922c1e97cc5dfcd96_1726588028420; _m_h5_tk_enc=04d100557c9995967160342570f9cf37; epssw=5*mmLNj8S818wQL90kHnh2ZLVDYTGV_XH7N5u_rH-7meDnO_TEmmWYeY0iqS_Z0kNrmj8qsZoLBJfjbFU2pReg4to2VAHgbFlmmJeECukR-b6Ym_WhdkLDdSitrr_NWxmkacKWplw8WEmV0DlmmQmmmmeQpSuAEJvRl4o0yU_cGMemplJ2lGyEL8HbXH_2YzQLmOnIuoZshDxmmem8QJCBlqcmr2ldmmrwH4D3rn7V11rPxrkU65xqcdo9NeL70_ekvai3v2LQg2DZo-wyOvWPl6wL6HDKCgVVVNmEmCrPz2SrmmCFz9h.; isg=BC0t0Tw4N2XH09bTCzFhrdeqPM-nimFckzikOW8zKkQz5kyYN98DLAP10KIA5nkU; tfstk=fTqZGjawjmVCVcjXcAoqU_ODtjotPcfW_oGjn-2mCfcMfhO08WF2hOCAWy80TXEgg-BtnjV0gja1RgwTBmncNSS5VRdM2nd4gVcGxv2K3xc0tj0fcmncN_sC6Ag-D7wC4p4gK9kjHAvgiV2nxYlnnxDgiX0nEYOimSmcL2DmIhYinqx3KAhnimm0iJc1xuqvTxgGFR04BVx1F_h7IX-zwkkM5bs-tn2QvA0Z5RcEQArEQVlrRAz5quyuIuH4DTYqg-ag1vFV46o3b5ri8mS2vcwz-5uU7s-EJy28m2zdaUe8I5zorljFKSP3ezngjsKs6r23mXZGhnluP8nEpo1pjjz3olgtDCfZLlyz0rSPFIH306rY7IYqSvHEN9WUW5yZFZLL6fTvkVBtLb6iSELxSbMEN9WekE3Tnvl5IVf..; t_sid=NagFXVH5ZNebU1d7Rfzd74sX2qp6w0Ov; utm_channel=NA
# }

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:83.0) Gecko/20100101 Firefox/83.0',
    'Accept': 'application/json, text/javascript',
    'Accept-Language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'Referer': 'https://www.lazada.vn',
    'Connection': 'keep-alive',
    'TE': 'Trailers',
    'Content_Type': 'application/x-www-form-urlencoded',
    'Cookie': 'JSID=101eab2b9458e6c9ca5b707d09eb728f; CSRFT=e711d81a54881; TID=fe7494058661f5d4542018253e68de34; _lang=vi_VN; t_fv=1695517001338; t_uid=LsW0fa4M3Ks8XYcV4l7zKxaQj5QHmeRZ; cna=1cI6HFtSfksCAXZFAxIkmTZU; lzd_cid=f89690c1-63de-4840-dfbb-dceb1c67e1a1; lwrid=AQGMoF8Dx6hMBvyYEc6vxe5uIyxx; lzd_sid=186dc9f382501313357155432138802c; _tb_token_=ef6563670551f; _ga=GA1.2.1179632289.1706846430; AMCVS_126E248D54200F960A4C98C6%40AdobeOrg=1; _ga_6BKZ3KVR8Y=GS1.2.1713597936.1.0.1713597936.0.0.0; lazada_share_info=977471931_10_7900_200053113878_977471931_null; _grayscale=41; _gcl_au=1.1.988091975.1722420347; asc_seller_mp_type=NORMAL; _fbp=fb.1.1724897922114.611610671608138109; hng=VN|vi|VND|704; hng.sig=EmlYr96z9MQGc5b9Jyf9txw1yLZDt_q0EWkckef954s; xlly_s=1; _gid=GA1.2.1141461690.1726557186; _uetsid=48ef847074c411ef98644bbf994c7b47; _uetvid=60e271e0a68e11ed806871409812ed5b; AMCV_126E248D54200F960A4C98C6%40AdobeOrg=-1124106680%7CMCIDTS%7C19984%7CMCMID%7C15638754640610053303222163502599952706%7CMCAAMLH-1727161986%7C3%7CMCAAMB-1727161986%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1726564386s%7CNONE%7CvVersion%7C5.2.0; _ga_3V5EYPLJ14=GS1.2.1726557185.13.1.1726557629.60.0.0; lwrtk=AAEEZum6Jb1dJ2CXAXdfYvfG+iivPnm2V03OyqGYxfSazrgSka0MGOo=; _m_h5_tk=e368987430e8834922c1e97cc5dfcd96_1726588028420; _m_h5_tk_enc=04d100557c9995967160342570f9cf37; tfstk=fTqZGjawjmVCVcjXcAoqU_ODtjotPcfW_oGjn-2mCfcMfhO08WF2hOCAWy80TXEgg-BtnjV0gja1RgwTBmncNSS5VRdM2nd4gVcGxv2K3xc0tj0fcmncN_sC6Ag-D7wC4p4gK9kjHAvgiV2nxYlnnxDgiX0nEYOimSmcL2DmIhYinqx3KAhnimm0iJc1xuqvTxgGFR04BVx1F_h7IX-zwkkM5bs-tn2QvA0Z5RcEQArEQVlrRAz5quyuIuH4DTYqg-ag1vFV46o3b5ri8mS2vcwz-5uU7s-EJy28m2zdaUe8I5zorljFKSP3ezngjsKs6r23mXZGhnluP8nEpo1pjjz3olgtDCfZLlyz0rSPFIH306rY7IYqSvHEN9WUW5yZFZLL6fTvkVBtLb6iSELxSbMEN9WekE3Tnvl5IVf..; t_sid=NagFXVH5ZNebU1d7Rfzd74sX2qp6w0Ov; utm_channel=NA; epssw=5*mmL4M5tsRNdxg90kHnh2ZexxWSmjkLH7mmmK0mEmNfueQklK0C8mR8J5gEqKRaS4KtdSJhQiwOGnQLNkErCR_HeQC86KjuhTMAkEx7LYWECrrnitRmmmrrrrOyRNWE17B2ldFfMmmxR7k9zdP62lJOcBjQcGJ6tGRbzE9Fhymn3xQtoSw85EkaK6YAXLanOdszPUF3cgbljLPfwmW5m7TH-rrUPZVTeiqb3Lnb36Wy9MGavpri0XT01mfVfjs0pK9h-Gq5cdQz27vRHyCmmmrUXVbVOmr8WmmHjFmm..; isg=BLi41-nKKvKyy0MsdsoMuiLBiWBKIRyrBgORJvIpBPOmDVj3mjHsO84vxR29RtSD',
}

params = {
    'jsv': '2.7.2',
    'appKey': '24677475',
    't': '1726586046091',
    'sign' :'976863904bf901b701fce285c28a7188',
    'api': 'mtop.relationrecommend.LazadaRecommend.recommend',
    'v': '1.0',
    'type': 'originaljson',
    'isSec': '1',
    'AntiCreep': 'true',
    'timeout':'20000',
    'dataType': 'json',
    'sessionOption': 'AutoLoginOnly',
    'x-i18n-language': 'vi',
    'x-i18n-regionID': 'VN',
    'data':'{"appId":"32104","params":"{\"appId\":\"32104\",\"isbackup\":true,\"newTileEnable\":true,\"language\":\"vi\",\"region_id\":\"VN\",\"platform\":\"pc\",\"scene\":\"homepage\",\"appVersion\":\"7.48.0\",\"anonymous_id\":\"1cI6HFtSfksCAXZFAxIkmTZU\",\"pageSize\":50,\"userId\":0,\"pageNo\":0}"}'
}

def parser_product(json):
    d = dict()
    d['id'] = json.get('id')
    d['sku'] = json.get('sku')
    d['short_description'] = json.get('short_description')
    d['price'] = json.get('price')
    d['list_price'] = json.get('list_price')
    d['price_usd'] = json.get('price_usd')
    d['discount'] = json.get('discount')
    d['discount_rate'] = json.get('discount_rate')
    d['review_count'] = json.get('review_count')
    d['order_count'] = json.get('order_count')
    d['inventory_status'] = json.get('inventory_status')
    d['is_visible'] = json.get('is_visible')
    #    d['stock_item_qty'] = json.get('stock_item').get('qty')
    #    d['stock_item_max_sale_qty'] = json.get('stock_item').get('max_sale_qty')
    d['product_name'] = json.get('meta_title')
    d['brand_id'] = json.get('brand').get('id')
    d['brand_name'] = json.get('brand').get('name')
    return d


# df_id = pd.read_csv('product_id_ncds.csv')
# p_ids = df_id.id.to_list()
# print(p_ids)
result = []
for pid in range(1,2):
    response = requests.get('https://www.lazada.vn/xe-mo-to-xe-tay-ga/', headers=headers, params=params)
    if response.status_code == 200:
        print('Crawl data {} success !!!'.format(pid))
        print(response.json())
        #result.append(parser_product(response.json()))
    # time.sleep(random.randrange(3, 5))
# df_product = pd.DataFrame(result)
# df_product.to_csv('crawled_data_ncds.csv', index=False)