

def get_url():
    url_list = []
    for i in range(5920,0,-1):
        url = 'http://www.szse.cn/api/report/ShowReport/data?SHOWTYPE=JSON&CATALOGID=1798&TABKEY=tab1&PAGENO={}&txtKsrq=2004-12-31&txtZzrq=2018-08-06&txtKsrq-txtZzrq=2018-08-06'.format(i)
        url_list.append(url)
    return url_list
