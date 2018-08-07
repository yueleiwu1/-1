import re
import datetime

from DB.db import set_status_code


def product_name_clean(product_name):
    pattern = re.compile(r'(&nbsp;)+')
    product_name = pattern.sub('',product_name)
    return product_name



def shen_content_clean(stop_date,start_date,show_date,tpsj):
    pattern1 = re.compile(r'\d+-\d+-\d+')
    pattern2 = re.compile(r'\d+-\d+-\d+\s\d+:\d+:\d+')
    pattern3 = re.compile(r'\d+')
    pattern4 = re.compile(r'\d+天')
    tpsj1 = pattern4.findall(tpsj)
    if len(stop_date)>0 and len(start_date)>0:
        if '开市' in start_date:
            stop_date = pattern1.findall(stop_date)[0]+' '+'00:00:00'
            start_date = pattern1.findall(start_date)[0]+' '+'00:00:00'
        else:
            stop_date = pattern1.findall(stop_date)[0]+' '+'00:00:00'
            start_date = pattern2.findall(start_date)[0]
    elif len(stop_date)==0 and len(start_date)>0:
        stop_date = ''
        if '开市' in start_date:
            start_date = pattern1.findall(start_date)[0]+' '+'00:00:00'
        else:
            start_date = pattern2.findall(start_date)[0]
    elif len(stop_date)>0 and len(start_date) == 0:
        stop_date = pattern1.findall(stop_date)[0]+' '+'00:00:00'
        start_date = ''
    else:
        if len(tpsj1)>0:
            tpsj = int(pattern3.findall(tpsj)[0])
            stop_date = show_date + ' ' + '00:00:00'
            start_date = str(datetime.datetime.strptime(stop_date,'%Y-%m-%d %H:%M:%S')+datetime.timedelta(days=tpsj))
        else:
            stop_date = show_date +' '+'00:00:00'
            start_date = show_date +' '+'00:00:00'
    return stop_date,start_date


def get_status_code(dt_code,stop_date,start_date):
    # fetches = select_content_shen(dt_code)
    if len(stop_date)>0 and len(start_date)>0:
        status_code = 1
    elif len(stop_date)>0 and len(start_date) ==0:
        status_code = 0
    else:
        status_code = 1
        set_status_code(dt_code)
    return status_code


















# def get_show_date(stop_date,start_date):
#     if len(stop_date)>0:
#         show_date = stop_date
#     else:
#         show_date = start_date
#     return show_date
#
# def get_timestamp(stop_date,start_date):
#     if len(stop_date)>0:
#         timestamp = time.mktime(time.strptime(stop_date,'%Y-%m-%d %H:%M:%S'))
#     else:
#         timestamp = time.mktime(time.strptime(start_date,'%Y-%m-%d %H:%M:%S'))
#     return timestamp

