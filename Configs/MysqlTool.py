import logging

import pandas as pd
import pymysql
from sqlalchemy import create_engine

from Configs.ConfigComment import INPUT_COMMENT_DB, INPUT_COMMENT_TABLE, OUT_COMMENT_DB, OUT_COMMENT_TABLE
from Configs.OtherTools import GetMd5
from Configs.Config import DB, TABLE, PASS, USER, HTML_SAVE_URL, PORT, HOST


# 将数据保存到数据库（传入数据为字典）
def SaveToMysql(data):
    engine = create_engine('mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8mb4'.format(USER, PASS, HOST, PORT, OUT_COMMENT_DB), pool_recycle=10, pool_size=200)
    connect = engine.connect()
    try:
        df = pd.DataFrame(data, index=[0])
        df.to_sql(name=OUT_COMMENT_TABLE, con=connect, if_exists='append', index=False, chunksize=100)
        connect.close()
    except Exception as e:
        logging.error("\nError: %s, Please check the error.\n" % e.args)
        _ = e


# 保存网页数据到本地
def SaveWeb(url, html):
    f = open(HTML_SAVE_URL + GetMd5(url) + '.html', 'a', encoding='utf-8')
    f.write(html)
    f.close()


# 提取mysql数据表中的某一列
def GetColFromMysql(colName):
    # 创建mysql连接
    conn = pymysql.connect(host = HOST, port = PORT, user = USER, password = PASS, database = INPUT_COMMENT_DB)
    cur = conn.cursor()

    # 执行sql语句
    sql = 'SELECT {} FROM {}'.format(colName, INPUT_COMMENT_TABLE)
    cur.execute(sql)

    # 将一列取出为列表
    ls = []
    for item in cur.fetchall():
        ls.append(item[0])

    # 返回sql语句执行结果
    conn.close()
    return ls


if __name__ == '__main__':
    # ls = GetColFromMysql('link')
    # print(ls)
    pass
