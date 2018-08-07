from URL.date_source import dateRange
import time


def get_url():
    """获取上交所停复牌所有url"""
    beginDate = "2008-04-02"
    endDate = time.strftime('%Y-%m-%d',time.localtime(time.time()))
    dates = dateRange(beginDate,endDate)
    url_list = []
    for date1 in dates:
        url = 'http://query.sse.com.cn/infodisplay/querySpecialTipsInfoByPage.do?&isPagination=true&searchDate={}&bgFlag=1&searchDo=1&pageHelp.pageSize=25&pageHelp.pageNo=1&pageHelp.beginPage=1&pageHelp.cacheSize=10'.format(date1)
        url_list.append(url)
    return url_list

get_url()