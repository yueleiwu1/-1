from DB.db import select_content,set_status_code1
import re
import time
import datetime

def save_content_rule(dt_code,stop_date,start_date):
    """去重规则：用以判断是否已经存在"""
    fetches = select_content(dt_code)
    if len(fetches) == 0:
        save = 1
    else:
        tup = (str(stop_date), str(start_date))
        if tup in fetches:
            save = 0
        else:
            save = 1
    return save

def hu_content_clean(stop_date,start_date):
    """日期清洗规则"""
    pattern = re.compile(r'\d+-\d+-\d+')
    date = pattern.findall(start_date)
    if stop_date == '-':
        if '连续停牌' in start_date:
            if len(date) == 2:
                stop_date1 = date[0]+' '+'00:00:00'
                start_date1 = date[1]+' '+'00:00:00'
            else:
                stop_date1 = date[0] + ' ' + '00:00:00'
                start_date1 = ''
        elif '停牌终止' in start_date:
            stop_date1 = ''
            start_date = date[0] + ' ' + '00:00:00'
            start_date1 = datetime.datetime.strptime(start_date,'%Y-%m-%d %H:%M:%S')+datetime.timedelta(days=1)
        else:
            stop_date1 = ''
            start_date1 = ''
    else:
        if start_date == '全天':
            stop_date1 = stop_date+' '+'00:00:00'
            start_date1 = datetime.datetime.strptime(stop_date1, '%Y-%m-%d %H:%M:%S') + datetime.timedelta(days=1)
        elif start_date == '9:30-10:30':
            stop_date1 = stop_date + ' ' + '09:30:00'
            start_date1 = stop_date + ' ' + '10:30:00'
        elif start_date == '下午':
            stop_date1 = stop_date + ' ' + '00:00:00'
            start_date1 = stop_date + ' ' + '00:06:00'
        else:
            stop_date1 = stop_date + ' ' + '00:00:00'
            start_date1 = stop_date + ' ' + '00:06:00'
    return stop_date1,start_date1











def hu_status_code_rule(dt_code,stop_date,start_date):
    stop_date = str(stop_date)
    start_date = str(start_date)
    if len(stop_date) >0 and len(start_date)>0:
        status_code = 1
    elif len(stop_date) >0 and len(start_date)==0:
        status_code = 0
    elif len(stop_date) == 0 and len(start_date)>0:
        fetches = select_content(dt_code)
        if len(fetches) == 0:
            status_code = 0
        elif len(fetches) == 1:
            if fetches[0][0] != '' and fetches[0][1] != '':
                status_code = 0
            elif fetches[0][0] != '' and fetches[0][1] == '':
                status_code = 1
                set_status_code1(fetches[0][0],dt_code)
            else:
                status_code = 0
        else:
            if fetches[0][0] != '' and fetches[0][1] == '':
                status_code = 1
                set_status_code1(fetches[0][0],dt_code)
            elif fetches[0][0] != '' and fetches[0][1] != ''and fetches[1][0] != '' and fetches[1][1] == '':
                    status_code = 1
                    set_status_code1(fetches[1][0],dt_code)
            else:
                status_code = 0
    else:
        status_code = 1
    return status_code

def get_timestamp(stop_date,start_date):
    if stop_date == '':
        timestamp = time.mktime(time.strptime(str(start_date),'%Y-%m-%d %H:%M:%S'))
    else:
        timestamp = time.mktime(time.strptime(str(stop_date),'%Y-%m-%d %H:%M:%S'))
    return timestamp
