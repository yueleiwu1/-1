import requests
import json
import time
from headers.header import shen_headers
from DB.getcode import get_dt_code
from DB.db import save_content_shen
from URL.shenjs_url import get_url
from Rule.shen_rule import shen_content_clean,product_name_clean,get_status_code
from logger_error.logger_error import loggerError


def get_content(url,dt_code_list):
    headers = shen_headers()
    response = requests.get(url, headers=headers)
    print(response.text)
    jsonobj = json.loads(response.text)
    print(jsonobj[0])
    print (jsonobj[0]['metadata'])
    items = jsonobj[0]['data']
    print(items)
    if len(items) > 0:
        for item in items:
            zqdm = item['zqdm']
            zqjc = item['zqjc']
            tpkssj = item['tpkssj']
            fpkssj = item['fpkssj']
            tpsj = item['tpsj']
            tpyy = item['tpyy']
            market_id = '00'
            sec_type = '01'
            dt_code = market_id + sec_type + zqdm
            if dt_code in dt_code_list:
                try:
                    product_name = product_name_clean(zqjc)
                    show_date = jsonobj[0]['metadata']['subname']
                    timestamp = time.mktime(time.strptime(show_date, '%Y-%m-%d'))
                    stop_date, start_date = shen_content_clean(tpkssj, fpkssj, show_date, tpsj)
                    status_code = get_status_code(dt_code, stop_date, start_date)
                    print(dt_code)
                    print('have')
                    print(zqdm, zqjc, tpkssj, fpkssj, tpsj, tpyy, market_id, sec_type, dt_code)
                    print(stop_date,start_date)
                    print (show_date)
                    print (timestamp)
                    print (product_name)
                    print (status_code)
                    print('\n')
                    save_content_shen(zqdm,dt_code, product_name,stop_date,start_date,tpkssj,fpkssj,tpsj,tpyy,show_date,status_code,timestamp)
                except Exception as e:
                    loggerError(e + '------------' + dt_code + '--------------' + productName)
            else:
                print('not save')
                print('\n')
    else:
        pass




def get_info():
    url_list = get_url()
    dt_code_list = get_dt_code()
    for url in url_list:
        get_content(url,dt_code_list)
        time.sleep(3)






if __name__ == '__main__':
    get_info()


