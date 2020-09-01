#!/usr/bin/env python3
import time, mysql.connector
import grab_data_two, update_data

conn = mysql.connector.connect(host='62.77.159.42',user='sakib3',database='bitbot',password='@&G6hdM@EZJKQu010au*jpIjs7EsB', autocommit=True)
cur = conn.cursor()


while True:
    if conn.is_connected() == True:
        pass
    else:
        conn = mysql.connector.connect(host='62.77.159.42',user='sakib3',database='bitbot',password='@&G6hdM@EZJKQu010au*jpIjs7EsB', autocommit=True)
        cur = conn.cursor()
    not_pending = grab_data_two.descri_false(cur)
    if not_pending == []:
        time.sleep(4000)
    else:
        for i in not_pending:
            current_time = time.time()
            next_pay = grab_data_two.payout_next(i, cur)
            if next_pay <= current_time:
                print(f'{i} available for payout')
                update_data.payout_true(i, cur)
        time.sleep(4000)
