import pymysql

conn = pymysql.connect(host = '47.97.111.88',user= 'dengtacj',passwd = 'dengtacj2015',db='db_stock_basics')

def get_dt_code():
    """获取所有股票证券等类型的code"""
    try:
        conn.ping()
    except:
        conn.ping(True)
    cur = conn.cursor()
    sql = 'select dt_code from t_stock_dict'
    cur.execute(sql)
    dt_code_list = []
    fetches = cur.fetchall()
    for fetch in fetches:
        # print(fetch[0])
        if (fetch[0][:2] == '00' or fetch[0][:2] == '01') and fetch[0][2:4] == '01':
            # print (fetch[0])
            dt_code_list.append(fetch[0])
        else:
            pass
    # print (len(dt_code_list))

    return dt_code_list

get_dt_code()