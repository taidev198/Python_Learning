#from seleniumbase import Driver
#
# def test():
#     driver = Driver(wire=True)
#     driver.get("https://lazada.vn")
#     for request in driver.requests:
#         print(request.url)
#     driver.quit()
#from selenium import webdriver
# import undetected_chromedriver as uc
# import time
#
# options = webdriver.ChromeOptions()
# options.set_capability('goog:loggingPrefs', {'performance': 'ALL'})
# driver = uc.Chrome(options=options)
# driver.get("https://facebook.com")
# time.sleep(5)
#
# print(driver.get_log('performance'))
import json
from xmlrpc.client import gzip_decode

import brotli

from seleniumwire import webdriver  # Import from seleniumwire
import re
from seleniumwire.utils import decode
from urllib3.response import GzipDecoder
import gzip

# Create a new instance of the Chrome driver
driver = webdriver.Firefox()

# Go to the Google home page
driver.get('https://www.lazada.vn/den-trang-tri-chuyen-dung/')

# for response in driver:
#     print(response)

# # Access requests via the `requests` attribute
for request in driver.requests:
    if request.response and request.url.__contains__('https://acs-m.lazada.vn/h5/mtop.lazada.guided.shopping.categories.categorieslpcommon/1.0/'):
        print(
           # json.loads(
           #     brotli.decompress( request.response.body)
           # )
            gzip_decode(request.response.body)
        )
driver.quit()