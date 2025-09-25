import pymysql
import send_email as send_email
import os

def get_mysql_connection():
    # 连接本地 MySQL 数据库 qiandao，用户 drmt
    return pymysql.connect(
        host='localhost',
        user=os.environ.get('SQLUSER'),
        password=os.environ.get('PWSQL'),
        database=os.environ.get('SQLDB'),
        charset='utf8mb4'
    )

def query_by_user_result(result):
    # result[2] 是指模机的用户id
    value = result[2]
    conn = get_mysql_connection()  
    #首先写入签到数据。
    with conn.cursor() as cursor:
        sql_insert = "INSERT INTO qiandaojilu (user_id, date, time, state) VALUES (%s, %s, %s, %s)"
        cursor.execute(sql_insert, (value, result[6], result[7], result[5]))
    conn.commit()
    print("信息写入数据库成功") 
    #以下是返回信息给用户，告诉他们签到成功。
    with conn.cursor() as cursor:
        # 假设你要查的表叫 user_info，字段叫 user_id
        sql = "SELECT distinct user_name FROM shiyongzhe WHERE user_id = %s"
        cursor.execute(sql, (value,))
        rows = cursor.fetchall()
        # 邮件部分继续暴力抑制错误
        try:
            if result[5] == "IN" and int(result[7].split(':')[0]) < 20:  # 只在签到时发送邮件，且时间在中午12点前
                sentence_info = rows[0][0] + "于" + result[6] + "的" + result[7] + "打卡。"
                send_email.send_email(sentence_info)
        except Exception as e:
            pass    
        return rows