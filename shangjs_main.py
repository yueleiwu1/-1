import requests
import json
import time
from URL.shangjs_url import get_url
from headers.header import hu_headers
from DB.db import save_content
from DB.getcode import get_dt_code
from Rule.hu_rule import save_content_rule,hu_content_clean,hu_status_code_rule,get_timestamp
from logger_error.logger_error import loggerError


def get_content(url,dt_code_list):
    headers = hu_headers()
    response = requests.get(url, headers=headers)
    jsonobj = json.loads(response.text.strip())
    print(jsonobj)
    items = jsonobj['pageHelp']['data']
    for item in items:
        productCode = item['productCode']
        productName = item['productName']
        stopDate = item['stopDate']
        stopReason = item['stopReason']
        stopTime = item['stopTime']
        show_date = item['showDate']
        market_id = '01'
        sec_type = '01'
        dt_code = market_id + sec_type + productCode
        # print (dt_code)
        if dt_code in dt_code_list:
            try:
                print(dt_code)
                print('have')
                print(productName, productCode, market_id, sec_type, dt_code, stopDate, stopTime, stopTime, stopReason)
                stopdate,startdate = hu_content_clean(stopDate,stopTime)
                print (type(stopdate))
                print (stopdate)
                print (type(startdate))
                print (startdate)
                status_code = hu_status_code_rule(dt_code,stopdate,startdate)
                # stopdate = str(stopdate)
                # startdate = str(startdate)
                timestamp = get_timestamp(stopdate,startdate)
                print (stopdate)
                print (startdate)
                print (status_code)
                save = save_content_rule(dt_code,stopdate,startdate)
                if save ==0:
                    pass
                elif save == 1:
                    save_content(productCode, dt_code, productName, stopdate, startdate, stopDate,stopTime,stopReason,show_date,status_code,timestamp)
                print('\n')
            except Exception as e:
                loggerError(e+'------------'+dt_code+'--------------'+productName)
        else:
            print('not save')
            print('\n')

def get_info():
    url_list = get_url()
    dt_code_list = get_dt_code()
    for url in url_list:
        get_content(url,dt_code_list)
        time.sleep(3)

if __name__ == '__main__':
    get_info()








