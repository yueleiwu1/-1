import pymysql

conn = pymysql.connect(host='localhost', user='root', db='test', password='123456')

def save_content(*args):
    """保存抓取的内容至数据库"""
    try:
        conn.ping()
    except:
        conn.ping(True)
    cur = conn.cursor()
    sql = 'insert into hu_stock_exchange3(product_code,dt_code,product_name,stop_date,start_date,i_stop_date,i_start_date,stop_reason,show_date,status_code,timestamp) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
    cur.execute(sql, (args))
    conn.commit()


def save_content_shen(*args):
    """保存抓取的内容至数据库"""
    try:
        conn.ping()
    except:
        conn.ping(True)
    cur = conn.cursor()
    sql = 'insert into shen_stock_exchange(product_code,dt_code,product_name,stop_date,start_date,i_stop_date,i_start_date,tpsj,stop_reason,show_date,status_code,timestamp) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
    cur.execute(sql, (args))
    conn.commit()



def set_status_code(dt_code):
    """修改相邻的停复牌日期的状态值"""
    try:
        conn.ping()
    except:
        conn.ping(True)
    cur = conn.cursor()
    sql = 'update hu_stock_exchange3 set status_code = 1 where dt_code = {} order by timestamp DESC limit 1'.format(dt_code)
    cur.execute(sql)
    conn.commit()


def set_status_code1(stop_date,dt_code):
    """修改相隔一行的停复牌日期状态值"""
    try:
        conn.ping()
    except:
        conn.ping(True)
    cur = conn.cursor()
    sql = "update hu_stock_exchange3 set status_code = 1 where stop_date = '{}' and dt_code={}".format(stop_date,dt_code)
    cur.execute(sql)
    conn.commit()





def select_content(dt_code):
    """选取指定dt_code已存数据库的stop_date和start_date用以比较和去重等"""
    try:
        conn.ping()
    except:
        conn.ping(True)
    cur = conn.cursor()
    sql = 'select stop_date,start_date from hu_stock_exchange3 where dt_code={} order by timestamp DESC'.format(dt_code)
    cur.execute(sql)
    conn.commit()
    fetches = cur.fetchall()
    return fetches


def select_content_shen(dt_code):
    """选取指定dt_code已存数据库的stop_date和start_date用以比较和去重等"""
    try:
        conn.ping()
    except:
        conn.ping(True)
    cur = conn.cursor()
    sql = 'select stop_date,start_date from shen_stock_exchange where dt_code={} order by timestamp DESC'.format(dt_code)
    cur.execute(sql)
    conn.commit()
    fetches = cur.fetchall()
    return fetches


def set_status_code(dt_code):
    """修改相邻的停复牌日期的状态值"""
    try:
        conn.ping()
    except:
        conn.ping(True)
    cur = conn.cursor()
    sql = 'update shen_stock_exchange set status_code = 1 where dt_code = {} order by timestamp DESC limit 1'.format(dt_code)
    cur.execute(sql)
    conn.commit()
